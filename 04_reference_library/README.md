# 04 Reference Library

This folder is the **external evidence base** for LiSPER.

Use it for papers, patents, citation exports, review notes, and source metadata that support the project across multiple stages. It is not a place for generated simulation data, active wet-lab protocols, or manuscript drafts.

```mermaid
flowchart TD
    accTitle: Reference Library Role
    accDescr: External papers, reviews, and patents are collected in the reference library and used to support design, simulation, experimental, and translation decisions.

    sources["External sources<br/>papers, reviews, patents"]
    library["Reference<br/>library"]
    design["Design<br/>rationale"]
    simulation["Simulation<br/>assumptions"]
    controls["Experimental<br/>controls"]
    translation["Translation<br/>context"]

    sources --> library
    library --> design
    library --> simulation
    library --> controls
    library --> translation

    classDef source fill:#0F172A,stroke:#64748B,stroke-width:2px,color:#E2E8F0
    classDef library fill:#0F172A,stroke:#38BDF8,stroke-width:2px,color:#E2E8F0
    classDef use fill:#0F172A,stroke:#22C55E,stroke-width:2px,color:#E2E8F0
    class sources source
    class library library
    class design,simulation,controls,translation use
```

## Current Collections

| Folder | Focus | Used For |
|---|---|---|
| [`Track A_Peptide Assay/`](Track%20A_Peptide%20Assay/) | Ordered synthetic peptide Li⁺/Na⁺ assay literature (beads, dialysis, ICP, QC/TFA) | Designing Track A wet protocols and interpreting vendor-peptide experiments |
| [`protein_design/IDP/`](protein_design/IDP/) | Intrinsically disordered proteins and flexible metal-binding regions | Explaining LiSPER flexibility, ensemble behavior, and IDP-inspired design choices |
| [`protein_design/LBP/`](protein_design/LBP/) | Lithium-binding peptides, surface display, and lithium recovery | Motif precedent, Li-binding context, and comparison to published lithium-capture biology |

## Boundary Rule

| Material | Put It Here? | Better Location |
|---|---:|---|
| Foundational papers used by multiple stages | Yes | This folder |
| Citation exports and source metadata | Yes | This folder |
| Reading notes that summarize external literature | Yes | This folder or the relevant study folder |
| Surface-display host-selection review outputs | No | `../02_experimental_validation/track_B_surface_display/research/surface_display_host_selection/` |
| Deployment architecture review outputs | No | `../03_industrial_translation/deployment_architecture/` |
| Figures for papers, decks, or reports | No | `../05_outputs_and_communication/figures/` |
| Scripts, repo guides, or intake notes | No | `../06_project_operations/` |

## How Literature Feeds LiSPER

```mermaid
flowchart TD
    accTitle: Literature To Design
    accDescr: LBP and IDP literature provide motif and flexibility logic that feeds LiSPER candidate design, simulation hypotheses, and validation priorities.

    lbp["LBP<br/>literature"]
    idp["IDP<br/>literature"]
    motifs["Motif<br/>precedent"]
    flexibility["Flexible<br/>architecture"]
    design["Candidate<br/>design"]
    hypotheses["MD and PMF<br/>hypotheses"]
    validation["Validation<br/>priorities"]

    lbp --> motifs
    idp --> flexibility
    motifs --> design
    flexibility --> design
    design --> hypotheses
    hypotheses --> validation
```

Keep this area source-centered: a future reader should be able to ask, "What evidence did LiSPER rely on?" and find the answer here.
