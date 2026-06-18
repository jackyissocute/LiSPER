# LiCl Production Worker Status

Last updated: 2026-06-19 02:47 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | LiCl |
| Candidate set | Final 8-candidate LiCl systems |
| Worker | Original AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | Running in parallel across all 8 candidates |
| Production progress | `1.09-3.78 ns / 20 ns` across active jobs |
| Current leader | `LiDA-1` at `3.78 ns / 20 ns` |
| Worker pool | `LISPER_JOBS=8`, `LISPER_NTHREAD_PER_JOB=2` |
| Effective CPU quota | 16 cores on the original AutoDL container |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | `1.66 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `1.10 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `1.09 ns / 20 ns`; clustering queued |
| `LiLC-1` | `1.69 ns / 20 ns`; clustering queued |
| `LiDS-1` | `2.58 ns / 20 ns`; clustering queued |
| `LiDA-1` | `3.78 ns / 20 ns`; clustering queued |
| `LiN3-Core` | `1.70 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `1.65 ns / 20 ns`; clustering queued |

## Notes

- LiCl minimization and equilibration are complete for all eight candidates.
- Production and clustering were launched only after confirming no active LiCl production duplicate was running.
- Active trajectories are not synced locally while production is running.
