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
| 20 ns production | 6/8 active across both workers: 4 Worker B jobs at `9.08-14.27 ns / 20 ns`, plus 2 Worker A backfill jobs at `2.93-4.42 ns / 20 ns` as of `2026-06-22 12:11 CST`; `LiDA-1` and `LiDS-1` complete |
| Structural clustering | 2/8 complete; `LiDA-1` top cluster `17.94%`; `LiDS-1` top cluster `14.59%`; others queued after production |
| PMF handoff | Umbrella windows active: `LiDA-1` `5/15`, active `005-007`; `LiDS-1` pull active at `301/500 ps` before window generation |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | Active checkpoint resume on Worker B; `13.52 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Active checkpoint resume on Worker B; `9.08 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Worker A backfill active; `2.93 ns / 20 ns`; clustering queued |
| `LiLC-1` | Active checkpoint resume on Worker B; `14.27 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; umbrella pull active at `301/500 ps` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; umbrella `5/15`, active `005-007` |
| `LiN3-Core` | Worker A backfill active; `4.42 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Active checkpoint resume on Worker B; `13.22 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
