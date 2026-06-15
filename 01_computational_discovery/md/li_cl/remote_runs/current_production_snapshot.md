# LiCl Production and Clustering Snapshot

Synced from remote logs on 2026-06-15 14:20 CST.

| Candidate | Stage | Status | Last step | Time ps | Progress | T K | P bar | Constraint RMSD | Fatal markers |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| LiD3-1 | production_20ns | complete | 10000000 | 20000 | 100.00% | final log complete | final log complete | final log complete | false |
| LiD3-1 | clustering_20ns | blocked: `trjconv_failed` | - | - | - | - | - | - | true |
| LiND-1 | production_20ns | blocked: `grompp_failed` | - | - | - | - | - | - | true |
| IDP-Li-1 | production_20ns | running | 6985000 | 13970.00000 | 69.85% | 2.97419e+02 | 6.39866e+01 | 1.66524e-06 | false |
| NaCl queue | production_20ns | waiting behind LiCl queue | - | - | - | - | - | - | false |

## QC Interpretation

- `LiD3-1` completed 20 ns LiCl production successfully at 2026-06-15 04:48:55 CST.
- The completed `LiD3-1` production log has no fatal-error markers. Key finished products have been synced locally: production `.log`, final `.gro`, `.edr`, and `mdrun.stdout.log`. The large complete `.xtc` remains on the remote to avoid repeated large transfers.
- `LiD3-1` did not produce a representative structure. The post-production `gmx trjconv` centering step failed because the selected `SYSTEM` index contains atom index 68234 while the trajectory contains 68233 atoms. This is an index/trajectory consistency problem at the clustering handoff, not a failed MD trajectory.
- `LiND-1` did not start production. Its production `gmx grompp` failed because `toppar/forcefield.itp` was not found from the production working context.
- The queue has moved on to `IDP-Li-1`, which is currently running 20 ns LiCl production. Its latest synced production state is 13.97 ns / 20 ns, temperature near 297 K, small constraint RMSD, and no fatal markers.
- No candidate has a valid `cluster_20ns/representative_top_cluster.pdb` yet, so umbrella sampling should not start.

## Synced Small Artifacts

| Candidate | Local artifact | Purpose |
|---|---|---|
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/run_prod_20ns/step5_production_20ns.log` | Completed production log |
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/run_prod_20ns/step5_production_20ns.gro` | Final production coordinates |
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/run_prod_20ns/step5_production_20ns.edr` | Completed production energy file |
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/cluster_20ns/trjconv_center.log` | Clustering failure diagnosis |
| LiND-1 | `remote_results/systems/LiND-1/gromacs/run_prod_20ns/step5_production_20ns.grompp.log` | Production setup failure diagnosis |
| IDP-Li-1 | `remote_results/systems/IDP-Li-1/gromacs/run_prod_20ns/step5_production_20ns.log` | Active production progress |
| LiCl queue | `remote_runs/production_clustering_summary.tsv` | Queue-level status summary |

## Runtime Estimate

The active `IDP-Li-1` production run has reached 6.985 million of 10 million steps after about 9.5 hours of `gmx mdrun` wall time.

| Scope | Estimate |
|---|---:|
| `IDP-Li-1` production remaining | about 4 hours if the current rate holds |
| LiD3-1 clustering repair | short after production CPU load is available |
| LiND-1 production repair | short setup repair, then full 20 ns production |
| All remaining LiCl production/clustering, if sequential CPU-only | roughly 8-10 days |
| NaCl production/clustering after LiCl, if sequential CPU-only | roughly 10 additional days |

These are rough CPU-only estimates from current observed rates. Actual time can shift with system size, clustering overhead, and remote CPU scheduling.

## Next Scientific Gate

Do not start umbrella sampling yet. The next gate is to obtain at least one valid clustered representative structure, ideally beginning with `LiD3-1` after repairing the trajectory-centering/index selection issue.
