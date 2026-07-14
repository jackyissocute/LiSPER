# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-14 10:10 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 131 equilibrations complete; 98 equilibrations + 26 production active |
| Real GROMACS work | 124 real one-thread `mdrun`; 124/124 computational threads |
| Idle reason | None; the four-thread safety reserve is preserved and queued distinct windows wait on the global gate |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Measured horizon | Full-pool rate ≈75,523 atom·ns/day; window MD median ≈6.91 d; rendered table ≈2026-07-21 12:05 CST (90% band 08:25–14:15 CST) |
| Next | Backfill distinct EQ/production work; recalibrate after the first production completion; run paired WHAM after both ion campaigns complete |

LiDA-1/NaCl initially failed at step 0 because its peptide crossed the periodic boundary, making the GROMACS pull-group distance 3.055 nm despite a minimum-image site distance of 0.336 nm. Only that scope was stopped; the peptide was made whole and centered, the bound start was rebuilt, and the relaunched GROMACS distance is 0.354 nm. All current work is healthy and the global gate is full.

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
