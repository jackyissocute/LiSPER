from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import csv
import os
import re
import subprocess

ROOT = Path(os.environ.get("LISPER_WORKDIR", "/root/LiSPER_remote/LiSPER_8cand_LiCl"))
GMX_ENV = "source /root/miniconda3/etc/profile.d/conda.sh && conda activate lisper-gmx"
NTHREAD = int(os.environ.get("LISPER_CLUSTER_NTHREAD", "2"))
NJOBS = int(os.environ.get("LISPER_CLUSTER_JOBS", "3"))
CLUSTER_CUTOFF_NM = float(os.environ.get("LISPER_CLUSTER_CUTOFF_NM", "0.20"))
CANDIDATES = [
    item.strip()
    for item in os.environ.get("LISPER_CLUSTER_CANDIDATES", "").split(",")
    if item.strip()
]


def run_shell(cmd, cwd, log, stdin=None):
    proc = subprocess.run(
        f"bash -lc {cmd!r}",
        shell=True,
        cwd=cwd,
        input=stdin,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    Path(log).write_text(proc.stdout)
    return proc.returncode


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
                pass
    if not values:
        return "", "", ""
    total = sum(size for _, size in values)
    top_cluster, top_size = max(values, key=lambda item: item[1])
    population = 100.0 * top_size / total if total else 0.0
    return str(top_cluster), str(int(top_size)), f"{population:.2f}"


def cluster_candidate(candidate):
    gromacs_dir = ROOT / "systems" / candidate / "gromacs"
    prod_dir = gromacs_dir / "run_prod_20ns"
    eq_dir = gromacs_dir / "run_eq"
    cluster_dir = gromacs_dir / "cluster_20ns"
    cluster_dir.mkdir(exist_ok=True)

    representative = cluster_dir / "representative_top_cluster.pdb"
    if representative.exists():
        top, frames, pop = parse_cluster_population(cluster_dir / "cluster_size.xvg")
        return {
            "candidate_id": candidate,
            "status": "already_clustered",
            "top_cluster_id": top,
            "top_cluster_frames": frames,
            "top_cluster_population_percent": pop,
            "detail": str(representative),
        }

    prod_log = prod_dir / "step5_production_20ns.log"
    if not production_finished(prod_log):
        return {
            "candidate_id": candidate,
            "status": "not_finished",
            "top_cluster_id": "",
            "top_cluster_frames": "",
            "top_cluster_population_percent": "",
            "detail": str(prod_log),
        }

    tpr = prod_dir / "step5_production_20ns.tpr"
    xtc = prod_dir / "step5_production_20ns.xtc"
    final_gro = prod_dir / "step5_production_20ns.gro"
    index = eq_dir / "index_clean.ndx"
    missing = [str(path) for path in (tpr, xtc, final_gro, index) if not path.exists()]
    if missing:
        return {
            "candidate_id": candidate,
            "status": "missing_inputs",
            "top_cluster_id": "",
            "top_cluster_frames": "",
            "top_cluster_population_percent": "",
            "detail": ";".join(missing),
        }

    ref_solu = cluster_dir / "final_solu_reference.gro"
    centered_solu = cluster_dir / "production_20ns_solu_centered.xtc"
    rc = run_shell(
        f"{GMX_ENV} && OMP_NUM_THREADS={NTHREAD} "
        f"gmx trjconv -s {tpr} -f {final_gro} -o {ref_solu} -n {index}",
        gromacs_dir,
        cluster_dir / "make_solu_reference.log",
        "0\n",
    )
    if rc:
        return {
            "candidate_id": candidate,
            "status": "reference_failed",
            "top_cluster_id": "",
            "top_cluster_frames": "",
            "top_cluster_population_percent": "",
            "detail": str(cluster_dir / "make_solu_reference.log"),
        }

    rc = run_shell(
        f"{GMX_ENV} && OMP_NUM_THREADS={NTHREAD} "
        f"gmx trjconv -s {tpr} -f {xtc} -o {centered_solu} -n {index} -pbc mol -center",
        gromacs_dir,
        cluster_dir / "trjconv_solu_center.log",
        "0\n0\n",
    )
    if rc:
        return {
            "candidate_id": candidate,
            "status": "trjconv_failed",
            "top_cluster_id": "",
            "top_cluster_frames": "",
            "top_cluster_population_percent": "",
            "detail": str(cluster_dir / "trjconv_solu_center.log"),
        }

    rc = run_shell(
        f"{GMX_ENV} && OMP_NUM_THREADS={NTHREAD} "
        f"gmx cluster -s {ref_solu} -f {centered_solu} "
        f"-method gromos -cutoff {CLUSTER_CUTOFF_NM:.3f} "
        f"-o {cluster_dir / 'clusters.xpm'} "
        f"-g {cluster_dir / 'cluster.log'} "
        f"-sz {cluster_dir / 'cluster_size.xvg'} "
        f"-clid {cluster_dir / 'cluster_id.xvg'} "
        f"-cl {representative}",
        gromacs_dir,
        cluster_dir / "gmx_cluster.stdout.log",
        "0\n0\n",
    )
    top, frames, pop = parse_cluster_population(cluster_dir / "cluster_size.xvg")
    return {
        "candidate_id": candidate,
        "status": "clustered" if rc == 0 and representative.exists() else "cluster_failed",
        "top_cluster_id": top,
        "top_cluster_frames": frames,
        "top_cluster_population_percent": pop,
        "detail": str(representative if representative.exists() else cluster_dir / "gmx_cluster.stdout.log"),
    }


def main():
    if not CANDIDATES:
        raise SystemExit("Set LISPER_CLUSTER_CANDIDATES")
    rows = []
    summary = ROOT / "remote_runs" / "cluster_ready_summary.tsv"
    summary.parent.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=NJOBS) as pool:
        futures = [pool.submit(cluster_candidate, candidate) for candidate in CANDIDATES]
        for future in as_completed(futures):
            rows.append(future.result())
            with summary.open("w", newline="") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=[
                        "candidate_id",
                        "status",
                        "top_cluster_id",
                        "top_cluster_frames",
                        "top_cluster_population_percent",
                        "detail",
                    ],
                    delimiter="\t",
                )
                writer.writeheader()
                writer.writerows(sorted(rows, key=lambda row: row["candidate_id"]))
    print(summary)


if __name__ == "__main__":
    main()
