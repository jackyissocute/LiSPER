# NaCl Production Worker Status

Last updated: 2026-06-18 14:00 CST

## Active Queue

| Item | Status |
|---|---|
| Condition | NaCl |
| Candidate set | Final 8-candidate NaCl systems |
| Worker | Second AutoDL machine |
| Stage | 20 ns production followed by structural clustering |
| Launch state | Running |
| Thread setting | `LISPER_NTHREAD=128` |

## Notes

- The worker was built from the completed 7-candidate NaCl setup batch plus the completed `LiN3-Core` NaCl add-on.
- All eight NaCl systems are equilibrated in the production worker manifest.
- Active trajectories are not synced locally while production is running.
