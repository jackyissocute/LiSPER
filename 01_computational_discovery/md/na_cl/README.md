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
| 20 ns production | Worker B active at `11/12` safe mdrun threads during the `LiLC-1` NaCl pull with 3 checkpoint-resumed production jobs at `12.98-19.40 ns / 20 ns`; replacement Worker A backfill active at `4.66-7.10 ns / 20 ns` as of `2026-06-23 23:50 CST`; `LiDA-1`, `LiDS-1`, and `LiLC-1` complete |
| Structural clustering | 3/8 complete; `LiDA-1` top cluster `17.94%`; `LiDS-1` top cluster `14.59%`; `LiLC-1` top cluster `1.95%`; others queued after production |
| PMF handoff | Umbrella windows: `LiDA-1` `15/15` complete with preliminary WHAM QC warning; `LiDS-1` `9/17`, active `009-012`; `LiLC-1` PBC-safe pull active |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | Recovered checkpoint resume on Worker B; `19.40 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Recovered checkpoint resume on Worker B; `12.98 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Replacement Worker A backfill active; `4.66 ns / 20 ns`; clustering queued |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `1.95%`; NaCl umbrella pull active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; umbrella `9/17`, active `009-012` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; umbrella `15/15` complete |
| `LiN3-Core` | Replacement Worker A backfill active; `7.10 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Recovered checkpoint resume on Worker B; `18.82 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
