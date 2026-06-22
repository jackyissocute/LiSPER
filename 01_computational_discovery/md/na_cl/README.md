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
| 20 ns production | Worker B active at `12/12` cores with 4 checkpoint-resumed jobs at `11.13-17.38 ns / 20 ns`; replacement Worker A backfill active at `3.86-5.85 ns / 20 ns` as of `2026-06-23 06:33 CST`; `LiDA-1` and `LiDS-1` complete |
| Structural clustering | 2/8 complete; `LiDA-1` top cluster `17.94%`; `LiDS-1` top cluster `14.59%`; others queued after production |
| PMF handoff | Umbrella windows: `LiDA-1` `15/15` complete; `LiDS-1` `1/17`, active `001-004` |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | Recovered checkpoint resume on Worker B; `16.59 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Recovered checkpoint resume on Worker B; `11.13 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Replacement Worker A backfill active; `3.86 ns / 20 ns`; clustering queued |
| `LiLC-1` | Recovered checkpoint resume on Worker B; `17.38 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; umbrella `1/17`, active `001-004` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; umbrella `15/15` complete |
| `LiN3-Core` | Replacement Worker A backfill active; `5.85 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | Recovered checkpoint resume on Worker B; `16.07 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
