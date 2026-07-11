# Vendor Peptide Order Checklist

Use this checklist when ordering LiSPER peptides from GenScript or another China peptide vendor.

## Decision

Track A peptides are purchased as finished synthetic peptides. Do not order plasmids, expression inserts, or bacterial production services for Track A.

## Recommended Specs

| Spec | Preferred default | Why |
|---|---|---|
| Sequence | Exact sequences in `candidate_order_table.csv` | Must match computational library |
| Purity | ≥95% HPLC for assay set; ≥98% if budget allows | Binding data need clean material |
| Quantity | Start 5–10 mg per candidate | Enough for QC + Li/Na replicates |
| Terminals | Free N- and C-termini unless assay plan says otherwise | Matches MD peptide model |
| Salt/counterion form | Prefer TFA-removed / acetate or HCl form if offered; record exact form | Na/TFA carryover can bias ion assays |
| QC package | HPLC chromatogram + MS for every peptide | Publication-grade identity/purity |
| Aliquoting | Request lyophilized powder in labeled vials | Easier storage and dilution |

## Order Priority

If budget is limited:

1. Always order `LiA3-Ref`.
2. Order current top computational subset first (after PMF ranking is ready).
3. Fill remaining candidates when funds allow.

If budget allows, order all 8 candidates in one batch for a full experimental-vs-PMF rank comparison.

## Vendor Questions To Confirm In Writing

- Exact amino-acid sequence and length for each vial label.
- Purity method and reported purity %.
- Counterion / residual TFA / residual sodium guidance.
- Solubility recommendation for aqueous buffer near pH 7.
- Storage and reconstitution instructions.
- Delivery of HPLC + MS certificates with shipment.
- Whether any N-terminal acetyl or C-terminal amide was added (default: none).

## Receipt Gate

Do not open binding assays until:

1. Vial labels match `candidate_order_table.csv`.
2. HPLC/MS certificates are filed under a future `ordering/receipts/` or lab notebook path.
3. Buffer blank ICP (or equivalent) shows acceptable Li/Na background after reconstitution.
