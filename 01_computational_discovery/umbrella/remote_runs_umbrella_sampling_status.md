# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-16 14:13 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 359 equilibrations + 79 production complete; 1 equilibration + 125 production active |
| Real GROMACS work | 126 unique one-thread `mdrun`; 126/126 umbrella-MD threads; five supplemental continuations run at nice 15 and idle I/O priority |
| Reserved support | 0/2 persistent threads in use; both remain available for launch, verification, monitoring, and analysis |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Measured horizon | 438 endpoint-valid stages average ≈73,720 atom·ns/day; 1,000 current-queue list-schedule resamples at 126 MD slots give table ≈2026-07-21 01:11 CST (90% band 00:30–01:39 CST), recalibrated as production evidence grows |
| Next | Keep the healthy 126-thread pool full, continue slow-tail priority, and run paired WHAM only after both ion campaigns complete |

All 126 jobs advance in distinct window directories. Completion requires both the configured final step and the GROMACS finish marker; no active log tail contains a fatal, SETTLE, or LINCS error.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 21/30 | 9 | 0 | 3/30 | 27 | 1 |
| LiA3-Ref | NaCl | 14/30 | 16 | 1 | 2/30 | 28 | 3 |
| LiD3-Core | LiCl | 22/30 | 8 | 0 | 6/30 | 24 | 0 |
| LiD3-Core | NaCl | 19/30 | 11 | 0 | 3/30 | 27 | 0 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 0/30 | 30 | 30 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 0/30 | 30 | 30 |
| LiDA-1 | LiCl | 27/30 | 3 | 0 | 16/30 | 14 | 0 |
| LiDA-1 | NaCl | 17/30 | 13 | 0 | 6/30 | 24 | 0 |
| LiDS-1 | LiCl | 20/30 | 10 | 0 | 9/30 | 21 | 1 |
| LiDS-1 | NaCl | 27/30 | 3 | 0 | 14/30 | 16 | 1 |
| LiLC-1 | LiCl | 17/30 | 13 | 0 | 5/30 | 25 | 0 |
| LiLC-1 | NaCl | 18/30 | 12 | 0 | 5/30 | 25 | 1 |
| LiN3-Core | LiCl | 20/30 | 10 | 0 | 4/30 | 26 | 0 |
| LiN3-Core | NaCl | 17/30 | 13 | 0 | 3/30 | 27 | 1 |
| LiND-Hybrid | LiCl | 30/30 | 0 | 0 | 1/30 | 29 | 29 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 2/30 | 28 | 28 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
