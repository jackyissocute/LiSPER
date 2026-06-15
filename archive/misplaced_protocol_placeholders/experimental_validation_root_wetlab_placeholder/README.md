# Wet Lab

Experimental planning and results for expression, purification, surface display, and Li+/Na+ selectivity assays.

## Experimental Workflow

```mermaid
flowchart TD
    A["Candidate selection"] --> B["Gene design"]
    B --> C["Codon optimization"]
    C --> D["Plasmid construction"]
    D --> E["Purified peptide track"]
    D --> J["Surface-display track"]
    E --> F["Protein purification"]
    F --> G["Li+ binding assay"]
    G --> H["Na+ competition assay"]
    J --> K["Whole-cell Li capture assay"]
    K --> L["Whole-cell Na competition assay"]
    H --> I["Li+/Na+ selectivity evidence"]
    L --> I
```

## Assay Design Packages

| Folder | Purpose |
|---|---|
| `surface_display_assays/` | Whole-cell Li+/Na+ binding and selectivity assay design for future eCPX surface-display constructs. |
| `../validation_framework/` | Overall Track A/Track B validation logic and complete protocol documents. |

## Records to Keep

| Record | Folder Use |
|---|---|
| Expression conditions | Compare constructs and induction conditions |
| Purification notes | Track yield and purity |
| Binding assay data | Validate computational predictions |
| Na+ competition data | Measure selectivity directly |
