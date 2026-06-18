# LiCl Production Worker Status

Last updated: 2026-06-18 20:45 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | LiCl |
| Candidate set | Final 8-candidate LiCl systems |
| Worker | Original AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | Running in parallel across all 8 candidates |
| Production progress | `0.35-1.24 ns / 20 ns` across active jobs |
| Current leader | `LiDA-1` at `1.24 ns / 20 ns` |
| Worker pool | `LISPER_JOBS=8`, `LISPER_NTHREAD_PER_JOB=2` |
| Effective CPU quota | 16 cores on the original AutoDL container |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | `0.54 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `0.36 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `0.35 ns / 20 ns`; clustering queued |
| `LiLC-1` | `0.55 ns / 20 ns`; clustering queued |
| `LiDS-1` | `0.84 ns / 20 ns`; clustering queued |
| `LiDA-1` | `1.24 ns / 20 ns`; clustering queued |
| `LiN3-Core` | `0.55 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `0.54 ns / 20 ns`; clustering queued |

## Notes

- LiCl minimization and equilibration are complete for all eight candidates.
- Production and clustering were launched only after confirming no active LiCl production duplicate was running.
- Active trajectories are not synced locally while production is running.
