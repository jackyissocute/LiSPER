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
| 20 ns production | Worker B recovered at `12/12` cores: 4 checkpoint-resumed jobs at `10.06-15.91 ns / 20 ns`; Worker A backfill reconnect pending as of `2026-06-22 21:41 CST`; `LiDA-1` and `LiDS-1` complete |
| Structural clustering | 2/8 complete; `LiDA-1` top cluster `17.94%`; `LiDS-1` top cluster `14.59%`; others queued after production |
| PMF handoff | Umbrella windows active: `LiDA-1` `11/15`, active `011-014`; `LiDS-1` `1/17`, queued behind current Worker B load |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | Recovered checkpoint resume on Worker B; `15.14 ns / 20 ns`; clustering queued |
| `LiD3-Flex` | Recovered checkpoint resume on Worker B; `10.06 ns / 20 ns`; clustering queued |
| `LiND-Hybrid` | Worker A backfill reconnect pending |
| `LiLC-1` | Recovered checkpoint resume on Worker B; `15.91 ns / 20 ns`; clustering queued |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; umbrella `1/17` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; umbrella `11/15`, active `011-014` |
| `LiN3-Core` | Worker A backfill reconnect pending |
| `LiA3-Ref` | Recovered checkpoint resume on Worker B; `14.66 ns / 20 ns`; clustering queued |

Live run summaries are kept in `remote_runs/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
