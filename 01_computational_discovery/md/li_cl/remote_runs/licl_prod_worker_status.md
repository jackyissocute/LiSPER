# LiCl Production Worker Status

Last updated: 2026-06-23 23:50 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | LiCl |
| Candidate set | Final 8-candidate LiCl systems |
| Worker | Replacement AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | 2 active LiCl production jobs + 6 completed/representative-ready conditions |
| Production progress | `14.68-14.77 ns / 20 ns` across active LiCl jobs |
| Current leader | Six LiCl conditions are representative-ready; `LiD3-Flex` and `LiND-Hybrid` remain in production |
| Worker pool | LiCl: 2 active jobs x 2 OpenMP threads; Worker A also carries 2 NaCl backfill jobs x 1 thread and 12 LiCl umbrella/pull threads |
| Effective CPU quota | 18/18 active mdrun threads on replacement Worker A, without oversubscription |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `12.69%`; umbrella window `000` active |
| `LiD3-Flex` | `14.68 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `14.77 ns / 20 ns`; clustering queued |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `4.15%`; umbrella window `000` active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%`; umbrella `6/21`, active `006-011` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%`; umbrella `4/19`, active `004-005` |
| `LiN3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `4.65%`; umbrella window `000` active |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `5.05%`; umbrella window `000` active |

## Notes

- LiCl minimization and equilibration are complete for all eight candidates.
- Production, clustering, and umbrella handoffs were launched only after confirming no active duplicate candidate-condition-stage was running.
- PBC-safe umbrella windows are active for `LiDA-1` LiCl (`4/19`, active `004-005`), `LiDS-1` LiCl (`6/21`, active `006-011`), `LiD3-Core` LiCl (`000`), `LiLC-1` LiCl (`000`), `LiN3-Core` LiCl (`000`), and `LiA3-Ref` LiCl (`000`).
- Active trajectories are not synced locally while production is running.
