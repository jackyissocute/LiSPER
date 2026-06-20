# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 8/8 active; `5.35-18.41 ns / 20 ns` as of `2026-06-20 11:28 CST` |
| Structural clustering | Queued after each production run |
| PMF handoff | Pending paired LiCl/NaCl representative set |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `8.14 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `5.41 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `5.35 ns / 20 ns`; clustering queued |
| `LiLC-1` | `8.29 ns / 20 ns`; clustering queued |
| `LiDS-1` | `12.63 ns / 20 ns`; clustering queued |
| `LiDA-1` | `18.41 ns / 20 ns`; clustering queued |
| `LiN3-Core` | `8.34 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `8.13 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
