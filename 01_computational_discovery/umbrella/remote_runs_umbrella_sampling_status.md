# Umbrella Sampling Status

Last updated: 2026-07-08 21:07 CST

## Launch Rule

Umbrella sampling is condition-specific. A candidate-condition can enter window design and umbrella sampling as soon as that condition has completed 20 ns production, structural clustering, and representative extraction. It does not need to wait for the matched LiCl/NaCl condition.

## Umbrella Window Meter

| Candidate | Condition | Worker | Complete / total | Active windows | Window meter |
|---|---|---|---:|---|---|
| `LiDA-1` | LiCl | GCP | V4 `27/27` | V4 WHAM/bootstrap complete; repair-focused QC review required | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟥` |
| `LiDS-1` | LiCl | GCP | V2 `27/27` | WHAM/bootstrap complete; QC review required | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟪` |
| `LiD3-Flex` | LiCl | GCP | V2 `17/27` | production windows `012-015` active | `🟩🟩🟩🟩🟩🟩🟦⬜⬜⬜` |
| `LiD3-Core` | LiCl | GCP | V2 `10/27` | production windows `010-011` active | `🟩🟩🟩🟩🟩🟩🟩🟦⬜⬜` |
| `LiLC-1` | LiCl | GCP | V2 `3/27` | equilibration window `003` active | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |
| `LiN3-Core` | LiCl | GCP | V2 `3/27` | equilibration window `003` active | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |
| `LiA3-Ref` | LiCl | GCP | V2 `2/27` | production window `002` active | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |
| `LiND-Hybrid` | LiCl | GCP | V2 `1/27` | production window `001` active | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |
| `LiDA-1` | NaCl | GCP | V4 `25/25` | WHAM/QC complete; manual region review required | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟨` |
| `LiDS-1` | NaCl | Worker B | V2 `27/27` | WHAM complete; QC review required | `🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩` |
| `LiD3-Flex` | NaCl | GCP | V2 `17/27` | production windows `017-021` active | `🟩🟩🟩🟩🟩🟩🟦⬜⬜⬜` |
| `LiLC-1` | NaCl | GCP | V2 `10/27` | production windows `010-011` active | `🟩🟩🟩🟩🟩🟩🟩🟦⬜⬜` |
| `LiA3-Ref` | NaCl | GCP | V2 `10/27` | production windows `010-011` active | `🟩🟩🟩🟩🟩🟩🟩🟦⬜⬜` |
| `LiD3-Core` | NaCl | GCP | V2 `10/27` | production windows `010-011` active | `🟩🟩🟩🟩🟩🟩🟩🟦⬜⬜` |
| `LiN3-Core` | NaCl | GCP | V2 `8/27` | production windows `008-009` active | `🟩🟩🟩🟩🟩🟩🟦⬜⬜⬜` |
| `LiND-Hybrid` | NaCl | GCP | V2 `2/27` | production windows `002-003` active | `🟩🟩🟩🟦⬜⬜⬜⬜⬜⬜` |

Current umbrella progress: active compute is on the 32-core GCP runner. Paired refined windows are active without duplicate candidate-condition-stage jobs. Complete-window counters here are audited from real completed `umbrella.gro`/done outputs, while active windows are listed separately. LiCl `LiDA-1` completed V4 window `026` repair and combined WHAM/bootstrap under `pmf_wham_v4_20260702_1855`; the V4 profile has `200/200` finite points but still has `12` poor-sampling warning lines at `z=2.24551-2.25665 nm` and a `2.73 kJ/mol` burn-in/time-slice span shift, so classification remains `REPAIR` pending materiality/next-repair review. `LiDS-1` has paired V2 `27/27` windows complete; LiCl WHAM/bootstrap completed under `pmf_wham_v2_20260703_0655` with `200/200` finite points, `22` warning lines, and poor/empty far-tail bins near `z=2.48-2.53 nm`, so classification is QC review and no Delta G is promoted. This heartbeat advanced `LiLC-1` LiCl and `LiN3-Core` LiCl to V2 `3/27`, with window `003` in equilibration. Old windows and repair outputs are retained only as diagnostics/preliminary QC evidence.

Capacity/progress check, 2026-07-08 21:07 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `79%` used. No extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-08 17:04 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `77%` used. No extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-08 13:02 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `76%` used. No extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-08 07:35 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `75%` used. No extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-08 02:11 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `73%` used. No extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-07 22:07 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `72%` used. No extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-07 18:04 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `71%` used. `LiN3-Core` NaCl advanced to V2 `8/27`, with windows `008-009` in equilibration; no extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-07 13:40 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `70%` used. `LiA3-Ref` LiCl advanced to V2 `2/27`; no extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-07 09:34 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `69%` used. `LiD3-Flex` LiCl/NaCl advanced to V2 `17/27`; `LiLC-1` and `LiN3-Core` LiCl advanced to V2 `2/27`. No extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-07 01:06 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `66%` used. No extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-06 21:01 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `65%` used. No extra job was submitted because active drivers are already occupying ready work.

Capacity/progress check, 2026-07-06 16:56 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `64%` used. `LiD3-Core` LiCl/NaCl and `LiLC-1` NaCl advanced to V2 `8/27`; no additional job was submitted because active drivers are occupying ready work.

Capacity/progress check, 2026-07-06 12:47 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `63%` used. NaCl `LiA3-Ref` advanced from active production windows `006-007` to active equilibration windows `008-009`; no additional job was submitted because active drivers are occupying ready work.

Capacity/progress check, 2026-07-06 08:43 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `61%` used. `LiLC-1`, `LiA3-Ref`, and `LiND-Hybrid` LiCl plus `LiND-Hybrid` NaCl advanced windows; no additional job was submitted because active drivers are occupying ready work.

Capacity/progress check, 2026-07-06 04:41 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `60%` used. `LiN3-Core` LiCl advanced to V2 `2/27`; no additional job was submitted because active drivers are already occupying the ready work.

Capacity/progress check, 2026-07-06 00:37 CST: GCP is healthy at `25` real workflow `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `59%` used. `LiND-Hybrid` LiCl moved from pull into first-window equilibration. No additional job was submitted because no non-active ready window was found outside active drivers.

Capacity/progress check, 2026-07-05 20:27 CST: GCP is healthy at `25` real `mdrun` jobs using `25` OpenMP threads, load near `25`, and data disk at `58%` used. No additional one-off job was submitted because active drivers are already advancing the ready tracks without duplicate candidate-condition-stage-window work.

Capacity/progress check, 2026-07-05 06:51 CST: GCP is at `24` real `mdrun` jobs using `24` OpenMP threads with data disk at `54%` used. `LiD3-Core` advanced to LiCl/NaCl V2 `6/27`, and `LiLC-1` NaCl advanced to V2 `6/27`; `LiND-Hybrid` LiCl/NaCl pulls remain active. A finished-marker/active-CWD audit found no non-active queued window with ready `umbrella.tpr`, so no one-off launch was submitted.

Capacity/progress check, 2026-07-05 02:50 CST: GCP is at `24` real `mdrun` jobs using `24` OpenMP threads with data disk at `53%` used. `LiD3-Flex` advanced to LiCl V2 `13/27` and NaCl V2 `12/27`; `LiND-Hybrid` LiCl/NaCl pulls remain active. A queued-window scan found no non-active queued window with ready `umbrella.tpr`, so no one-off launch was submitted.

Capacity launch, 2026-07-03 15:10 CST: GCP was at `26` real OpenMP threads before scheduling. After duplicate-driver/CWD checks, single-slot LiCl V2 drivers were launched for `LiLC-1`, `LiN3-Core`, and `LiA3-Ref`; verification showed `28` real `mdrun` processes using `29` OpenMP threads, with the three new LiCl tracks in pull `mdrun`. `LiND-Hybrid` LiCl was checked but not launched because the verified/projected load would exceed the `30`-thread cap once all single-slot drivers were active.

Capacity check, 2026-07-04 14:50 CST: GCP remains healthy at `28` real `mdrun` jobs using `29` OpenMP threads, load near `29`, and data disk at `50%` used. No additional umbrella job was launched because the next one-core job would reach the `30`-thread scheduling cap while active drivers and WHAM/filesystem work still need headroom.

Capacity/progress check, 2026-07-04 18:50 CST: GCP remains at `28` real `mdrun` jobs using `29` OpenMP threads with data disk at `51%` used. `LiND-Hybrid` NaCl production is still active at approximately `19.84/20 ns`. `LiN3-Core` NaCl V2 advanced to `4/27`; windows `004-005` are now active. No additional job was launched because the worker remains at the scheduling cap.

Launch/progress check, 2026-07-04 22:50 CST: `LiND-Hybrid` NaCl production reached `20.00/20 ns`, wrote final coordinates, and clustering produced `cluster_20ns/representative_top_cluster.pdb`. A guarded duplicate check confirmed no active or existing `LiND-Hybrid` NaCl V2 umbrella windows, then the NaCl V2 umbrella driver was launched with `LISPER_JOBS=2`. Verification showed the new pull `mdrun` active and total GCP load at `28` real `mdrun` jobs using `28` OpenMP threads. `LiA3-Ref` NaCl advanced to V2 `6/27`, with windows `006-007` active.

LiND-Hybrid LiCl launch, 2026-07-04 23:39 CST: GCP was at `28` real `mdrun` jobs using `28` OpenMP threads before launch. A guarded duplicate check confirmed no active or existing `LiND-Hybrid` LiCl V2 umbrella windows; the LiCl V2 umbrella driver was launched with `LISPER_JOBS=1` to preserve headroom under the `30`-thread scheduling cap. Verification showed the new LiCl pull `mdrun` active alongside the NaCl pull, with total GCP load at `29` real `mdrun` jobs using `29` OpenMP threads.

LiDA-1 LiCl V4 status, 2026-07-03 02:55 CST: V4 window `026` finished from the V3 checkpoint and wrote final coordinates plus pull traces. `pmf_wham_v4_20260702_1855` completed from `27` combined LiCl windows with `200/200` finite profile points and `0` nonfinite points, but retained `12` poor-sampling warning lines at the outer tail (`z=2.24551-2.25665 nm`) and `2.73 kJ/mol` burn-in/time-slice span shift. Classification remains `REPAIR`; no Delta G is promoted until the outer-tail materiality and any next minimal repair are decided.

Scheduling note, 2026-06-29 19:15 CST: Worker A is at `18/18` real `mdrun` threads and Worker B is at `12/12` real `mdrun` threads. The last two Worker B cores were assigned to LiDA-1 NaCl V3 tail repair extensions for windows `020-021`, targeting poor-sampling bins near the outer reference tail. No candidate-condition-stage-window is duplicated.

Scheduling correction, 2026-06-30 02:59 CST: Worker B briefly expanded to `14/12` real `mdrun` threads when the `LiA3-Ref` NaCl driver opened three window-equilibration jobs while LiDA-1 V3 repair was still active. The LiA3-Ref driver and windows `001-002` were stopped, leaving window `000` active and returning Worker B to `12/12` threads. LiDA-1 V3 repair windows `020-021` were protected.

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
| Worker B | 0 production threads | 10 V2 windows + 2 V3 tail repairs | 12/12 real `mdrun` active now |

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

Current old/default complete windows are retained as diagnostics: `LiDA-1` NaCl `000-014`, `LiDA-1` NaCl repair extensions `000`, `001`, `002`, `013`, `014`, `LiDS-1` NaCl `000-016`, `LiDA-1` LiCl `000-013`, `LiDS-1` LiCl `000-020`, `LiD3-Core` LiCl `000-002`, `LiLC-1` LiCl `000-002`, `LiN3-Core` LiCl `000-002`, `LiA3-Ref` LiCl `000-001`, `LiLC-1` NaCl `000-003`, `LiA3-Ref` NaCl `000-003`, and `LiD3-Core` NaCl `000-003`. Old active windows were stopped on 2026-06-25 14:25 CST to prevent further compute burn on a workflow that is expected to fail final QC. Active umbrella compute is now V2-only for refined candidate-condition tracks, including the newly launched `LiLC-1`, `LiN3-Core`, and `LiA3-Ref` LiCl pulls.

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
