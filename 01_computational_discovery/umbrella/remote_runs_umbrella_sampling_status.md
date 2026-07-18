# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-19 07:00 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 221 equilibrations complete, 97 active; 14 production complete, 29 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 97 EQ windows + 29 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 2/2 threads used transiently for the off-host sync and live verification; both return after those checks |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 47.81M atom·ns. The latest one-hour same-host/protocol progress basis is ≈71,415 atom·ns/day/job (≈9.00M/day at 126 jobs), giving median table ETA 2026-07-24 14:31 CST; ±20% throughput sensitivity gives 2026-07-23 17:16 to 2026-07-25 22:24 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to the four highest remaining atom-weighted campaigns, the paired LiD3-Flex and LiND-Hybrid runs, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Two hundred twenty-one EQ windows and fourteen production windows verified their configured final step plus `Finished mdrun`; 29 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 7/30 | 23 | 4 | 0/30 | 30 | 0 |
| LiA3-Ref | NaCl | 9/30 | 21 | 2 | 0/30 | 30 | 1 |
| LiD3-Core | LiCl | 18/30 | 12 | 1 | 0/30 | 30 | 2 |
| LiD3-Core | NaCl | 16/30 | 14 | 3 | 0/30 | 30 | 2 |
| LiD3-Flex | LiCl | 1/30 | 29 | 19 | 0/30 | 30 | 1 |
| LiD3-Flex | NaCl | 0/30 | 30 | 22 | 0/30 | 30 | 0 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 9/30 | 21 | 4 |
| LiDA-1 | NaCl | 27/30 | 3 | 0 | 5/30 | 25 | 6 |
| LiDS-1 | LiCl | 25/30 | 5 | 0 | 0/30 | 30 | 1 |
| LiDS-1 | NaCl | 21/30 | 9 | 0 | 0/30 | 30 | 1 |
| LiLC-1 | LiCl | 16/30 | 14 | 1 | 0/30 | 30 | 2 |
| LiLC-1 | NaCl | 12/30 | 18 | 5 | 0/30 | 30 | 3 |
| LiN3-Core | LiCl | 10/30 | 20 | 7 | 0/30 | 30 | 1 |
| LiN3-Core | NaCl | 11/30 | 19 | 4 | 0/30 | 30 | 3 |
| LiND-Hybrid | LiCl | 7/30 | 23 | 13 | 0/30 | 30 | 1 |
| LiND-Hybrid | NaCl | 11/30 | 19 | 16 | 0/30 | 30 | 1 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
