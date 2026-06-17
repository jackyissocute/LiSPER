# 12 Track A Controls and Troubleshooting

## Required Controls

| Control | Why it is needed |
|---|---|
| No-peptide blank | Measures Li/Na loss to tubes, filters, and buffers. |
| Buffer-only blank | Detects Li/Na contamination. |
| His6-SUMO-only or empty vector purification control | Measures tag/SUMO/resin background. |
| LiA3-Ref LiSPER | Sequence-related negative control. |
| SUMO protease blank | Detects protease and cleavage-buffer interference. |
| Li-only condition | Tests lithium association without sodium. |
| Na-only condition | Tests nonspecific sodium association. |
| Li+Na condition | Direct selectivity condition. |
| Known LBP if available | Positive method control. |

## Troubleshooting Table

| Stage | Problem | Likely cause | Solution |
|---|---|---|---|
| Transformation | no colonies | cells/plasmid/antibiotic issue | repeat with positive control and fresh plates |
| Colony confirmation | wrong insert signal | colony mix-up or construct issue | test another colony; sequence junctions |
| Expression | no fusion band | weak expression or induction failure | verify host/IPTG; use anti-His blot |
| Expression | insoluble fusion | aggregation | lower IPTG/temp; shorter induction |
| Lysis | viscous lysate | DNA release | clarify longer; use nuclease if approved |
| Ni-NTA | target in flow-through | resin overload or poor binding | reduce load; check pH/imidazole |
| Cleavage | incomplete SUMO cleavage | buffer/protease issue | optimize protease ratio, time, temp |
| Recovery | peptide lost | wrong filter/resin/tube adsorption | avoid MWCO mismatch; collect all flow-through |
| QC | no peptide visible | peptide too small for gel | use MS/HPLC |
| Binding assay | high Li loss in blank | tube/filter adsorption or precipitation | change plasticware; run no-cell/no-peptide controls |
| Binding assay | high Na binding | nonspecific electrostatics | compare LiA3-Ref; adjust buffer/ionic strength |
| Analysis | poor mass balance | separation/sample prep artifact | measure wash and pellet fractions |

## Decision Rules

Do not interpret binding data unless:

- peptide prep has some identity/QC evidence,
- no-peptide blank is acceptable,
- LiA3-Ref is included,
- Li and Na measurements are within analytical range,
- sample handling is consistent across candidates.

## Escalation Path

If purified peptide recovery repeatedly fails:

1. Do not call the peptide scientifically failed.
2. Record the failure as a production/recovery limitation.
3. Continue Track B surface-display validation if ready.
4. Consider synthetic peptide purchase for top candidates if budget allows.

