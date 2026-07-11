# 04 Track A Controls and Troubleshooting

## Required Controls

| Control | Why it is needed |
|---|---|
| No-peptide blank | Measures Li/Na loss to tubes, filters, and buffers |
| Buffer-only blank | Detects Li/Na contamination |
| `LiA3-Ref` | Sequence-related negative/reference control |
| Li-only condition | Tests lithium association without sodium |
| Na-only condition | Tests nonspecific sodium association |
| Li+Na condition | Direct selectivity condition |
| Known LBP peptide, if available | Positive method control |

## Troubleshooting Table

| Stage | Problem | Likely cause | Solution |
|---|---|---|---|
| Receipt | label/sequence mismatch | order or shipping error | quarantine vial; reorder; do not assay |
| QC | no MS peak for expected mass | wrong sequence or bad lot | contact vendor; hold assays |
| Reconstitution | cloudy / precipitate | poor solubility | adjust pH/solvent with vendor guidance |
| Binding assay | high Li loss in blank | tube/filter adsorption | change plasticware; validate separation |
| Binding assay | high Na binding | nonspecific electrostatics | compare `LiA3-Ref`; adjust ionic strength |
| Binding assay | high blank ions | water/salt/TFA contamination | remake buffers; check vendor counterion |
| Analysis | poor mass balance | separation/sample prep artifact | measure wash and retained fractions |

## Decision Rules

Do not interpret binding data unless:

- peptide lot has identity/purity evidence,
- no-peptide blank is acceptable,
- `LiA3-Ref` is included,
- Li and Na measurements are within analytical range,
- sample handling is consistent across candidates.

## Escalation Path

If one candidate lot fails QC repeatedly:

1. Do not call the peptide scientifically failed.
2. Record it as a supply/QC limitation.
3. Reorder that sequence or advance other QC-passing candidates to Track B planning.
