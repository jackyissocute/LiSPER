# Umbrella Sampling Status

Last updated: 2026-06-21 12:26 CST

## Launch Rule

Umbrella sampling is condition-specific. A candidate-condition can enter window design and umbrella sampling as soon as that condition has completed 20 ns production, structural clustering, and representative extraction. It does not need to wait for the matched LiCl/NaCl condition.

## Active Umbrella Tasks

| Candidate | Condition | Worker | Stage | Threads | Status |
|---|---|---|---|---:|---|
| `LiDA-1` | LiCl | Worker A | Initial pulling from clustered full-system representative | 1 | Active |
| `LiDS-1` | LiCl | Worker A | Initial pulling from clustered full-system representative | 1 | Active |
| `LiDA-1` | NaCl | Worker B | Initial pulling from clustered full-system representative | 1 | Active |

## Compute Fit

| Worker | Existing MD load | Umbrella load | Total |
|---|---:|---:|---:|
| Worker A | 14 threads | 2 threads | 16/16 |
| Worker B | 10 threads | 1 thread | 11/12 |

No candidate-condition-stage is duplicated. Umbrella jobs were launched only for clustered conditions with representative structures already available.

## Implementation

Umbrella orchestration uses:

```text
01_computational_discovery/md/remote_orchestration/scripts/run_lisper_umbrella_sampling.py
```

The driver extracts the full solvated representative frame from the completed production trajectory, selects the nearest Li+ or Na+ ion to the peptide center of mass, builds explicit `SOLU`, `SOLV`, `SYSTEM`, and `TARGET_ION` index groups, runs a short pulling trajectory, then launches one-thread umbrella windows sequentially by default.
