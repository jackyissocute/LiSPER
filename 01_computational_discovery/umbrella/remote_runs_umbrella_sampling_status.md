# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-24 12:56 CST

## Live state

| Item | Value |
|---|---|
| Active host | EPYC 9554P, 128 hardware threads |
| Campaigns | 8 candidates × LiCl/NaCl = 16 independent paired-site campaigns |
| Stage | 16/16 pulls complete; 480/480 windows generated; 480 equilibrations complete; 418 production complete, 62 active |
| Real GROMACS work | 62 unique one-thread production `mdrun`; 62/126 umbrella-MD threads in 62 distinct directories, with all currently ready windows active |
| Reserved support | 1/2 threads active for the off-host restart sync; all campaign drivers are resumed |
| Bound starts | 16/16 regenerated, minimized, and validated without `-maxwarn` |
| Window protocol | 0.075 nm spacing; 0.5 ns equilibration; 2.0 ns production; 3 endpoint guards |
| Pre-WHAM gate | GROMACS 2026.0 `-ac` with retained `-oiact`/ACF evidence; production bootstrap is explicitly `-bs-method traj` |
| Measured horizon | Progress-adjusted queue = 1.77M atom·ns. The latest 351-minute same-host/protocol progress basis is ≈8.84M atom·ns/day aggregate, giving median eight-row table ETA 2026-07-24 17:45 CST; ±20% throughput sensitivity gives 2026-07-24 16:57 to 2026-07-24 18:57 CST |
| Next | Keep all 62 tail windows running; launch paired WHAM immediately as each remaining candidate pair completes |

A five-second `/proc` sample found all 62 real GROMACS executables advancing, with 62 actual MD threads and no duplicate working directory. All currently ready windows are active. All 16 pulls independently verified configured step 500,000 plus `Finished mdrun`; each generated 30 windows. All 480 EQ windows and 418 production windows verified their configured final step plus `Finished mdrun`; 62 production windows are active. No active log contains a fatal, water-SETTLE, or LINCS warning. LiDA-1 reached 30/30 production for both ions; paired WHAM completed with retained IACT/ACF and trajectory-bootstrap evidence, and its first table row is validated at Delta Delta G = -19.340 ± 3.642 kJ/mol, indicating Li preference within this protocol. The off-host restart sync is retrying after a transient connection reset; no simulation repair is active. Tail throughput will continue to recalibrate the forecast.

## Candidate window counts

| Candidate | Solution | EQ complete/30 | EQ left | EQ active | Production complete/30 | Production left | Production active |
|---|---|---:|---:|---:|---:|---:|---:|
| LiA3-Ref | LiCl | 30/30 | 0 | 0 | 24/30 | 6 | 6 |
| LiA3-Ref | NaCl | 30/30 | 0 | 0 | 15/30 | 15 | 15 |
| LiD3-Core | LiCl | 30/30 | 0 | 0 | 27/30 | 3 | 3 |
| LiD3-Core | NaCl | 30/30 | 0 | 0 | 24/30 | 6 | 6 |
| LiD3-Flex | LiCl | 30/30 | 0 | 0 | 28/30 | 2 | 2 |
| LiD3-Flex | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDA-1 | LiCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDA-1 | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |
| LiDS-1 | LiCl | 30/30 | 0 | 0 | 29/30 | 1 | 1 |
| LiDS-1 | NaCl | 30/30 | 0 | 0 | 26/30 | 4 | 4 |
| LiLC-1 | LiCl | 30/30 | 0 | 0 | 20/30 | 10 | 10 |
| LiLC-1 | NaCl | 30/30 | 0 | 0 | 25/30 | 5 | 5 |
| LiN3-Core | LiCl | 30/30 | 0 | 0 | 24/30 | 6 | 6 |
| LiN3-Core | NaCl | 30/30 | 0 | 0 | 29/30 | 1 | 1 |
| LiND-Hybrid | LiCl | 30/30 | 0 | 0 | 27/30 | 3 | 3 |
| LiND-Hybrid | NaCl | 30/30 | 0 | 0 | 30/30 | 0 | 0 |

## Analysis contract

`evaluate_paired_pmf_qc.py` outputs the radially corrected, endpoint-referenced PMF binding differences and paired Delta Delta G whenever profiles exist. Negative Delta Delta G means Li preference. WHAM uses per-window IACT weighting with retained IACT/ACF evidence and trajectory bootstrap; histogram support, endpoint span, early/late difference, burn-in sensitivity, and bootstrap uncertainty remain numerical diagnostics rather than invented universal PASS gates.

These PMF values support within-protocol Li/Na selectivity comparisons. They are not labeled as 1 M standard binding free energies.
