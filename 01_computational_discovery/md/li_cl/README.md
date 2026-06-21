# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 6/8 active; `9.26-14.31 ns / 20 ns` as of `2026-06-21 18:05 CST`; `LiDA-1` and `LiDS-1` complete |
| Structural clustering | 2/8 complete; `LiDA-1` top cluster `17.64%`; `LiDS-1` top cluster `15.69%`; others queued after production |
| PMF handoff | Umbrella sampling active for clustered LiCl conditions: `LiDA-1` and `LiDS-1` |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `14.09 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `9.30 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `9.26 ns / 20 ns`; clustering queued |
| `LiLC-1` | `14.25 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%`; umbrella window sampling active |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%`; umbrella window sampling active |
| `LiN3-Core` | `14.31 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `13.96 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
