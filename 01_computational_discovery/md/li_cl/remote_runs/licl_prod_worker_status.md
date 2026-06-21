# LiCl Production Worker Status

Last updated: 2026-06-21 12:07 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | LiCl |
| Candidate set | Final 8-candidate LiCl systems |
| Worker | Original AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | 6 active LiCl jobs + 2 completed/clustered representatives |
| Production progress | `8.61-13.30 ns / 20 ns` across active LiCl jobs |
| Current leader | `LiDS-1` and `LiDA-1` at `20.00 ns / 20 ns`, both representative-ready |
| Worker pool | LiCl: 6 active jobs x 2 OpenMP threads; Worker A also carries 2 NaCl backfill jobs x 1 thread |
| Effective CPU quota | 14/16 active threads on Worker A; 2 cores are free but no safe ready-made umbrella task is currently present |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | `13.09 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `8.63 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `8.61 ns / 20 ns`; clustering queued |
| `LiLC-1` | `13.22 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%` |
| `LiN3-Core` | `13.30 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `12.97 ns / 20 ns`; clustering queued |

## Notes

- LiCl minimization and equilibration are complete for all eight candidates.
- Production and clustering were launched only after confirming no active LiCl production duplicate was running.
- `LiDA-1` is now paired with a NaCl representative and is ready for umbrella-window design once the protocol/launcher is written.
- Active trajectories are not synced locally while production is running.
