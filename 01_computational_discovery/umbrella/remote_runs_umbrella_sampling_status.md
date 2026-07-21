# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-21 21:41 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 418 equilibrations complete, 10 active; 170 production complete, 116 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 10 EQ windows + 116 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 1/2 threads used by the active off-host restart sync; the second support thread was used transiently for live verification and is now free |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 25.28M atom·ns. The latest 180-minute same-host/protocol progress basis is ≈69,548 atom·ns/day/job (≈8.76M/day at 126 jobs), giving median table ETA 2026-07-24 18:56 CST; ±20% throughput sensitivity gives 2026-07-24 07:24 to 2026-07-25 12:14 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to LiND-Hybrid/LiCl, LiA3-Ref/NaCl, LiD3-Flex/NaCl, and LiLC-1/NaCl, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Four hundred eighteen EQ windows and one hundred seventy production windows verified their configured final step plus `Finished mdrun`; 116 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. The off-host restart sync is retrying after one SSH timeout; the timeout did not affect simulation MD. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 23/30 | 7 | 1 | 4/30 | 26 | 11 |
| LiA3-Ref | NaCl | 19/30 | 11 | 0 | 7/30 | 23 | 1 |
| LiD3-Core | LiCl | 27/30 | 3 | 1 | 16/30 | 14 | 6 |
| LiD3-Core | NaCl | 26/30 | 4 | 1 | 6/30 | 24 | 6 |
| LiD3-Flex | LiCl | 29/30 | 1 | 1 | 9/30 | 21 | 18 |
| LiD3-Flex | NaCl | 28/30 | 2 | 1 | 7/30 | 23 | 18 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 20/30 | 10 | 3 |
| LiDA-1 | NaCl | 29/30 | 1 | 1 | 23/30 | 7 | 5 |
| LiDS-1 | LiCl | 28/30 | 2 | 0 | 14/30 | 16 | 7 |
| LiDS-1 | NaCl | 25/30 | 5 | 1 | 12/30 | 18 | 8 |
| LiLC-1 | LiCl | 23/30 | 7 | 0 | 8/30 | 22 | 2 |
| LiLC-1 | NaCl | 22/30 | 8 | 1 | 5/30 | 25 | 3 |
| LiN3-Core | LiCl | 26/30 | 4 | 0 | 5/30 | 25 | 5 |
| LiN3-Core | NaCl | 27/30 | 3 | 1 | 11/30 | 19 | 5 |
| LiND-Hybrid | LiCl | 26/30 | 4 | 1 | 9/30 | 21 | 6 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 14/30 | 16 | 12 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
