from pathlib import Path
import csv
import os
import time

from run_lisper_production_cluster import ROOT, run_production_and_cluster

WAIT_FOR_PID = os.environ.get("WAIT_FOR_PID", "").strip()
CANDIDATES = [
    item.strip()
    for item in os.environ.get(
        "LISPER_REQUEUE_CANDIDATES",
        "LiND-1,IDP-Li-2,LowCharge-Li,LiD2-IDP",
    ).split(",")
    if item.strip()
]
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


def wait_for_pid():
    if not WAIT_FOR_PID:
        return
    while Path(f"/proc/{WAIT_FOR_PID}").exists():
        time.sleep(60)


def load_existing_summary(path):
    if not path.exists():
        return []
    with path.open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_summary(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in FIELDNAMES})


def merge_rows(existing, repaired):
    by_candidate = {row.get("candidate_id", ""): row for row in existing}
    for row in repaired:
        by_candidate[row["candidate_id"]] = row
    order = [row.get("candidate_id", "") for row in existing]
    for row in repaired:
        if row["candidate_id"] not in order:
            order.append(row["candidate_id"])
    return [by_candidate[candidate] for candidate in order if candidate]


def main():
    wait_for_pid()
    repaired_rows = []
    requeue_summary = ROOT / "remote_runs" / "production_clustering_requeue_summary.tsv"
    main_summary = ROOT / "production_clustering_summary.tsv"

    for candidate in CANDIDATES:
        row = run_production_and_cluster(candidate)
        repaired_rows.append(row)
        write_summary(requeue_summary, repaired_rows)
        merged = merge_rows(load_existing_summary(main_summary), repaired_rows)
        write_summary(main_summary, merged)
        print(candidate, row.get("production_status", ""), row.get("cluster_status", ""), flush=True)


if __name__ == "__main__":
    main()
