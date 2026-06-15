from pathlib import Path
import os
import subprocess
import time

ROOT = Path(os.environ.get("LISPER_WORKDIR", "/root/LiSPER_remote/LiSPER_LiCl"))
REMOTE_ROOT = Path(os.environ.get("LISPER_REMOTE_ROOT", "/root/LiSPER_remote"))
WAIT_FOR_PID = os.environ.get("WAIT_FOR_PID", "").strip()
REPAIR_CANDIDATES = os.environ.get(
    "LISPER_REPAIR_CANDIDATES",
    "LiD3-1,LiND-1,IDP-Li-1,IDP-Li-2,LowCharge-Li,LiD2-IDP,StrongBind-Li,SoftCage-Li,IDP-Rich-Li,Control-Negative",
)
REQUEUE_CANDIDATES = os.environ.get(
    "LISPER_REQUEUE_CANDIDATES",
    "LiND-1,IDP-Li-2,LowCharge-Li,LiD2-IDP",
)


def wait_for_pid():
    if not WAIT_FOR_PID:
        return
    while Path(f"/proc/{WAIT_FOR_PID}").exists():
        time.sleep(60)


def run_step(name, command, log_path):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w") as log:
        log.write(f"# {name}\n")
        log.write(" ".join(command) + "\n\n")
        log.flush()
        return subprocess.run(command, stdout=log, stderr=subprocess.STDOUT).returncode


def main():
    wait_for_pid()
    remote_runs = ROOT / "remote_runs"

    repair_rc = run_step(
        "repair peptide-only clustering for completed LiCl productions",
        [
            "env",
            f"LISPER_WORKDIR={ROOT}",
            f"LISPER_REPAIR_CANDIDATES={REPAIR_CANDIDATES}",
            "python3",
            str(REMOTE_ROOT / "repair_completed_clustering.py"),
        ],
        remote_runs / "post_driver_repair_clustering.log",
    )

    requeue_rc = run_step(
        "requeue topology-failed LiCl productions",
        [
            "env",
            f"LISPER_WORKDIR={ROOT}",
            f"LISPER_REQUEUE_CANDIDATES={REQUEUE_CANDIDATES}",
            "python3",
            str(REMOTE_ROOT / "requeue_failed_production_cluster.py"),
        ],
        remote_runs / "post_driver_requeue_failed.log",
    )

    summary = remote_runs / "post_licl_driver_recovery.status"
    summary.write_text(
        "\n".join(
            [
                f"repair_clustering_exit_code={repair_rc}",
                f"requeue_failed_exit_code={requeue_rc}",
            ]
        )
        + "\n"
    )
    raise SystemExit(0 if repair_rc == 0 and requeue_rc == 0 else 1)


if __name__ == "__main__":
    main()
