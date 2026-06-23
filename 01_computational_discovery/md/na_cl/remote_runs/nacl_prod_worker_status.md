# NaCl Production Worker Status

Last updated: 2026-06-23 20:41 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | Second AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | Worker B active: 4 production jobs + 4 active `LiDS-1` NaCl umbrella windows; replacement Worker A backfill active for two NaCl jobs |
| Production progress | Worker B jobs `12.62-19.67 ns / 20 ns`; Worker A backfill jobs `4.52-6.88 ns / 20 ns`; `LiDA-1` and `LiDS-1` complete |
| Current leader | `LiDA-1` and `LiDS-1` at `20.00 ns / 20 ns`, representative ready |
| Worker pool | Worker B: 4 active production jobs x 2 OpenMP threads plus 4 active `LiDS-1` NaCl umbrella windows x 1 thread |
| Effective CPU quota | Worker B confirmed at 12/12 cores; replacement Worker A confirmed at 18/18 cores |
| Optimization reason | The queued NaCl pair was backfilled onto Worker A after two CPU slots opened, avoiding duplicate candidate-condition-stage work |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | Recovered checkpoint resume on Worker B; `18.84 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Recovered checkpoint resume on Worker B; `12.62 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Replacement Worker A backfill active; `4.52 ns / 20 ns`; clustering queued |
| `LiLC-1` | Recovered checkpoint resume on Worker B; `19.67 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; umbrella `9/17`, active `009-012` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; umbrella `15/15` complete; preliminary WHAM QC warning |
| `LiN3-Core` | Replacement Worker A backfill active; `6.88 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Recovered checkpoint resume on Worker B; `18.28 ns / 20 ns`; clustering queued |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- The first sequential single-candidate launcher was replaced by the tracked parallel launcher.
- On 2026-06-19, the NaCl worker was checkpoint-restarted with `.cpt` files and `-append` using 6 concurrent jobs x 2 OpenMP threads. This matches the 12-core quota and avoids the previous 8 x 16 oversubscription.
- On 2026-06-20, `LiND-Hybrid` and `LiN3-Core` were backfilled onto Worker A as 2 concurrent jobs x 1 OpenMP thread after `LiDA-1` LiCl completed and freed two CPU slots. The original queued directories on Worker B were disabled to prevent duplicate launches.
- On 2026-06-21, `LiDA-1` NaCl completed and clustered, producing a representative with top-cluster population `17.94%`.
- On 2026-06-22, `LiDS-1` NaCl completed and clustered, producing a representative with top-cluster population `14.59%`.
- PBC-safe umbrella windows are complete for `LiDA-1` NaCl (`15/15`) with WHAM QC warnings. `LiDS-1` NaCl has `9/17` windows complete and active windows `009-012`.
- On 2026-06-22 evening, Worker B came back reachable after shutdown with no active `gmx` processes. Four interrupted production jobs were cleanly resumed from checkpoints. The first recovery attempt exposed an `OMP_NUM_THREADS=12` environment mismatch; diagnostics are preserved remotely, and the corrected relaunch sets per-job `OMP_NUM_THREADS` to match `-ntomp`.
- The old Worker A was replaced by a copied 18-core AutoDL container. The copied LiCl and NaCl-backfill jobs resumed from checkpoints, and extra LiCl umbrella windows were launched to use the full 18-core quota without oversubscription.
- Older production logs may still contain the previous oversubscription warning because GROMACS appends into the same log during checkpoint continuation; the active relaunched jobs report `Using 2 OpenMP threads`.
- Active trajectories are not synced locally while production is running.
