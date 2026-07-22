# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-22 09:57 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 432 equilibrations complete, 7 active; 212 production complete, 119 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 7 EQ windows + 119 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 1/2 threads used by the active off-host restart sync; the second support thread was used transiently for live verification and is now free |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 20.79M atom·ns. The latest 159-minute same-host/protocol progress basis is ≈70,573 atom·ns/day/job (≈8.89M/day at 126 jobs), giving median table ETA 2026-07-24 18:05 CST; ±20% throughput sensitivity gives 2026-07-24 08:44 to 2026-07-25 08:06 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to LiND-Hybrid/LiCl, LiA3-Ref/NaCl, LiLC-1/NaCl, and LiLC-1/LiCl, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Four hundred thirty-two EQ windows and two hundred twelve production windows verified their configured final step plus `Finished mdrun`; 119 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. The off-host restart sync is actively transferring fresh restart data; simulation MD is unaffected. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 24/30 | 6 | 1 | 8/30 | 22 | 9 |
| LiA3-Ref | NaCl | 19/30 | 11 | 1 | 7/30 | 23 | 2 |
| LiD3-Core | LiCl | 28/30 | 2 | 1 | 18/30 | 12 | 6 |
| LiD3-Core | NaCl | 27/30 | 3 | 0 | 8/30 | 22 | 5 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 13/30 | 17 | 15 |
| LiD3-Flex | NaCl | 29/30 | 1 | 1 | 9/30 | 21 | 20 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 22/30 | 8 | 2 |
| LiDA-1 | NaCl | 30/30 | 0 | 0 | 28/30 | 2 | 2 |
| LiDS-1 | LiCl | 28/30 | 2 | 0 | 19/30 | 11 | 2 |
| LiDS-1 | NaCl | 27/30 | 3 | 0 | 17/30 | 13 | 3 |
| LiLC-1 | LiCl | 24/30 | 6 | 1 | 8/30 | 22 | 4 |
| LiLC-1 | NaCl | 24/30 | 6 | 0 | 8/30 | 22 | 3 |
| LiN3-Core | LiCl | 26/30 | 4 | 0 | 9/30 | 21 | 7 |
| LiN3-Core | NaCl | 29/30 | 1 | 0 | 12/30 | 18 | 9 |
| LiND-Hybrid | LiCl | 27/30 | 3 | 2 | 10/30 | 20 | 16 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 16/30 | 14 | 14 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
