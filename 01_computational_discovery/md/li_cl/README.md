# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 8/8 active; `3.36-11.57 ns / 20 ns` as of `2026-06-19 20:25 CST` |
| Structural clustering | Queued after each production run |
| PMF handoff | Pending paired LiCl/NaCl representative set |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `5.10 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `3.41 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `3.36 ns / 20 ns`; clustering queued |
| `LiLC-1` | `5.22 ns / 20 ns`; clustering queued |
| `LiDS-1` | `7.92 ns / 20 ns`; clustering queued |
| `LiDA-1` | `11.57 ns / 20 ns`; clustering queued |
| `LiN3-Core` | `5.26 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `5.12 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
