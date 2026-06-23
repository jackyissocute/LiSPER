# Umbrella Sampling Status

Last updated: 2026-06-23 08:43 CST

## Launch Rule

Umbrella sampling is condition-specific. A candidate-condition can enter window design and umbrella sampling as soon as that condition has completed 20 ns production, structural clustering, and representative extraction. It does not need to wait for the matched LiCl/NaCl condition.

## Umbrella Window Meter

| Candidate | Condition | Worker | Complete / total | Active windows | Window meter |
|---|---|---|---:|---|---|
| `LiDA-1` | LiCl | replacement Worker A | pull active | window set regenerating | `🟦 pull` |
| `LiDS-1` | LiCl | replacement Worker A | `6/21` | pull/resume active | `🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜` |
| `LiD3-Core` | LiCl | replacement Worker A | pull active | window set pending | `🟦 pull` |
| `LiLC-1` | LiCl | replacement Worker A | pull active | window set pending | `🟦 pull` |
| `LiN3-Core` | LiCl | replacement Worker A | pull active | window set pending | `🟦 pull` |
| `LiA3-Ref` | LiCl | replacement Worker A | pull active | window set pending | `🟦 pull` |
| `LiDA-1` | NaCl | Worker B | `15/15` | complete | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩` |
| `LiDS-1` | NaCl | Worker B | `1/17` | `001-004` | `🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜` |

Current umbrella progress: `20` current windows complete; `6` window mdruns active and `5` LiCl pull mdruns active across both workers.

NaCl `LiDA-1` completed all 15 valid windows and now has a preliminary GROMACS WHAM profile for QC. LiCl `LiDS-1` has six valid windows complete and a conservative six-job resume driver active. NaCl `LiDS-1` has four one-thread windows active (`001-004`), filling Worker B to `12/12` threads. LiCl `LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` cleared clustering this cycle and started PBC-safe pull gates.

## Compute Fit

| Worker | Existing MD load | Umbrella load | Total |
|---|---:|---:|---:|
| replacement Worker A | 6 threads | 6 threads | 12/18 |
| Worker B | 8 threads | 4 threads | 12/12 |

No candidate-condition-stage is duplicated. Umbrella jobs were launched only for clustered conditions with representative structures already available.

## PBC-Safe Umbrella Repair

The first NaCl `LiDA-1` pull exposed a real GROMACS periodic-boundary failure: the peptide-ion pull distance exceeded the allowed half-box distance. The failed pull directory is retained remotely as diagnostic evidence and is not treated as scientific output.

The umbrella driver now computes a per-system safe pull extension from the actual full-system `.gro` box vectors before generating windows. It records both the requested extension and the effective extension in `umbrella_metadata.tsv`, archives incompatible or failed pull/window folders, and only reuses a pull trajectory when its saved configuration marker matches the current PBC-safe settings.

Current valid windows are `LiDS-1` LiCl `000-005`, `LiDA-1` NaCl `000-014`, and `LiDS-1` NaCl `000`. Active windows are `LiDS-1` NaCl `001-004`; LiDS-1 LiCl has a resume driver in its pull stage before filling additional windows. `LiDA-1` LiCl is regenerating its pull/window set after archiving an incompatible prior marker as diagnostic evidence, so its older LiCl windows are not counted as current scientific output.

Preliminary PMF/QC output exists for NaCl `LiDA-1` under `pmf_wham_prelim_20260623_0905/`: GROMACS WHAM converged from 15 complete windows after a 100 ps burn-in. This is a QC profile, not final Delta G, until histogram overlap and convergence/error checks are reviewed.

`LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` LiCl completed clustering with top cluster populations `12.69%`, `4.15%`, `4.65%`, and `5.05%`, respectively. These low populations suggest broad peptide disorder, but representative structures were produced and their LiCl pull gates are now active.

`LiDS-1` NaCl completed production and clustering with top-cluster population `14.59%`. Its first umbrella launch exposed two setup issues: a stale index atom count during full-frame extraction and a stale `topol.top` water count during pull `grompp`. Both diagnostics are preserved under `na_cl/remote_results/umbrella_sampling/LiDS-1/`. The repaired driver now extracts the frame from the production TPR's `System` group and uses the cleaned production topology; the repaired pull finished and `LiDS-1` NaCl window `000` is active. WHAM, PMF, Delta G, and Delta Delta G output are not available yet.

## Implementation

Umbrella orchestration uses:

```text
01_computational_discovery/md/remote_orchestration/scripts/run_lisper_umbrella_sampling.py
```

The driver extracts the full solvated representative frame from the completed production trajectory, selects the nearest Li+ or Na+ ion to the peptide center of mass, builds explicit `SOLU`, `SOLV`, `SYSTEM`, and `TARGET_ION` index groups, caps the initial pull below the GROMACS PBC half-box limit, then launches one-thread umbrella windows sequentially by default.
