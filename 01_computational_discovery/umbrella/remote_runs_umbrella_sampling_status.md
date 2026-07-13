# Umbrella Sampling Status

Scientific steward snapshot: 2026-07-13 20:33 CST

## Decision (authoritative)

LiLC-1 umbrella production is stopped with checkpoints preserved. The former numerical `PASS`/`REPAIR` evaluator and heuristic region lock are retired; their historical outputs are not scientific verdicts. Seven historical Na paths omitted required published NBFIX terms; LiDA-1 alone contains both audited terms. Affected Na results are scientifically unusable. The five-donor-COM distance is also rejected for a same-site dissociation claim because it permits off-site peptide-oxygen rebinding.

| Item | Value |
|---|---|
| Active host | EPYC 9554P 128t worker |
| Active campaign | **LiLC-1** locked-site pilot (LiCl + NaCl) |
| Stage | **METHOD CORRECTION** — stopped at approximately 2.22 ns/window; 30 Li and 30 Na checkpoints preserved |
| Drivers | 0 real `gmx mdrun` processes; analysis and bounded method tests may use the worker |
| Geometry screen | **8/8** paired starts are within their declared distance screen; this does not validate binding or PMF reliability |
| Promotion | **Frozen** while the estimand, autocorrelation-aware uncertainty, overlap evidence, physical state definitions, and independent-replica plan are reviewed |
| Capacity | 0/124 real one-thread `mdrun`; idle because no scientifically valid production protocol is currently authorized, not to reduce fixed machine cost |

## Paired site-lock status

| Candidate | Classification | Declared site | Status |
|---|---|---|---|
| `LiLC-1` | pilot | terminal Asp14 | **METHOD CORRECTION** — Na rebuild and new coordinate/restraint design required |
| `LiD3-Core` | held | central Asp9 | geometry screened; method review blocks launch |
| `LiD3-Flex` | held | central Asp11 | geometry screened; method review blocks launch |
| `LiND-Hybrid` | held | central Asp11 | geometry screened; method review blocks launch |
| `LiDS-1` | held | central Asp7 | geometry screened; method review blocks launch |
| `LiDA-1` | held | central Asp7/Asp9 | geometry screened; method review blocks launch |
| `LiN3-Core` | held | central Asn9 | geometry screened; method review blocks launch |
| `LiA3-Ref` | held | central Ala9 backbone | geometry screened; method review blocks launch |

## Corrected evidence path

1. Pin and hash the corrected Na topology with `SOD-OC` and `CLA-SOD` NBFIX, then rebuild its representative sampling, pull, equilibration, and umbrella inputs.
2. Define whether the estimand is a 1 M standard binding free energy or finite-concentration selectivity; do not subtract unlike concentrations/boxes blindly.
3. Compare radial/path-coordinate restraint designs on short pilots and verify that the declared chemical site is preserved while hydration, coordination, and peptide modes are characterized.
4. Derive the coordinate Jacobian, restraint-release, reference-state, and standard-volume contributions before production.
5. Generate/adapt window centers from measured neighboring support; spacing, spring, equilibration, and production lengths remain measured design choices rather than universal gates.
6. Use autocorrelation-aware WHAM, cumulative/disjoint blocks, independently initialized campaigns, sensitivity analysis, and propagated uncertainty as an evidence package—not a script-generated `PASS`.
7. Submit the written protocol and LiLC-1 proof for explicit user approval before formal 124-thread production.

## Data handling

- Preserve raw trajectories, checkpoints, pull files, WHAM logs, and retired analysis outputs.
- Synchronize only public-safe evidence and method descriptions to GitHub.
- Do not create `delta_g_summary.tsv` or `selectivity_summary.tsv` until the supported estimand and claim scope are documented.
