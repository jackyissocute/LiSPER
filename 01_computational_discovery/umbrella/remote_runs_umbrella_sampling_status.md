# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-17 15:52 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 382 equilibrations + 160 production complete; 23 equilibration + 103 production active |
| Real GROMACS work | 126 unique one-thread `mdrun`; 126/126 umbrella-MD threads; all use `-ntmpi 1 -ntomp 1` in distinct window directories |
| Reserved support | 0/2 persistent threads in use; both remain available for launch, verification, monitoring, and analysis |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | 542 endpoint-valid stages average ≈73,429 atom·ns/day (≈9.25M atom·ns/day at 126 jobs); 1,000 current-queue campaign-block resamples give median table ETA ≈2026-07-21 01:09 CST (90% band 00:45–01:31 CST), recalibrated as production evidence grows |
| Next | Keep the verified 126-job pool full and run paired WHAM only after both ion campaigns complete |

All 126 jobs consumed CPU during a five-second `/proc` check and remain unique. LiA3-Ref/NaCl uses the 125-job ceiling and ready LiA3-Ref/LiCl owns the 126th slot; LiD3-Core/NaCl was removed from the top ceiling because all 30 of its windows were already active or complete. Only those two scheduler processes were replaced, with every healthy MD child preserved. The shared fast capacity check and duplicate-window guard remain active. Completion requires both the configured final step and the GROMACS finish marker; no active log tail contains a fatal, water-SETTLE failure, or LINCS warning.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 25/30 | 5 | 5 | 3/30 | 27 | 18 |
| LiA3-Ref | NaCl | 19/30 | 11 | 4 | 4/30 | 26 | 4 |
| LiD3-Core | LiCl | 24/30 | 6 | 0 | 6/30 | 24 | 2 |
| LiD3-Core | NaCl | 19/30 | 11 | 11 | 3/30 | 27 | 16 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 21/30 | 9 | 6 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 24/30 | 6 | 5 |
| LiDA-1 | LiCl | 27/30 | 3 | 0 | 17/30 | 13 | 0 |
| LiDA-1 | NaCl | 19/30 | 11 | 0 | 7/30 | 23 | 5 |
| LiDS-1 | LiCl | 23/30 | 7 | 0 | 10/30 | 20 | 1 |
| LiDS-1 | NaCl | 28/30 | 2 | 0 | 15/30 | 15 | 2 |
| LiLC-1 | LiCl | 19/30 | 11 | 0 | 5/30 | 25 | 3 |
| LiLC-1 | NaCl | 21/30 | 9 | 0 | 6/30 | 24 | 0 |
| LiN3-Core | LiCl | 21/30 | 9 | 0 | 4/30 | 26 | 4 |
| LiN3-Core | NaCl | 17/30 | 13 | 3 | 3/30 | 27 | 13 |
| LiND-Hybrid | LiCl | 30/30 | 0 | 0 | 13/30 | 17 | 13 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 19/30 | 11 | 11 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
