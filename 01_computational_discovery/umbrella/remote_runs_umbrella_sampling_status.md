# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-21 18:41 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 412 equilibrations complete, 12 active; 161 production complete, 114 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 12 EQ windows + 114 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 1/2 threads used by the active off-host restart sync; the second support thread was used transiently for live verification and is now free |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 26.38M atom·ns. The latest 180-minute same-host/protocol progress basis is ≈68,846 atom·ns/day/job (≈8.67M/day at 126 jobs), giving median table ETA 2026-07-24 19:40 CST; ±20% throughput sensitivity gives 2026-07-24 07:30 to 2026-07-25 13:55 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to LiND-Hybrid/LiCl, LiD3-Flex/NaCl, LiA3-Ref/NaCl, and LiLC-1/NaCl, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Four hundred twelve EQ windows and one hundred sixty-one production windows verified their configured final step plus `Finished mdrun`; 114 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. The off-host restart sync is active after multiple verified completions. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 22/30 | 8 | 2 | 4/30 | 26 | 10 |
| LiA3-Ref | NaCl | 19/30 | 11 | 0 | 6/30 | 24 | 2 |
| LiD3-Core | LiCl | 27/30 | 3 | 1 | 16/30 | 14 | 6 |
| LiD3-Core | NaCl | 25/30 | 5 | 1 | 6/30 | 24 | 5 |
| LiD3-Flex | LiCl | 29/30 | 1 | 1 | 8/30 | 22 | 18 |
| LiD3-Flex | NaCl | 28/30 | 2 | 1 | 4/30 | 26 | 17 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 20/30 | 10 | 2 |
| LiDA-1 | NaCl | 29/30 | 1 | 0 | 22/30 | 8 | 6 |
| LiDS-1 | LiCl | 27/30 | 3 | 1 | 13/30 | 17 | 8 |
| LiDS-1 | NaCl | 25/30 | 5 | 1 | 12/30 | 18 | 7 |
| LiLC-1 | LiCl | 22/30 | 8 | 1 | 7/30 | 23 | 3 |
| LiLC-1 | NaCl | 22/30 | 8 | 0 | 5/30 | 25 | 3 |
| LiN3-Core | LiCl | 26/30 | 4 | 0 | 5/30 | 25 | 5 |
| LiN3-Core | NaCl | 26/30 | 4 | 2 | 10/30 | 20 | 6 |
| LiND-Hybrid | LiCl | 25/30 | 5 | 1 | 9/30 | 21 | 5 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 14/30 | 16 | 11 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
