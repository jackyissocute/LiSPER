# LiCl Production Worker Status

Last updated: 2026-06-18 17:45 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | LiCl |
| Candidate set | Final 8-candidate LiCl systems |
| Worker | Original AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | Running in parallel across all 8 candidates |
| Worker pool | `LISPER_JOBS=8`, `LISPER_NTHREAD_PER_JOB=2` |
| Effective CPU quota | 16 cores on the original AutoDL container |

## Notes

- LiCl minimization and equilibration are complete for all eight candidates.
- Production and clustering were launched only after confirming no active LiCl production duplicate was running.
- Active trajectories are not synced locally while production is running.
