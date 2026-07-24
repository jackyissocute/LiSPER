# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-25 00:15 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 480 equilibrations complete; 480 production complete, 0 active |
| Real GROMACS work | 0 production `mdrun`; 0/126 umbrella-MD threads; no queued or failed windows |
| Reserved support | 1/2 threads active for the off-host restart sync; all campaign drivers are resumed |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Terminal progress-adjusted queue = 0.000M atom·ns; all eight rows completed 2026-07-25 00:15 CST. ETA, throughput band, and production recalibration are closed and no longer applicable |
| Next | No remaining simulation or paired-analysis work; pause the steward automation after public verification |

Live `/proc` verification found no remaining production `mdrun`. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. All 480 EQ and all 480 production windows verified configured final nsteps plus `Finished mdrun`. No campaign failed or required repair. Eight paired rows are protocol-validated: LiDA-1 -19.340 ± 3.642, LiDS-1 -7.615 ± 7.286, LiD3-Core -3.630 ± 6.337, LiD3-Flex -1.360 ± 10.003, LiND-Hybrid -8.975 ± 9.825, LiLC-1 -0.554 ± 6.093, LiA3-Ref -0.034 ± 5.878, and LiN3-Core -0.815 ± 2.879 kJ/mol. These are radially corrected, endpoint-referenced within-protocol estimates, not 1 M standard binding free energies. Negative means nominal Li preference; uncertainty does not imply sign confidence when it spans zero.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiA3-Ref | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiD3-Core | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiD3-Core | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDA-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDS-1 | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDS-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiLC-1 | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiLC-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiN3-Core | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiN3-Core | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiND-Hybrid | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
