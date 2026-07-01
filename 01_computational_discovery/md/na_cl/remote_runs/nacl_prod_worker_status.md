# NaCl Production Worker Status

Last updated: 2026-07-02 02:46 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | 32-core GCP runner; AutoDL retained only as backup/source |
| Stage | 20 ns production followed by structural clustering |
| Launch state | GCP active: one remaining `LiND-Hybrid` NaCl production tail plus refined NaCl umbrella windows for `LiD3-Flex`, `LiD3-Core`, `LiLC-1`, `LiA3-Ref`, and `LiN3-Core`; `LiDA-1` and `LiDS-1` NaCl WHAM/QC outputs are retained as preliminary evidence |
| Production progress | Seven NaCl conditions are produced and representative-ready; `LiND-Hybrid` remains active at `15.37 ns / 20 ns` |
| Current leader | `LiDA-1`, `LiDS-1`, `LiLC-1`, `LiA3-Ref`, `LiD3-Core`, `LiD3-Flex`, and `LiN3-Core` at `20.00 ns / 20 ns`, representative ready |
| Worker pool | GCP: `27` real `mdrun` processes using `28` OpenMP threads across production, umbrella, and LiDA-1 LiCl repair |
| Effective CPU quota | GCP is at `28/32` active `mdrun` threads; scheduling remains safe with a small reserve for SSH, Python drivers, WHAM/QC, and filesystem work |
| Optimization reason | GCP migration consolidated active work and avoided duplicate candidate-condition-stage-window launches |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `10.34%`; refined NaCl V2 `2/27`, active `002-003` |
| `LiD3-Flex` | `20.00 ns / 20 ns`; representative ready; top cluster `3.80%`; refined NaCl V2 `2/27`, active `002-006` |
| `LiND-Hybrid` | GCP backfill active; `15.37 ns / 20 ns`; clustering queued after production completion |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `1.95%`; refined NaCl V2 `2/27`, active `002-003` |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; umbrella `17/17` complete; preliminary WHAM/QC complete with `2` empty and `12/100` weak bins at the 100-bin setting |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; umbrella `15/15` complete; WHAM QC repair extensions `5/5` complete; combined WHAM/bootstrap QC complete; still preliminary pending tail/time-slice review |
| `LiN3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `11.44%`; refined NaCl V2 `0/27`, active `000-001` |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `7.35%`; refined NaCl V2 `2/27`, active `002-003` |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- The first sequential single-candidate launcher was replaced by the tracked parallel launcher.
- On 2026-06-19, the NaCl worker was checkpoint-restarted with `.cpt` files and `-append` using 6 concurrent jobs x 2 OpenMP threads. This matches the 12-core quota and avoids the previous 8 x 16 oversubscription.
- On 2026-06-20, `LiND-Hybrid` and `LiN3-Core` were backfilled onto Worker A as 2 concurrent jobs x 1 OpenMP thread after `LiDA-1` LiCl completed and freed two CPU slots. The original queued directories on Worker B were disabled to prevent duplicate launches.
- On 2026-06-21, `LiDA-1` NaCl completed and clustered, producing a representative with top-cluster population `17.94%`.
- On 2026-06-22, `LiDS-1` NaCl completed and clustered, producing a representative with top-cluster population `14.59%`.
- On 2026-06-23, `LiLC-1` NaCl completed and clustered, producing a representative with top-cluster population `1.95%`; this low population suggests strong conformational disorder, but the representative file is valid and its PBC-safe umbrella pull is active.
- PBC-safe umbrella windows are complete for `LiDA-1` NaCl (`15/15`) with repair extensions (`5/5`) and `LiDS-1` NaCl (`17/17`) with preliminary WHAM/QC complete. A valid-15 WHAM diagnostic for `LiDA-1` NaCl found persistent weak edge bins and time-sliced Delta G instability, so five copied edge-window extensions were run as repair sampling without overwriting the original windows. Those repair extensions are complete, and combined original-plus-repair WHAM/bootstrap improved the histogram to `0` empty bins and `1/100` weak bin. The result remains preliminary until tail-materiality and time-slice convergence review are finished. `LiDS-1` NaCl preliminary WHAM/QC has `2` empty bins and `12/100` weak bins, so it remains preliminary and likely needs repair planning after bottleneck review. `LiLC-1` NaCl windows `004-005` are active; `LiA3-Ref` and `LiD3-Core` NaCl windows `004-007` are active.
- On 2026-06-22 evening, Worker B came back reachable after shutdown with no active `gmx` processes. Four interrupted production jobs were cleanly resumed from checkpoints. The first recovery attempt exposed an `OMP_NUM_THREADS=12` environment mismatch; diagnostics are preserved remotely, and the corrected relaunch sets per-job `OMP_NUM_THREADS` to match `-ntomp`.
- The old Worker A was replaced by a copied 18-core AutoDL container. The copied LiCl and NaCl-backfill jobs resumed from checkpoints, and extra LiCl umbrella windows were launched to use the full 18-core quota without oversubscription.
- Older production logs may still contain the previous oversubscription warning because GROMACS appends into the same log during checkpoint continuation; the active relaunched jobs report `Using 2 OpenMP threads`.
- Active trajectories are not synced locally while production is running.
