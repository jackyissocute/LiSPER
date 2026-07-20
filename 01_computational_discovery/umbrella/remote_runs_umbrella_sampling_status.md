# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-21 03:40 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 393 equilibrations complete, 9 active; 98 production complete, 117 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 9 EQ windows + 117 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 1/2 threads used by the off-host restart sync; the second support thread was used transiently for live verification and is now free |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 31.82M atom·ns. The latest 180-minute same-host/protocol progress basis is ≈68,561 atom·ns/day/job (≈8.64M/day at 126 jobs), giving median table ETA 2026-07-24 20:05 CST; ±20% throughput sensitivity gives 2026-07-24 05:21 to 2026-07-25 18:11 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to LiD3-Flex/NaCl, LiND-Hybrid/LiCl, LiD3-Flex/LiCl, and LiA3-Ref/LiCl, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Three hundred ninety-three EQ windows and ninety-eight production windows verified their configured final step plus `Finished mdrun`; 117 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. A backup-only SSH timeout automatically retried and completed at 03:22 CST without affecting MD. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 19/30 | 11 | 2 | 3/30 | 27 | 5 |
| LiA3-Ref | NaCl | 17/30 | 13 | 1 | 3/30 | 27 | 4 |
| LiD3-Core | LiCl | 24/30 | 6 | 1 | 10/30 | 20 | 8 |
| LiD3-Core | NaCl | 24/30 | 6 | 1 | 5/30 | 25 | 3 |
| LiD3-Flex | LiCl | 28/30 | 2 | 0 | 0/30 | 30 | 22 |
| LiD3-Flex | NaCl | 28/30 | 2 | 0 | 0/30 | 30 | 14 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 18/30 | 12 | 2 |
| LiDA-1 | NaCl | 28/30 | 2 | 0 | 20/30 | 10 | 2 |
| LiDS-1 | LiCl | 27/30 | 3 | 0 | 9/30 | 21 | 6 |
| LiDS-1 | NaCl | 25/30 | 5 | 0 | 9/30 | 21 | 4 |
| LiLC-1 | LiCl | 20/30 | 10 | 0 | 5/30 | 25 | 3 |
| LiLC-1 | NaCl | 21/30 | 9 | 1 | 5/30 | 25 | 3 |
| LiN3-Core | LiCl | 24/30 | 6 | 1 | 3/30 | 27 | 6 |
| LiN3-Core | NaCl | 25/30 | 5 | 1 | 6/30 | 24 | 6 |
| LiND-Hybrid | LiCl | 25/30 | 5 | 0 | 1/30 | 29 | 11 |
| LiND-Hybrid | NaCl | 28/30 | 2 | 1 | 1/30 | 29 | 18 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
