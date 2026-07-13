# 03 Track A Data Analysis and Interpretation

## Required Data

| Data type | Required fields |
|---|---|
| Peptide lot | candidate, vendor, lot, purity, concentration estimate, QC status |
| Assay condition | buffer, pH, temperature, time, Li, Na |
| Measurement | Li free, Na free, bound/recovered fraction if available |
| Controls | no peptide, `LiA3-Ref`, buffer blank |
| Replicates | technical and independent-aliquot IDs |

## Core Formulas

```text
Li_bound = Li_initial - Li_free
Na_bound = Na_initial - Na_free
percent_Li_bound = 100 * Li_bound / Li_initial
percent_Na_bound = 100 * Na_bound / Na_initial
```

Selectivity relative to solution composition:

```text
Li_Na_selectivity = (Li_bound / Na_bound) / (Li_initial / Na_initial)
```

If `Na_bound` is near the detection limit, report a lower-bound selectivity estimate using the Na detection limit rather than reporting infinity.

## Normalization

Normalize binding by:

- peptide mass or molar amount,
- assay volume,
- peptide lot,
- background from `LiA3-Ref`,
- background from no-peptide blank.

## Interpretation Criteria

Strong evidence:

- peptide identity confirmed by vendor HPLC/MS,
- Li binding above controls,
- Na binding low,
- Li/Na selectivity greater than `LiA3-Ref`,
- reproducible across independent aliquots/lots.

Ambiguous evidence:

- Li and Na both bind strongly,
- binding appears only in one aliquot,
- mass balance is poor,
- no-peptide blank loses Li.

Negative evidence:

- candidate matches `LiA3-Ref` and no-peptide controls,
- no reproducible Li binding,
- apparent selectivity caused by Na measurement artifact.

## Computational Comparison

Build an experimental rank table and compare with PMF / ΔΔG rank. Useful outcomes:

- strong agreement,
- partial agreement with explainable outliers,
- failure of a design feature that guides redesign.

## What Track A Can Claim

Track A can support:

- molecular LiSPER peptide recognition,
- peptide-level Li/Na selectivity,
- experimental support for computational design.

Track A cannot by itself claim:

- surface-display function,
- packed-bed performance,
- industrial raffinate compatibility.
