# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-17 07:50 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 374 equilibrations + 135 production complete; 18 equilibration + 108 production active |
| Real GROMACS work | 126 unique one-thread `mdrun`; 126/126 umbrella-MD threads; all use `-ntmpi 1 -ntomp 1` in distinct window directories |
| Reserved support | 0/2 persistent threads in use; both remain available for launch, verification, monitoring, and analysis |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Measured horizon | 509 endpoint-valid stages average ≈73,673 atom·ns/day (≈9.28M atom·ns/day at 126 jobs); 1,000 current-queue list-schedule resamples give median table ETA ≈2026-07-20 20:24 CST (90% band 19:38–21:02 CST), recalibrated as production evidence grows |
| Next | Keep the verified 126-job pool full and run paired WHAM only after both ion campaigns complete |

All 126 jobs consumed CPU during a five-second `/proc` check and remain unique. The two new slots went to the highest remaining atom-weighted ready campaigns, LiA3-Ref/NaCl and LiN3-Core/NaCl. Their schedulers now use 125- and 126-job caps, respectively, and the shared driver prevents a restarted scheduler from duplicating an already-active window. Completion requires both the configured final step and the GROMACS finish marker; no active log tail contains a fatal, water-SETTLE failure, or LINCS warning.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 22/30 | 8 | 3 | 3/30 | 27 | 4 |
| LiA3-Ref | NaCl | 19/30 | 11 | 2 | 2/30 | 28 | 5 |
| LiD3-Core | LiCl | 23/30 | 7 | 2 | 6/30 | 24 | 2 |
| LiD3-Core | NaCl | 19/30 | 11 | 0 | 3/30 | 27 | 4 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 16/30 | 14 | 14 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 18/30 | 12 | 12 |
| LiDA-1 | LiCl | 27/30 | 3 | 0 | 16/30 | 14 | 3 |
| LiDA-1 | NaCl | 19/30 | 11 | 0 | 6/30 | 24 | 7 |
| LiDS-1 | LiCl | 22/30 | 8 | 1 | 10/30 | 20 | 1 |
| LiDS-1 | NaCl | 28/30 | 2 | 0 | 15/30 | 15 | 2 |
| LiLC-1 | LiCl | 18/30 | 12 | 1 | 5/30 | 25 | 3 |
| LiLC-1 | NaCl | 19/30 | 11 | 4 | 6/30 | 24 | 0 |
| LiN3-Core | LiCl | 21/30 | 9 | 0 | 4/30 | 26 | 4 |
| LiN3-Core | NaCl | 17/30 | 13 | 5 | 3/30 | 27 | 9 |
| LiND-Hybrid | LiCl | 30/30 | 0 | 0 | 10/30 | 20 | 20 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 12/30 | 18 | 18 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
