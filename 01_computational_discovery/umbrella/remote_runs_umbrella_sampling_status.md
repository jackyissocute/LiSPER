# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-14 00:26 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | LiDA-1 and LiDS-1 pulls complete; 12 pulls at 46.6–71.1%; 40 window equilibrations active across LiDA-1/LiCl, LiDA-1/NaCl, and LiDS-1/NaCl |
| Real GROMACS work | 52 real `mdrun`; 124/124 computational threads (12 × 7-thread pulls + 40 × 1-thread windows) |
| Idle reason | None; the four-thread safety reserve is preserved and queued distinct windows wait on the global gate |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Next | Finish pulls; automatically backfill distinct window equilibration/production; run paired WHAM after both ion campaigns complete |

LiDA-1/NaCl initially failed at step 0 because its peptide crossed the periodic boundary, making the GROMACS pull-group distance 3.055 nm despite a minimum-image site distance of 0.336 nm. Only that scope was stopped; the peptide was made whole and centered, the bound start was rebuilt, and the relaunched GROMACS distance is 0.354 nm. LiDA-1 and LiDS-1 now have 30+30 generated windows per pair, and the scheduler is filling the global gate without fatal, SETTLE, or LINCS errors.

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
