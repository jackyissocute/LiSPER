# LiCl Production and Clustering Snapshot

Synced from remote logs on 2026-06-14 19:48 CST.

| Candidate | Stage | Status | Last step | Time ps | Progress | T K | P bar | Constraint RMSD | Fatal markers |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| LiD3-1 | production_20ns | running | 6355000 | 12710.00000 | 63.55% | 2.95817e+02 | 7.77719e+01 | 2.81087e-06 | false |

## QC Interpretation

- Active remote job: `LiD3-1` LiCl 20 ns production MD.
- Current progress: 12.71 ns of 20 ns complete.
- Temperature is stable near 296 K.
- Constraint RMSD remains small, consistent with a numerically healthy constrained run.
- No fatal-error markers were found in the synced production log.
- The `cluster_20ns/` folder exists but is still empty, which is expected before production finishes.
- No representative structure is available yet; umbrella-sampling setup should wait for clustering.

## Runtime Estimate

The active `LiD3-1` production run has reached 6.355 million of 10 million steps after about 16.0 hours of `gmx mdrun` wall time.

| Scope | Estimate |
|---|---:|
| `LiD3-1` production remaining | about 9-10 hours |
| All remaining LiCl production/clustering, if sequential at current speed | about 10 days |
| NaCl production/clustering after LiCl, if sequential at current speed | about 10 additional days |

These are rough CPU-only estimates from the current LiD3-1 rate. Actual time can shift with system size, clustering overhead, and remote CPU scheduling.
