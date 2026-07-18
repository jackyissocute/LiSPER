# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-18 13:58 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 14/16 pulls complete, 2 active; 420/480 windows generated; 28 equilibrations complete, 111 active; 0 production complete, 1 active |
| Real GROMACS work | 114 unique `mdrun`: 2 seven-thread pulls + 111 one-thread EQ windows + 1 one-thread production window; 126/126 umbrella-MD threads in 114 distinct directories |
| Reserved support | 2/2 threads used transiently for the off-host sync and live verification; both return after those checks |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 53.99M atom·ns. The last verified same-host/protocol rate basis is ≈72,934 atom·ns/day/job (≈9.19M/day at 126 jobs), giving median table ETA 2026-07-24 15:00 CST; ±20% throughput sensitivity gives 2026-07-23 15:30 to 2026-07-26 02:15 CST |
| Next | Preserve the healthy 126/126 pool; as pulls finish, give newly free slots to ready windows with the greatest remaining atom-weighted campaign work |

A five-second `/proc` sample found all 114 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. Fourteen pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Twenty-eight LiDA-1/LiCl EQ windows verified their configured final step plus `Finished mdrun`, and the first production window is active. No active log contains a fatal, water-SETTLE, or LINCS warning. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 0/30 | 30 | 3 | 0/30 | 30 | 0 |
| LiA3-Ref | NaCl | 0/30 | 30 | 3 | 0/30 | 30 | 0 |
| LiD3-Core | LiCl | 0/30 | 30 | 5 | 0/30 | 30 | 0 |
| LiD3-Core | NaCl | 0/30 | 30 | 6 | 0/30 | 30 | 0 |
| LiD3-Flex | LiCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiD3-Flex | NaCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiDA-1 | LiCl | 28/30 | 2 | 2 | 0/30 | 30 | 1 |
| LiDA-1 | NaCl | 0/30 | 30 | 22 | 0/30 | 30 | 0 |
| LiDS-1 | LiCl | 0/30 | 30 | 23 | 0/30 | 30 | 0 |
| LiDS-1 | NaCl | 0/30 | 30 | 19 | 0/30 | 30 | 0 |
| LiLC-1 | LiCl | 0/30 | 30 | 13 | 0/30 | 30 | 0 |
| LiLC-1 | NaCl | 0/30 | 30 | 3 | 0/30 | 30 | 0 |
| LiN3-Core | LiCl | 0/30 | 30 | 2 | 0/30 | 30 | 0 |
| LiN3-Core | NaCl | 0/30 | 30 | 4 | 0/30 | 30 | 0 |
| LiND-Hybrid | LiCl | 0/30 | 30 | 2 | 0/30 | 30 | 0 |
| LiND-Hybrid | NaCl | 0/30 | 30 | 4 | 0/30 | 30 | 0 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
