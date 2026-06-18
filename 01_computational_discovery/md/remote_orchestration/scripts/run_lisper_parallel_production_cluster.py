from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import csv
import os
import re
import subprocess
import threading

ROOT = Path(os.environ.get("LISPER_WORKDIR", "/root/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker"))
GMX_ENV = "source /root/miniconda3/etc/profile.d/conda.sh && conda activate lisper-gmx"
NJOBS = int(os.environ.get("LISPER_JOBS", "4"))
NTHREAD = int(os.environ.get("LISPER_NTHREAD_PER_JOB", "16"))
NPROD_STEPS = int(os.environ.get("LISPER_PROD_STEPS", "10000000"))
XTC_EVERY_STEPS = int(os.environ.get("LISPER_XTC_EVERY_STEPS", "5000"))
CLUSTER_CUTOFF_NM = float(os.environ.get("LISPER_CLUSTER_CUTOFF_NM", "0.20"))
SUMMARY = ROOT / "production_clustering_summary.tsv"
FIELDNAMES = [
    "candidate_id",
    "production_status",
    "cluster_status",
    "top_cluster_id",
    "top_cluster_frames",
    "top_cluster_population_percent",
    "production_wall_s",
    "production_ns_per_day",
    "production_hour_per_ns",
    "production_finished_at",
    "production_dir",
    "cluster_dir",
]
summary_lock = threading.Lock()
rows_by_candidate = {}


def run_shell(cmd, cwd=None, log=None, stdin=None):
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


def update_mdp(template, output):
    text = Path(template).read_text()
    replacements = {
        "nsteps": str(NPROD_STEPS),
        "nstxout-compressed": str(XTC_EVERY_STEPS),
        "nstenergy": str(XTC_EVERY_STEPS),
        "nstlog": str(XTC_EVERY_STEPS),
    }
    lines = []
    seen = set()
    for line in text.splitlines():
        stripped = line.strip()
        key = stripped.split("=", 1)[0].strip() if "=" in stripped else ""
        if key in replacements:
            lines.append(f"{key:<24}= {replacements[key]}")
            seen.add(key)
        else:
            lines.append(line)
    for key, value in replacements.items():
        if key not in seen:
            lines.append(f"{key:<24}= {value}")
    Path(output).write_text("\n".join(lines) + "\n")


def topology_for(gromacs_dir):
    topologies = sorted(gromacs_dir.glob("topol_clean_attempt*.top"))
    if topologies:
        return topologies[-1]
    cleaned = gromacs_dir / "run_min" / "topol_cleaned.top"
    if cleaned.exists():
        production_topology = gromacs_dir / "topol_cleaned_for_prod.top"
        if not production_topology.exists():
            production_topology.write_text(cleaned.read_text())
        return production_topology
    return gromacs_dir / "topol.top"


def read_equilibrated_candidates():
    with (ROOT / "equilibration_summary.tsv").open() as handle:
        return [
            row["candidate_id"]
            for row in csv.DictReader(handle, delimiter="\t")
            if row["status"] == "equilibrated"
        ]


def parse_performance(log_path):
    if not log_path.exists():
        return "", "", "", ""
    text = log_path.read_text(errors="replace")
    wall = ns_per_day = hour_per_ns = finished = ""
    match = re.search(r"Time:\s+\S+\s+(\S+)\s+\S+", text)
    if match:
        wall = match.group(1)
    match = re.search(r"Performance:\s+(\S+)\s+(\S+)", text)
    if match:
        ns_per_day = match.group(1)
        hour_per_ns = match.group(2)
    match = re.search(r"Finished mdrun on rank 0 (.+)", text)
    if match:
        finished = match.group(1).strip()
    return wall, ns_per_day, hour_per_ns, finished


def production_finished(prod_log):
    return prod_log.exists() and "Finished mdrun" in prod_log.read_text(errors="replace")


def parse_cluster_population(size_xvg):
    values = []
    if not size_xvg.exists():
        return "", "", ""
    for line in size_xvg.read_text(errors="replace").splitlines():
        if not line or line.startswith(("#", "@")):
            continue
        parts = line.split()
        if len(parts) >= 2:
            try:
                values.append((int(float(parts[0])), float(parts[1])))
            except ValueError:
                continue
    if not values:
        return "", "", ""
    total = sum(size for _, size in values)
    top_cluster, top_size = max(values, key=lambda item: item[1])
    population = 100.0 * top_size / total if total else 0.0
    return str(top_cluster), str(int(top_size)), f"{population:.2f}"


def write_summary():
    with SUMMARY.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, delimiter="\t")
        writer.writeheader()
        for candidate in sorted(rows_by_candidate):
            row = rows_by_candidate[candidate]
            writer.writerow({field: row.get(field, "") for field in FIELDNAMES})


def record(row):
    with summary_lock:
        rows_by_candidate[row["candidate_id"]] = row
        write_summary()


def run_candidate(candidate):
    gromacs_dir = ROOT / "systems" / candidate / "gromacs"
    eq_dir = gromacs_dir / "run_eq"
    prod_dir = gromacs_dir / "run_prod_20ns"
    cluster_dir = gromacs_dir / "cluster_20ns"
    prod_dir.mkdir(exist_ok=True)
    cluster_dir.mkdir(exist_ok=True)

    mdp = prod_dir / "step5_production_20ns.mdp"
    if not mdp.exists():
        update_mdp(gromacs_dir / "step5_production.mdp", mdp)
    topology = topology_for(gromacs_dir)
    coordinates = eq_dir / "step4.1_equilibration.gro"
    index = eq_dir / "index_clean.ndx"
    tpr = prod_dir / "step5_production_20ns.tpr"
    prod_log = prod_dir / "step5_production_20ns.log"

    if not tpr.exists():
        code, _ = run_shell(
            f"{GMX_ENV} && gmx grompp -f {mdp} -o {tpr} -c {coordinates} "
            f"-p {topology} -n {index} -maxwarn 1",
            cwd=gromacs_dir,
            log=prod_dir / "step5_production_20ns.grompp.log",
        )
        if code != 0:
            return {"candidate_id": candidate, "production_status": "grompp_failed"}

    if not production_finished(prod_log):
        cpt = prod_dir / "step5_production_20ns.cpt"
        cpi = f"-cpi {cpt} -append" if cpt.exists() else ""
        code, _ = run_shell(
            f"{GMX_ENV} && cd {prod_dir} && OMP_NUM_THREADS={NTHREAD} "
            f"gmx mdrun -deffnm step5_production_20ns {cpi} -ntmpi 1 -ntomp {NTHREAD}",
            cwd=gromacs_dir,
            log=prod_dir / "step5_production_20ns.mdrun.stdout.log",
        )
        if code != 0 or not production_finished(prod_log):
            wall, ns_per_day, hour_per_ns, finished = parse_performance(prod_log)
            return {
                "candidate_id": candidate,
                "production_status": "mdrun_failed",
                "production_wall_s": wall,
                "production_ns_per_day": ns_per_day,
                "production_hour_per_ns": hour_per_ns,
                "production_finished_at": finished,
            }

    ref_solu = cluster_dir / "final_solu_reference.gro"
    centered_solu = cluster_dir / "production_20ns_solu_centered.xtc"
    representative = cluster_dir / "representative_top_cluster.pdb"

    if not representative.exists():
        code, _ = run_shell(
            f"{GMX_ENV} && OMP_NUM_THREADS={NTHREAD} "
            f"gmx trjconv -s {tpr} -f {prod_dir / 'step5_production_20ns.gro'} "
            f"-o {ref_solu} -n {index}",
            cwd=gromacs_dir,
            log=cluster_dir / "make_solu_reference.log",
            stdin="0\n",
        )
        if code != 0:
            wall, ns_per_day, hour_per_ns, finished = parse_performance(prod_log)
            return {
                "candidate_id": candidate,
                "production_status": "produced",
                "cluster_status": "reference_failed",
                "production_wall_s": wall,
                "production_ns_per_day": ns_per_day,
                "production_hour_per_ns": hour_per_ns,
                "production_finished_at": finished,
            }

        code, _ = run_shell(
            f"{GMX_ENV} && OMP_NUM_THREADS={NTHREAD} "
            f"gmx trjconv -s {tpr} -f {prod_dir / 'step5_production_20ns.xtc'} "
            f"-o {centered_solu} -n {index} -pbc mol -center",
            cwd=gromacs_dir,
            log=cluster_dir / "trjconv_solu_center.log",
            stdin="0\n0\n",
        )
        if code != 0:
            wall, ns_per_day, hour_per_ns, finished = parse_performance(prod_log)
            return {
                "candidate_id": candidate,
                "production_status": "produced",
                "cluster_status": "trjconv_failed",
                "production_wall_s": wall,
                "production_ns_per_day": ns_per_day,
                "production_hour_per_ns": hour_per_ns,
                "production_finished_at": finished,
            }

        code, _ = run_shell(
            f"{GMX_ENV} && OMP_NUM_THREADS={NTHREAD} "
            f"gmx cluster -s {ref_solu} -f {centered_solu} "
            f"-method gromos -cutoff {CLUSTER_CUTOFF_NM} "
            f"-o {cluster_dir / 'clusters.xpm'} "
            f"-g {cluster_dir / 'cluster.log'} "
            f"-cl {representative} "
            f"-clid {cluster_dir / 'cluster_id.xvg'} "
            f"-sz {cluster_dir / 'cluster_size.xvg'}",
            cwd=gromacs_dir,
            log=cluster_dir / "gmx_cluster.stdout.log",
            stdin="0\n0\n",
        )
        cluster_status = "clustered" if code == 0 else "cluster_failed"
    else:
        cluster_status = "clustered"

    top_cluster, top_size, top_population = parse_cluster_population(cluster_dir / "cluster_size.xvg")
    wall, ns_per_day, hour_per_ns, finished = parse_performance(prod_log)
    return {
        "candidate_id": candidate,
        "production_status": "produced",
        "cluster_status": cluster_status,
        "top_cluster_id": top_cluster,
        "top_cluster_frames": top_size,
        "top_cluster_population_percent": top_population,
        "production_wall_s": wall,
        "production_ns_per_day": ns_per_day,
        "production_hour_per_ns": hour_per_ns,
        "production_finished_at": finished,
        "production_dir": str(prod_dir),
        "cluster_dir": str(cluster_dir),
    }


def main():
    candidates = read_equilibrated_candidates()
    print(f"Starting parallel production/clustering: candidates={len(candidates)} jobs={NJOBS} threads_per_job={NTHREAD}")
    with ThreadPoolExecutor(max_workers=NJOBS) as pool:
        futures = {pool.submit(run_candidate, candidate): candidate for candidate in candidates}
        for future in as_completed(futures):
            candidate = futures[future]
            try:
                row = future.result()
            except Exception as exc:
                row = {"candidate_id": candidate, "production_status": f"exception:{exc}"}
            record(row)
            print(candidate, row.get("production_status", ""), row.get("cluster_status", ""), flush=True)


if __name__ == "__main__":
    main()
