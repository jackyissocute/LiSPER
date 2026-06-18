# NaCl Remote Status

Last updated: `2026-06-18 10:50 CST`

Seven NaCl systems minimized successfully on AutoDL and are now in the equilibration phase under the active 8-candidate workflow.

| Item | Status |
|---|---|
| Remote batch | Equilibration running after detached retry |
| PID | `1179` |
| Workdir | `/root/LiSPER_remote/LiSPER_8cand_NaCl` |
| Queued candidates | `LiA3-Ref`, `LiD3-Core`, `LiD3-Flex`, `LiDA-1`, `LiDS-1`, `LiLC-1`, `LiND-Hybrid` |
| QC hold | `LiN3-Core` NaCl package lacks the CHARMM-GUI `gromacs/` input folder |
| Current gate | Wait for equilibration summaries, then inspect logs before production MD |

## Interpretation

The new LiD3-Core ESMFold file passed sequence and single-chain QC, and its NaCl CHARMM-GUI system is now included in the running GROMACS setup queue. The first detached launch stopped before writing top-level summaries, so a retry was launched with unbuffered logging. The retry minimized all seven queued systems; LiD3-Core and LiDS-1 required water-overlap repairs before successful minimization. `LiN3-Core` should not be launched until a corrected NaCl CHARMM-GUI GROMACS archive is supplied.
