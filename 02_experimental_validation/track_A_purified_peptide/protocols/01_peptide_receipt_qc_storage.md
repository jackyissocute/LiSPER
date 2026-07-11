# 01 Peptide Receipt, QC, and Storage

## Purpose

Confirm that vendor-delivered synthetic peptides match the ordered LiSPER sequences and are suitable for Li+/Na+ binding assays.

## Why This Matters

Binding results are not interpretable if peptide identity, purity, concentration, counterion form, or storage condition is unknown.

## Receipt Checklist

1. Match vial labels to `../ordering/candidate_order_table.csv`.
2. File vendor HPLC chromatogram and MS report for each peptide.
3. Record purity %, counterion/salt form, lot number, and quantity.
4. Confirm terminals (free N/C vs acetyl/amide) match the order.

## Recommended QC

| QC method | Purpose |
|---|---|
| Vendor HPLC + MS | Primary identity and purity evidence |
| Optional lab LC-MS / MALDI | Independent mass confirmation if available |
| ICP / ion blank of reconstituted peptide buffer | Detect Li/Na contamination before assays |
| Visual solubility check | Catch precipitation before titration series |

## Concentration Estimation

LiSPER peptides often lack aromatic residues, so A280 is usually not useful.

Use one of:

- lyophilized dry mass + volumetric reconstitution,
- HPLC peak calibration if available,
- amino-acid analysis if available,
- quantitative MS if available.

## Minimum QC Before Binding Assays

Proceed only when each peptide has:

- matching sequence/label record,
- HPLC/MS certificate on file,
- estimated concentration method recorded,
- buffer blank checked for Li/Na background,
- aliquots prepared for single-use or limited freeze-thaw.

## Storage Plan

| Storage format | Use |
|---|---|
| Lyophilized powder, cold and dry | Preferred long-term storage |
| Fresh aqueous aliquot, 4 C | Same-day or next-day handling only |
| Frozen aliquots, -80 C preferred | Working stocks after reconstitution |

Avoid repeated freeze-thaw cycles. Prefer low-bind tubes for aqueous stocks.

## Common Failure Modes

| Problem | Likely cause | Solution |
|---|---|---|
| Concentration drifts | adsorption or precipitation | low-bind tubes; check pH/solubility |
| High Li/Na blank | salt/TFA/water contamination | remake buffer; recheck vendor salt form |
| Assay batch inconsistency | freeze-thaw or uneven aliquots | fresh single-use aliquots |
