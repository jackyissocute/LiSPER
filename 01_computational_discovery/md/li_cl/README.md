# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 6/8 active; `9.99-15.44 ns / 20 ns` as of `2026-06-22 00:07 CST`; `LiDA-1` and `LiDS-1` complete |
| Structural clustering | 2/8 complete; `LiDA-1` top cluster `17.64%`; `LiDS-1` top cluster `15.69%`; others queued after production |
| PMF handoff | Umbrella windows active: `LiDA-1` `1/19`, active `001`; `LiDS-1` `0/21`, active `000` |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `15.19 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `10.01 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `9.99 ns / 20 ns`; clustering queued |
| `LiLC-1` | `15.37 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%`; umbrella `0/21`, active `000` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%`; umbrella `1/19`, active `001` |
| `LiN3-Core` | `15.44 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `15.04 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
