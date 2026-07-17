# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-17 19:50 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 384 equilibrations + 161 production complete; 19 equilibration + 107 production active |
| Real GROMACS work | 126 unique one-thread `mdrun`; 126/126 umbrella-MD threads; all use `-ntmpi 1 -ntomp 1` in distinct window directories |
| Reserved support | 0/2 persistent threads in use; both remain available for launch, verification, monitoring, and analysis |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | 545 endpoint-valid stages average ≈73,169 atom·ns/day (≈9.22M atom·ns/day at 126 jobs); 1,000 current-queue campaign-block resamples give median table ETA ≈2026-07-21 05:00 CST (90% band 04:30–05:38 CST), recalibrated as production evidence grows |
| Next | Keep the verified 126-job pool full and run paired WHAM only after both ion campaigns complete |

All 126 jobs consumed CPU during a five-second `/proc` check and remain unique. Ready LiN3-Core/LiCl owns the 126th-slot ceiling as the largest remaining progress-adjusted atom-weighted workload; LiA3-Ref/NaCl returned to the lower ceiling after all 30 windows became active or complete. Only those two scheduler processes were replaced, with every healthy MD child preserved. The shared fast capacity check and duplicate-window guard remain active. Completion requires both the configured final step and the GROMACS finish marker; no active log tail contains a fatal, water-SETTLE failure, or LINCS warning.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 25/30 | 5 | 5 | 3/30 | 27 | 21 |
| LiA3-Ref | NaCl | 21/30 | 9 | 9 | 4/30 | 26 | 17 |
| LiD3-Core | LiCl | 24/30 | 6 | 0 | 6/30 | 24 | 2 |
| LiD3-Core | NaCl | 19/30 | 11 | 0 | 3/30 | 27 | 16 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 21/30 | 9 | 5 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 24/30 | 6 | 2 |
| LiDA-1 | LiCl | 27/30 | 3 | 0 | 17/30 | 13 | 0 |
| LiDA-1 | NaCl | 19/30 | 11 | 0 | 7/30 | 23 | 1 |
| LiDS-1 | LiCl | 23/30 | 7 | 0 | 10/30 | 20 | 1 |
| LiDS-1 | NaCl | 28/30 | 2 | 0 | 15/30 | 15 | 2 |
| LiLC-1 | LiCl | 19/30 | 11 | 0 | 5/30 | 25 | 3 |
| LiLC-1 | NaCl | 21/30 | 9 | 0 | 6/30 | 24 | 0 |
| LiN3-Core | LiCl | 21/30 | 9 | 5 | 4/30 | 26 | 10 |
| LiN3-Core | NaCl | 17/30 | 13 | 0 | 4/30 | 26 | 12 |
| LiND-Hybrid | LiCl | 30/30 | 0 | 0 | 13/30 | 17 | 8 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 19/30 | 11 | 7 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
