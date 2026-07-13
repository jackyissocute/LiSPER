# Worker A Cleanup Snapshot - 2026-06-28 19:05 CST

## Action

- Preserved a filtered local snapshot of the inactive 10-candidate legacy workspace before cleanup.
- Removed the inactive remote legacy archive from Worker A.
- Worker A disk usage improved from `96%` used (`1.4 GB` free) to `80%` used (`6.1 GB` free).

## Preserved Locally

- Local safety snapshot: `01_computational_discovery/md/remote_runs/legacy_10_candidate_runs_workerA_snapshot/`
- Snapshot size: `1.4 GB`
- Snapshot file count: `945`
- Snapshot scope: summary tables, logs, structures, topology/config files, and small diagnostic artifacts.
- Excluded from snapshot: heavy trajectory/checkpoint/binary time-series files such as `.xtc`, `.trr`, `.tpr`, `.edr`, `.cpt`, and `.xvg`.

## GitHub Policy

The local safety snapshot is intentionally ignored by Git because it is too large for normal GitHub commits. This repository preserves the cleanup manifest, public progress dashboards, current refined umbrella outputs, and QC/status files in Git. Large raw trajectory-scale artifacts remain local or on active compute storage unless a separate large-data archive is set up.

## Remote Safety Check

No active `mdrun` working directory was inside the legacy archive before removal. Active production and refined umbrella directories were not modified.
