# Analysis

Working area for notebooks, exploratory calculations, intermediate tables, and result interpretation.

## Analysis Flow

```mermaid
flowchart LR
    A["MD trajectories"] --> B["Clustering summaries"]
    B --> C["Representative structures"]
    C --> D["Umbrella/PMF outputs"]
    D --> E["Li+/Na+ selectivity ranking"]
```

## Expected Contents

| Type | Example |
|---|---|
| Notebooks | trajectory inspection, PMF convergence, ranking plots |
| Intermediate tables | cluster populations, RMSD/RMSF, contact summaries |
| Exploratory scripts | one-off analysis before promotion to `../../06_shared/scripts/` |

Promote repeatable analysis code to `../../06_shared/scripts/` once the workflow stabilizes.
