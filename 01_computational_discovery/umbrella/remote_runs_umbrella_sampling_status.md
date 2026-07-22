# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-23 06:57 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 452 equilibrations complete, 6 active; 282 production complete, 120 active |
| Real GROMACS work | 126 unique one-thread `mdrun`: 6 EQ windows + 120 production windows; 126/126 umbrella-MD threads in 126 distinct directories |
| Reserved support | 2/2 threads used by the work-conserving admission guard and active off-host restart sync |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 13.03M atom·ns. The latest 177-minute same-host/protocol progress basis is ≈70,821 atom·ns/day/job (≈8.92M/day at 126 jobs), giving median table ETA 2026-07-24 17:59 CST; ±20% throughput sensitivity gives 2026-07-24 12:09 to 2026-07-25 02:45 CST |
| Next | Preserve the healthy 126/126 pool; give newly free slots to LiA3-Ref/NaCl, LiLC-1/LiCl, LiD3-Core/NaCl, and LiLC-1/NaCl, then recalculate |

A five-second `/proc` sample found all 126 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. Four hundred fifty-two EQ windows and two hundred eighty-two production windows verified their configured final step plus `Finished mdrun`; 120 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. LiDA-1/NaCl remains at 30/30 production, but paired WHAM remains gated on LiDA-1/LiCl at 26/30. The off-host restart sync is active; simulation MD is unaffected. Production throughput will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 26/30 | 4 | 2 | 15/30 | 15 | 8 |
| LiA3-Ref | NaCl | 22/30 | 8 | 0 | 8/30 | 22 | 5 |
| LiD3-Core | LiCl | 30/30 | 0 | 0 | 22/30 | 8 | 4 |
| LiD3-Core | NaCl | 27/30 | 3 | 0 | 12/30 | 18 | 9 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 26/30 | 4 | 3 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 19/30 | 11 | 11 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 26/30 | 4 | 1 |
| LiDA-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDS-1 | LiCl | 29/30 | 1 | 0 | 21/30 | 9 | 2 |
| LiDS-1 | NaCl | 28/30 | 2 | 0 | 20/30 | 10 | 5 |
| LiLC-1 | LiCl | 26/30 | 4 | 1 | 10/30 | 20 | 9 |
| LiLC-1 | NaCl | 27/30 | 3 | 2 | 8/30 | 22 | 16 |
| LiN3-Core | LiCl | 27/30 | 3 | 1 | 13/30 | 17 | 11 |
| LiN3-Core | NaCl | 30/30 | 0 | 0 | 18/30 | 12 | 11 |
| LiND-Hybrid | LiCl | 30/30 | 0 | 0 | 12/30 | 18 | 17 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 22/30 | 8 | 8 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
