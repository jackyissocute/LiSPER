# Umbrella Sampling Status

Last updated: 2026-06-21 14:36 CST

## Launch Rule

Umbrella sampling is condition-specific. A candidate-condition can enter window design and umbrella sampling as soon as that condition has completed 20 ns production, structural clustering, and representative extraction. It does not need to wait for the matched LiCl/NaCl condition.

## Active Umbrella Tasks

| Candidate | Condition | Worker | Stage | Threads | Status |
|---|---|---|---|---:|---|
| `LiDA-1` | LiCl | Worker A | PBC-safe initial pulling from clustered full-system representative | 1 | Active; effective pull extension 1.80 nm |
| `LiDS-1` | LiCl | Worker A | PBC-safe initial pulling from clustered full-system representative | 1 | Active; effective pull extension 2.00 nm |
| `LiDA-1` | NaCl | Worker B | PBC-safe initial pulling from clustered full-system representative | 1 | Active; effective pull extension 1.40 nm |

## Compute Fit

| Worker | Existing MD load | Umbrella load | Total |
|---|---:|---:|---:|
| Worker A | 14 threads | 2 threads | 16/16 |
| Worker B | 10 threads | 1 thread | 11/12 |

No candidate-condition-stage is duplicated. Umbrella jobs were launched only for clustered conditions with representative structures already available.

## PBC-Safe Umbrella Repair

The first NaCl `LiDA-1` pull exposed a real GROMACS periodic-boundary failure: the peptide-ion pull distance exceeded the allowed half-box distance. The failed pull directory is retained remotely as diagnostic evidence and is not treated as scientific output.

The umbrella driver now computes a per-system safe pull extension from the actual full-system `.gro` box vectors before generating windows. It records both the requested extension and the effective extension in `umbrella_metadata.tsv`, archives incompatible or failed pull/window folders, and only reuses a pull trajectory when its saved configuration marker matches the current PBC-safe settings.

## Implementation

Umbrella orchestration uses:

```text
01_computational_discovery/md/remote_orchestration/scripts/run_lisper_umbrella_sampling.py
```

The driver extracts the full solvated representative frame from the completed production trajectory, selects the nearest Li+ or Na+ ion to the peptide center of mass, builds explicit `SOLU`, `SOLV`, `SYSTEM`, and `TARGET_ION` index groups, caps the initial pull below the GROMACS PBC half-box limit, then launches one-thread umbrella windows sequentially by default.
