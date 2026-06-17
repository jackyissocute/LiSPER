from pathlib import Path
import csv
import math
import os
import re
import shutil
import subprocess
import time

ROOT = Path(os.environ.get("LISPER_WORKDIR", "/root/LiSPER_remote/LiSPER_LiCl"))
GMX_ENV = "source /root/miniconda3/etc/profile.d/conda.sh && conda activate lisper-gmx"
CANDIDATE = os.environ.get("LISPER_CANDIDATE", "LiD3-1")
NTHREAD = 16
MAX_REPAIRS = 8
WAIT_FOR_PID = os.environ.get("WAIT_FOR_PID", "").strip()


def wait_for_existing_batch():
    if not WAIT_FOR_PID:
        return
    while Path(f"/proc/{WAIT_FOR_PID}").exists():
        time.sleep(60)


def run_shell(cmd, cwd=None, log=None):
    full = f"bash -lc {cmd!r}"
    proc = subprocess.run(
        full,
        shell=True,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if log:
        Path(log).write_text(proc.stdout)
    return proc.returncode, proc.stdout


def parse_gro(path):
    lines = Path(path).read_text().splitlines()
    atoms = []
    for line in lines[2:-1]:
        atoms.append(
            {
                "atomnr": int(line[15:20]),
                "resnr": int(line[:5]),
                "resname": line[5:10].strip(),
                "atomname": line[10:15].strip(),
                "xyz": (
                    float(line[20:28]),
                    float(line[28:36]),
                    float(line[36:44]),
                ),
                "line": line,
            }
        )
    return lines[0], atoms, list(map(float, lines[-1].split()))


def write_gro(path, title, atoms, box):
    lines = [title, f"{len(atoms):5d}"]
    lines.extend(atom["line"] for atom in atoms)
    lines.append(" ".join(f"{value:10.5f}" for value in box))
    Path(path).write_text("\n".join(lines) + "\n")


def box_matrix(box):
    if len(box) == 9:
        a = (box[0], box[3], box[4])
        b = (box[5], box[1], box[6])
        c = (box[7], box[8], box[2])
    else:
        a = (box[0], 0.0, 0.0)
        b = (0.0, box[1], 0.0)
        c = (0.0, 0.0, box[2])
    return [[a[0], b[0], c[0]], [a[1], b[1], c[1]], [a[2], b[2], c[2]]]


def det3(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def inv3(matrix):
    determinant = det3(matrix)
    return [
        [
            (
                matrix[(j + 1) % 3][(i + 1) % 3]
                * matrix[(j + 2) % 3][(i + 2) % 3]
                - matrix[(j + 1) % 3][(i + 2) % 3]
                * matrix[(j + 2) % 3][(i + 1) % 3]
            )
            / determinant
            for j in range(3)
        ]
        for i in range(3)
    ]


def mv(matrix, vector):
    return tuple(sum(matrix[row][i] * vector[i] for i in range(3)) for row in range(3))


def pbc_dist(r1, r2, matrix, inverse):
    fractional = mv(inverse, (r1[0] - r2[0], r1[1] - r2[1], r1[2] - r2[2]))
    fractional = tuple(value - round(value) for value in fractional)
    cartesian = mv(matrix, fractional)
    return math.sqrt(sum(value * value for value in cartesian))


def find_repair_residue(gro, bad_atomnr):
    title, atoms, box = parse_gro(gro)
    target = next((atom for atom in atoms if atom["atomnr"] == bad_atomnr), None)
    if target is None:
        return None, "bad_atom_not_found"
    if target["resname"] != "TIP3":
        return (
            None,
            f"bad_atom_not_water:{target['resname']}:{target['resnr']}:{target['atomname']}",
        )
    matrix = box_matrix(box)
    inverse = inv3(matrix)
    nearest = []
    for atom in atoms:
        if atom["resnr"] == target["resnr"]:
            continue
        distance = pbc_dist(target["xyz"], atom["xyz"], matrix, inverse)
        if distance < 0.13:
            nearest.append((distance, atom))
    nearest.sort(key=lambda item: item[0])
    for distance, atom in nearest:
        if atom["resname"] == "TIP3":
            return (
                atom["resnr"],
                "remove_neighbor_water:{}:{}:dist={:.4f};target={}:{}".format(
                    atom["resnr"],
                    atom["atomname"],
                    distance,
                    target["resnr"],
                    target["atomname"],
                ),
            )
    return target["resnr"], f"remove_target_water:{target['resnr']}:{target['atomname']}"


def remove_water(gro_in, top_in, gro_out, top_out, resnr):
    title, atoms, box = parse_gro(gro_in)
    removed = [
        atom for atom in atoms if atom["resnr"] == resnr and atom["resname"] == "TIP3"
    ]
    kept = [
        atom
        for atom in atoms
        if not (atom["resnr"] == resnr and atom["resname"] == "TIP3")
    ]
    if len(removed) != 3:
        raise RuntimeError(f"Expected 3 TIP3 atoms for residue {resnr}, removed {len(removed)}")
    write_gro(gro_out, title, kept, box)
    text = Path(top_in).read_text()
    match = re.search(r"^(TIP3\s+)(\d+)\s*$", text, flags=re.M)
    if not match:
        raise RuntimeError("TIP3 molecule count not found in topology")
    old = int(match.group(2))
    new = old - 1
    text = text[: match.start()] + f"{match.group(1)}{new}\n" + text[match.end() :]
    Path(top_out).write_text(text)
    return old, new


def max_force_info(log_text):
    if "not finite" in log_text or re.search(r"Maximum force\s+=\s+inf", log_text):
        match = re.search(r"Maximum force\s+=\s+\S+\s+on atom\s+(\d+)", log_text)
        if match:
            return "inf", int(match.group(1))
        matches = re.findall(r"Fmax=\s*inf, atom=\s*(\d+)", log_text)
        if matches:
            return "inf", int(matches[-1])
    match = re.search(r"Maximum force\s+=\s+([0-9.eE+-]+)\s+on atom\s+(\d+)", log_text)
    if match:
        return float(match.group(1)), int(match.group(2))
    return None, None


def write_solu_solv_index(gro_path, ndx_path):
    lines = Path(gro_path).read_text().splitlines()
    protein_positions = []
    solvent_positions = []
    for position, line in enumerate(lines[2:-1], start=1):
        resname = line[5:10].strip()
        if resname in {"TIP3", "LIT", "CLA", "SOD"}:
            solvent_positions.append(position)
        else:
            protein_positions.append(position)

    def format_group(name, values):
        out = [f"[ {name} ]"]
        for i in range(0, len(values), 15):
            out.append(" ".join(f"{value:5d}" for value in values[i : i + 15]))
        return out

    all_positions = list(range(1, len(lines) - 1))
    out = []
    out.extend(format_group("SOLU", protein_positions))
    out.append("")
    out.extend(format_group("SOLV", solvent_positions))
    out.append("")
    out.extend(format_group("SYSTEM", all_positions))
    Path(ndx_path).write_text("\n".join(out) + "\n")


def minimize(gromacs_dir):
    run_dir = gromacs_dir / "run_min"
    if run_dir.exists():
        shutil.rmtree(run_dir)
    run_dir.mkdir()
    current_gro = gromacs_dir / "step3_input.gro"
    current_top = gromacs_dir / "topol.top"
    repairs = []

    for attempt in range(MAX_REPAIRS + 1):
        prefix = f"min_attempt{attempt}"
        tpr = run_dir / f"{prefix}.tpr"
        grompp_log = run_dir / f"{prefix}.grompp.log"
        mdrun_log = run_dir / f"{prefix}.mdrun.log"
        code, _ = run_shell(
            f"{GMX_ENV} && gmx grompp -f step4.0_minimization.mdp -o {tpr} "
            f"-c {current_gro} -r {current_gro} -p {current_top} -n index.ndx -maxwarn 1",
            cwd=gromacs_dir,
            log=grompp_log,
        )
        if code != 0:
            return "grompp_failed", repairs

        code, out = run_shell(
            f"{GMX_ENV} && cd {run_dir} && gmx mdrun -deffnm {prefix} "
            f"-ntmpi 1 -ntomp {NTHREAD}",
            cwd=gromacs_dir,
            log=mdrun_log,
        )
        log_path = run_dir / f"{prefix}.log"
        log_text = log_path.read_text(errors="replace") if log_path.exists() else out
        force, atom = max_force_info(log_text)
        if force != "inf" and force is not None and float(force) < 1000:
            for extension in ["gro", "edr", "log", "trr", "tpr"]:
                source = run_dir / f"{prefix}.{extension}"
                if source.exists():
                    shutil.copy2(source, run_dir / f"step4.0_minimization.{extension}")
            shutil.copy2(current_gro, run_dir / "step3_input_cleaned.gro")
            shutil.copy2(current_top, run_dir / "topol_cleaned.top")
            (run_dir / "repair_summary.txt").write_text(
                "\n".join(repairs) + ("\n" if repairs else "")
            )
            return "minimized", repairs
        if force == "inf" and atom is not None and attempt < MAX_REPAIRS:
            resnr, reason = find_repair_residue(current_gro, atom)
            if resnr is None:
                return f"repair_failed:{reason}", repairs
            new_gro = run_dir / f"clean_attempt{attempt + 1}.gro"
            new_top = gromacs_dir / f"topol_clean_attempt{attempt + 1}.top"
            old, new = remove_water(current_gro, current_top, new_gro, new_top, resnr)
            repairs.append(f"attempt{attempt}:atom{atom}:{reason}:TIP3 {old}->{new}")
            current_gro, current_top = new_gro, new_top
            continue
        return f"not_converged:force={force}:atom={atom}", repairs

    return "max_repairs_exceeded", repairs


def equilibrate(gromacs_dir):
    min_dir = gromacs_dir / "run_min"
    eq_dir = gromacs_dir / "run_eq"
    if eq_dir.exists():
        shutil.rmtree(eq_dir)
    eq_dir.mkdir()
    clean_topologies = sorted(gromacs_dir.glob("topol_clean_attempt*.top"))
    topology = clean_topologies[-1] if clean_topologies else gromacs_dir / "topol.top"
    coordinates = min_dir / "step4.0_minimization.gro"
    restraints = min_dir / "step3_input_cleaned.gro"
    index = eq_dir / "index_clean.ndx"
    tpr = eq_dir / "step4.1_equilibration.tpr"
    write_solu_solv_index(coordinates, index)

    code, _ = run_shell(
        f"{GMX_ENV} && gmx grompp -f step4.1_equilibration.mdp -o {tpr} "
        f"-c {coordinates} -r {restraints} -p {topology} -n {index} -maxwarn 1",
        cwd=gromacs_dir,
        log=eq_dir / "step4.1_equilibration.grompp.log",
    )
    if code != 0:
        return "grompp_failed"

    code, _ = run_shell(
        f"{GMX_ENV} && cd {eq_dir} && OMP_NUM_THREADS={NTHREAD} "
        f"gmx mdrun -deffnm step4.1_equilibration -ntmpi 1 -ntomp {NTHREAD}",
        cwd=gromacs_dir,
        log=eq_dir / "step4.1_equilibration.mdrun.stdout.log",
    )
    log = eq_dir / "step4.1_equilibration.log"
    if code == 0 and log.exists() and "Finished mdrun" in log.read_text(errors="replace"):
        return "equilibrated"
    return "mdrun_failed"


def update_summary(path, row, fieldnames):
    rows = []
    if path.exists():
        with path.open() as handle:
            rows = [
                existing
                for existing in csv.DictReader(handle, delimiter="\t")
                if existing["candidate_id"] != CANDIDATE
            ]
    rows.insert(0, row)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main():
    wait_for_existing_batch()
    gromacs_dir = ROOT / "systems" / CANDIDATE / "gromacs"
    status, repairs = minimize(gromacs_dir)
    update_summary(
        ROOT / "minimization_summary.tsv",
        {
            "candidate_id": CANDIDATE,
            "status": status,
            "repairs": ";".join(repairs),
            "run_dir": str(gromacs_dir / "run_min"),
        },
        ["candidate_id", "status", "repairs", "run_dir"],
    )
    print(CANDIDATE, status, ";".join(repairs))
    if status != "minimized":
        return

    eq_status = equilibrate(gromacs_dir)
    update_summary(
        ROOT / "equilibration_summary.tsv",
        {
            "candidate_id": CANDIDATE,
            "status": eq_status,
            "run_dir": str(gromacs_dir / "run_eq"),
        },
        ["candidate_id", "status", "run_dir"],
    )
    print(CANDIDATE, eq_status)


if __name__ == "__main__":
    main()
