# NaCl Remote Status

Last updated: `2026-06-18 10:50 CST`

Seven NaCl systems minimized and equilibrated successfully on AutoDL under the active 8-candidate workflow.

| Item | Status |
|---|---|
| Remote batch | Complete after detached retry |
| PID | `1179` |
| Workdir | `/root/LiSPER_remote/LiSPER_8cand_NaCl` |
| Queued candidates | `LiA3-Ref`, `LiD3-Core`, `LiD3-Flex`, `LiDA-1`, `LiDS-1`, `LiLC-1`, `LiND-Hybrid` |
| Pending queue add-on | `LiN3-Core` NaCl package is now GROMACS-ready locally but not part of this already-running batch |
| Current gate | Inspect minimization/equilibration summaries before production MD |

## Interpretation

The new LiD3-Core ESMFold file passed sequence and single-chain QC, and its NaCl CHARMM-GUI system is now included in the running GROMACS setup queue. The first detached launch stopped before writing top-level summaries, so a retry was launched with unbuffered logging. The retry minimized all seven queued systems; LiD3-Core and LiDS-1 required water-overlap repairs before successful minimization. A corrected `LiN3-Core` NaCl GROMACS-ready archive has now been imported locally and should be added as a separate follow-up queue after the current 7-candidate equilibration gate is inspected.
