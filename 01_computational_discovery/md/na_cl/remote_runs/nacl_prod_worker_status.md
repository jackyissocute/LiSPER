# NaCl Production Worker Status

Last updated: 2026-06-19 09:00 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | Second AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | Optimized checkpoint resume: 6 active jobs + 2 queued jobs |
| Production progress | `0.08-0.49 ns / 20 ns` across the NaCl branch |
| Current leader | `LiDA-1` at `0.49 ns / 20 ns` |
| Worker pool | `LISPER_JOBS=6`, `LISPER_NTHREAD_PER_JOB=2` |
| Effective CPU quota | 12 cores on the second AutoDL container |
| Optimization reason | Replaced the oversubscribed 8-job x 16-thread launch with a quota-matched 6-job x 2-thread launch |

## Per-Candidate Production Progress

| Candidate | State |
|---|---|
| `LiD3-Core` | Active checkpoint resume; `0.12 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Active checkpoint resume; `0.08 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Queued behind optimized worker pool; `0.16 ns / 20 ns`; clustering queued |
| `LiLC-1` | Active checkpoint resume; `0.24 ns / 20 ns`; clustering queued |
| `LiDS-1` | Active checkpoint resume; `0.35 ns / 20 ns`; clustering queued |
| `LiDA-1` | Active checkpoint resume; `0.49 ns / 20 ns`; clustering queued |
| `LiN3-Core` | Queued behind optimized worker pool; `0.12 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Active checkpoint resume; `0.12 ns / 20 ns`; clustering queued |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- The first sequential single-candidate launcher was replaced by the tracked parallel launcher.
- On 2026-06-19, the NaCl worker was checkpoint-restarted with `.cpt` files and `-append` using 6 concurrent jobs x 2 OpenMP threads. This matches the 12-core quota and avoids the previous 8 x 16 oversubscription.
- Older production logs may still contain the previous oversubscription warning because GROMACS appends into the same log during checkpoint continuation; the active relaunched jobs report `Using 2 OpenMP threads`.
- Active trajectories are not synced locally while production is running.
