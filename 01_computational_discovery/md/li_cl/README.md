# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 2/8 active on replacement Worker A; `15.53-15.61 ns / 20 ns` as of `2026-06-24 09:28 CST`; 6/8 produced |
| Structural clustering | 6/8 complete; top clusters: `LiDA-1` `17.64%`, `LiDS-1` `15.69%`, `LiD3-Core` `12.69%`, `LiLC-1` `4.15%`, `LiN3-Core` `4.65%`, `LiA3-Ref` `5.05%` |
| PMF handoff | Umbrella active: `LiDA-1` `8/19`, active `008-009`; `LiDS-1` `12/21`, active `012-017`; `LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` each have window `001` active after window `000` completed |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `12.69%`; pull active |
| `LiD3-Flex` | `15.53 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `15.61 ns / 20 ns`; clustering queued |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `4.15%`; umbrella window `001` active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%`; umbrella `12/21`, active `012-017` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%`; umbrella `8/19`, active `008-009` |
| `LiN3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `4.65%`; umbrella window `001` active |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `5.05%`; umbrella window `001` active |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
