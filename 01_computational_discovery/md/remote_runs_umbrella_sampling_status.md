# Umbrella Sampling Status

Last updated: 2026-06-25 13:25 CST

## Launch Rule

Umbrella sampling is condition-specific. A candidate-condition can enter window design and umbrella sampling as soon as that condition has completed 20 ns production, structural clustering, and representative extraction. It does not need to wait for the matched LiCl/NaCl condition.

## Umbrella Window Meter

| Candidate | Condition | Worker | Complete / total | Active windows | Window meter |
|---|---|---|---:|---|---|
| `LiDA-1` | LiCl | replacement Worker A | `14/19` | `014-015` | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟦🟦` |
| `LiDS-1` | LiCl | replacement Worker A | `21/21` | complete | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩` |
| `LiD3-Core` | LiCl | replacement Worker A | `3/21` | `003` | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |
| `LiLC-1` | LiCl | replacement Worker A | `3/21` | `003` | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |
| `LiN3-Core` | LiCl | replacement Worker A | `3/21` | `003` | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |
| `LiA3-Ref` | LiCl | replacement Worker A | `2/21` | `002` | `🟩🟩🟦⬜⬜⬜⬜⬜⬜⬜` |
| `LiDA-1` | NaCl | Worker B | `15/15` + `5/5` repair | combined WHAM QC complete | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 + 🟩 repair` |
| `LiDS-1` | NaCl | Worker B | `17/17`; v2 pull active | v2 pull `umbrella_sampling_binding_site_v2` | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩` + `🟦 v2` |
| `LiLC-1` | NaCl | Worker B | `4/21` | `004-005` | `🟩🟩🟩🟩🟦🟦⬜⬜⬜⬜` |
| `LiA3-Ref` | NaCl | Worker B | `4/21` | `004-007` | `🟩🟩🟩🟩🟦🟦🟦🟦⬜⬜` |
| `LiD3-Core` | NaCl | Worker B | `4/21` | `004-007` | `🟩🟩🟩🟩🟦🟦🟦🟦⬜⬜` |

Current umbrella progress: `90` current windows plus LiDA-1 NaCl repair extensions completed (`5/5`). Old-parameter umbrella driver processes remain paused or guarded under `UMBRELLA_QC_HOLD` after repeated WHAM overlap/bin warnings. Replacement Worker A is running audited v2 LiCl pull stages for `LiDS-1` and `LiDA-1` in separate `umbrella_sampling_binding_site_v2` folders. Worker B had safe headroom at the 13:25 CST check, so audited v2 NaCl `LiDS-1` was launched in `umbrella_sampling_binding_site_v2` with `LISPER_JOBS=6`; it is in the pull stage after a topology-path repair made `topol_cleaned_for_prod.top` point to the successful production-root topology.

NaCl `LiDA-1` completed all 15 valid windows and now has a combined original-plus-repair GROMACS WHAM/bootstrap QC pass. The repair improved histogram coverage from `1` empty bin and `29/200` weak bins to `0` empty bins and `1/100` weak bin at the 100-bin combined setting. The result remains preliminary because the residual warning sits at the outer tail and the time-sliced plateau/minimum estimate shifts (`2.02-2.97 kJ/mol` across 100-bin slices). `LiDS-1` completed WHAM/QC for both old-parameter conditions: LiCl has `0` empty bins and `9/100` weak bins, while NaCl has `2` empty bins and `12/100` weak bins. Both old-parameter `LiDS-1` PMFs remain preliminary; the paired v2 LiCl/NaCl reruns are now the path toward reliable Delta G and Delta Delta G.

## Compute Fit

| Worker | Existing MD load | Umbrella load | Total |
|---|---:|---:|---:|
| replacement Worker A | 6 threads | 7 umbrella threads, including 2 v2 pulls | 13/18 |
| Worker B | 2 production threads | 5 umbrella threads, including 1 v2 pull | 8/12 |

No candidate-condition-stage is duplicated. Umbrella jobs were launched only for clustered conditions with representative structures already available.

## Parameter Audit Hold

The common umbrella default strategy is now under QC audit because the first completed WHAM analyses show repeated coverage warnings:

- `LiDA-1` NaCl original WHAM: `1` empty bin and `29/200` weak/single-window bins; combined repair improved this to `0` empty and `1/100` weak bin but still needs tail/time-slice review.
- `LiDS-1` LiCl preliminary WHAM: `0` empty bins but `9/100` weak/single-window bins.
- `LiDS-1` NaCl preliminary WHAM: `2` empty bins and `12/100` weak/single-window bins, with time-slice shifts.

The umbrella driver is being tailored to this IDP-like peptide system rather than using a generic umbrella recipe. Active v2 launches use the dominant-cluster full-system representative frame, define the reaction coordinate as `BINDING_SITE_to_TARGET_ION` from peptide donor atoms in the representative structure, and archive any old peptide-COM pull before reuse. Defaults were changed from `0.5 ns` pull, `1.0 ns/window`, and `0.10 nm` spacing to `1.0 ns` pull, `0.5 ns` window equilibration, `2.0 ns` production per window, and `0.075 nm` spacing. A hold-file guard remains in place so normal/old launches stop unless an audited v2 launch explicitly opts in.

Rationale:

- The 20 ns production plus clustering step is used directly: the umbrella start frame is extracted from the top-cluster representative time, not an arbitrary peptide conformation.
- Because these peptides are flexible, pulling relative to the whole-peptide center of mass can be a poor binding coordinate. The new coordinate uses the local donor/binding-site atom group selected from the representative frame.
- The CHARMM-GUI water box is PBC-limited, so the effective pull extension is still capped by measured box vectors before windows are generated.
- Existing WHAM warnings mean old complete windows remain diagnostic/preliminary. Final Delta G should come only from WHAM/QC after the audited coordinate, denser windows, explicit window equilibration, bootstrap/error analysis, and time-sliced convergence checks pass.

## PBC-Safe Umbrella Repair

The first NaCl `LiDA-1` pull exposed a real GROMACS periodic-boundary failure: the peptide-ion pull distance exceeded the allowed half-box distance. The failed pull directory is retained remotely as diagnostic evidence and is not treated as scientific output.

The umbrella driver now computes a per-system safe pull extension from the actual full-system `.gro` box vectors before generating windows. It records both the requested extension and the effective extension in `umbrella_metadata.tsv`, archives incompatible or failed pull/window folders, and only reuses a pull trajectory when its saved configuration marker matches the current PBC-safe settings.

Current valid complete windows are `LiDA-1` NaCl `000-014`, `LiDA-1` NaCl repair extensions `000`, `001`, `002`, `013`, `014`, `LiDS-1` NaCl `000-016`, `LiDA-1` LiCl `000-013`, `LiDS-1` LiCl `000-020`, `LiD3-Core` LiCl `000-002`, `LiLC-1` LiCl `000-002`, `LiN3-Core` LiCl `000-002`, `LiA3-Ref` LiCl `000-001`, `LiLC-1` NaCl `000-003`, `LiA3-Ref` NaCl `000-003`, and `LiD3-Core` NaCl `000-003`. Active windows are `LiDA-1` LiCl `014-015`, `LiD3-Core` LiCl `003`, `LiLC-1` LiCl `003`, `LiN3-Core` LiCl `003`, `LiA3-Ref` LiCl `002`, `LiLC-1` NaCl `004-005`, `LiA3-Ref` NaCl `004-007`, and `LiD3-Core` NaCl `004-007`.

Preliminary PMF/QC output exists for NaCl `LiDA-1` under `pmf_wham_prelim_20260623_0905/`: GROMACS WHAM converged from 15 complete windows after a 100 ps burn-in. The original QC summary reports preliminary outer-minus-minimum PMF `3.70 kJ/mol`, with `1` empty histogram bin and `29/200` weak/single-window bins. The follow-up valid-15 diagnostic under `pmf_wham_diagnostic_valid15_20260624_095453/` produced `0` empty bins at 100, 75, and 50 bins, but retained `14`, `10`, and `6` weak/single-window bins, respectively. Five copied edge windows (`000`, `001`, `002`, `013`, `014`) completed `umbrella_ext` repair sampling under `pmf_wham_repair_edge_extend_20260624_101516/`. Combined original-plus-repair WHAM/bootstrap output under `pmf_wham_combined_repair_20260624_201216/` produced `0` empty bins and `1/100` weak bin at the 100-bin setting, but remains QC-only pending tail-materiality and time-slice convergence review.

`LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` LiCl completed clustering with top cluster populations `12.69%`, `4.15%`, `4.65%`, and `5.05%`, respectively. `LiLC-1` NaCl also clustered with top cluster population `1.95%`. These low populations suggest broad peptide disorder, but representative structures were produced and their next umbrella gates can proceed.

`LiDS-1` NaCl completed production and clustering with top-cluster population `14.59%`. Its old-parameter umbrella run finished all `17/17` windows. Preliminary WHAM/QC is complete, but Delta G and Delta Delta G output are not final. Audited binding-site v2 NaCl `LiDS-1` was launched at 2026-06-25 13:24 CST on Worker B; the first attempt failed at `grompp` because the script selected the `run_min` topology copy, then the retry succeeded after preferring the production-root topology used by the earlier successful windows. Monitor the active v2 pull, then v2 window generation, WHAM/bootstrap, and time-slice convergence before promoting any Delta G value.

`LiA3-Ref` and `LiD3-Core` NaCl completed clustering this cycle with top-cluster populations `7.35%` and `10.34%`. Both were launched into umbrella pulls on Worker B. `LiD3-Core` initially failed at pull `grompp` because the umbrella script preferred a stale `topol_clean_attempt1.top`; the script now prefers the production-consistent `topol_clean_attempt2.top` before the `run_min` copy, and the repaired pull is running. The failed pulls are diagnostics only and are not scientific output.

## Implementation

Umbrella orchestration uses:

```text
01_computational_discovery/md/remote_orchestration/scripts/run_lisper_umbrella_sampling.py
```

The driver extracts the full solvated representative frame from the completed production trajectory, selects the nearest Li+ or Na+ ion to the peptide center of mass, builds explicit `SOLU`, `SOLV`, `SYSTEM`, and `TARGET_ION` index groups, caps the initial pull below the GROMACS PBC half-box limit, then launches one-thread umbrella windows sequentially by default.
