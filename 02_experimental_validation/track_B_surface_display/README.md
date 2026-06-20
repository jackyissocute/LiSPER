# Track B: Surface Display Validation

Track B is the main follow-up wet-lab engineering stage after ordered synthetic peptide binding assays identify the best LiSPER candidates.

It answers the biological-deployment question:

> Can LiSPER remain functional when displayed on a biological surface?

This track uses future eCPX surface-display constructs to test surface expression, surface accessibility, whole-cell Li+ capture, Li+/Na+ selectivity, condition optimization, and capture-release-reuse.

Track B is no longer meant to prove peptide-intrinsic binding from scratch. Track A ordered-peptide statistics should do that first. Track B asks whether the best peptides can become a practical bacterial capture material.

## Contents

| Folder | Purpose |
|---|---|
| `planning/` | Decision-ready Track B study plans, module priorities, and professor discussion brief. |
| `plasmids/` | Placeholder for future eCPX construct designs. No eCPX plasmids are designed yet. |
| `protocols/` | Track B protocol overview and future display workflow protocols. |
| `assays/surface_display_assays/` | Whole-cell Li+/Na+ binding and selectivity assay design package. |
| `research/surface_display_host_selection/` | Host, environment, and display-platform technology assessment. |

## Start Here

1. Read `planning/integrated_surface_display_optimization_plan.md`.
2. Use `planning/professor_discussion_brief.md` to discuss scope and priorities with the professor.
3. Read `protocols/00_track_B_surface_display_protocol_overview.md`.
4. Read `assays/surface_display_assays/whole_cell_LiNa_binding_assay_plan.md`.
5. Use `assays/surface_display_assays/construct_design_implications.md` before any future eCPX plasmid design.

## Current Planning Position

Track B should follow synthetic peptide screening rather than replace it:

```text
synthetic peptide Li/Na ranking
↓
top 2-3 candidates plus controls
↓
eCPX surface-display proof
↓
condition optimization
↓
capture-release-reuse testing
↓
optional strain comparison
```

## Main Study Goal

The strongest Track B study is not just "display a peptide on cells." The goal is to identify:

- the best displayed LiSPER candidate,
- the best assay/operating condition,
- the best normalization strategy,
- whether capture can be reversed and reused,
- whether surface-display performance supports a low-cost Bio-DLE direction.
