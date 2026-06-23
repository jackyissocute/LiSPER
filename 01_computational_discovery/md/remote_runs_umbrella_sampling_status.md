# Umbrella Sampling Status

Last updated: 2026-06-23 20:41 CST

## Launch Rule

Umbrella sampling is condition-specific. A candidate-condition can enter window design and umbrella sampling as soon as that condition has completed 20 ns production, structural clustering, and representative extraction. It does not need to wait for the matched LiCl/NaCl condition.

## Umbrella Window Meter

| Candidate | Condition | Worker | Complete / total | Active windows | Window meter |
|---|---|---|---:|---|---|
| `LiDA-1` | LiCl | replacement Worker A | `2/19` | `002-003` | `🟩🟩🟦🟦⬜⬜⬜⬜⬜⬜` |
| `LiDS-1` | LiCl | replacement Worker A | `0/21` | `000-005` | `🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜` |
| `LiD3-Core` | LiCl | replacement Worker A | `0/21` | `000` | `🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiLC-1` | LiCl | replacement Worker A | `0/21` | `000` | `🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiN3-Core` | LiCl | replacement Worker A | `0/21` | `000` | `🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiA3-Ref` | LiCl | replacement Worker A | `0/21` | `000` | `🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiDA-1` | NaCl | Worker B | `15/15` | complete | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩` |
| `LiDS-1` | NaCl | Worker B | `9/17` | `009-012` | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦⬜⬜⬜⬜` |

Current umbrella progress: `26` current windows complete; `16` window mdruns active and no pull mdruns active across both workers.

NaCl `LiDA-1` completed all 15 valid windows and now has a preliminary GROMACS WHAM profile with QC warnings. The extra `window_001_1.42nm_superseded_duplicate_diagnostic_20260621_211137` directory is diagnostic only and is not counted as scientific output. LiCl `LiDA-1` completed windows `000-001` and has windows `002-003` active. LiCl `LiDS-1` has windows `000-005` active. LiCl `LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` each have window `000` active. NaCl `LiDS-1` has nine valid windows complete and four one-thread windows active (`009-012`), filling Worker B to `12/12` threads.

## Compute Fit

| Worker | Existing MD load | Umbrella load | Total |
|---|---:|---:|---:|
| replacement Worker A | 6 threads | 12 threads | 18/18 |
| Worker B | 8 threads | 4 threads | 12/12 |

No candidate-condition-stage is duplicated. Umbrella jobs were launched only for clustered conditions with representative structures already available.

## PBC-Safe Umbrella Repair

The first NaCl `LiDA-1` pull exposed a real GROMACS periodic-boundary failure: the peptide-ion pull distance exceeded the allowed half-box distance. The failed pull directory is retained remotely as diagnostic evidence and is not treated as scientific output.

The umbrella driver now computes a per-system safe pull extension from the actual full-system `.gro` box vectors before generating windows. It records both the requested extension and the effective extension in `umbrella_metadata.tsv`, archives incompatible or failed pull/window folders, and only reuses a pull trajectory when its saved configuration marker matches the current PBC-safe settings.

Current valid complete windows are `LiDA-1` NaCl `000-014`, `LiDS-1` NaCl `000-008`, and `LiDA-1` LiCl `000-001`. Active windows are `LiDA-1` LiCl `002-003`, `LiDS-1` LiCl `000-005`, `LiD3-Core` LiCl `000`, `LiLC-1` LiCl `000`, `LiN3-Core` LiCl `000`, `LiA3-Ref` LiCl `000`, and `LiDS-1` NaCl `009-012`. `LiDS-1` LiCl archived its earlier windows as superseded diagnostics during the PBC-safe pull rerun, so those older LiCl windows are not counted as current scientific output.

Preliminary PMF/QC output exists for NaCl `LiDA-1` under `pmf_wham_prelim_20260623_0905/`: GROMACS WHAM converged from 15 complete windows after a 100 ps burn-in. The QC summary reports preliminary outer-minus-minimum PMF `3.70 kJ/mol`, with `1` empty histogram bin and `29/200` weak/single-window bins. This is a QC profile, not final Delta G, until histogram overlap, uncertainty, and time-sliced convergence checks are reviewed and any needed polishing is run.

`LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` LiCl completed clustering with top cluster populations `12.69%`, `4.15%`, `4.65%`, and `5.05%`, respectively. These low populations suggest broad peptide disorder, but representative structures were produced and their LiCl pull gates are now active.

`LiDS-1` NaCl completed production and clustering with top-cluster population `14.59%`. Its first umbrella launch exposed two setup issues: a stale index atom count during full-frame extraction and a stale `topol.top` water count during pull `grompp`. Both diagnostics are preserved under `na_cl/remote_results/umbrella_sampling/LiDS-1/`. The repaired driver now extracts the frame from the production TPR's `System` group and uses the cleaned production topology; the repaired pull finished and `LiDS-1` NaCl window `000` is active. WHAM, PMF, Delta G, and Delta Delta G output are not available yet.

## Implementation

Umbrella orchestration uses:

```text
01_computational_discovery/md/remote_orchestration/scripts/run_lisper_umbrella_sampling.py
```

The driver extracts the full solvated representative frame from the completed production trajectory, selects the nearest Li+ or Na+ ion to the peptide center of mass, builds explicit `SOLU`, `SOLV`, `SYSTEM`, and `TARGET_ION` index groups, caps the initial pull below the GROMACS PBC half-box limit, then launches one-thread umbrella windows sequentially by default.
