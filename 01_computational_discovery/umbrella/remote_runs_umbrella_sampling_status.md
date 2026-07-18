# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-18 11:57 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 4/16 pulls complete, 12 active; 120/480 windows generated; 0 equilibrations complete, 42 active; 0 production complete |
| Real GROMACS work | 54 unique `mdrun`: 12 seven-thread pulls + 42 one-thread EQ windows; 126/126 umbrella-MD threads in 54 distinct directories |
| Reserved support | 2/2 threads used transiently for the off-host sync and live verification; both return after those checks |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 54.69M atom·ns. The last verified same-host/protocol rate basis is ≈72,934 atom·ns/day/job (≈9.19M/day at 126 jobs), giving nominal table ETA 2026-07-24 14:50 CST; ±20% throughput sensitivity gives 2026-07-23 15:00 to 2026-07-26 02:30 CST |
| Next | Preserve the healthy 126/126 pool; as pulls finish, give newly free slots to ready windows with the greatest remaining atom-weighted campaign work |

A five-second `/proc` sample found all 54 real GROMACS executables advancing, with 126 actual MD threads and no duplicate working directory. LiDA-1 and LiDS-1 LiCl/NaCl pulls independently verified configured step 500,000 plus `Finished mdrun`; all four generated 30 windows. LiDA-1 owns the 42 active one-thread EQ slots; the higher-atom-count LiDS-1 windows are ready and receive newly freed capacity without interrupting healthy work. No active log contains a fatal, water-SETTLE, or LINCS warning. New one-thread EQ/production evidence will recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiA3-Ref | NaCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiD3-Core | LiCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiD3-Core | NaCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiD3-Flex | LiCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiD3-Flex | NaCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiDA-1 | LiCl | 0/30 | 30 | 30 | 0/30 | 30 | 0 |
| LiDA-1 | NaCl | 0/30 | 30 | 12 | 0/30 | 30 | 0 |
| LiDS-1 | LiCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiDS-1 | NaCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiLC-1 | LiCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiLC-1 | NaCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiN3-Core | LiCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiN3-Core | NaCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiND-Hybrid | LiCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |
| LiND-Hybrid | NaCl | 0/30 | 30 | 0 | 0/30 | 30 | 0 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
