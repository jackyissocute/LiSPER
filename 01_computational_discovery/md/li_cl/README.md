# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 2/8 active on replacement Worker A; `14.68-14.77 ns / 20 ns` as of `2026-06-23 23:50 CST`; 6/8 produced |
| Structural clustering | 6/8 complete; top clusters: `LiDA-1` `17.64%`, `LiDS-1` `15.69%`, `LiD3-Core` `12.69%`, `LiLC-1` `4.15%`, `LiN3-Core` `4.65%`, `LiA3-Ref` `5.05%` |
| PMF handoff | Umbrella active: `LiDA-1` `4/19`, active `004-005`; `LiDS-1` `6/21`, active `006-011`; `LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` each have window `000` active |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `12.69%`; pull active |
| `LiD3-Flex` | `14.68 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `14.77 ns / 20 ns`; clustering queued |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `4.15%`; pull active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%`; umbrella `6/21`, active `006-011` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%`; umbrella `4/19`, active `004-005` |
| `LiN3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `4.65%`; pull active |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `5.05%`; umbrella window `000` active |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
