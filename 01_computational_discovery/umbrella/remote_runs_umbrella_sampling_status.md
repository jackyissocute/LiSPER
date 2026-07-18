# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-19 01:00 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 181 equilibrations complete, 99 active; 0 production complete, 27 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 99 EQ windows + 27 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 2/2 threads used transiently for the off-host sync and live verification; both return after those checks |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 50.00M atom·ns. The latest two-hour same-host/protocol progress basis is ≈72,163 atom·ns/day/job (≈9.09M/day at 126 jobs), giving median table ETA 2026-07-24 12:58 CST; ±20% throughput sensitivity gives 2026-07-23 14:59 to 2026-07-25 21:58 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to the four highest remaining atom-weighted campaigns, the paired LiD3-Flex and LiND-Hybrid runs, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. One hundred eighty-one EQ windows verified their configured final step plus `Finished mdrun`, and 27 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 5/30 | 25 | 4 | 0/30 | 30 | 0 |
| LiA3-Ref | NaCl | 6/30 | 24 | 3 | 0/30 | 30 | 0 |
| LiD3-Core | LiCl | 10/30 | 20 | 8 | 0/30 | 30 | 1 |
| LiD3-Core | NaCl | 13/30 | 17 | 4 | 0/30 | 30 | 0 |
| LiD3-Flex | LiCl | 0/30 | 30 | 14 | 0/30 | 30 | 0 |
| LiD3-Flex | NaCl | 0/30 | 30 | 14 | 0/30 | 30 | 0 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 0/30 | 30 | 12 |
| LiDA-1 | NaCl | 27/30 | 3 | 0 | 0/30 | 30 | 9 |
| LiDS-1 | LiCl | 25/30 | 5 | 0 | 0/30 | 30 | 1 |
| LiDS-1 | NaCl | 19/30 | 11 | 2 | 0/30 | 30 | 1 |
| LiLC-1 | LiCl | 15/30 | 15 | 1 | 0/30 | 30 | 0 |
| LiLC-1 | NaCl | 10/30 | 20 | 2 | 0/30 | 30 | 1 |
| LiN3-Core | LiCl | 8/30 | 22 | 8 | 0/30 | 30 | 1 |
| LiN3-Core | NaCl | 8/30 | 22 | 4 | 0/30 | 30 | 1 |
| LiND-Hybrid | LiCl | 2/30 | 28 | 15 | 0/30 | 30 | 0 |
| LiND-Hybrid | NaCl | 3/30 | 27 | 20 | 0/30 | 30 | 0 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
