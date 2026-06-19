# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 8/8 active; `2.28-7.86 ns / 20 ns` as of `2026-06-19 11:50 CST` |
| Structural clustering | Queued after each production run |
| PMF handoff | Pending paired LiCl/NaCl representative set |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `3.46 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `2.31 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `2.28 ns / 20 ns`; clustering queued |
| `LiLC-1` | `3.54 ns / 20 ns`; clustering queued |
| `LiDS-1` | `5.37 ns / 20 ns`; clustering queued |
| `LiDA-1` | `7.86 ns / 20 ns`; clustering queued |
| `LiN3-Core` | `3.56 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `3.47 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
