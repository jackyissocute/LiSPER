from pathlib import Path
import csv
import os
import subprocess

ROOT = Path(os.environ.get("LISPER_WORKDIR", "/root/LiSPER_remote/LiSPER_LiCl"))
GMX_ENV = "source /root/miniconda3/etc/profile.d/conda.sh && conda activate lisper-gmx"
NTHREAD = int(os.environ.get("LISPER_REPAIR_NTHREAD", "1"))
CLUSTER_CUTOFF_NM = float(os.environ.get("LISPER_CLUSTER_CUTOFF_NM", "0.20"))
CANDIDATES = [
    item.strip()
    for item in os.environ.get("LISPER_REPAIR_CANDIDATES", "LiD3-1,IDP-Li-1").split(",")
    if item.strip()
]


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


def produced_candidates():
    produced = set()
    summary = ROOT / "production_clustering_summary.tsv"
    if summary.exists():
        with summary.open() as handle:
            rows = csv.DictReader(handle, delimiter="\t")
            produced.update(row["candidate_id"] for row in rows if row.get("production_status") == "produced")
    for candidate in CANDIDATES:
        prod_log = ROOT / "systems" / candidate / "gromacs" / "run_prod_20ns" / "step5_production_20ns.log"
        if prod_log.exists() and "Finished mdrun" in prod_log.read_text(errors="replace"):
            produced.add(candidate)
    return produced


def repair_candidate(candidate):
    gromacs_dir = ROOT / "systems" / candidate / "gromacs"
    prod_dir = gromacs_dir / "run_prod_20ns"
    eq_dir = gromacs_dir / "run_eq"
    repair_dir = gromacs_dir / "cluster_20ns_repair"
    repair_dir.mkdir(parents=True, exist_ok=True)

    tpr = prod_dir / "step5_production_20ns.tpr"
    xtc = prod_dir / "step5_production_20ns.xtc"
    final_gro = prod_dir / "step5_production_20ns.gro"
    index = eq_dir / "index_clean.ndx"

    required = [tpr, xtc, final_gro, index]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        return {
            "candidate_id": candidate,
            "repair_status": "missing_inputs",
            "detail": ";".join(missing),
        }

    ref_solu = repair_dir / "final_solu_reference.gro"
    centered_solu = repair_dir / "production_20ns_solu_centered.xtc"
    representative = repair_dir / "representative_top_cluster.pdb"

    rc, _ = run_shell(
        f"{GMX_ENV} && OMP_NUM_THREADS={NTHREAD} gmx trjconv "
        f"-s {tpr} -f {final_gro} -o {ref_solu} -n {index}",
        cwd=gromacs_dir,
        log=repair_dir / "make_solu_reference.log",
        stdin="0\n",
    )
    if rc != 0:
        return {
            "candidate_id": candidate,
            "repair_status": "reference_failed",
            "detail": str(repair_dir / "make_solu_reference.log"),
        }

    rc, _ = run_shell(
        f"{GMX_ENV} && OMP_NUM_THREADS={NTHREAD} gmx trjconv "
        f"-s {tpr} -f {xtc} -o {centered_solu} -n {index} -pbc mol -center",
        cwd=gromacs_dir,
        log=repair_dir / "trjconv_solu_center.log",
        stdin="0\n0\n",
    )
    if rc != 0:
        return {
            "candidate_id": candidate,
            "repair_status": "trjconv_failed",
            "detail": str(repair_dir / "trjconv_solu_center.log"),
        }

    rc, _ = run_shell(
        f"{GMX_ENV} && OMP_NUM_THREADS={NTHREAD} gmx cluster "
        f"-s {ref_solu} -f {centered_solu} "
        f"-method gromos -cutoff {CLUSTER_CUTOFF_NM:.3f} "
        f"-o {repair_dir / 'clusters.xpm'} "
        f"-g {repair_dir / 'cluster.log'} "
        f"-sz {repair_dir / 'cluster_size.xvg'} "
        f"-clid {repair_dir / 'cluster_id.xvg'} "
        f"-cl {representative}",
        cwd=gromacs_dir,
        log=repair_dir / "gmx_cluster.log",
        stdin="0\n0\n",
    )
    if rc != 0:
        return {
            "candidate_id": candidate,
            "repair_status": "cluster_failed",
            "detail": str(repair_dir / "gmx_cluster.log"),
        }

    status = "clustered" if representative.exists() else "cluster_missing_representative"
    return {
        "candidate_id": candidate,
        "repair_status": status,
        "detail": str(representative),
    }


def main():
    produced = produced_candidates()
    rows = []
    for candidate in CANDIDATES:
        if candidate not in produced:
            rows.append(
                {
                    "candidate_id": candidate,
                    "repair_status": "not_produced",
                    "detail": "production not marked produced in summary",
                }
            )
            continue
        rows.append(repair_candidate(candidate))

    out = ROOT / "remote_runs" / "clustering_repair_summary.tsv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["candidate_id", "repair_status", "detail"],
            delimiter="\t",
        )
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
