# LiCl GROMACS Remote Progress Report

Generated from synced remote outputs on 2026-06-13.

## Summary

- Minimized and equilibrated systems: 10/10
- Active remote GROMACS processes at sync time: 0
- Remote execution mode: CPU-only GROMACS, 1 MPI rank x 16 OpenMP threads
- Synced outputs: minimized GRO/logs, equilibrated GRO/XTC/EDR/logs, cleaned indexes, cleaned topologies, repair summaries

## Systems

| Candidate | Min | Eq | Eq wall s | ns/day | Finished | Repair note |
|---|---:|---:|---:|---:|---|---|
| LiD3-1 | minimized | equilibrated | 1143.401 | 9.446 | Sat Jun 13 23:17:05 2026 | attempt0:atom19899:remove_neighbor_water:160:H2:dist=0.0953;target=6674:H1:TIP3 22634->22633 |
| LiND-1 | minimized | equilibrated | 1227.245 | 8.800 | Sat Jun 13 21:06:52 2026 | none |
| IDP-Li-1 | minimized | equilibrated | 652.789 | 16.545 | Sat Jun 13 21:17:47 2026 | attempt0:atom25963:remove_neighbor_water:1611:OH2:dist=0.0972;target=8667:H2:TIP3 11395->11394 |
| IDP-Li-2 | minimized | equilibrated | 834.583 | 12.941 | Sat Jun 13 21:31:45 2026 | none |
| LowCharge-Li | minimized | equilibrated | 825.979 | 13.075 | Sat Jun 13 21:45:33 2026 | none |
| LiD2-IDP | minimized | equilibrated | 851.490 | 12.684 | Sat Jun 13 21:59:47 2026 | none |
| StrongBind-Li | minimized | equilibrated | 905.921 | 11.922 | Sat Jun 13 22:14:56 2026 | attempt0:atom43780:remove_neighbor_water:1955:H2:dist=0.0312;target=14619:H2:TIP3 16971->16970 |
| SoftCage-Li | minimized | equilibrated | 642.801 | 16.802 | Sat Jun 13 22:25:42 2026 | none |
| IDP-Rich-Li | minimized | equilibrated | 765.587 | 14.107 | Sat Jun 13 22:38:30 2026 | none |
| Control-Negative | minimized | equilibrated | 1079.966 | 10.000 | Sat Jun 13 22:56:32 2026 | none |

## Files

- Summary TSV: `01_computational_discovery/md/li_cl/remote_runs/equilibration_progress.tsv`
- Minimization summary: `01_computational_discovery/md/li_cl/remote_runs/minimization_summary.tsv`
- Equilibration summary: `01_computational_discovery/md/li_cl/remote_runs/equilibration_summary.tsv`
- Per-system outputs: `01_computational_discovery/md/li_cl/remote_results/systems/<candidate>/gromacs/run_min/` and `run_eq/`
