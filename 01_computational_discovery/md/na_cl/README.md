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
| 20 ns production | 8/8 active across both workers: 6 Worker B jobs at `4.83-17.15 ns / 20 ns`, plus 2 Worker A backfill jobs at `0.78-1.08 ns / 20 ns` as of `2026-06-21 02:41 CST` |
| Structural clustering | Queued after each production run |
| PMF handoff | Pending |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | Active checkpoint resume; `7.25 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Active checkpoint resume; `4.83 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Worker A backfill active; `0.78 ns / 20 ns`; clustering queued |
| `LiLC-1` | Active checkpoint resume; `7.58 ns / 20 ns`; clustering queued |
| `LiDS-1` | Active checkpoint resume; `11.48 ns / 20 ns`; clustering queued |
| `LiDA-1` | Active checkpoint resume; `17.15 ns / 20 ns`; clustering queued |
| `LiN3-Core` | Worker A backfill active; `1.08 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Active checkpoint resume; `7.10 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
