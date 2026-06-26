# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

| Stage | Status |
|---|---|
| ESMFold intake | 8/8 ready |
| CHARMM-GUI LiCl systems | 8/8 GROMACS-ready |
| Minimization | 8/8 minimized |
| Equilibration | 8/8 equilibrated |
| 20 ns production | 8/8 complete |
| Structural clustering | 8/8 complete; new top clusters: `LiD3-Flex` `4.40%`, `LiND-Hybrid` `12.89%` |
| Free-energy handoff | Representatives are handed to `../../umbrella/`; old/default umbrella windows are diagnostics only. Refined LiCl windows/pulls are active for `LiDA-1`, `LiDS-1`, and `LiD3-Flex`; final PMF/Delta G waits in `../../pmf/` for WHAM/bootstrap/time-slice QC |

## Candidate Notes

| Candidate | LiCl production state |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `12.69%`; umbrella `3/21` complete; window `003` active |
| `LiD3-Flex` | `20.00 ns / 20 ns`; representative ready, top cluster `4.40%`; refined umbrella pull active |
| `LiND-Hybrid` | `20.00 ns / 20 ns`; representative ready, top cluster `12.89%` |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `4.15%`; umbrella `3/21` complete; window `003` active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `15.69%`; old-parameter umbrella `21/21` complete but preliminary; audited v2 window equilibration active |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.64%`; old-parameter umbrella `14/19` stopped as diagnostic; audited v2 production windows active |
| `LiN3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `4.65%`; umbrella `3/21` complete; window `003` active |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `5.05%`; umbrella `2/21` complete; window `002` active |

Live MD run summaries are kept in `remote_runs/`. Umbrella sampling status is in `../../umbrella/remote_runs_umbrella_sampling_status.md`; WHAM/PMF QC is in `../../pmf/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
