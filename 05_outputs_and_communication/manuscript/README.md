# Manuscript

Drafts, outlines, tables, figure captions, and supplementary-material planning.

## Story Arc

```mermaid
flowchart TD
    accTitle: Manuscript Story Arc
    accDescr: The manuscript story moves from design rationale through simulation workflow and Li over Na selectivity results into experimental validation.

    rationale["Design<br/>rationale"]
    workflow["Simulation<br/>workflow"]
    results["Li/Na<br/>results"]
    validation["Experimental<br/>validation"]

    rationale --> workflow
    workflow --> results
    results --> validation
```

Use this folder for publication-style organization. Keep raw analysis and trajectories in `../../01_computational_discovery/analysis/`, `../../01_computational_discovery/md/`, `../../01_computational_discovery/umbrella/`, and `../../01_computational_discovery/pmf/`.

Decks and milestone summaries belong one level up in `../presentations/` and `../milestones/`.
