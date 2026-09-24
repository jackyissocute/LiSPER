# NaCl Molecular Dynamics

NaCl MD is tracked under the final 8-candidate names.

NaCl simulations were generated as matched comparison systems for the final eight-candidate library.

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
| Free-energy handoff | Complete for all eight candidates; paired estimates are in `../../pmf/` |

## Candidate Notes

| Candidate | NaCl production state |
|---|---|
| `LiD3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `10.34%` |
| `LiD3-Flex` | `20.00 ns / 20 ns`; representative ready; top cluster `3.80%` |
| `LiND-Hybrid` | `20.00 ns / 20 ns`; representative ready |
| `LiLC-1` | `20.00 ns / 20 ns`; representative ready; top cluster `1.95%` |
| `LiDS-1` | `20.00 ns / 20 ns`; representative ready; top cluster `14.59%` |
| `LiDA-1` | `20.00 ns / 20 ns`; representative ready; top cluster `17.94%` |
| `LiN3-Core` | `20.00 ns / 20 ns`; representative ready; top cluster `11.44%` |
| `LiA3-Ref` | `20.00 ns / 20 ns`; representative ready; top cluster `7.35%` |

MD run records are in `remote_runs/`; completed umbrella evidence and WHAM/PMF QC are in `../../umbrella/` and `../../pmf/`.
