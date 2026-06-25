# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 2/8 active on replacement Worker A; `15.53-15.61 ns / 20 ns` as of `2026-06-25 09:35 CST`; 6/8 produced |
| Structural clustering | 6/8 complete; top clusters: `LiDA-1` `17.64%`, `LiDS-1` `15.69%`, `LiD3-Core` `12.69%`, `LiLC-1` `4.15%`, `LiN3-Core` `4.65%`, `LiA3-Ref` `5.05%` |
| PMF handoff | Umbrella active: `LiDA-1` `14/19`, active `014-015`; `LiDS-1` `21/21` complete with preliminary WHAM/QC complete; `LiD3-Core`, `LiLC-1`, and `LiN3-Core` each have `3/21` complete with window `003` active; `LiA3-Ref` has `2/21` complete with window `002` active |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `12.69%`; umbrella `3/21` complete; window `003` active |
| `LiD3-Flex` | `15.53 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `15.61 ns / 20 ns`; clustering queued |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `4.15%`; umbrella `3/21` complete; window `003` active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%`; umbrella `21/21` complete; preliminary WHAM/QC complete with weak-bin warnings |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%`; umbrella `14/19`, active `014-015` |
| `LiN3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `4.65%`; umbrella `3/21` complete; window `003` active |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `5.05%`; umbrella `2/21` complete; window `002` active |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
