# NaCl Remote Status

Last updated: `2026-06-18 13:06 CST`

Seven NaCl systems minimized and equilibrated successfully on AutoDL under the active 8-candidate workflow.

| Item | Status |
|---|---|
| Remote batch | Complete after detached retry |
| PID | `1179` |
| Workdir | `/root/LiSPER_remote/LiSPER_8cand_NaCl` |
| Queued candidates | `LiA3-Ref`, `LiD3-Core`, `LiD3-Flex`, `LiDA-1`, `LiDS-1`, `LiLC-1`, `LiND-Hybrid` |
| Add-on setup | `LiN3-Core` NaCl minimized cleanly and equilibration is running in a separate focused add-on queue |
| Current gate | Inspect minimization/equilibration summaries before production MD |

## Interpretation

The new LiD3-Core ESMFold file passed sequence and single-chain QC, and its NaCl CHARMM-GUI system is included in the completed seven-candidate setup batch. The first detached launch stopped before writing top-level summaries, so a retry was launched with unbuffered logging. The retry minimized all seven queued systems; LiD3-Core and LiDS-1 required water-overlap repairs before successful minimization. The corrected `LiN3-Core` NaCl GROMACS-ready archive has now been imported locally, minimized cleanly, and moved into equilibration as a separate focused add-on queue.
