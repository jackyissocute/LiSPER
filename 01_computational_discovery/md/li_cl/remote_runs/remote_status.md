# LiCl Remote Status

Last updated: 2026-06-18 13:06 CST

## Active Setup Queue

| Item | Status |
|---|---|
| Candidate set | Final 8-candidate LiCl systems |
| Remote workdir | `LiSPER_8cand_LiCl` |
| Queue | Minimization followed by equilibration |
| Launch state | Minimization complete; equilibration running |
| Local gate | Wait for minimization and equilibration summaries before production |

## Notes

- The full LiCl set is GROMACS-ready locally and has been synced to the remote setup workdir.
- Minimization completed for all eight candidates; equilibration is running.
- Production MD should not be launched until setup summaries pass QC.
