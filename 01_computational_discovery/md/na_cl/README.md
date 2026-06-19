# NaCl Molecular Dynamics

NaCl MD is tracked under the final 8-candidate names.

NaCl simulations are being generated as matched comparison systems for the revised 8-candidate library.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI NaCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized including LiN3-Core add-on |
| Equilibration | 8/8 equilibrated |
| 20 ns production | Optimized checkpoint resume: 6 active + 2 queued; `0.08-0.49 ns / 20 ns` as of `2026-06-19 08:51 CST` |
| Structural clustering | Queued after each production run |
| PMF handoff | Pending |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | Active checkpoint resume; `0.12 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Active checkpoint resume; `0.08 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Queued behind optimized worker pool; `0.16 ns / 20 ns`; clustering queued |
| `LiLC-1` | Active checkpoint resume; `0.24 ns / 20 ns`; clustering queued |
| `LiDS-1` | Active checkpoint resume; `0.35 ns / 20 ns`; clustering queued |
| `LiDA-1` | Active checkpoint resume; `0.49 ns / 20 ns`; clustering queued |
| `LiN3-Core` | Queued behind optimized worker pool; `0.12 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Active checkpoint resume; `0.12 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
