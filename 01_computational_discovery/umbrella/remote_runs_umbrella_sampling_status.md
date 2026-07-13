# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-13 22:58 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pull trajectories running and advancing |
| Real GROMACS work | 16 real `mdrun`; 112/124 computational threads |
| Idle reason | 16 indivisible pulls × 7 threads = 112; first completed pull automatically backfills one-thread windows toward 124/124 |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Next | Pull completion → automatic window extraction/equilibration/production → paired WHAM |

LiDA-1/NaCl initially failed at step 0 because its peptide crossed the periodic boundary, making the GROMACS pull-group distance 3.055 nm despite a minimum-image site distance of 0.336 nm. Only that scope was stopped; the peptide was made whole and centered, the bound start was rebuilt, and the relaunched GROMACS distance is 0.354 nm. All 16 pulls now advance without fatal, SETTLE, or LINCS errors.

## Analysis contract

`evaluate_paired_pmf_qc.py` now outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. Histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty are numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
