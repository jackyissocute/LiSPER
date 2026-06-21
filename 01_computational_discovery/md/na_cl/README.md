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
| 20 ns production | 7/8 active across both workers: 5 Worker B jobs at `7.13-16.89 ns / 20 ns`, plus 2 Worker A backfill jobs at `1.99-2.94 ns / 20 ns` as of `2026-06-21 21:14 CST`; `LiDA-1` complete |
| Structural clustering | 1/8 complete; `LiDA-1` top cluster `17.94%`; others queued after production |
| PMF handoff | Umbrella windows active: `LiDA-1` `1/15`, active `001-002` |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | Active checkpoint resume on Worker B; `10.51 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Active checkpoint resume on Worker B; `7.13 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Worker A backfill active; `1.99 ns / 20 ns`; clustering queued |
| `LiLC-1` | Active checkpoint resume on Worker B; `11.16 ns / 20 ns`; clustering queued |
| `LiDS-1` | Active checkpoint resume on Worker B; `16.89 ns / 20 ns`; clustering queued |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; umbrella `1/15`, active `001-002` |
| `LiN3-Core` | Worker A backfill active; `2.94 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Active checkpoint resume on Worker B; `10.31 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
