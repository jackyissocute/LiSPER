# NaCl Production Worker Status

Last updated: 2026-06-21 12:07 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | Second AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | 5 active jobs on Worker B + 2 backfill active jobs on Worker A + 1 completed/clustered representative |
| Production progress | Worker B jobs `6.00-14.21 ns / 20 ns`; Worker A backfill jobs `1.43-2.08 ns / 20 ns`; `LiDA-1` complete |
| Current leader | `LiDA-1` at `20.00 ns / 20 ns`, representative ready |
| Worker pool | Worker B: 5 active jobs x 2 OpenMP threads; Worker A backfill: 2 active jobs x 1 OpenMP thread |
| Effective CPU quota | Worker B uses 10/12 cores; Worker A uses 14/16 total active threads after `LiDS-1` LiCl and `LiDA-1` NaCl completed |
| Optimization reason | The queued NaCl pair was backfilled onto Worker A after two CPU slots opened, avoiding duplicate candidate-condition-stage work |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | Active checkpoint resume on Worker B; `8.95 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Active checkpoint resume on Worker B; `6.00 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Active backfill on Worker A; `1.43 ns / 20 ns`; clustering queued |
| `LiLC-1` | Active checkpoint resume on Worker B; `9.39 ns / 20 ns`; clustering queued |
| `LiDS-1` | Active checkpoint resume on Worker B; `14.21 ns / 20 ns`; clustering queued |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%` |
| `LiN3-Core` | Active backfill on Worker A; `2.08 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Active checkpoint resume on Worker B; `8.77 ns / 20 ns`; clustering queued |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- The first sequential single-candidate launcher was replaced by the tracked parallel launcher.
- On 2026-06-19, the NaCl worker was checkpoint-restarted with `.cpt` files and `-append` using 6 concurrent jobs x 2 OpenMP threads. This matches the 12-core quota and avoids the previous 8 x 16 oversubscription.
- On 2026-06-20, `LiND-Hybrid` and `LiN3-Core` were backfilled onto Worker A as 2 concurrent jobs x 1 OpenMP thread after `LiDA-1` LiCl completed and freed two CPU slots. The original queued directories on Worker B were disabled to prevent duplicate launches.
- On 2026-06-21, `LiDA-1` NaCl completed and clustered, producing a representative with top-cluster population `17.94%`.
- Older production logs may still contain the previous oversubscription warning because GROMACS appends into the same log during checkpoint continuation; the active relaunched jobs report `Using 2 OpenMP threads`.
- Active trajectories are not synced locally while production is running.
