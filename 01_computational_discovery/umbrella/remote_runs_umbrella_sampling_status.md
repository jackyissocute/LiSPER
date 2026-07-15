# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-15 10:07 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 308 equilibrations + 38 production complete; 38 equilibrations + 88 production active |
| Real GROMACS work | 126 real one-thread `mdrun`; 126/126 computational threads |
| Idle reason | None; the two-thread system reserve is preserved and queued distinct windows wait on the global gate |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Measured horizon | 346-stage mean ≈73,945 atom·ns/day; twelve-hour pure-126 aggregate ≈9.17M atom·ns/day, within 0.4% of the 124-thread baseline and rate noise; table ≈2026-07-21 12:20 CST (90% band 09:20–14:50 CST), recalibrated as 2.500–3.788 ns/day production evidence grows |
| Next | Keep the healthy 126-thread pool full, continue slow-tail priority, and run paired WHAM only after both ion campaigns complete |

LiDA-1/NaCl initially failed at step 0 because its peptide crossed the periodic boundary, making the GROMACS pull-group distance 3.055 nm despite a minimum-image site distance of 0.336 nm. Only that scope was stopped; the peptide was made whole and centered, the bound start was rebuilt, and the relaunched GROMACS distance is 0.354 nm. The live ceiling is 126 and slow LiD3-Flex/LiND-Hybrid allocation has risen from 32 to 88 jobs without interrupting healthy work. All current work is healthy and the global gate is full.

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
