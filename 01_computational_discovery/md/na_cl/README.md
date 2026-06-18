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
| 20 ns production | 8/8 active; `0.02-0.14 ns / 20 ns` as of `2026-06-18 20:45 CST` |
| Structural clustering | Queued after each production run |
| PMF handoff | Pending |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | `0.03 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | `0.02 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | `0.04 ns / 20 ns`; clustering queued |
| `LiLC-1` | `0.06 ns / 20 ns`; clustering queued |
| `LiDS-1` | `0.09 ns / 20 ns`; clustering queued |
| `LiDA-1` | `0.14 ns / 20 ns`; clustering queued |
| `LiN3-Core` | `0.03 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `0.03 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
