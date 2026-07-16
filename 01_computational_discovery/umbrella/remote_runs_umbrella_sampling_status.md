# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-16 10:46 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 359 equilibrations + 76 production complete; 0 equilibrations + 124 production active |
| Real GROMACS work | 124 real one-thread `mdrun`; 124/126 computational threads; two slots intentionally released after SSH responsiveness degraded at 126 |
| Idle reason | One additional compute slot is idle because the live workers retain the old 124-slot environment; restarting healthy piped jobs is higher risk than preserving them |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Measured horizon | 435 valid-stage mean ≈73,722 atom·ns/day; the measured 124-thread aggregate is ≈9.20M atom·ns/day; table ≈2026-07-21 12:20 CST (90% band 09:20–14:50 CST), recalibrated as 1.566–3.788 ns/day production evidence grows |
| Next | Keep the healthy 126-thread pool full, continue slow-tail priority, and run paired WHAM only after both ion campaigns complete |

LiDA-1/NaCl initially failed at step 0 because its peptide crossed the periodic boundary, making the GROMACS pull-group distance 3.055 nm despite a minimum-image site distance of 0.336 nm. Only that scope was stopped; the peptide was made whole and centered, the bound start was rebuilt, and the relaunched GROMACS distance is 0.354 nm. Slow LiD3-Flex/LiND-Hybrid allocation is 120 jobs. Two supplemental LiA3-Ref/NaCl runs were stopped after 126-thread SSH degradation; their 83,360/83,440-step partial outputs are quarantined and excluded from completion. Completion checks now require the configured final step in addition to the GROMACS finish marker.

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
