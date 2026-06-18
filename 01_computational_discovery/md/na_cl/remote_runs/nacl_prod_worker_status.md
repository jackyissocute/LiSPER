# NaCl Production Worker Status

Last updated: 2026-06-19 05:49 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | Second AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | Running in parallel across all 8 candidates |
| Production progress | `0.07-0.38 ns / 20 ns` across active jobs |
| Current leader | `LiDA-1` at `0.38 ns / 20 ns` |
| Worker pool | `LISPER_JOBS=8`, `LISPER_NTHREAD_PER_JOB=16` |
| Effective CPU quota | 12 cores on the second AutoDL container |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | `0.09 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `0.07 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `0.12 ns / 20 ns`; clustering queued |
| `LiLC-1` | `0.18 ns / 20 ns`; clustering queued |
| `LiDS-1` | `0.27 ns / 20 ns`; clustering queued |
| `LiDA-1` | `0.38 ns / 20 ns`; clustering queued |
| `LiN3-Core` | `0.09 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `0.09 ns / 20 ns`; clustering queued |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- The first sequential single-candidate launcher was replaced by the tracked parallel launcher so all ready NaCl candidates run concurrently on the second worker.
- Active trajectories are not synced locally while production is running.
