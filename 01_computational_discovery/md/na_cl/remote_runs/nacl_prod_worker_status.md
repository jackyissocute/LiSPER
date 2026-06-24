# NaCl Production Worker Status

Last updated: 2026-06-24 21:05 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | Second AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | Worker B active: 1 production job + active `LiLC-1`, `LiA3-Ref`, and repaired `LiD3-Core` NaCl umbrella windows; `LiDA-1` NaCl repair extensions and combined WHAM/bootstrap QC completed; replacement Worker A backfill active for two NaCl jobs |
| Production progress | Worker B production job `14.19 ns / 20 ns`; Worker A backfill jobs `5.09-7.78 ns / 20 ns`; five NaCl conditions are produced and representative-ready |
| Current leader | `LiDA-1`, `LiDS-1`, `LiLC-1`, `LiA3-Ref`, and `LiD3-Core` at `20.00 ns / 20 ns`, representative ready |
| Worker pool | Worker B: 1 active production job x 2 OpenMP threads plus 10 active NaCl umbrella windows x 1 thread |
| Effective CPU quota | Worker B is at 12/12 active mdrun threads; replacement Worker A is at 15/18 active mdrun threads |
| Optimization reason | The queued NaCl pair was backfilled onto Worker A after two CPU slots opened, avoiding duplicate candidate-condition-stage work |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `10.34%`; umbrella windows `000-003` active after topology-selection repair |
| `LiD3-Flex` | Recovered checkpoint resume on Worker B; `14.19 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Replacement Worker A backfill active; `5.09 ns / 20 ns`; clustering queued |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `1.95%`; umbrella `2/21` complete; windows `002-003` active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; umbrella `17/17` complete; preliminary WHAM/QC ready |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; umbrella `15/15` complete; WHAM QC repair extensions `5/5` complete; combined WHAM/bootstrap QC complete; still preliminary pending tail/time-slice review |
| `LiN3-Core` | Replacement Worker A backfill active; `7.78 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `7.35%`; umbrella windows `000-003` active |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- The first sequential single-candidate launcher was replaced by the tracked parallel launcher.
- On 2026-06-19, the NaCl worker was checkpoint-restarted with `.cpt` files and `-append` using 6 concurrent jobs x 2 OpenMP threads. This matches the 12-core quota and avoids the previous 8 x 16 oversubscription.
- On 2026-06-20, `LiND-Hybrid` and `LiN3-Core` were backfilled onto Worker A as 2 concurrent jobs x 1 OpenMP thread after `LiDA-1` LiCl completed and freed two CPU slots. The original queued directories on Worker B were disabled to prevent duplicate launches.
- On 2026-06-21, `LiDA-1` NaCl completed and clustered, producing a representative with top-cluster population `17.94%`.
- On 2026-06-22, `LiDS-1` NaCl completed and clustered, producing a representative with top-cluster population `14.59%`.
- On 2026-06-23, `LiLC-1` NaCl completed and clustered, producing a representative with top-cluster population `1.95%`; this low population suggests strong conformational disorder, but the representative file is valid and its PBC-safe umbrella pull is active.
- PBC-safe umbrella windows are complete for `LiDA-1` NaCl (`15/15`) with WHAM QC warnings and `LiDS-1` NaCl (`17/17`) with preliminary WHAM/QC ready. A valid-15 WHAM diagnostic for `LiDA-1` NaCl found persistent weak edge bins and time-sliced Delta G instability, so five copied edge-window extensions were run as repair sampling without overwriting the original windows. Those repair extensions are complete, and combined original-plus-repair WHAM/bootstrap improved the histogram to `0` empty bins and `1/100` weak bin. The result remains preliminary until tail-materiality and time-slice convergence review are finished. `LiLC-1` NaCl windows `002-003` are active; `LiA3-Ref` and `LiD3-Core` NaCl windows `000-003` are active.
- On 2026-06-22 evening, Worker B came back reachable after shutdown with no active `gmx` processes. Four interrupted production jobs were cleanly resumed from checkpoints. The first recovery attempt exposed an `OMP_NUM_THREADS=12` environment mismatch; diagnostics are preserved remotely, and the corrected relaunch sets per-job `OMP_NUM_THREADS` to match `-ntomp`.
- The old Worker A was replaced by a copied 18-core AutoDL container. The copied LiCl and NaCl-backfill jobs resumed from checkpoints, and extra LiCl umbrella windows were launched to use the full 18-core quota without oversubscription.
- Older production logs may still contain the previous oversubscription warning because GROMACS appends into the same log during checkpoint continuation; the active relaunched jobs report `Using 2 OpenMP threads`.
- Active trajectories are not synced locally while production is running.
