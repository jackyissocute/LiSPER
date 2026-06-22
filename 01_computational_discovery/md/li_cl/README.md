# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 6/8 active; `11.42-17.72 ns / 20 ns` as of `2026-06-22 12:11 CST`; `LiDA-1` and `LiDS-1` complete |
| Structural clustering | 2/8 complete; `LiDA-1` top cluster `17.64%`; `LiDS-1` top cluster `15.69%`; others queued after production |
| PMF handoff | Umbrella windows active: `LiDA-1` `4/19`, active `004`; `LiDS-1` `2/21`, active `002` |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `17.34 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `11.42 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `11.47 ns / 20 ns`; clustering queued |
| `LiLC-1` | `17.64 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%`; umbrella `2/21`, active `002` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%`; umbrella `4/19`, active `004` |
| `LiN3-Core` | `17.72 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `17.15 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
