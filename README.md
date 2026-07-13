# LiSPER

LiSPER develops short peptides for preferential lithium capture over sodium in
aqueous solution. The computational deliverables are:

1. standard binding free energies, `DeltaG_bind_Li` and `DeltaG_bind_Na`;
2. selectivity, `DeltaDeltaG_Li-Na = DeltaG_bind_Li - DeltaG_bind_Na`.

Negative `DeltaDeltaG_Li-Na` favors Li+. Capture and release kinetics are a
separate question and are not inferred from equilibrium free energies.

## Current status

Snapshot: `2026-07-13 22:06 CST`.

- Eight candidate sequences are present. The audited source holdings contain
  all eight complete LiCl CHARMM-GUI exports, but no complete NaCl export;
  NaCl source fragments are insufficient for production.
- The complete LiCl exports, plus NaCl ion-count metadata for `LiA3-Ref`, encode
  free, uncapped peptides with charged NH3+ and COO- termini at 0.15 M salt.
- No peptide binding-free-energy or selectivity row has been accepted: `0/8`.
- The active work is force-field and functional-group validation before peptide
  production.

## Computational estimator

The primary selectivity calculation is the matched thermodynamic cycle

`DeltaDeltaG_Li-Na = DeltaG_bulk_Li-to-Na - DeltaG_site_Li-to-Na`.

Both legs must use the same force field, water model, temperature,
electrostatics, finite-size treatment, and alchemical path. Absolute affinity
will use a standard-state double-decoupling calculation after the force field
and bound-state definition are validated.

The method contract and exact modeled chemical species are documented in
[`01_computational_discovery/free_energy/COMPUTATIONAL_VALIDATION_STRATEGY.md`](01_computational_discovery/free_energy/COMPUTATIONAL_VALIDATION_STRATEGY.md)
and
[`01_computational_discovery/free_energy/SYSTEM_AND_ESTIMAND.md`](01_computational_discovery/free_energy/SYSTEM_AND_ESTIMAND.md).

## Repository map

| Path | Purpose |
|---|---|
| `01_computational_discovery/sequences/` | Eight candidate sequences |
| `01_computational_discovery/esmfold/` | Starting structural models |
| `01_computational_discovery/md/` | Audited CHARMM-GUI inputs and incomplete historical holdings |
| `01_computational_discovery/free_energy/` | Current estimands, model validation, and alchemical workflow |
| `02_experimental_validation/` | Wet-lab validation planning |
| `04_reference_library/` | Literature evidence |

Computational predictions rank hypotheses; experimental Li/Na competition
measurements remain necessary for validating capture performance.
