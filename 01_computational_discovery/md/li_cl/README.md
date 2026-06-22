# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 3/8 active on replacement Worker A; `13.15-19.76 ns / 20 ns` as of `2026-06-23 06:33 CST`; 5/8 produced |
| Structural clustering | 5/8 complete; top clusters: `LiDA-1` `17.64%`, `LiDS-1` `15.69%`, `LiD3-Core` `12.69%`, `LiLC-1` `4.15%`, `LiN3-Core` `4.65%` |
| PMF handoff | Umbrella active: `LiDS-1` `4/21`, active `004-005`; pulls active for `LiDA-1`, `LiD3-Core`, `LiLC-1`, and `LiN3-Core` |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `12.69%`; pull active |
| `LiD3-Flex` | `13.15 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `13.25 ns / 20 ns`; clustering queued |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `4.15%`; pull active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%`; umbrella `4/21`, active `004-005` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%`; pull active |
| `LiN3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `4.65%`; pull active |
| `LiA3-Ref` | `19.76 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
