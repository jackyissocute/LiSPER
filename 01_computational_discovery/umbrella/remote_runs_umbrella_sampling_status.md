# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-22 12:57 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 435 equilibrations complete, 5 active; 220 production complete, 121 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 5 EQ windows + 121 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 1/2 threads used by the active off-host restart sync; the second support thread was used transiently for live verification and is now free |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 19.69M atom·ns. The latest 180-minute same-host/protocol progress basis is ≈70,076 atom·ns/day/job (≈8.83M/day at 126 jobs), giving median table ETA 2026-07-24 18:29 CST; ±20% throughput sensitivity gives 2026-07-24 09:33 to 2026-07-25 07:51 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to LiA3-Ref/NaCl, LiND-Hybrid/LiCl, LiLC-1/NaCl, and LiLC-1/LiCl, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Four hundred thirty-five EQ windows and two hundred twenty production windows verified their configured final step plus `Finished mdrun`; 121 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. LiDA-1/NaCl reached 30/30 production, but paired WHAM remains gated on LiDA-1/LiCl. The off-host restart sync is actively transferring fresh restart data; simulation MD is unaffected. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 25/30 | 5 | 0 | 8/30 | 22 | 10 |
| LiA3-Ref | NaCl | 19/30 | 11 | 1 | 7/30 | 23 | 2 |
| LiD3-Core | LiCl | 29/30 | 1 | 0 | 18/30 | 12 | 7 |
| LiD3-Core | NaCl | 27/30 | 3 | 0 | 8/30 | 22 | 6 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 14/30 | 16 | 14 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 11/30 | 19 | 18 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 23/30 | 7 | 1 |
| LiDA-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDS-1 | LiCl | 28/30 | 2 | 0 | 20/30 | 10 | 1 |
| LiDS-1 | NaCl | 27/30 | 3 | 0 | 17/30 | 13 | 4 |
| LiLC-1 | LiCl | 24/30 | 6 | 1 | 8/30 | 22 | 4 |
| LiLC-1 | NaCl | 24/30 | 6 | 1 | 8/30 | 22 | 4 |
| LiN3-Core | LiCl | 26/30 | 4 | 0 | 9/30 | 21 | 10 |
| LiN3-Core | NaCl | 29/30 | 1 | 0 | 12/30 | 18 | 11 |
| LiND-Hybrid | LiCl | 27/30 | 3 | 2 | 10/30 | 20 | 16 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 17/30 | 13 | 13 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
