# NaCl Production Worker Status

Last updated: 2026-06-18 14:12 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | Second AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | Running in parallel across all 8 candidates |
| Worker pool | `LISPER_JOBS=8`, `LISPER_NTHREAD_PER_JOB=16` |
| Effective CPU quota | 12 cores on the second AutoDL container |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- The first sequential single-candidate launcher was replaced by the tracked parallel launcher so all ready NaCl candidates run concurrently on the second worker.
- Active trajectories are not synced locally while production is running.
