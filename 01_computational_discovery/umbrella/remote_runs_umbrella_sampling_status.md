# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-23 18:57 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 460 equilibrations complete, 12 active; 323 production complete, 114 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 12 EQ windows + 114 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 2/2 threads used by the work-conserving admission guard and active off-host restart sync |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 8.53M atom·ns. The latest 176-minute same-host/protocol progress basis is ≈71,375 atom·ns/day/job (≈8.99M/day at 126 jobs), giving median table ETA 2026-07-24 17:43 CST; ±20% throughput sensitivity gives 2026-07-24 13:55 to 2026-07-24 23:25 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to LiA3-Ref/NaCl, LiLC-1/LiCl, LiD3-Core/NaCl, and LiA3-Ref/LiCl, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Four hundred sixty EQ windows and three hundred twenty-three production windows verified their configured final step plus `Finished mdrun`; 114 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. LiDA-1/NaCl remains at 30/30 production, but paired WHAM remains gated on LiDA-1/LiCl at 27/30; three windows are advancing. The off-host restart sync is active on its reserved thread; simulation MD is unaffected. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 28/30 | 2 | 1 | 17/30 | 13 | 7 |
| LiA3-Ref | NaCl | 23/30 | 7 | 6 | 9/30 | 21 | 11 |
| LiD3-Core | LiCl | 30/30 | 0 | 0 | 25/30 | 5 | 3 |
| LiD3-Core | NaCl | 27/30 | 3 | 3 | 13/30 | 17 | 12 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 26/30 | 4 | 4 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 25/30 | 5 | 5 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 27/30 | 3 | 3 |
| LiDA-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDS-1 | LiCl | 29/30 | 1 | 0 | 22/30 | 8 | 7 |
| LiDS-1 | NaCl | 28/30 | 2 | 0 | 24/30 | 6 | 2 |
| LiLC-1 | LiCl | 27/30 | 3 | 1 | 12/30 | 18 | 10 |
| LiLC-1 | NaCl | 30/30 | 0 | 0 | 12/30 | 18 | 15 |
| LiN3-Core | LiCl | 28/30 | 2 | 1 | 18/30 | 12 | 8 |
| LiN3-Core | NaCl | 30/30 | 0 | 0 | 22/30 | 8 | 8 |
| LiND-Hybrid | LiCl | 30/30 | 0 | 0 | 15/30 | 15 | 15 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 26/30 | 4 | 4 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
