# Umbrella Sampling Status

Last updated: 2026-06-24 10:18 CST

## Launch Rule

Umbrella sampling is condition-specific. A candidate-condition can enter window design and umbrella sampling as soon as that condition has completed 20 ns production, structural clustering, and representative extraction. It does not need to wait for the matched LiCl/NaCl condition.

## Umbrella Window Meter

| Candidate | Condition | Worker | Complete / total | Active windows | Window meter |
|---|---|---|---:|---|---|
| `LiDA-1` | LiCl | replacement Worker A | `8/19` | `008-009` | `🟩🟩🟩🟩🟩🟩🟩🟩🟦🟦` |
| `LiDS-1` | LiCl | replacement Worker A | `12/21` | `012-017` | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦⬜⬜⬜` |
| `LiD3-Core` | LiCl | replacement Worker A | `0/21` | `000` | `🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiLC-1` | LiCl | replacement Worker A | `0/21` | `000` | `🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiN3-Core` | LiCl | replacement Worker A | `0/21` | `000` | `🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiA3-Ref` | LiCl | replacement Worker A | `0/21` | `000` | `🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiDA-1` | NaCl | Worker B | `15/15` | repair windows `000,001,002,013,014` active | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 + 🟦 repair` |
| `LiDS-1` | NaCl | Worker B | `17/17` | complete | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩` |
| `LiLC-1` | NaCl | Worker B | `0/21` | `000-001` | `🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiA3-Ref` | NaCl | Worker B | `0/pending` | pull active | `🟦 pull` |
| `LiD3-Core` | NaCl | Worker B | `0/pending` | pull active after topology repair | `🟦 pull` |

Current umbrella progress: `56` current windows complete; `12` window mdruns active on replacement Worker A, `2` `LiLC-1` NaCl windows active on Worker B, `LiA3-Ref` plus `LiD3-Core` NaCl pulls active on Worker B, and `5` LiDA-1 NaCl WHAM/QC repair extension windows active on Worker B.

NaCl `LiDA-1` completed all 15 valid windows and now has a preliminary GROMACS WHAM profile with QC warnings. A valid-15 diagnostic WHAM pass showed that coarser binning removes the empty-bin artifact, but weak edge bins persist and time-sliced outer-minus-minimum Delta G is unstable (`0.93-2.41 kJ/mol`), so five edge-window extension repairs were launched in a separate repair folder. LiCl `LiDA-1` completed windows `000-007` and has windows `008-009` active. LiCl `LiDS-1` completed windows `000-011` and has windows `012-017` active. NaCl `LiDS-1` completed all 17 valid windows and is ready for preliminary WHAM/QC when compute and analysis scheduling allow. NaCl `LiLC-1` has windows `000-001` active. NaCl `LiA3-Ref` and `LiD3-Core` were clustered this cycle and entered PBC-safe umbrella pulls; `LiD3-Core` required a topology-selection repair before the pull started.

## Compute Fit

| Worker | Existing MD load | Umbrella load | Total |
|---|---:|---:|---:|
| replacement Worker A | 6 threads | 12 threads | 18/18 |
| Worker B | 2 production threads | 2 window threads + 2 pull threads + 5 repair extension threads | 11/12 |

No candidate-condition-stage is duplicated. Umbrella jobs were launched only for clustered conditions with representative structures already available.

## PBC-Safe Umbrella Repair

The first NaCl `LiDA-1` pull exposed a real GROMACS periodic-boundary failure: the peptide-ion pull distance exceeded the allowed half-box distance. The failed pull directory is retained remotely as diagnostic evidence and is not treated as scientific output.

The umbrella driver now computes a per-system safe pull extension from the actual full-system `.gro` box vectors before generating windows. It records both the requested extension and the effective extension in `umbrella_metadata.tsv`, archives incompatible or failed pull/window folders, and only reuses a pull trajectory when its saved configuration marker matches the current PBC-safe settings.

Current valid complete windows are `LiDA-1` NaCl `000-014`, `LiDS-1` NaCl `000-016`, `LiDA-1` LiCl `000-007`, `LiDS-1` LiCl `000-011`, plus first LiCl windows for `LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref`. Active windows are `LiDA-1` LiCl `008-009`, `LiDS-1` LiCl `012-017`, `LiD3-Core` LiCl `001`, `LiLC-1` LiCl `001`, `LiN3-Core` LiCl `001`, `LiA3-Ref` LiCl `001`, and `LiLC-1` NaCl `000-001`; `LiA3-Ref` and `LiD3-Core` NaCl pulls are active.

Preliminary PMF/QC output exists for NaCl `LiDA-1` under `pmf_wham_prelim_20260623_0905/`: GROMACS WHAM converged from 15 complete windows after a 100 ps burn-in. The original QC summary reports preliminary outer-minus-minimum PMF `3.70 kJ/mol`, with `1` empty histogram bin and `29/200` weak/single-window bins. The follow-up valid-15 diagnostic under `pmf_wham_diagnostic_valid15_20260624_095453/` produced `0` empty bins at 100, 75, and 50 bins, but retained `14`, `10`, and `6` weak/single-window bins, respectively. Time-sliced outer-minus-minimum Delta G changed from `1.40` to `0.93` to `2.41 kJ/mol`, so this remains QC-only. Five copied edge windows (`000`, `001`, `002`, `013`, `014`) were relaunched as `umbrella_ext` repairs under `pmf_wham_repair_edge_extend_20260624_101516/`; combined WHAM and bootstrap should run after these extensions complete.

`LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` LiCl completed clustering with top cluster populations `12.69%`, `4.15%`, `4.65%`, and `5.05%`, respectively. `LiLC-1` NaCl also clustered with top cluster population `1.95%`. These low populations suggest broad peptide disorder, but representative structures were produced and their next umbrella gates can proceed.

`LiDS-1` NaCl completed production and clustering with top-cluster population `14.59%`. Its repaired umbrella run finished all `17/17` windows. WHAM, PMF, Delta G, and Delta Delta G output are not final yet; the next analysis gate is preliminary WHAM/QC, followed by overlap and convergence review.

`LiA3-Ref` and `LiD3-Core` NaCl completed clustering this cycle with top-cluster populations `7.35%` and `10.34%`. Both were launched into umbrella pulls on Worker B. `LiD3-Core` initially failed at pull `grompp` because the umbrella script preferred a stale `topol_clean_attempt1.top`; the script now prefers the production-consistent `topol_clean_attempt2.top` before the `run_min` copy, and the repaired pull is running. The failed pulls are diagnostics only and are not scientific output.

## Implementation

Umbrella orchestration uses:

```text
01_computational_discovery/md/remote_orchestration/scripts/run_lisper_umbrella_sampling.py
```

The driver extracts the full solvated representative frame from the completed production trajectory, selects the nearest Li+ or Na+ ion to the peptide center of mass, builds explicit `SOLU`, `SOLV`, `SYSTEM`, and `TARGET_ION` index groups, caps the initial pull below the GROMACS PBC half-box limit, then launches one-thread umbrella windows sequentially by default.
