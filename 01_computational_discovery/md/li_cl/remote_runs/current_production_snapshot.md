# LiCl Production and Clustering Snapshot

Synced from remote logs on 2026-06-14 22:03 CST.

| Candidate | Stage | Status | Last step | Time ps | Progress | T K | P bar | Constraint RMSD | Fatal markers |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| LiD3-1 | production_20ns | running | 7235000 | 14470.00000 | 72.35% | 2.98860e+02 | -9.39621e+01 | 5.07506e-06 | false |

## QC Interpretation

- Active remote job: `LiD3-1` LiCl 20 ns production MD.
- Current progress: 14.47 ns of 20 ns complete.
- Temperature is stable near 299 K.
- Constraint RMSD remains small, consistent with a numerically healthy constrained run.
- No fatal-error markers were found in the synced production log.
- The `cluster_20ns/` folder exists but is still empty, which is expected before production finishes.
- No representative structure is available yet; umbrella-sampling setup should wait for clustering.

## Runtime Estimate

The active `LiD3-1` production run has reached 7.235 million of 10 million steps after about 18.3 hours of `gmx mdrun` wall time.

| Scope | Estimate |
|---|---:|
| `LiD3-1` production remaining | about 6-7 hours |
| All remaining LiCl production/clustering, if sequential at current speed | about 10 days |
| NaCl production/clustering after LiCl, if sequential at current speed | about 10 additional days |

These are rough CPU-only estimates from the current LiD3-1 rate. Actual time can shift with system size, clustering overhead, and remote CPU scheduling.
