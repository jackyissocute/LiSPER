from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import csv
import math
import os
import re
import subprocess
import time

ROOT = Path(os.environ["LISPER_WORKDIR"])
CANDIDATE = os.environ.get("LISPER_CANDIDATE", "LiDA-1")
ION_RESNAME = os.environ["LISPER_ION_RESNAME"]
NTHREAD = int(os.environ.get("LISPER_NTHREAD_PER_JOB", "1"))
NJOBS = int(os.environ.get("LISPER_JOBS", "1"))
PULL_NS = float(os.environ.get("LISPER_PULL_NS", "0.5"))
WINDOW_NS = float(os.environ.get("LISPER_WINDOW_NS", "1.0"))
WINDOW_SPACING_NM = float(os.environ.get("LISPER_WINDOW_SPACING_NM", "0.10"))
WINDOW_EXTENSION_NM = float(os.environ.get("LISPER_WINDOW_EXTENSION_NM", "2.00"))
PULL_K = float(os.environ.get("LISPER_PULL_K", "1000"))
GMX_ENV = "source /root/miniconda3/etc/profile.d/conda.sh && conda activate lisper-gmx"

GROMACS_DIR = ROOT / "systems" / CANDIDATE / "gromacs"
PROD_DIR = GROMACS_DIR / "run_prod_20ns"
CLUSTER_DIR = GROMACS_DIR / "cluster_20ns"
UMB_DIR = GROMACS_DIR / "umbrella_sampling"
SUMMARY = UMB_DIR / "umbrella_summary.tsv"


def run_shell(cmd, cwd=GROMACS_DIR, log=None, stdin=None):
    proc = subprocess.run(
        f"bash -lc {cmd!r}",
        shell=True,
        cwd=cwd,
        input=stdin,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if log:
        Path(log).write_text(proc.stdout)
    return proc.returncode, proc.stdout


def read_representative_time_ps():
    pdb = CLUSTER_DIR / "representative_top_cluster.pdb"
    title = pdb.read_text(errors="replace").splitlines()[0]
    match = re.search(r"t=\s*([0-9.]+)", title)
    if not match:
        raise RuntimeError(f"Could not parse representative time from {pdb}")
    return float(match.group(1))


def write_index_with_target(frame_gro, out_ndx):
    lines = Path(frame_gro).read_text(errors="replace").splitlines()
    natoms = int(lines[1].strip())
    atom_lines = lines[2 : 2 + natoms]
    solu_atoms = []
    solv_atoms = []
    ion_atoms = []
    solu_coords = []
    ion_coords = []
    for idx, line in enumerate(atom_lines, start=1):
        resname = line[5:10].strip()
        x = float(line[20:28])
        y = float(line[28:36])
        z = float(line[36:44])
        if resname in {"ASP", "ALA", "GLY", "PRO", "SER", "ASN"}:
            solu_atoms.append(idx)
            solu_coords.append((x, y, z))
        else:
            solv_atoms.append(idx)
        if resname == ION_RESNAME:
            ion_atoms.append(idx)
            ion_coords.append((idx, x, y, z))
    if not solu_atoms:
        raise RuntimeError("No peptide atoms found for SOLU group")
    if not ion_atoms:
        raise RuntimeError(f"No {ION_RESNAME} atoms found")

    cx = sum(x for x, _, _ in solu_coords) / len(solu_coords)
    cy = sum(y for _, y, _ in solu_coords) / len(solu_coords)
    cz = sum(z for _, _, z in solu_coords) / len(solu_coords)
    target = min(
        ion_coords,
        key=lambda item: (item[1] - cx) ** 2 + (item[2] - cy) ** 2 + (item[3] - cz) ** 2,
    )
    target_atom = target[0]
    initial_distance = math.sqrt(
        (target[1] - cx) ** 2 + (target[2] - cy) ** 2 + (target[3] - cz) ** 2
    )

    with Path(out_ndx).open("w") as handle:
        handle.write("[ SOLU ]\n")
        for i in range(0, len(solu_atoms), 15):
            handle.write(" ".join(str(a) for a in solu_atoms[i : i + 15]) + "\n")
        handle.write("\n[ SOLV ]\n")
        for i in range(0, len(solv_atoms), 15):
            handle.write(" ".join(str(a) for a in solv_atoms[i : i + 15]) + "\n")
        handle.write("\n[ SYSTEM ]\n")
        for i in range(0, natoms, 15):
            handle.write(" ".join(str(a) for a in range(i + 1, min(i + 16, natoms + 1))) + "\n")
        handle.write("\n[ TARGET_ION ]\n")
        handle.write(f"{target_atom}\n")
    return target_atom, initial_distance


def base_mdp(nsteps, continuation, pull_rate, pull_init, output_every=500):
    template = (PROD_DIR / "step5_production_20ns.mdp").read_text()
    replacements = {
        "nsteps": str(nsteps),
        "nstxout-compressed": str(output_every),
        "nstenergy": str(output_every),
        "nstlog": str(output_every),
        "continuation": continuation,
    }
    lines = []
    seen = set()
    for line in template.splitlines():
        key = line.split("=", 1)[0].strip() if "=" in line else ""
        if key in replacements:
            lines.append(f"{key:<24}= {replacements[key]}")
            seen.add(key)
        elif key == "pull":
            continue
        else:
            lines.append(line)
    for key, value in replacements.items():
        if key not in seen:
            lines.append(f"{key:<24}= {value}")
    lines.extend(
        [
            "",
            "pull                     = yes",
            "pull_ngroups             = 2",
            "pull_ncoords             = 1",
            "pull_group1_name         = SOLU",
            "pull_group2_name         = TARGET_ION",
            "pull_coord1_type         = umbrella",
            "pull_coord1_geometry     = distance",
            "pull_coord1_groups       = 1 2",
            "pull_coord1_dim          = Y Y Y",
            f"pull_coord1_k            = {PULL_K:g}",
            f"pull_coord1_init         = {pull_init:.4f}",
            f"pull_coord1_rate         = {pull_rate:.6f}",
            "pull_nstxout             = 100",
            "pull_nstfout             = 100",
        ]
    )
    if continuation == "no":
        lines.extend(["gen_vel                  = yes", "gen_temp                 = 298.15", "gen_seed                 = -1"])
    return "\n".join(lines) + "\n"


def parse_pullx(pullx):
    points = []
    for line in Path(pullx).read_text(errors="replace").splitlines():
        if not line or line.startswith(("#", "@")):
            continue
        parts = line.split()
        if len(parts) >= 2:
            try:
                points.append((float(parts[0]), float(parts[1])))
            except ValueError:
                pass
    if not points:
        raise RuntimeError(f"No pullx points parsed from {pullx}")
    return points


def closest_time(points, distance):
    return min(points, key=lambda item: abs(item[1] - distance))[0]


def topology_for():
    cleaned = GROMACS_DIR / "topol_cleaned_for_prod.top"
    if cleaned.exists():
        return cleaned
    return GROMACS_DIR / "topol.top"


def grompp_mdrun(window_dir, mdp, gro, deffnm):
    tpr = window_dir / f"{deffnm}.tpr"
    code, _ = run_shell(
        f"{GMX_ENV} && gmx grompp -f {mdp} -c {gro} -p {topology_for()} "
        f"-n {UMB_DIR / 'umbrella_index.ndx'} -o {tpr} -maxwarn 1",
        log=window_dir / f"{deffnm}.grompp.log",
    )
    if code != 0:
        return "grompp_failed"
    code, _ = run_shell(
        f"{GMX_ENV} && cd {window_dir} && OMP_NUM_THREADS={NTHREAD} "
        f"gmx mdrun -deffnm {deffnm} -ntmpi 1 -ntomp {NTHREAD}",
        log=window_dir / f"{deffnm}.mdrun.stdout.log",
    )
    if code != 0:
        return "mdrun_failed"
    log = window_dir / f"{deffnm}.log"
    if not log.exists() or "Finished mdrun" not in log.read_text(errors="replace"):
        return "incomplete"
    return "complete"


def write_summary(rows):
    with SUMMARY.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "candidate_id",
                "ion_resname",
                "target_atom",
                "representative_time_ps",
                "window_id",
                "target_distance_nm",
                "status",
                "path",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main():
    UMB_DIR.mkdir(exist_ok=True)
    rep_time = read_representative_time_ps()
    full_rep = UMB_DIR / "representative_full_system.gro"
    if not full_rep.exists():
        code, _ = run_shell(
            f"{GMX_ENV} && gmx trjconv -s {PROD_DIR / 'step5_production_20ns.tpr'} "
            f"-f {PROD_DIR / 'step5_production_20ns.xtc'} -dump {rep_time:.3f} "
            f"-o {full_rep} -n {GROMACS_DIR / 'index.ndx'} -pbc mol -center",
            log=UMB_DIR / "extract_representative_full_system.log",
            stdin="0\n2\n",
        )
        if code != 0:
            raise RuntimeError("Failed to extract full representative frame")

    target_atom, initial_distance = write_index_with_target(full_rep, UMB_DIR / "umbrella_index.ndx")
    metadata = UMB_DIR / "umbrella_metadata.tsv"
    metadata.write_text(
        "candidate_id\tion_resname\ttarget_atom\trepresentative_time_ps\tinitial_distance_nm\tpull_ns\twindow_ns\twindow_spacing_nm\twindow_extension_nm\n"
        f"{CANDIDATE}\t{ION_RESNAME}\t{target_atom}\t{rep_time:.3f}\t{initial_distance:.4f}\t{PULL_NS:.3f}\t{WINDOW_NS:.3f}\t{WINDOW_SPACING_NM:.3f}\t{WINDOW_EXTENSION_NM:.3f}\n"
    )

    pull_dir = UMB_DIR / "pull"
    pull_dir.mkdir(exist_ok=True)
    pull_mdp = pull_dir / "pull.mdp"
    pull_steps = int(PULL_NS * 500000)
    pull_rate = WINDOW_EXTENSION_NM / (PULL_NS * 1000.0)
    pull_mdp.write_text(base_mdp(pull_steps, "no", pull_rate, initial_distance))
    pull_status = "complete"
    if not (pull_dir / "pull.log").exists() or "Finished mdrun" not in (pull_dir / "pull.log").read_text(errors="replace"):
        pull_status = grompp_mdrun(pull_dir, pull_mdp, full_rep, "pull")
    if pull_status != "complete":
        write_summary([
            {
                "candidate_id": CANDIDATE,
                "ion_resname": ION_RESNAME,
                "target_atom": target_atom,
                "representative_time_ps": f"{rep_time:.3f}",
                "window_id": "pull",
                "target_distance_nm": "",
                "status": pull_status,
                "path": str(pull_dir),
            }
        ])
        raise RuntimeError(f"Pulling stage failed: {pull_status}")

    points = parse_pullx(pull_dir / "pull_pullx.xvg")
    distances = [
        round(initial_distance + i * WINDOW_SPACING_NM, 4)
        for i in range(int(WINDOW_EXTENSION_NM / WINDOW_SPACING_NM) + 1)
    ]
    rows = []
    window_jobs = []
    for i, dist in enumerate(distances):
        win = UMB_DIR / f"window_{i:03d}_{dist:.2f}nm"
        win.mkdir(exist_ok=True)
        gro = win / "start.gro"
        if not gro.exists():
            dump_time = closest_time(points, dist)
            code, _ = run_shell(
                f"{GMX_ENV} && gmx trjconv -s {pull_dir / 'pull.tpr'} -f {pull_dir / 'pull.xtc'} "
                f"-dump {dump_time:.3f} -o {gro} -n {UMB_DIR / 'umbrella_index.ndx'}",
                log=win / "extract_window.log",
                stdin="2\n",
            )
            if code != 0:
                rows.append(
                    {
                        "candidate_id": CANDIDATE,
                        "ion_resname": ION_RESNAME,
                        "target_atom": target_atom,
                        "representative_time_ps": f"{rep_time:.3f}",
                        "window_id": f"{i:03d}",
                        "target_distance_nm": f"{dist:.4f}",
                        "status": "extract_failed",
                        "path": str(win),
                    }
                )
                continue
        mdp = win / "umbrella.mdp"
        mdp.write_text(base_mdp(int(WINDOW_NS * 500000), "no", 0.0, dist, output_every=500))
        window_jobs.append((i, dist, win, mdp, gro))

    def run_window(job):
        i, dist, win, mdp, gro = job
        status = "complete"
        if not (win / "umbrella.log").exists() or "Finished mdrun" not in (win / "umbrella.log").read_text(errors="replace"):
            status = grompp_mdrun(win, mdp, gro, "umbrella")
        return {
            "candidate_id": CANDIDATE,
            "ion_resname": ION_RESNAME,
            "target_atom": target_atom,
            "representative_time_ps": f"{rep_time:.3f}",
            "window_id": f"{i:03d}",
            "target_distance_nm": f"{dist:.4f}",
            "status": status,
            "path": str(win),
        }

    with ThreadPoolExecutor(max_workers=NJOBS) as pool:
        futures = [pool.submit(run_window, job) for job in window_jobs]
        for fut in as_completed(futures):
            rows.append(fut.result())
            write_summary(sorted(rows, key=lambda row: row["window_id"]))
            time.sleep(0.1)
    write_summary(sorted(rows, key=lambda row: row["window_id"]))


if __name__ == "__main__":
    main()
