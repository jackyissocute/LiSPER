# 10 Purified Peptide Li+/Na+ Binding Assay Protocol

## Purpose

Measure whether recovered LiSPER peptides bind Li+ and preferentially reject Na+.

## Assay Principle

Compare Li and Na distribution between peptide-associated and free fractions. The exact separation format may need optimization because LiSPER peptides are small.

## Recommended Assay Conditions

| Parameter | Starting value |
|---|---|
| Buffer | HEPES or PIPES adjusted with KOH |
| pH | 7.0-7.5 |
| Li+ | 0.1, 0.5, 1, 5, 10 mM |
| Na+ | 1, 10, 100, 500 mM |
| Temperature | 25 C first; then 30/37 C if needed |
| Incubation | 15, 30, 60 min |
| Replicates | at least 3 biological peptide preparations when possible |

## Compatibility Requirements

Before running binding assays, remove or account for:

- imidazole from Ni-NTA elution,
- nickel or cobalt resin carryover,
- high sodium buffers,
- EDTA or strong chelators,
- glycerol/salts introduced during cleavage or storage,
- plastic/filter background binding.

Use potassium-based pH adjustment where possible so sodium is not accidentally introduced into the baseline buffer.

## Li-Only Assay

1. Prepare peptide in low-sodium assay buffer.
2. Prepare LiCl series.
3. Incubate peptide and Li+.
4. Separate free and peptide-associated Li using validated method.
5. Measure Li by ICP-OES/ICP-MS or validated screening kit.
6. Compare to no-peptide, SUMO-only, and LiA3-Ref controls.

## Na-Only Assay

1. Repeat the same workflow using NaCl.
2. Include higher Na concentrations relevant to competition.
3. Measure sodium background carefully.

## Mixed Li+Na Competition Assay

Suggested first matrix:

- 1 mM Li + 1 mM Na.
- 1 mM Li + 10 mM Na.
- 1 mM Li + 100 mM Na.
- 10 mM Li + 100 mM Na.

## Separation Options

| Option | Use | Concern |
|---|---|---|
| Equilibrium dialysis | Good molecular binding logic | Peptide may pass membrane unless MWCO is appropriate. |
| Ultrafiltration | Simple if peptide retained | 1-2 kDa peptide may be lost. |
| Immobilized peptide assay | Easier separation | Adds support effects; becomes closer to future Track C. |
| Direct MS/ICP after cleanup | Useful for method development | Needs analytical access. |

## Interpretation

A promising peptide shows:

- Li binding above no-peptide and LiA3-Ref controls.
- Na binding low relative to Li.
- Li enrichment in mixed Li+Na assays.

## Minimum Reporting Template

For each peptide and condition, record:

| Field | Why |
|---|---|
| peptide preparation ID | separates biological prep variability from sequence effect |
| estimated peptide amount | needed for binding normalization |
| buffer composition and pH | ions and pH strongly affect interpretation |
| Li/Na input concentration | defines competition strength |
| Li/Na measured in blanks | detects background contamination |
| Li/Na measured after peptide incubation | primary readout |
| recovery/separation method | prevents confusing separation artifact with binding |
