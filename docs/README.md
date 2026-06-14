# Docs

Project-level design logic, repository guidance, and scientific decision records live here.

## Core Documents

| File | Purpose |
|---|---|
| `candidate_design_rationale.md` | Why the 10 peptide candidates were designed |
| `repository_guide.md` | How the repository is organized |
| `md_to_pmf_workflow.md` | Why production MD and clustering precede umbrella sampling |

## Decision Flow

```mermaid
flowchart LR
    A["Literature motifs"] --> B["Candidate design"]
    B --> C["Computational workflow"]
    C --> D["MD/PMF results"]
    D --> E["Wet-lab prioritization"]
```

Use this folder for notes that explain choices, not for bulky raw data or generated trajectories.
