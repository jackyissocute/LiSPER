# Track A: Purified Peptide Validation

Track A answers the molecular-recognition question:

> Does the LiSPER peptide itself selectively recognize Li+ over Na+?

This track uses the current His6-SUMO-LiSPER plasmids to express soluble fusion proteins, cleave SUMO, recover native LiSPER peptides, and test Li+/Na+ binding directly.

```mermaid
flowchart TD
    accTitle: Track A Bench Workflow
    accDescr: Track A starts with His6-SUMO-LiSPER plasmids and proceeds through expression, purification, cleavage, peptide recovery, QC, and Li over Na binding assays.

    plasmid["His6-SUMO<br/>plasmid"]
    transformation["Transformation"]
    expression["Expression<br/>test"]
    purification["Ni-NTA<br/>purification"]
    cleavage["SUMO<br/>cleavage"]
    recovery["Native peptide<br/>recovery"]
    assay["Li/Na<br/>binding assay"]
    evidence["Molecular<br/>evidence"]

    plasmid --> transformation
    transformation --> expression
    expression --> purification
    purification --> cleavage
    cleavage --> recovery
    recovery --> assay
    assay --> evidence
```

## Contents

| Folder | Purpose |
|---|---|
| `plasmids/` | Current His6-SUMO-LiSPER plasmid package and vector records. |
| `protocols/` | Ordered Track A protocols from transformation through binding-data analysis. |

## Start Here

1. Read `protocols/00_track_A_protocol_overview.md`.
2. Use `protocols/README.md` as the ordered protocol index.
3. Start with `Control-Negative` plus 2-4 priority candidates before scaling to all 10.
