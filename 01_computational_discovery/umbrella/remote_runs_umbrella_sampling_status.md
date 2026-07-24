# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-24 21:35 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 480 equilibrations complete; 476 production complete, 4 active |
| Real GROMACS work | 5 unique one-thread production `mdrun`; 5/126 umbrella-MD threads in 5 distinct directories, with all currently ready windows active |
| Reserved support | 1/2 threads active for the off-host restart sync; all campaign drivers are resumed |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 0.038M atom·ns. The latest 515-minute tail progress basis is ≈4.84M atom·ns/day aggregate, giving median eight-row table ETA 2026-07-24 21:47 CST; ±20% throughput sensitivity gives 2026-07-24 21:45 to 2026-07-24 21:50 CST |
| Next | Keep all 5 tail windows running; launch paired WHAM immediately as each remaining candidate pair completes |

A five-second `/proc` sample found all 4 real GROMACS executables advancing, with 4 actual MD threads and no duplicate working directory. All currently ready windows are active. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. All 480 EQ windows and 476 production windows verified their configured final step plus `Finished mdrun`; 4 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. Five paired rows are protocol-validated: LiDA-1 -19.340 ± 3.642, LiDS-1 -7.615 ± 7.286, LiD3-Core -3.630 ± 6.337, LiD3-Flex -1.360 ± 10.003, and LiND-Hybrid -8.975 ± 9.825 kJ/mol. The uncertainty is retained explicitly and does not imply sign confidence when it spans zero. The patched off-host restart sync is advancing through restart checkpoints. No simulation repair is active. Tail throughput will continue to recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 30/30 | 0 | 0 | 29/30 | 1 | 1 |
| LiA3-Ref | NaCl | 30/30 | 0 | 0 | 29/30 | 1 | 1 |
| LiD3-Core | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiD3-Core | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDA-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDS-1 | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDS-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiLC-1 | LiCl | 30/30 | 0 | 0 | 29/30 | 1 | 1 |
| LiLC-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiN3-Core | LiCl | 30/30 | 0 | 0 | 29/30 | 1 | 1 |
| LiN3-Core | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiND-Hybrid | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
