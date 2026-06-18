# NaCl Molecular Dynamics

NaCl MD is tracked under the final 8-candidate names.

NaCl simulations are being generated as matched comparison systems for the revised 8-candidate library.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI NaCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized including LiN3-Core add-on |
| Equilibration | 8/8 equilibrated |
| 20 ns production | Running on second AutoDL worker |
| Structural clustering | Queued after each production run |
| PMF handoff | Pending |

## Candidate Notes

| Candidate | NaCl state |
|---|---|
| `LiA3-Ref` | Minimized and equilibrated |
| `LiD3-Core` | Minimized after water-overlap repair; equilibrated |
| `LiD3-Flex` | Minimized and equilibrated |
| `LiDA-1` | Minimized and equilibrated |
| `LiDS-1` | Minimized after water-overlap repair; equilibrated |
| `LiLC-1` | Minimized and equilibrated |
| `LiND-Hybrid` | Minimized and equilibrated |
| `LiN3-Core` | Minimized and equilibrated; included in production worker |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
