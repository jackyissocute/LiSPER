# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 7/8 active; `6.56-15.47 ns / 20 ns` as of `2026-06-20 20:43 CST`; `LiDA-1` complete |
| Structural clustering | 1/8 complete; `LiDA-1` top cluster `17.64%`; others queued after production |
| PMF handoff | Pending paired LiCl/NaCl representative set |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `9.98 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `6.58 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `6.56 ns / 20 ns`; clustering queued |
| `LiLC-1` | `10.08 ns / 20 ns`; clustering queued |
| `LiDS-1` | `15.47 ns / 20 ns`; clustering queued |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%` |
| `LiN3-Core` | `10.14 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `9.88 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
