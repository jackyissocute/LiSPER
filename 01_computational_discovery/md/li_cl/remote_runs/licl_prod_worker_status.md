# LiCl Production Worker Status

Last updated: 2026-06-21 18:05 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | LiCl |
| Candidate set | Final 8-candidate LiCl systems |
| Worker | Original AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | 6 active LiCl jobs + 2 completed/clustered representatives |
| Production progress | `9.26-14.31 ns / 20 ns` across active LiCl jobs |
| Current leader | `LiDS-1` and `LiDA-1` at `20.00 ns / 20 ns`, both representative-ready |
| Worker pool | LiCl: 6 active jobs x 2 OpenMP threads; Worker A also carries 2 NaCl backfill jobs x 1 thread and 2 LiCl umbrella pulls x 1 thread |
| Effective CPU quota | 16/16 active mdrun threads on Worker A, without oversubscription |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | `14.09 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `9.30 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `9.26 ns / 20 ns`; clustering queued |
| `LiLC-1` | `14.25 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%` |
| `LiN3-Core` | `14.31 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `13.96 ns / 20 ns`; clustering queued |

## Notes

- LiCl minimization and equilibration are complete for all eight candidates.
- Production and clustering were launched only after confirming no active LiCl production duplicate was running.
- PBC-safe umbrella pulling is active for `LiDA-1` LiCl and `LiDS-1` LiCl.
- Active trajectories are not synced locally while production is running.
