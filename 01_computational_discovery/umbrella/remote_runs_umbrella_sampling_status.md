# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-19 17:39 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 321 equilibrations complete, 37 active; 23 production complete, 89 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 37 EQ windows + 89 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 2/2 threads used transiently for the off-host sync and live verification; both return after those checks |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 43.97M atom·ns. The latest 180-minute same-host/protocol progress basis is ≈67,624 atom·ns/day/job (≈8.52M/day at 126 jobs), giving median table ETA 2026-07-24 21:30 CST; ±20% throughput sensitivity gives 2026-07-24 00:51 to 2026-07-26 04:28 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to the four highest remaining atom-weighted campaigns, the paired LiD3-Flex and LiND-Hybrid runs, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Three hundred twenty-one EQ windows and twenty-three production windows verified their configured final step plus `Finished mdrun`; 89 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 11/30 | 19 | 1 | 0/30 | 30 | 3 |
| LiA3-Ref | NaCl | 13/30 | 17 | 2 | 0/30 | 30 | 3 |
| LiD3-Core | LiCl | 21/30 | 9 | 3 | 0/30 | 30 | 9 |
| LiD3-Core | NaCl | 20/30 | 10 | 1 | 0/30 | 30 | 5 |
| LiD3-Flex | LiCl | 18/30 | 12 | 8 | 0/30 | 30 | 8 |
| LiD3-Flex | NaCl | 20/30 | 10 | 7 | 0/30 | 30 | 4 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 12/30 | 18 | 2 |
| LiDA-1 | NaCl | 27/30 | 3 | 0 | 10/30 | 20 | 8 |
| LiDS-1 | LiCl | 25/30 | 5 | 1 | 0/30 | 30 | 4 |
| LiDS-1 | NaCl | 24/30 | 6 | 1 | 1/30 | 29 | 6 |
| LiLC-1 | LiCl | 17/30 | 13 | 1 | 0/30 | 30 | 5 |
| LiLC-1 | NaCl | 17/30 | 13 | 2 | 0/30 | 30 | 5 |
| LiN3-Core | LiCl | 17/30 | 13 | 1 | 0/30 | 30 | 3 |
| LiN3-Core | NaCl | 15/30 | 15 | 3 | 0/30 | 30 | 5 |
| LiND-Hybrid | LiCl | 20/30 | 10 | 4 | 0/30 | 30 | 8 |
| LiND-Hybrid | NaCl | 26/30 | 4 | 2 | 0/30 | 30 | 11 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
