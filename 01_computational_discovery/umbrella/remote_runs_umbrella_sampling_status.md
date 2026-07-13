# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-13 19:05 CST

## Decision (authoritative)

Locked-site umbrella sampling remains live on the remote EPYC 9554P worker. The former numerical `PASS`/`REPAIR` evaluator and heuristic region lock are retired; their historical outputs are not scientific verdicts.

| Item | Value |
|---|---|
| Active host | EPYC 9554P 128t worker |
| Active campaign | **LiLC-1** locked-site pilot (LiCl + NaCl) |
| Stage | Pull + 0.5 ns window equilibration + initial 2.0 ns production complete; matched continuation to 4.0 ns running (30 windows/ion; 0 fatal-log matches) |
| Drivers | 60 real `gmx mdrun` processes (30 LiCl + 30 NaCl), `-ntmpi 1 -ntomp 1` |
| Geometry screen | **8/8** paired starts are within their declared distance screen; this does not validate binding or PMF reliability |
| Promotion | **Frozen** while the estimand, autocorrelation-aware uncertainty, overlap evidence, physical state definitions, and independent-replica plan are reviewed |
| Capacity | 60/124 real one-thread `mdrun`; 64 slots idle because only the 60 pilot windows are scientifically authorized during method review |

## Paired site-lock status

| Candidate | Classification | Declared site | Status |
|---|---|---|---|
| `LiLC-1` | pilot | terminal Asp14 | **SAMPLING** — matched continuation to 4.0 ns running; old QC verdict retired |
| `LiD3-Core` | held | central Asp9 | geometry screened; method review blocks launch |
| `LiD3-Flex` | held | central Asp11 | geometry screened; method review blocks launch |
| `LiND-Hybrid` | held | central Asp11 | geometry screened; method review blocks launch |
| `LiDS-1` | held | central Asp7 | geometry screened; method review blocks launch |
| `LiDA-1` | held | central Asp7/Asp9 | geometry screened; method review blocks launch |
| `LiN3-Core` | held | central Asn9 | geometry screened; method review blocks launch |
| `LiA3-Ref` | held | central Ala9 backbone | geometry screened; method review blocks launch |

## Corrected evidence path

1. Finish the already-running LiLC-1 continuation; duration alone is not a reliability claim.
2. Run `gmx wham -ac` and preserve per-window IACT estimates, histograms, PMFs, logs, trajectory-bootstrap profiles, and time-block profiles.
3. Report overlap connectivity and unsampled regions directly; do not convert them to an invented universal percentage cutoff.
4. Declare bound/reference states from peptide-ion physics and the reaction-coordinate definition before interpreting the PMF. The retired heuristic regions remain historical only.
5. Estimate the declared-state probability contrast by Boltzmann integration and label it diagnostic/non-standard-state. Do not claim absolute binding free energy without the required restraint, coordinate-measure/Jacobian, state-volume, and standard-state treatment.
6. Add independently initialized replicas and report within-window/time and between-replica variation. Contiguous early/late blocks are convergence diagnostics, not independent replicas.
7. Test sensitivity to analysis start, blocks, bins, declared regions, and bootstrap choices. Promotion remains a documented scientific review decision, never a script-generated `PASS`.

## Data handling

- Preserve raw trajectories, checkpoints, pull files, WHAM logs, and retired analysis outputs.
- Synchronize only public-safe evidence and method descriptions to GitHub.
- Do not create `delta_g_summary.tsv` or `selectivity_summary.tsv` until the supported estimand and claim scope are documented.
