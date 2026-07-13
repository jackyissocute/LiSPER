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
| 20 ns production | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> |
| Structural clustering | <img alt="complete" src="https://img.shields.io/badge/complete-8%2F8-22C55E"> representatives ready |
| Free-energy handoff | <img alt="running" src="https://img.shields.io/badge/paired_umbrella-running-38BDF8"> all eight NaCl pulls active; PMF waits in `../../pmf/` |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `10.34%`; paired pull active |
| `LiD3-Flex` | `20.00 ns / 20 ns`; representative ready; top cluster `3.80%`; paired pull active |
| `LiND-Hybrid` | `20.00 ns / 20 ns`; representative ready; paired pull active |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `1.95%`; paired pull active |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%`; paired pull active |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%`; paired pull active |
| `LiN3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `11.44%`; paired pull active |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `7.35%`; paired pull active |

Live MD run summaries are kept in `remote_runs/`. Umbrella sampling status is in `../../umbrella/remote_runs_umbrella_sampling_status.md`; WHAM/PMF QC is in `../../pmf/`. Prior library snapshots, if any, live under cold storage — see `../remote_orchestration/SYNC_PATHS.md`.
