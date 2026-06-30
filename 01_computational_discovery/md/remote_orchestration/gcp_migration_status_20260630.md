# GCP Migration Steward Snapshot - 2026-06-30 13:15 CST

## Current State

The active LiSPER MD/umbrella workload has been migrated onto the 32-core GCP runner. The runner is carrying active umbrella sampling, NaCl overflow production/clustering, and the LiDA-1 NaCl V4 tail-repair clean continuation.

Verified GCP snapshot:

| Item | Status |
|---|---|
| CPU worker | 32 vCPU GCP runner |
| Active GROMACS use | about 30/32 mdrun cores |
| Data disk | about 23 GB used, 76 GB free on `/mnt/lisper_data` |
| Active drivers | LiCl umbrella, NaCl umbrella, NaCl production/clustering, LiDA-1 V4 repair |
| Recent fatal errors | none found in the checked GCP logs |

## Shutdown-Safety Archive

Before treating AutoDL as disposable, recent small recovery/analysis files from both AutoDL workers were copied into a GCP safety archive:

`/mnt/lisper_data/LiSPER_remote/autodl_shutdown_archive/20260630_131115`

Archive contents:

| Source | Files | Size |
|---|---:|---:|
| AutoDL Worker A | 136 | 66 MB |
| AutoDL Worker B | 102 | 53 MB |
| Total | 238 | 118 MB |

The archive contains recent checkpoints, logs, `xvg`, `tsv`, `tpr`, `mdp`, and similar small recovery/QC files. It intentionally excludes active large trajectory files and does not overwrite the live GCP working directories.

## Handoff Interpretation

GCP can continue the scientific workflow independently. AutoDL has been left untouched for now, but the active jobs have a GCP counterpart and recent AutoDL recovery evidence has been preserved on the GCP disk. The next steward heartbeat should monitor GCP as the primary worker and use AutoDL only for backup comparison unless the user explicitly asks to shut it down.

## Next Scientific Gate

When LiDA-1 NaCl V4 tail repair finishes, sync the completed V4 outputs, rerun combined WHAM/bootstrap/time-slice QC, then classify the result as `PASS`, `REPAIR`, `WAIT-RUNNING`, or `BLOCKED`.
