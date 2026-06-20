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
| 20 ns production | 8/8 active across both workers: 6 Worker B jobs at `3.80-13.49 ns / 20 ns`, plus 2 Worker A overflow jobs at `0.13-0.16 ns / 20 ns` as of `2026-06-20 17:29 CST` |
| Structural clustering | Queued after each production run |
| PMF handoff | Pending |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | Active checkpoint resume; `5.65 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Active checkpoint resume; `3.80 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Worker A overflow active; `0.16 ns / 20 ns`; clustering queued |
| `LiLC-1` | Active checkpoint resume; `5.97 ns / 20 ns`; clustering queued |
| `LiDS-1` | Active checkpoint resume; `9.04 ns / 20 ns`; clustering queued |
| `LiDA-1` | Active checkpoint resume; `13.49 ns / 20 ns`; clustering queued |
| `LiN3-Core` | Worker A overflow active; `0.13 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Active checkpoint resume; `5.52 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
