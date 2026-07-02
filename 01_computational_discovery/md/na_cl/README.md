# NaCl Molecular Dynamics

NaCl MD is tracked under the final 8-candidate names.

NaCl simulations are being generated as matched comparison systems for the revised 8-candidate library.

## Status

Legend: 🟢 complete, 🔵 running, 🟡 queued, 🟣 QC, 🔺 repair/warning, ⚫ planned. NaCl color is identity only.

| Stage | Status |
|---|---|
| ESMFold intake | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> ready |
| CHARMM-GUI NaCl systems | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> GROMACS-ready |
| Minimization | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> minimized including LiN3-Core add-on |
| Equilibration | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> equilibrated |
| 20 ns production | <img alt="running" src="https://img.shields.io/badge/running-backfill-38BDF8"> 6/8 complete; Worker A backfill active |
| Structural clustering | <img alt="running" src="https://img.shields.io/badge/running-6%2F8-38BDF8"> new top cluster: `LiD3-Flex` `3.80%` |
| Free-energy handoff | <img alt="running" src="https://img.shields.io/badge/refined_umbrella-running-38BDF8"> reps handed to `../../umbrella/`; PMF waits in `../../pmf/` |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `10.34%`; umbrella `4/21` complete; windows `004-007` active |
| `LiD3-Flex` | `20.00 ns / 20 ns`; representative ready, top cluster `3.80%`; refined umbrella pull active |
| `LiND-Hybrid` | Replacement Worker A backfill active; `7.48 ns / 20 ns`; clustering queued |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `1.95%`; umbrella `4/21` complete; windows `004-005` active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; old-parameter umbrella `17/17` complete; preliminary WHAM/QC complete with empty/weak-bin warnings; audited binding-site v2 window equilibration active on Worker B |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; old-parameter umbrella `15/15` complete; repair extensions `5/5` complete; combined WHAM/bootstrap QC complete but preliminary; audited binding-site v2 window equilibration active on Worker B with `LISPER_JOBS=4` |
| `LiN3-Core` | Replacement Worker A backfill active; `11.52 ns / 20 ns`; clustering queued |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `7.35%`; umbrella `4/21` complete; windows `004-007` active |

Live MD run summaries are kept in `remote_runs/`. Umbrella sampling status is in `../../umbrella/remote_runs_umbrella_sampling_status.md`; WHAM/PMF QC is in `../../pmf/`. Earlier non-active library summaries are archived under `remote_runs/legacy_10_candidate/`.
