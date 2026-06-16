# LiCl Production and Clustering Snapshot

Synced from remote logs on 2026-06-16 11:27 CST.

| Candidate | Stage | Status | Last step | Time ps | Progress | T K | P bar | Constraint RMSD | Fatal markers |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| LiD3-1 | production_20ns | complete | 10000000 | 20000 | 100.00% | final log complete | final log complete | final log complete | false |
| LiD3-1 | clustering_20ns_repair | complete | 2001 frames | - | top cluster 15.69% | - | - | - | false |
| LiND-1 | production_20ns | rerun queued after topology-path repair | - | - | - | - | - | - | false |
| IDP-Li-1 | production_20ns | complete | 10000000 | 20000 | 100.00% | final log complete | final log complete | final log complete | false |
| IDP-Li-1 | clustering_20ns_repair | complete | 2001 frames | - | top cluster 7.00% | - | - | - | false |
| IDP-Li-2 | production_20ns | rerun queued after topology-path repair | - | - | - | - | - | - | false |
| LowCharge-Li | production_20ns | rerun queued after topology-path repair | - | - | - | - | - | - | false |
| LiD2-IDP | production_20ns | rerun queued after topology-path repair | - | - | - | - | - | - | false |
| StrongBind-Li | production_20ns | running | 8935000 | 17870.00000 | 89.35% | 297.04 | -152.67 | 1.71264e-06 | false |
| SoftCage-Li | production_20ns | queued | - | - | - | - | - | - | false |
| IDP-Rich-Li | production_20ns | queued | - | - | - | - | - | - | false |
| Control-Negative | production_20ns | queued | - | - | - | - | - | - | false |
| NaCl queue | production_20ns | waiting behind LiCl queue with patched script | - | - | - | - | - | - | false |

## QC Interpretation

- `StrongBind-Li` LiCl production is active and healthy at 17.87 ns / 20 ns, with temperature near 300 K, fluctuating NPT pressure, small constraint RMSD, and no fatal markers in the synced log tail.
- `LiD3-1` and `IDP-Li-1` completed 20 ns LiCl production and now have repaired peptide-only representative structures.
- Repaired top-cluster populations remain low: `LiD3-1` 15.69% and `IDP-Li-1` 7.00%. This supports the IDP-like hypothesis and means later PMF setup should consider whether extra representative clusters are scientifically useful.
- The earlier `toppar/forcefield.itp` production setup failures are treated as setup/path failures, not peptide physics failures. The post-StrongBind recovery watcher is expected to requeue affected candidates through corrected topology-path logic.
- NaCl production/clustering remains queued behind the LiCl branch.

## Synced Small Artifacts

| Candidate | Local artifact | Purpose |
|---|---|---|
| StrongBind-Li | `remote_results/systems/StrongBind-Li/gromacs/run_prod_20ns/step5_production_20ns.log` | Active production progress/QC |
| StrongBind-Li | `remote_results/systems/StrongBind-Li/gromacs/run_prod_20ns/step5_production_20ns.grompp.log` | Production setup record |
| LiD3-1 | `remote_results/systems/LiD3-1/gromacs/cluster_20ns_repair/representative_top_cluster.pdb` | Repaired representative structure |
| IDP-Li-1 | `remote_results/systems/IDP-Li-1/gromacs/cluster_20ns_repair/representative_top_cluster.pdb` | Repaired representative structure |
| LiCl repair | `remote_runs/clustering_repair_summary.tsv` | Repaired clustering status summary |
| LiCl queue | `remote_runs/production_clustering_summary.tsv` | Queue-level status summary |

## Runtime Estimate

`StrongBind-Li` is 2.13 ns from the 20 ns endpoint. At the observed CPU-only pace, the active run likely needs roughly 1.5-3 more hours before clustering and queue recovery can begin.

| Scope | Estimate |
|---|---:|
| `StrongBind-Li` production remaining | roughly 1.5-3 hours |
| LiD3-1 clustering repair | complete |
| IDP-Li-1 clustering repair | complete |
| Remaining LiCl production/clustering, if sequential CPU-only | roughly 8-10 days |
| NaCl production/clustering after LiCl, if sequential CPU-only | roughly 10 additional days |
| PMF / Delta G extraction after representatives | roughly 3-7 days |

## Next Scientific Gate

After `StrongBind-Li` reaches 20 ns, the conservative next step is repaired peptide-only clustering for `StrongBind-Li`, followed by corrected LiCl production reruns for candidates that were previously blocked by topology include paths. Umbrella sampling should wait until matched Li+ and Na+ representative structures exist for the same peptide.
