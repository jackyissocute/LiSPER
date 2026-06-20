# Track A Planning

Track A now begins with ordered synthetic LiSPER peptides.

Use this folder to plan direct peptide binding assays before committing to surface-display plasmid construction.

| File | Purpose |
|---|---|
| [Ordered synthetic peptide binding plan](ordered_synthetic_peptide_binding_plan.md) | Main plan for using vendor-ordered peptides to validate computational Li/Na selectivity predictions |

## Current Logic

```mermaid
flowchart TD
    accTitle: Ordered Peptide Validation
    accDescr: Track A starts with ordered synthetic peptides, measures Li and Na binding directly, compares the results with computational ranking, and selects candidates for Track B.

    computational["Computational<br/>ranking"]
    order["Order synthetic<br/>peptides"]
    assay["Direct Li/Na<br/>binding assays"]
    compare["Compare with<br/>PMF ranking"]
    select["Select top<br/>display candidates"]

    computational --> order
    order --> assay
    assay --> compare
    compare --> select
```

The His6-SUMO plasmid and purification materials remain available one level up as a fallback production route.
