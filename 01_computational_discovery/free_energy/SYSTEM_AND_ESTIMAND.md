# Modeled system and estimands

## Chemical species read from the CHARMM-GUI exports

The audited holdings contain eight complete CHARMM-GUI exports, all for LiCl.
`LiA3-Ref` also retains NaCl ion-count and peptide-topology metadata, but its
GROMACS export is incomplete. The available source files record:

- `conc = 0.15` with `LIT/CLA` or `SOD/CLA`;
- a free N-terminal `NH3` atom type;
- terminal `OT1/OT2` carboxylate oxygens;
- deprotonated Asp carboxylates;
- separate LiCl and NaCl boxes where both exports exist.

None of the eight NaCl directories contains a complete CHARMM-GUI source
export. They are not accepted as production inputs and must be restored from
the original CHARMM-GUI packages before paired calculations.

The calculations therefore describe free, uncapped, zwitterionic peptides at
the protonation state encoded by those topologies. Acetylation, amidation,
surface attachment, or fusion to a protein defines a different chemical
species and requires a new system.

## Quantities to report

Standard binding free energy:

`DeltaG_bind_ion = RT ln(Kd_ion / 1 M)`.

Selectivity:

`DeltaDeltaG_Li-Na = DeltaG_bind_Li - DeltaG_bind_Na`.

The primary selectivity estimator is the matched site/bulk alchemical cycle:

`DeltaDeltaG_Li-Na = DeltaG_bulk_Li-to-Na - DeltaG_site_Li-to-Na`.

The cycle follows the published ion-selectivity construction
(https://doi.org/10.1073/pnas.1007150107) and the GROMACS free-energy
implementation
(https://manual.gromacs.org/2026.0/reference-manual/special/free-energy-implementation.html).

Absolute standard-state affinity will use double decoupling with explicit
restraint and standard-volume corrections
(https://doi.org/10.1021/jp807701h). Kinetics is not inferred from either
equilibrium estimator.

## Force-field validation before peptide production

Asp carboxylate and peptide amide/carbonyl interactions are represented by
acetate and N-methylacetamide/acetamide model compounds. The current reference
is the 2024 Group-1-ion Drude parameterization, which uses these compounds and
QM plus condensed-phase targets
(https://doi.org/10.1021/acs.jctc.3c01380).

Sampling length, lambda placement, and replica count are extended from
autocorrelation, state support, time-block stability, between-replica
variation, and model sensitivity. They are not fixed publication thresholds.
