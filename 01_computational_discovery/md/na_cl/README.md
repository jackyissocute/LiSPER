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
| 20 ns production | Worker B has `LiD3-Flex` active; replacement Worker A backfill has `LiN3-Core` and `LiND-Hybrid` active as of `2026-06-24 18:25 CST`; five candidates are produced |
| Structural clustering | 5/8 complete; top clusters: `LiDA-1` `17.94%`, `LiDS-1` `14.59%`, `LiLC-1` `1.95%`, `LiA3-Ref` `7.35%`, `LiD3-Core` `10.34%` |
| PMF handoff | Umbrella windows: `LiDA-1` `15/15` complete plus repair extensions `5/5` complete, combined WHAM/bootstrap QC complete but still preliminary; `LiDS-1` `17/17` complete and ready for preliminary WHAM/QC; `LiLC-1` windows `002-003` active; `LiA3-Ref` and repaired `LiD3-Core` windows `000-003` active |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `10.34%`; umbrella windows `000-003` active after topology-selection repair |
| `LiD3-Flex` | Recovered checkpoint resume on Worker B; `14.19 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Replacement Worker A backfill active; `5.09 ns / 20 ns`; clustering queued |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `1.95%`; umbrella `2/21` complete; windows `002-003` active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; umbrella `17/17` complete; preliminary WHAM/QC ready |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; umbrella `15/15` complete; repair extensions `5/5` complete; combined WHAM/bootstrap QC complete; still preliminary pending tail/time-slice review |
| `LiN3-Core` | Replacement Worker A backfill active; `7.78 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `7.35%`; umbrella windows `000-003` active |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
