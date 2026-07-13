# Track A Planning

Track A begins with commercial synthetic LiSPER peptides (GenScript or equivalent China peptide vendor).

No plasmid design and no bacterial peptide production in this track.

| File | Purpose |
|---|---|
| [Ordered synthetic peptide binding plan](ordered_synthetic_peptide_binding_plan.md) | Main plan for vendor peptides validating computational Li/Na ranking |

```mermaid
flowchart TD
    accTitle: Ordered Peptide Validation
    accDescr: Track A orders synthetic peptides, measures Li and Na binding, compares with PMF ranking, and selects Track B candidates.

    computational["Computational<br/>ranking"]
    order["Order peptides<br/>from vendor"]
    assay["Direct Li/Na<br/>binding assays"]
    compare["Compare with<br/>PMF ranking"]
    select["Select top<br/>display candidates"]

    computational --> order
    order --> assay
    assay --> compare
    compare --> select
```

Ordering details live in `../ordering/`.
