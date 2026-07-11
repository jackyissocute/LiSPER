# 02 Li+/Na+ Binding Assay Protocol

## Purpose

Measure whether vendor-ordered LiSPER peptides bind Li+ and preferentially reject Na+.

## Assay Principle

Compare Li and Na distribution between peptide-associated and free fractions. Separation format may need optimization because LiSPER peptides are small (~1–2 kDa).

## Recommended Assay Conditions

| Parameter | Starting value |
|---|---|
| Buffer | HEPES or PIPES adjusted with KOH |
| pH | 7.0–7.5 |
| Li+ | 0.1, 0.5, 1, 5, 10 mM |
| Na+ | 1, 10, 100, 500 mM |
| Temperature | 25 C first; then 30/37 C if needed |
| Incubation | 15, 30, 60 min |
| Replicates | at least 3 technical replicates; biological = independent peptide aliquots/lots when possible |

## Compatibility Requirements

Before assays, remove or account for:

- high sodium buffers,
- EDTA or strong chelators,
- residual TFA or unknown vendor salts if they interfere,
- plastic/filter background binding.

Use potassium-based pH adjustment so sodium is not accidentally introduced into the baseline buffer.

## Li-Only Assay

1. Prepare peptide in low-sodium assay buffer.
2. Prepare LiCl series.
3. Incubate peptide and Li+.
4. Separate free and peptide-associated Li using a validated method.
5. Measure Li by ICP-OES/ICP-MS or a validated screening kit.
6. Compare to no-peptide and `LiA3-Ref` controls.

## Na-Only Assay

1. Repeat the same workflow using NaCl.
2. Include higher Na concentrations relevant to competition.
3. Measure sodium background carefully.

## Li+Na Competition Assay

Suggested conditions:

- 1 mM Li + 1 mM Na
- 1 mM Li + 10 mM Na
- 1 mM Li + 100 mM Na
- 10 mM Li + 100 mM Na for higher-signal tests

Quantify both Li and Na in free and bound/recovered fractions.

## Separation Notes

Small peptides often defeat standard ultrafiltration assumptions. Validate peptide retention before trusting any filter-based bound/free split. Alternatives:

- equilibrium dialysis,
- immobilized-peptide / bead format,
- outsourced ICP on carefully prepared pre/post samples.

## Preferred Quantification

| Method | Role |
|---|---|
| ICP-OES | Preferred routine Li/Na quantification |
| ICP-MS | Lower concentrations / trace checks |
| Ion chromatography | Local alternative if validated |
| Colorimetric kit | Screening only; confirm hits by ICP |

## Pass Gate To Analysis

Do not interpret selectivity until:

- peptide QC from protocol 01 is complete,
- no-peptide blank is acceptable,
- `LiA3-Ref` is included in the same batch,
- Li and Na measurements are within analytical range.
