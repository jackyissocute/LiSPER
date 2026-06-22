# NaCl Production Worker Status

Last updated: 2026-06-22 09:10 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | Second AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | 4 active jobs on Worker B + 2 backfill active jobs on Worker A + 2 completed/clustered representatives |
| Production progress | Worker B jobs `8.75-13.70 ns / 20 ns`; Worker A backfill jobs `2.73-4.12 ns / 20 ns`; `LiDA-1` and `LiDS-1` complete |
| Current leader | `LiDA-1` and `LiDS-1` at `20.00 ns / 20 ns`, representative ready |
| Worker pool | Worker B: 4 active jobs x 2 OpenMP threads plus 3 active `LiDA-1` NaCl umbrella windows x 1 thread; Worker A backfill: 2 active jobs x 1 OpenMP thread |
| Effective CPU quota | Worker B uses 11/12 cores after the `LiDS-1` NaCl umbrella extraction failed before window launch; Worker A uses 16/16 active mdrun threads including two LiCl umbrella windows |
| Optimization reason | The queued NaCl pair was backfilled onto Worker A after two CPU slots opened, avoiding duplicate candidate-condition-stage work |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | Active checkpoint resume on Worker B; `12.97 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Active checkpoint resume on Worker B; `8.75 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Active backfill on Worker A; `2.73 ns / 20 ns`; clustering queued |
| `LiLC-1` | Active checkpoint resume on Worker B; `13.70 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; umbrella extraction blocked |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%` |
| `LiN3-Core` | Active backfill on Worker A; `4.12 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Active checkpoint resume on Worker B; `12.73 ns / 20 ns`; clustering queued |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- The first sequential single-candidate launcher was replaced by the tracked parallel launcher.
- On 2026-06-19, the NaCl worker was checkpoint-restarted with `.cpt` files and `-append` using 6 concurrent jobs x 2 OpenMP threads. This matches the 12-core quota and avoids the previous 8 x 16 oversubscription.
- On 2026-06-20, `LiND-Hybrid` and `LiN3-Core` were backfilled onto Worker A as 2 concurrent jobs x 1 OpenMP thread after `LiDA-1` LiCl completed and freed two CPU slots. The original queued directories on Worker B were disabled to prevent duplicate launches.
- On 2026-06-21, `LiDA-1` NaCl completed and clustered, producing a representative with top-cluster population `17.94%`.
- On 2026-06-22, `LiDS-1` NaCl completed and clustered, producing a representative with top-cluster population `14.59%`.
- PBC-safe umbrella windows are active for `LiDA-1` NaCl (`5/15`, active `005-007`). `LiDS-1` NaCl umbrella setup is blocked before window generation by a GROMACS full-system representative extraction crash; diagnostics are preserved in synced umbrella logs.
- Older production logs may still contain the previous oversubscription warning because GROMACS appends into the same log during checkpoint continuation; the active relaunched jobs report `Using 2 OpenMP threads`.
- Active trajectories are not synced locally while production is running.
