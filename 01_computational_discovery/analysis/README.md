# Analysis

Working area for notebooks, exploratory calculations, intermediate tables, and result interpretation.

## Analysis Flow

```mermaid
flowchart TD
    accTitle: Analysis Evidence Flow
    accDescr: Analysis starts from MD trajectories, summarizes structural clusters, selects representative structures, and supports Li over Na ranking.

    trajectories["MD<br/>trajectories"]
    clusters["Clustering<br/>summaries"]
    representatives["Representative<br/>structures"]
    pmf_outputs["Umbrella and<br/>PMF outputs"]
    ranking["Li/Na<br/>ranking"]

    trajectories --> clusters
    clusters --> representatives
    representatives --> pmf_outputs
    pmf_outputs --> ranking
```

## Expected Contents

| Type | Example |
|---|---|
| Notebooks | trajectory inspection, PMF convergence, ranking plots |
| Intermediate tables | cluster populations, RMSD/RMSF, contact summaries |
| Exploratory scripts | one-off analysis before promotion to `../../06_project_operations/scripts/` |

Promote repeatable analysis code to `../../06_project_operations/scripts/` once the workflow stabilizes.
