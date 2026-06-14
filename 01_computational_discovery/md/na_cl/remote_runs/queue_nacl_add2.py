from pathlib import Path
import csv
import os
import shutil
import subprocess
import time

ROOT = Path("/root/LiSPER_remote/LiSPER_NaCl")
WAIT_FOR_PID = os.environ.get("WAIT_FOR_PID", "").strip()
ADD_CANDIDATES = ["LiD3-1", "StrongBind-Li"]


def wait_for_pid():
    if not WAIT_FOR_PID:
        return
    while Path(f"/proc/{WAIT_FOR_PID}").exists():
        time.sleep(60)


def run(cmd, log_path):
    proc = subprocess.run(
        cmd,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    Path(log_path).write_text(proc.stdout)
    if proc.returncode != 0:
        raise SystemExit(f"Command failed ({proc.returncode}): {cmd}\nSee {log_path}")


def read_tsv(path):
    if not path.exists():
        return [], []
    with path.open() as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path, fieldnames, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def candidate_order():
    fields, rows = read_tsv(ROOT / "ready_gromacs_systems.full.tsv")
    if not rows:
        fields, rows = read_tsv(ROOT / "ready_gromacs_systems.tsv")
    return [row["candidate_id"] for row in rows]


def merge_summary(base_path, add_path):
    fieldnames, base_rows = read_tsv(base_path)
    add_fields, add_rows = read_tsv(add_path)
    if not fieldnames:
        fieldnames = add_fields
    merged = {row["candidate_id"]: row for row in base_rows}
    for row in add_rows:
        merged[row["candidate_id"]] = row
    order = candidate_order()
    rows = [merged[candidate] for candidate in order if candidate in merged]
    rows.extend(row for candidate, row in merged.items() if candidate not in order)
    write_tsv(base_path, fieldnames, rows)


def main():
    wait_for_pid()

    remote_runs = ROOT / "remote_runs"
    remote_runs.mkdir(parents=True, exist_ok=True)

    ready_path = ROOT / "ready_gromacs_systems.tsv"
    full_ready = ROOT / "ready_gromacs_systems.full.tsv"
    shutil.copy2(ready_path, full_ready)
    fields, ready_rows = read_tsv(full_ready)
    add_ready = [row for row in ready_rows if row["candidate_id"] in ADD_CANDIDATES]
    if len(add_ready) != len(ADD_CANDIDATES):
        found = {row["candidate_id"] for row in add_ready}
        missing = [candidate for candidate in ADD_CANDIDATES if candidate not in found]
        raise SystemExit(f"Missing candidates from ready table: {missing}")

    min_summary = ROOT / "minimization_summary.tsv"
    eq_summary = ROOT / "equilibration_summary.tsv"
    if min_summary.exists():
        shutil.copy2(min_summary, remote_runs / "minimization_summary_before_add2.tsv")
    if eq_summary.exists():
        shutil.copy2(eq_summary, remote_runs / "equilibration_summary_before_add2.tsv")

    write_tsv(ready_path, fields, add_ready)

    run(
        "python3 /root/LiSPER_remote/run_lisper_nacl_minimize.py",
        remote_runs / "nacl_add2_minimize.stdout.log",
    )
    shutil.copy2(min_summary, remote_runs / "minimization_summary_add2.tsv")

    run(
        "python3 /root/LiSPER_remote/run_lisper_nacl_equilibrate.py",
        remote_runs / "nacl_add2_equilibrate.stdout.log",
    )
    shutil.copy2(eq_summary, remote_runs / "equilibration_summary_add2.tsv")

    before_min = remote_runs / "minimization_summary_before_add2.tsv"
    before_eq = remote_runs / "equilibration_summary_before_add2.tsv"
    if before_min.exists():
        shutil.copy2(before_min, min_summary)
        merge_summary(min_summary, remote_runs / "minimization_summary_add2.tsv")
    if before_eq.exists():
        shutil.copy2(before_eq, eq_summary)
        merge_summary(eq_summary, remote_runs / "equilibration_summary_add2.tsv")

    shutil.copy2(full_ready, ready_path)
    print("NaCl add2 complete:", ", ".join(ADD_CANDIDATES))


if __name__ == "__main__":
    main()
