# Docs

Project-level design logic, repository guidance, and scientific decision records live here.

## Core Documents

| File | Purpose |
|---|---|
| `candidate_design_rationale.md` | Why the final 8 peptide candidates were designed |
| `readme_polish_report_2026-06-15.md` | What changed during the repository-wide README polish pass |
| `../../01_computational_discovery/free_energy/COMPUTATIONAL_VALIDATION_STRATEGY.md` | Current computational estimands and method |

## Decision Flow

```mermaid
flowchart TD
    accTitle: Decision Documentation Flow
    accDescr: Project documentation records how literature motifs inform candidate design, computational workflow, free-energy results, and wet-lab prioritization.

    literature["Literature<br/>motifs"]
    design["Candidate<br/>design"]
    workflow["Computational<br/>workflow"]
    results["MD/alchemical free-energy<br/>results"]
    wetlab["Wet-lab<br/>prioritization"]

    literature --> design
    design --> workflow
    workflow --> results
    results --> wetlab
```

Use this folder for notes that explain choices, not for bulky raw data or generated trajectories.
