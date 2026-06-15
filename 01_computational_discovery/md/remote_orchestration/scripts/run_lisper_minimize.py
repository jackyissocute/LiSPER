from pathlib import Path
import csv, subprocess, re, math, shutil, os, sys

ROOT = Path(os.environ.get("LISPER_WORKDIR", "/root/LiSPER_remote/LiSPER_LiCl"))
GMX_ENV = "source /root/miniconda3/etc/profile.d/conda.sh && conda activate lisper-gmx"
NTHREAD = 16
MAX_REPAIRS = 8

# Candidate list from staged manifest
with open(ROOT / "ready_gromacs_systems.tsv") as f:
    candidates = [row["candidate_id"] for row in csv.DictReader(f, delimiter="\t")]


def run_shell(cmd, cwd=None, log=None):
    full = f"bash -lc {cmd!r}"
    p = subprocess.run(full, shell=True, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if log:
        Path(log).write_text(p.stdout)
    return p.returncode, p.stdout


def parse_gro(path):
    lines = Path(path).read_text().splitlines()
    atoms = []
    for line in lines[2:-1]:
        atomnr = int(line[15:20])
        atoms.append({
            "atomnr": atomnr,
            "resnr": int(line[:5]),
            "resname": line[5:10].strip(),
            "atomname": line[10:15].strip(),
            "xyz": (float(line[20:28]), float(line[28:36]), float(line[36:44])),
            "line": line,
        })
    box = list(map(float, lines[-1].split()))
    return lines[0], atoms, box


def write_gro(path, title, atoms, box):
    lines = [title, f"{len(atoms):5d}"] + [a["line"] for a in atoms] + [" ".join(f"{x:10.5f}" for x in box)]
    Path(path).write_text("\n".join(lines) + "\n")


def box_matrix(box):
    if len(box) == 9:
        a = (box[0], box[3], box[4])
        b = (box[5], box[1], box[6])
        c = (box[7], box[8], box[2])
    else:
        a = (box[0], 0.0, 0.0); b = (0.0, box[1], 0.0); c = (0.0, 0.0, box[2])
    return [[a[0], b[0], c[0]], [a[1], b[1], c[1]], [a[2], b[2], c[2]]]


def det3(m):
    return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])


def inv3(m):
    d = det3(m)
    return [[(m[(j+1)%3][(i+1)%3]*m[(j+2)%3][(i+2)%3]-m[(j+1)%3][(i+2)%3]*m[(j+2)%3][(i+1)%3])/d for j in range(3)] for i in range(3)]


def mv(m, v):
    return (sum(m[0][i]*v[i] for i in range(3)), sum(m[1][i]*v[i] for i in range(3)), sum(m[2][i]*v[i] for i in range(3)))


def pbc_dist(r1, r2, M, Minv):
    ds = mv(Minv, (r1[0]-r2[0], r1[1]-r2[1], r1[2]-r2[2]))
    ds = tuple(x - round(x) for x in ds)
    dc = mv(M, ds)
    return math.sqrt(sum(x*x for x in dc))


def find_repair_residue(gro, bad_atomnr):
    title, atoms, box = parse_gro(gro)
    target = next((a for a in atoms if a["atomnr"] == bad_atomnr), None)
    if not target:
        return None, "bad_atom_not_found"
    if target["resname"] != "TIP3":
        return None, f"bad_atom_not_water:{target[resname]}:{target[resnr]}:{target[atomname]}"
    M = box_matrix(box); Minv = inv3(M)
    nearest = []
    for a in atoms:
        if a["resnr"] == target["resnr"]:
            continue
        d = pbc_dist(target["xyz"], a["xyz"], M, Minv)
        if d < 0.13:
            nearest.append((d, a))
    nearest.sort(key=lambda x: x[0])
    # Prefer removing another water residue involved in the clash; otherwise remove target water.
    for d, a in nearest:
        if a["resname"] == "TIP3":
            return a["resnr"], "remove_neighbor_water:{}:{}:dist={:.4f};target={}:{}".format(a["resnr"], a["atomname"], d, target["resnr"], target["atomname"])
    return target["resnr"], "remove_target_water:{}:{}".format(target["resnr"], target["atomname"])


def remove_water(gro_in, top_in, gro_out, top_out, resnr):
    title, atoms, box = parse_gro(gro_in)
    removed = [a for a in atoms if a["resnr"] == resnr and a["resname"] == "TIP3"]
    kept = [a for a in atoms if not (a["resnr"] == resnr and a["resname"] == "TIP3")]
    if len(removed) != 3:
        raise RuntimeError(f"Expected 3 TIP3 atoms for residue {resnr}, removed {len(removed)}")
    write_gro(gro_out, title, kept, box)
    text = Path(top_in).read_text()
    m = re.search(r"^(TIP3\s+)(\d+)\s*$", text, flags=re.M)
    if not m:
        raise RuntimeError("TIP3 molecule count not found in topology")
    old = int(m.group(2)); new = old - 1
    text = text[:m.start()] + f"{m.group(1)}{new}\n" + text[m.end():]
    Path(top_out).write_text(text)
    return old, new


def max_force_info(log_text):
    if "not finite" in log_text or re.search(r"Maximum force\s+=\s+inf", log_text):
        m = re.search(r"Maximum force\s+=\s+\S+\s+on atom\s+(\d+)", log_text)
        if not m:
            matches = re.findall(r"Fmax=\s*inf, atom=\s*(\d+)", log_text)
            if matches:
                return "inf", int(matches[-1])
        else:
            return "inf", int(m.group(1))
    m = re.search(r"Maximum force\s+=\s+([0-9.eE+-]+)\s+on atom\s+(\d+)", log_text)
    if m:
        return float(m.group(1)), int(m.group(2))
    return None, None

summary = []
for cand in candidates:
    gdir = ROOT / "systems" / cand / "gromacs"
    rundir = gdir / "run_min"
    if rundir.exists():
        shutil.rmtree(rundir)
    rundir.mkdir()
    current_gro = gdir / "step3_input.gro"
    current_top = gdir / "topol.top"
    repairs = []
    status = "failed"
    for attempt in range(MAX_REPAIRS + 1):
        prefix = f"min_attempt{attempt}"
        tpr = rundir / f"{prefix}.tpr"
        grompp_log = rundir / f"{prefix}.grompp.log"
        mdrun_log = rundir / f"{prefix}.mdrun.log"
        cmd = f"{GMX_ENV} && gmx grompp -f step4.0_minimization.mdp -o {tpr} -c {current_gro} -r {current_gro} -p {current_top} -n index.ndx -maxwarn 1"
        code, out = run_shell(cmd, cwd=gdir, log=grompp_log)
        if code != 0:
            status = "grompp_failed"
            break
        cmd = f"{GMX_ENV} && cd {rundir} && gmx mdrun -deffnm {prefix} -ntmpi 1 -ntomp {NTHREAD}"
        code, out = run_shell(cmd, cwd=gdir, log=mdrun_log)
        log_text = (rundir / f"{prefix}.log").read_text(errors="replace") if (rundir / f"{prefix}.log").exists() else out
        force, atom = max_force_info(log_text)
        if force != "inf" and force is not None and float(force) < 1000:
            # Promote successful final outputs to stable names
            for ext in ["gro", "edr", "log", "trr", "tpr"]:
                src = rundir / f"{prefix}.{ext}"
                if src.exists():
                    shutil.copy2(src, rundir / f"step4.0_minimization.{ext}")
            shutil.copy2(current_gro, rundir / "step3_input_cleaned.gro")
            shutil.copy2(current_top, rundir / "topol_cleaned.top")
            status = "minimized"
            break
        if force == "inf" and atom is not None and attempt < MAX_REPAIRS:
            resnr, reason = find_repair_residue(current_gro, atom)
            if resnr is None:
                status = f"repair_failed:{reason}"
                break
            new_gro = rundir / f"clean_attempt{attempt+1}.gro"
            new_top = gdir / f"topol_clean_attempt{attempt+1}.top"
            old, new = remove_water(current_gro, current_top, new_gro, new_top, resnr)
            repairs.append(f"attempt{attempt}:atom{atom}:{reason}:TIP3 {old}->{new}")
            current_gro, current_top = new_gro, new_top
            continue
        status = f"not_converged:force={force}:atom={atom}"
        break
    (rundir / "repair_summary.txt").write_text("\n".join(repairs) + ("\n" if repairs else ""))
    summary.append({"candidate_id": cand, "status": status, "repairs": ";".join(repairs), "run_dir": str(rundir)})

with open(ROOT / "minimization_summary.tsv", "w", newline="") as f:
    fields = ["candidate_id", "status", "repairs", "run_dir"]
    w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
    w.writeheader(); w.writerows(summary)

for row in summary:
    print(row["candidate_id"], row["status"], row["repairs"])
