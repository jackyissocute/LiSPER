# NaCl Production Worker Status

Last updated: 2026-06-20 23:41 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | Second AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | 6 active jobs on Worker B + 2 backfill active jobs on Worker A |
| Production progress | Worker B jobs `4.47-15.93 ns / 20 ns`; Worker A backfill jobs `0.57-0.76 ns / 20 ns` |
| Current leader | `LiDA-1` at `15.93 ns / 20 ns` |
| Worker pool | Worker B: `LISPER_JOBS=6`, `LISPER_NTHREAD_PER_JOB=2`; Worker A backfill: `LISPER_JOBS=2`, `LISPER_NTHREAD_PER_JOB=1` |
| Effective CPU quota | Worker B uses 12/12 cores; Worker A uses 16/16 after LiDA-1 LiCl completed |
| Optimization reason | The queued NaCl pair was backfilled onto Worker A after two CPU slots opened, avoiding duplicate candidate-condition-stage work |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | Active checkpoint resume on Worker B; `6.72 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Active checkpoint resume on Worker B; `4.47 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Active backfill on Worker A; `0.57 ns / 20 ns`; clustering queued |
| `LiLC-1` | Active checkpoint resume on Worker B; `7.02 ns / 20 ns`; clustering queued |
| `LiDS-1` | Active checkpoint resume on Worker B; `10.63 ns / 20 ns`; clustering queued |
| `LiDA-1` | Active checkpoint resume on Worker B; `15.93 ns / 20 ns`; clustering queued |
| `LiN3-Core` | Active backfill on Worker A; `0.76 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Active checkpoint resume on Worker B; `6.58 ns / 20 ns`; clustering queued |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- The first sequential single-candidate launcher was replaced by the tracked parallel launcher.
- On 2026-06-19, the NaCl worker was checkpoint-restarted with `.cpt` files and `-append` using 6 concurrent jobs x 2 OpenMP threads. This matches the 12-core quota and avoids the previous 8 x 16 oversubscription.
- On 2026-06-20, `LiND-Hybrid` and `LiN3-Core` were backfilled onto Worker A as 2 concurrent jobs x 1 OpenMP thread after `LiDA-1` LiCl completed and freed two CPU slots. The original queued directories on Worker B were disabled to prevent duplicate launches.
- Older production logs may still contain the previous oversubscription warning because GROMACS appends into the same log during checkpoint continuation; the active relaunched jobs report `Using 2 OpenMP threads`.
- Active trajectories are not synced locally while production is running.
