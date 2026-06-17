# LiCl Production and Clustering Snapshot

Synced from remote logs on 2026-06-17 18:34 CST.

| Candidate | Stage | Status | Last step | Time ps | Progress | T K | P bar | Constraint RMSD | Fatal markers |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| LiD3-1 | production_20ns | complete | 10000000 | 20000 | 100.00% | final log complete | final log complete | final log complete | false |
| LiD3-1 | clustering_20ns_repair | complete | 2001 frames | - | top cluster 15.69% | - | - | - | false |
| LiND-1 | production_20ns | complete | 10000000 | 20000 | 100.00% | final log complete | final log complete | final log complete | false |
| LiND-1 | clustering_20ns | complete | 2001 frames | - | top cluster 2.40% | - | - | - | false |
| IDP-Li-1 | production_20ns | complete | 10000000 | 20000 | 100.00% | final log complete | final log complete | final log complete | false |
| IDP-Li-1 | clustering_20ns_repair | complete | 2001 frames | - | top cluster 7.00% | - | - | - | false |
| IDP-Li-2 | production_20ns | running | 2230000 | 4460.00000 | 22.30% | 300.46 | -49.12 | 3.26269e-06 | false |
| LowCharge-Li | production_20ns | rerun queued after topology-path repair | - | - | - | - | - | - | false |
| LiD2-IDP | production_20ns | rerun queued after topology-path repair | - | - | - | - | - | - | false |
| StrongBind-Li | production_20ns | complete | 10000000 | 20000 | 100.00% | final log complete | final log complete | final log complete | false |
| StrongBind-Li | clustering_20ns_repair | complete | 2001 frames | - | top cluster 3.45% | - | - | - | false |
| SoftCage-Li | production_20ns | queued | - | - | - | - | - | - | false |
| IDP-Rich-Li | production_20ns | queued | - | - | - | - | - | - | false |
| Control-Negative | production_20ns | queued | - | - | - | - | - | - | false |
| NaCl queue | production_20ns | waiting behind LiCl queue with patched script | - | - | - | - | - | - | false |

## QC Interpretation

- `LiND-1` completed 20 ns LiCl production cleanly and produced a peptide-only representative structure in `cluster_20ns/representative_top_cluster.pdb`.
- `LiD3-1`, `LiND-1`, `IDP-Li-1`, and `StrongBind-Li` now have LiCl representative structures.
- Top-cluster populations remain low: `LiD3-1` 15.69%, `LiND-1` 2.40%, `IDP-Li-1` 7.00%, and `StrongBind-Li` 3.45%. This supports the IDP-like hypothesis and means later PMF setup should consider whether extra representative clusters are scientifically useful.
- `IDP-Li-2` is now running through corrected 20 ns LiCl production. The latest synced frame shows normal temperature, small constraint RMSD, and no fatal markers.
- NaCl production/clustering remains queued behind the LiCl branch.

## Synced Small Artifacts

| Candidate | Local artifact | Purpose |
|---|---|---|
| StrongBind-Li | `remote_results/systems/StrongBind-Li/gromacs/run_prod_20ns/step5_production_20ns.log` | Completed production progress/QC |
| StrongBind-Li | `remote_results/systems/StrongBind-Li/gromacs/run_prod_20ns/step5_production_20ns.grompp.log` | Production setup record |
| StrongBind-Li | `remote_results/systems/StrongBind-Li/gromacs/cluster_20ns_repair/representative_top_cluster.pdb` | Repaired representative structure |
| LiND-1 | `remote_results/systems/LiND-1/gromacs/run_prod_20ns/step5_production_20ns.log` | Completed production progress/QC |
| LiND-1 | `remote_results/systems/LiND-1/gromacs/cluster_20ns/representative_top_cluster.pdb` | Representative structure |
| IDP-Li-2 | `remote_results/systems/IDP-Li-2/gromacs/run_prod_20ns/step5_production_20ns.log` | Active production progress/QC |
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/cluster_20ns_repair/representative_top_cluster.pdb` | Repaired representative structure |
| IDP-Li-1 | `remote_results/systems/IDP-Li-1/gromacs/cluster_20ns_repair/representative_top_cluster.pdb` | Repaired representative structure |
| LiCl repair | `remote_runs/clustering_repair_summary.tsv` | Repaired clustering status summary |
| LiCl queue | `remote_runs/production_clustering_summary.tsv` | Queue-level status summary |

## Runtime Estimate

`IDP-Li-2` has reached 4.46 ns of the 20 ns production target. At the observed CPU-only pace, the active run likely needs roughly 18-22 more hours before clustering can begin.

| Scope | Estimate |
|---|---:|
| `IDP-Li-2` production remaining | roughly 18-22 hours |
| LiD3-1 clustering repair | complete |
| LiND-1 clustering | complete |
| IDP-Li-1 clustering repair | complete |
| StrongBind-Li clustering repair | complete |
| Remaining LiCl production/clustering, if sequential CPU-only | roughly 5-7 days |
| NaCl production/clustering after LiCl, if sequential CPU-only | roughly 10 additional days |
| PMF / Delta G extraction after representatives | roughly 3-7 days |

## Next Scientific Gate

The current scientific gate is `IDP-Li-2` 20 ns LiCl production. After it reaches 20 ns, the conservative next step is peptide-only clustering for `IDP-Li-2`, followed by continued corrected LiCl production for the remaining candidates. Umbrella sampling should wait until matched Li+ and Na+ representative structures exist for the same peptide.
