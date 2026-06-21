# Umbrella Sampling Status

Last updated: 2026-06-22 03:10 CST

## Launch Rule

Umbrella sampling is condition-specific. A candidate-condition can enter window design and umbrella sampling as soon as that condition has completed 20 ns production, structural clustering, and representative extraction. It does not need to wait for the matched LiCl/NaCl condition.

## Umbrella Window Meter

| Candidate | Condition | Worker | Complete / total | Active windows | Window meter |
|---|---|---|---:|---|---|
| `LiDA-1` | LiCl | Worker A | `2/19` | `002` | `🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiDS-1` | LiCl | Worker A | `1/21` | `001` | `🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiDA-1` | NaCl | Worker B | `3/15` | `003-004` | `🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜` |

Total valid umbrella window progress: `6/55` complete; `4` windows active.

## Compute Fit

| Worker | Existing MD load | Umbrella load | Total |
|---|---:|---:|---:|
| Worker A | 14 threads | 2 threads | 16/16 |
| Worker B | 10 threads | 2 threads | 12/12 |

No candidate-condition-stage is duplicated. Umbrella jobs were launched only for clustered conditions with representative structures already available.

## PBC-Safe Umbrella Repair

The first NaCl `LiDA-1` pull exposed a real GROMACS periodic-boundary failure: the peptide-ion pull distance exceeded the allowed half-box distance. The failed pull directory is retained remotely as diagnostic evidence and is not treated as scientific output.

The umbrella driver now computes a per-system safe pull extension from the actual full-system `.gro` box vectors before generating windows. It records both the requested extension and the effective extension in `umbrella_metadata.tsv`, archives incompatible or failed pull/window folders, and only reuses a pull trajectory when its saved configuration marker matches the current PBC-safe settings.

Current repaired pulls completed cleanly and generated PBC-safe window sets. Completed valid windows are `LiDA-1` LiCl `000-001`, `LiDS-1` LiCl `000`, and `LiDA-1` NaCl `000-002`. A duplicate NaCl `window_001` launch was caught, stopped, and archived as diagnostic; that superseded folder is preserved but not counted as a valid scientific window. Active windows are `LiDA-1` LiCl `002`, `LiDS-1` LiCl `001`, and `LiDA-1` NaCl `003-004`. WHAM, PMF, Delta G, and Delta Delta G output are not available yet.

## Implementation

Umbrella orchestration uses:

```text
01_computational_discovery/md/remote_orchestration/scripts/run_lisper_umbrella_sampling.py
```

The driver extracts the full solvated representative frame from the completed production trajectory, selects the nearest Li+ or Na+ ion to the peptide center of mass, builds explicit `SOLU`, `SOLV`, `SYSTEM`, and `TARGET_ION` index groups, caps the initial pull below the GROMACS PBC half-box limit, then launches one-thread umbrella windows sequentially by default.
