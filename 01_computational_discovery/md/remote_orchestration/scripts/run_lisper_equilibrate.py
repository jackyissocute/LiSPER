from pathlib import Path
import csv
import shutil
import subprocess

ROOT = Path("/root/LiSPER_remote/LiSPER_LiCl")
GMX_ENV = "source /root/miniconda3/etc/profile.d/conda.sh && conda activate lisper-gmx"
NTHREAD = 16


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


def write_solu_solv_index(gro_path, ndx_path):
    lines = Path(gro_path).read_text().splitlines()
    protein_positions = []
    solvent_positions = []

    for pos, line in enumerate(lines[2:-1], start=1):
        resname = line[5:10].strip()
        if resname in {"TIP3", "LIT", "CLA", "SOD"}:
            solvent_positions.append(pos)
        else:
            protein_positions.append(pos)

    def write_group(name, values):
        out = [f"[ {name} ]"]
        for i in range(0, len(values), 15):
            out.append(" ".join(f"{value:5d}" for value in values[i : i + 15]))
        return out

    all_positions = list(range(1, len(lines) - 2 + 1))
    out = []
    out.extend(write_group("SOLU", protein_positions))
    out.append("")
    out.extend(write_group("SOLV", solvent_positions))
    out.append("")
    out.extend(write_group("SYSTEM", all_positions))
    Path(ndx_path).write_text("\n".join(out) + "\n")


with open(ROOT / "minimization_summary.tsv") as handle:
    rows = [
        row
        for row in csv.DictReader(handle, delimiter="\t")
        if row["status"] == "minimized"
    ]

summary = []

for row in rows:
    candidate = row["candidate_id"]
    gromacs_dir = ROOT / "systems" / candidate / "gromacs"
    minimization_dir = gromacs_dir / "run_min"
    equilibration_dir = gromacs_dir / "run_eq"

    if equilibration_dir.exists():
        shutil.rmtree(equilibration_dir)
    equilibration_dir.mkdir()

    clean_topologies = sorted(gromacs_dir.glob("topol_clean_attempt*.top"))
    topology = clean_topologies[-1] if clean_topologies else gromacs_dir / "topol.top"
    coordinates = minimization_dir / "step4.0_minimization.gro"
    restraints = minimization_dir / "step3_input_cleaned.gro"
    index = equilibration_dir / "index_clean.ndx"
    tpr = equilibration_dir / "step4.1_equilibration.tpr"

    write_solu_solv_index(coordinates, index)

    grompp = (
        f"{GMX_ENV} && "
        f"gmx grompp -f step4.1_equilibration.mdp "
        f"-o {tpr} "
        f"-c {coordinates} "
        f"-r {restraints} "
        f"-p {topology} "
        f"-n {index} "
        f"-maxwarn 1"
    )
    code, _ = run_shell(
        grompp,
        cwd=gromacs_dir,
        log=equilibration_dir / "step4.1_equilibration.grompp.log",
    )
    if code != 0:
        summary.append(
            {
                "candidate_id": candidate,
                "status": "grompp_failed",
                "run_dir": str(equilibration_dir),
            }
        )
        continue

    mdrun = (
        f"{GMX_ENV} && "
        f"cd {equilibration_dir} && "
        f"OMP_NUM_THREADS={NTHREAD} "
        f"gmx mdrun -deffnm step4.1_equilibration "
        f"-ntmpi 1 -ntomp {NTHREAD}"
    )
    code, _ = run_shell(
        mdrun,
        cwd=gromacs_dir,
        log=equilibration_dir / "step4.1_equilibration.mdrun.stdout.log",
    )
    log = equilibration_dir / "step4.1_equilibration.log"
    status = (
        "equilibrated"
        if code == 0 and log.exists() and "Finished mdrun" in log.read_text(errors="replace")
        else "mdrun_failed"
    )
    summary.append(
        {
            "candidate_id": candidate,
            "status": status,
            "run_dir": str(equilibration_dir),
        }
    )

with open(ROOT / "equilibration_summary.tsv", "w", newline="") as handle:
    fieldnames = ["candidate_id", "status", "run_dir"]
    writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    writer.writerows(summary)

for item in summary:
    print(item["candidate_id"], item["status"])
