# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 8/8 active; `1.09-3.78 ns / 20 ns` as of `2026-06-19 02:47 CST` |
| Structural clustering | Queued after each production run |
| PMF handoff | Pending paired LiCl/NaCl representative set |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `1.66 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `1.10 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `1.09 ns / 20 ns`; clustering queued |
| `LiLC-1` | `1.69 ns / 20 ns`; clustering queued |
| `LiDS-1` | `2.58 ns / 20 ns`; clustering queued |
| `LiDA-1` | `3.78 ns / 20 ns`; clustering queued |
| `LiN3-Core` | `1.70 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `1.65 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
