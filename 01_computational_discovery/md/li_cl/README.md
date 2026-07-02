# LiCl Molecular Dynamics

LiCl MD is tracked under the final 8-candidate names.

## Status

Status colors match the dashboard palette: complete `#22C55E`, running `#38BDF8`, queued `#FACC15`, QC review `#A78BFA`, warning/repair/failed `#FB7185`/`#EF4444`, and planned `#64748B`. LiCl `#818CF8` is an identity accent only.

| Stage | Status |
|---|---|
| ESMFold intake | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> ready |
| CHARMM-GUI LiCl systems | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> GROMACS-ready |
| Minimization | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> minimized |
| Equilibration | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> equilibrated |
| 20 ns production | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> |
| Structural clustering | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> new top clusters: `LiD3-Flex` `4.40%`, `LiND-Hybrid` `12.89%` |
| Free-energy handoff | <img alt="running" src="https://img.shields.io/badge/refined_umbrella-running-38BDF8"> Representatives are handed to `../../umbrella/`; old/default umbrella windows are diagnostics only. Final PMF/Delta G waits in `../../pmf/` for WHAM/bootstrap/time-slice QC |

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
