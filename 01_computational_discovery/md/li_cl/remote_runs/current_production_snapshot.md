# LiCl Production and Clustering Snapshot

Synced from remote logs on 2026-06-15 20:26 CST.

| Candidate | Stage | Status | Last step | Time ps | Progress | T K | P bar | Constraint RMSD | Fatal markers |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| LiD3-1 | production_20ns | complete | 10000000 | 20000 | 100.00% | final log complete | final log complete | final log complete | false |
| LiD3-1 | clustering_20ns_repair | complete | 2001 frames | - | top cluster 15.69% | - | - | - | false |
| LiND-1 | production_20ns | blocked: `grompp_failed` | - | - | - | - | - | - | true |
| IDP-Li-1 | production_20ns | complete | 10000000 | 20000 | 100.00% | final log complete | final log complete | final log complete | false |
| IDP-Li-1 | clustering_20ns_repair | complete | 2001 frames | - | top cluster 7.00% | - | - | - | false |
| IDP-Li-2 | production_20ns | blocked: `grompp_failed` | - | - | - | - | - | - | true |
| LowCharge-Li | production_20ns | blocked: `grompp_failed` | - | - | - | - | - | - | true |
| LiD2-IDP | production_20ns | blocked: `grompp_failed` | - | - | - | - | - | - | true |
| StrongBind-Li | production_20ns | running | 910000 | 1820.00000 | 9.10% | 2.98966e+02 | 7.73441e+01 | 3.30142e-06 | false |
| NaCl queue | production_20ns | waiting behind LiCl queue | - | - | - | - | - | - | false |

## QC Interpretation

- `LiD3-1` completed 20 ns LiCl production successfully at 2026-06-15 04:48:55 CST.
- The completed `LiD3-1` production log has no fatal-error markers. Key finished products have been synced locally: production `.log`, final `.gro`, `.edr`, and `mdrun.stdout.log`. The large complete `.xtc` remains on the remote to avoid repeated large transfers.
- The original `LiD3-1` post-production `gmx trjconv` centering step failed because the selected `SYSTEM` index contains atom index 68234 while the trajectory contains 68233 atoms. This was repaired with a peptide-only clustering path.
- `IDP-Li-1` completed 20 ns LiCl production successfully at 2026-06-15 18:36:57 CST. Its original full-system clustering also failed by the same one-atom index mismatch, then succeeded with the peptide-only repair path.
- Repaired representative structures now exist for `LiD3-1` and `IDP-Li-1` under `cluster_20ns_repair/representative_top_cluster.pdb`.
- Top-cluster populations are low: `LiD3-1` 314/2001 frames (15.69%) and `IDP-Li-1` 140/2001 frames (7.00%). This is consistent with strong conformational heterogeneity and supports treating these peptides as flexible/IDP-like systems.
- `LiND-1`, `IDP-Li-2`, `LowCharge-Li`, and `LiD2-IDP` did not start production. Their production `gmx grompp` failed because `toppar/forcefield.itp` was not found from the production working context.
- The queue has moved on to `StrongBind-Li`, which is currently running 20 ns LiCl production. Its latest synced production state is 1.82 ns / 20 ns, temperature near 299 K, small constraint RMSD, and no fatal markers.

## Synced Small Artifacts

| Candidate | Local artifact | Purpose |
|---|---|---|
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/run_prod_20ns/step5_production_20ns.log` | Completed production log |
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/run_prod_20ns/step5_production_20ns.gro` | Final production coordinates |
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/run_prod_20ns/step5_production_20ns.edr` | Completed production energy file |
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/cluster_20ns/trjconv_center.log` | Clustering failure diagnosis |
| LiND-1 | `remote_results/systems/LiND-1/gromacs/run_prod_20ns/step5_production_20ns.grompp.log` | Production setup failure diagnosis |
| IDP-Li-1 | `remote_results/systems/IDP-Li-1/gromacs/run_prod_20ns/step5_production_20ns.log` | Active production progress |
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/cluster_20ns_repair/representative_top_cluster.pdb` | Repaired representative structure |
| IDP-Li-1 | `remote_results/systems/IDP-Li-1/gromacs/cluster_20ns_repair/representative_top_cluster.pdb` | Repaired representative structure |
| LiCl repair | `remote_runs/clustering_repair_summary.tsv` | Repaired clustering status summary |
| LiCl queue | `remote_runs/production_clustering_summary.tsv` | Queue-level status summary |

## Runtime Estimate

The active `StrongBind-Li` production run has reached 0.910 million of 10 million steps after about 1.8 hours of `gmx mdrun` wall time.

| Scope | Estimate |
|---|---:|
| `StrongBind-Li` production remaining | roughly 18-20 hours if the current rate holds |
| LiD3-1 clustering repair | complete |
| IDP-Li-1 clustering repair | complete |
| LiND-1 production repair | short setup repair, then full 20 ns production |
| All remaining LiCl production/clustering, if sequential CPU-only | roughly 8-10 days |
| NaCl production/clustering after LiCl, if sequential CPU-only | roughly 10 additional days |

These are rough CPU-only estimates from current observed rates. Actual time can shift with system size, clustering overhead, and remote CPU scheduling.

## Next Scientific Gate

`LiD3-1` and `IDP-Li-1` now have representative structures from repaired peptide-only clustering. The next scientific gate is to decide whether to use the largest cluster representative directly for umbrella sampling or to inspect/compare additional clusters because the top-cluster populations are low.
