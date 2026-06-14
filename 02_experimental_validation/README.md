# 02 Experimental Validation

This stage contains the wet-lab validation paths for LiSPER: current His6-SUMO-LiSPER plasmid designs, expression/purification planning, binding-assay planning, surface-display validation research, and experimental protocols.

```mermaid
flowchart LR
    A["Computationally ranked candidates"] --> B["Purified peptide track"]
    A --> C["Surface-display track"]
    B --> D["plasmids/"]
    D --> E["wetlab/"]
    E --> F["Li+/Na+ binding assays"]
    C --> G["surface_display_host_selection/"]
    G --> H["Whole-cell Li capture assays"]
    F --> I["LiSPER selectivity evidence"]
    H --> I
```

## Contents

| Folder | Purpose |
|---|---|
| `plasmids/` | Current vendor-ready His6-SUMO-LiSPER constructs, vector maps, and design review. |
| `wetlab/` | Expression, purification, SUMO cleavage, peptide recovery, and assay planning. |
| `protocols/` | Reproducible experimental protocols and operating notes. |
| `surface_display_host_selection/` | Parallel validation track for displaying LiSPER on cells and testing whole-cell Li+/Na+ selectivity. |

Superseded direct His/T7-LiSPER plasmids were moved to `../archive/superseded_plasmid_designs/`.
