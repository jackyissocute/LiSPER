# Umbrella Sampling Status

Last updated: 2026-06-29 19:15 CST

## Launch Rule

Umbrella sampling is condition-specific. A candidate-condition can enter window design and umbrella sampling as soon as that condition has completed 20 ns production, structural clustering, and representative extraction. It does not need to wait for the matched LiCl/NaCl condition.

## Umbrella Window Meter

| Candidate | Condition | Worker | Complete / total | Active windows | Window meter |
|---|---|---|---:|---|---|
| `LiDA-1` | LiCl | Worker A | V2 `19/27` | production windows `019-022` | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟦` |
| `LiDS-1` | LiCl | Worker A | V2 `12/27` | equil windows `012-015` | `🟩🟩🟩🟩🟩🟩🟩🟦⬜⬜` |
| `LiD3-Flex` | LiCl | Worker A | V2 `0/27` | production windows `000-003` | `🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜` |
| `LiD3-Core` | LiCl | Worker A | V2 `0/27` | equil windows `000-001` | `🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiLC-1` | LiCl | replacement Worker A | `3/21` | `003` | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |
| `LiN3-Core` | LiCl | replacement Worker A | `3/21` | `003` | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |
| `LiA3-Ref` | LiCl | replacement Worker A | `2/21` | `002` | `🟩🟩🟦⬜⬜⬜⬜⬜⬜⬜` |
| `LiDA-1` | NaCl | Worker B | V2 `22/22` + V3 repair | V3 tail extensions `020-021` active | `🟩🟩🟩🟩🟩🟩🟩🟩🟦🟦` |
| `LiDS-1` | NaCl | Worker B | V2 `27/27` | WHAM complete; QC review required | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩` |
| `LiD3-Flex` | NaCl | Worker B | V2 `2/27` | production windows `002-006` | `🟩🟩🟦🟦🟦🟦🟦⬜⬜⬜` |
| `LiLC-1` | NaCl | Worker B | V2 `0/27` | production windows `000-001` | `🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiA3-Ref` | NaCl | Worker B | V2 `0/27` | pull active | `🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜` |
| `LiD3-Core` | NaCl | Worker B | V2 `0/27` | production windows `000-001` | `🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜` |

Current umbrella progress: old/default umbrella compute remains guarded after repeated WHAM overlap/bin warnings. Paired refined windows are active without duplicate candidate-condition-stage jobs. LiCl `LiDA-1` advanced to `19/27` and is running windows `019-022`; LiCl `LiDS-1` advanced to `16/27` and is running windows `016-019`; LiCl `LiD3-Flex` is running windows `000-003`; LiCl `LiD3-Core` is running windows `000-001`. NaCl `LiDA-1` completed V2 `22/22`, GROMACS WHAM/bootstrap/time-slice QC stayed preliminary, and V3 tail repair extensions for windows `020-021` are active to improve far-tail/reference sampling. NaCl `LiDS-1` completed V2 `27/27` and GROMACS WHAM completed with QC review required; NaCl `LiD3-Flex` has `2/27` complete and production windows `002-006` active. `LiLC-1` and `LiD3-Core` NaCl are running windows `000-001`. `LiA3-Ref` NaCl refined pull remains active. Old windows and repair outputs are retained only as diagnostics/preliminary QC evidence.

Scheduling note, 2026-06-29 19:15 CST: Worker A is at `18/18` real `mdrun` threads and Worker B is at `12/12` real `mdrun` threads. The last two Worker B cores were assigned to LiDA-1 NaCl V3 tail repair extensions for windows `020-021`, targeting poor-sampling bins near the outer reference tail. No candidate-condition-stage-window is duplicated.

Recovery note, 2026-06-29 00:38 CST: both workers were reachable but had no real `gmx mdrun` jobs after an accidental stop around 00:09-00:10 CST. The two NaCl production tails on Worker A were resumed from `.cpt` checkpoints with `-append`. Refined umbrella drivers were relaunched without duplicate candidate-condition-stage windows: Worker A runs `LiDA-1` cap `4`, `LiDS-1` cap `4`, `LiD3-Flex` cap `4`, and `LiD3-Core` cap `2`; Worker B runs `LiDS-1` cap `3`, `LiD3-Flex` cap `5`, `LiD3-Core` cap `2`, and `LiLC-1` cap `2`. Verified recovery load is Worker A `17/18` real `mdrun` threads and Worker B `10/12`; Worker B is below 12 while two drivers remain in single-core pull stages.

Disk note, 2026-06-29 02:58 CST: Worker B reached `92%` used during recovery. The inactive duplicate `offloaded_to_workerA_20260620_172855` copy was checked against active `mdrun` CWDs, then removed from Worker B because the corresponding production tails are already running from checkpoints on Worker A. Worker B recovered from `2.6 GB` to `3.0 GB` free (`91%` used). Active umbrella windows and PMF products were not removed.

Disk note, 2026-06-29 06:58 CST: Worker B rose to `93%` used while refined jobs continued. After checking actual `gmx` PIDs, inactive old/default `gromacs/umbrella_sampling/window_*/umbrella.xtc` trajectories were removed from superseded non-v2 runs only. This freed `6.0 GB`; the follow-up filesystem check reported Worker B at `73%` used (`8.2 GB` free). Active refined `umbrella_sampling_binding_site_v2` windows, logs, coordinates, pull files, energy files, and PMF products were preserved.

Large cleanup, 2026-06-29 10:00 CST: both workers were cleaned after enumerating active `gmx` CWDs. Deleted only stale duplicate roots, superseded old/default umbrella trajectories, completed refined-window `.xtc`/`.trr` files, and completed non-active refined pull trajectories. Preserved active CWDs, production trajectories, `.tpr`, `.gro`, `.edr`, logs, `pullx`/`pullf`, manifests, PMF/WHAM outputs, and checkpointed active production files. Worker A improved from `88%` used (`3.7 GB` free) to `41%` used (`18 GB` free). Worker B improved from `74%` used (`7.9 GB` free) to `26%` used (`23 GB` free). Cleanup logs were synced under `01_computational_discovery/umbrella/remote_runs/cleanup/`.

LiDA-1 NaCl V2 WHAM status: 22 refined windows have complete `umbrella.tpr`, `pullx`, and `pullf` inputs. `pmf_wham_v2_20260628_230007` completed with GROMACS `gmx wham` and wrote `profile_v2.xvg`, `histo_v2.xvg`, and `wham_v2_qc_summary.tsv`. The QC summary has `200/200` finite profile points, `0` nonfinite points, PMF span `9.19057 kJ/mol`, and `3` warning-keyword hits from poor sampling in far-tail bins 197-199. No final Delta G is promoted until tail materiality, repair need, bootstrap/error, and time-slice convergence are checked.

NaCl `LiDA-1` completed all 15 valid old-parameter windows and has a combined original-plus-repair GROMACS WHAM/bootstrap QC pass. The repair improved histogram coverage from `1` empty bin and `29/200` weak bins to `0` empty bins and `1/100` weak bin at the 100-bin combined setting. The result remains preliminary because the residual warning sits at the outer tail and the time-sliced plateau/minimum estimate shifts (`2.02-2.97 kJ/mol` across 100-bin slices). `LiDS-1` completed WHAM/QC for both old-parameter conditions: LiCl has `0` empty bins and `9/100` weak bins, while NaCl has `2` empty bins and `12/100` weak bins. These old-parameter PMFs remain QC-only; the paired v2 LiCl/NaCl reruns are now the route to publishable Delta G and Delta Delta G.

## Compute Fit

| Worker | Existing MD load | Umbrella load | Total |
|---|---:|---:|---:|
| Worker A | 4 production threads | 14 V2 windows | 18/18 real `mdrun` active now |
| Worker B | 0 production threads | 10 V2 windows/pulls + 2 V3 tail repairs | 12/12 real `mdrun` active now |

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

Current old/default complete windows are retained as diagnostics: `LiDA-1` NaCl `000-014`, `LiDA-1` NaCl repair extensions `000`, `001`, `002`, `013`, `014`, `LiDS-1` NaCl `000-016`, `LiDA-1` LiCl `000-013`, `LiDS-1` LiCl `000-020`, `LiD3-Core` LiCl `000-002`, `LiLC-1` LiCl `000-002`, `LiN3-Core` LiCl `000-002`, `LiA3-Ref` LiCl `000-001`, `LiLC-1` NaCl `000-003`, `LiA3-Ref` NaCl `000-003`, and `LiD3-Core` NaCl `000-003`. Old active windows were stopped on 2026-06-25 14:25 CST to prevent further compute burn on a workflow that is expected to fail final QC. Active umbrella compute is now v2-only: paired `LiDA-1` and `LiDS-1` LiCl/NaCl windows.

Preliminary PMF/QC output exists for NaCl `LiDA-1` under `pmf_wham_prelim_20260623_0905/`: GROMACS WHAM converged from 15 complete windows after a 100 ps burn-in. The original QC summary reports preliminary outer-minus-minimum PMF `3.70 kJ/mol`, with `1` empty histogram bin and `29/200` weak/single-window bins. The follow-up valid-15 diagnostic under `pmf_wham_diagnostic_valid15_20260624_095453/` produced `0` empty bins at 100, 75, and 50 bins, but retained `14`, `10`, and `6` weak/single-window bins, respectively. Five copied edge windows (`000`, `001`, `002`, `013`, `014`) completed `umbrella_ext` repair sampling under `pmf_wham_repair_edge_extend_20260624_101516/`. Combined original-plus-repair WHAM/bootstrap output under `pmf_wham_combined_repair_20260624_201216/` produced `0` empty bins and `1/100` weak bin at the 100-bin setting, but remains QC-only pending tail-materiality and time-slice convergence review.

`LiD3-Core`, `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` LiCl completed clustering with top cluster populations `12.69%`, `4.15%`, `4.65%`, and `5.05%`, respectively. `LiLC-1` NaCl also clustered with top cluster population `1.95%`. These low populations suggest broad peptide disorder, but representative structures were produced and their next umbrella gates can proceed.

`LiDS-1` NaCl completed production and clustering with top-cluster population `14.59%`. Its old-parameter umbrella run finished all `17/17` windows. Preliminary WHAM/QC is complete, but Delta G and Delta Delta G output are not final. Audited binding-site v2 NaCl `LiDS-1` was launched at 2026-06-25 13:24 CST on Worker B; the first attempt failed at `grompp` because the script selected the `run_min` topology copy, then the retry succeeded after preferring the production-root topology used by the earlier successful windows. `LiDA-1` NaCl v2 was launched at 2026-06-25 14:25 CST with a corrected `LISPER_JOBS=4` cap so paired `LiDS-1` plus `LiDA-1` NaCl v2 windows can run without exceeding Worker B's thread quota. Monitor active v2 pulls, then v2 window generation, WHAM/bootstrap, and time-slice convergence before promoting any Delta G value.

`LiA3-Ref` and `LiD3-Core` NaCl completed clustering this cycle with top-cluster populations `7.35%` and `10.34%`. Both were launched into umbrella pulls on Worker B. `LiD3-Core` initially failed at pull `grompp` because the umbrella script preferred a stale `topol_clean_attempt1.top`; the script now prefers the production-consistent `topol_clean_attempt2.top` before the `run_min` copy, and the repaired pull is running. The failed pulls are diagnostics only and are not scientific output.

## Implementation

Umbrella orchestration uses:

```text
01_computational_discovery/umbrella/remote_orchestration/scripts/run_lisper_umbrella_sampling.py
```

The driver extracts the full solvated representative frame from the completed production trajectory, selects the nearest Li+ or Na+ ion to the peptide center of mass, builds explicit `SOLU`, `SOLV`, `SYSTEM`, and `TARGET_ION` index groups, caps the initial pull below the GROMACS PBC half-box limit, then launches one-thread umbrella windows sequentially by default.
