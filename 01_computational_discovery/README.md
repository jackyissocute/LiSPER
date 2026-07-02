# 01 Computational Discovery

This stage contains the in silico LiSPER discovery workflow: candidate sequences, structure prediction, CHARMM-GUI system construction, GROMACS simulations, umbrella sampling, PMF analysis, data, and analysis outputs.

## Current State

The active computational library is the final **8-candidate** panel in `sequences/candidates.tsv`. ESMFold intake and matched LiCl/NaCl CHARMM-GUI setup are complete for all eight candidates. Current progress reporting focuses on 20 ns production/clustering handoff, refined umbrella sampling, WHAM/PMF QC, and paired Delta Delta G promotion.

Status colors should follow the dashboard palette: complete `#22C55E`, running `#38BDF8`, queued `#FACC15`, QC review `#A78BFA`, warning/repair/failed `#FB7185`/`#EF4444`, and planned `#64748B`. LiCl and NaCl colors are identity accents only: LiCl `#818CF8`, NaCl `#2DD4BF`.

```mermaid
flowchart TD
    accTitle: Computational Discovery Folders
    accDescr: The computational discovery folder moves from candidate sequences through structure prediction, system setup, molecular dynamics, umbrella sampling, PMF analysis, and final interpretation.

    sequences["sequences/"]
    esmfold["esmfold/"]
    charmm_gui["charmm-gui/"]
    md["md/"]
    umbrella["umbrella/"]
    pmf["pmf/"]
    analysis["analysis/"]

    sequences --> esmfold
    esmfold --> charmm_gui
    charmm_gui --> md
    md --> umbrella
    umbrella --> pmf
    pmf --> analysis

    classDef planned fill:#0F172A,stroke:#64748B,stroke-width:2px,color:#E2E8F0
    classDef running fill:#0F172A,stroke:#38BDF8,stroke-width:2px,color:#E2E8F0
    classDef qc fill:#0F172A,stroke:#A78BFA,stroke-width:2px,color:#E2E8F0
    classDef complete fill:#0F172A,stroke:#22C55E,stroke-width:2px,color:#E2E8F0
    class sequences,esmfold,charmm_gui,md complete
    class umbrella running
    class pmf qc
    class analysis planned
```

## Contents

| Folder | Purpose |
|---|---|
| `sequences/` | Candidate peptide sequences and metadata. |
| `esmfold/` | ESMFold predictions and CHARMM-GUI-ready PDBs. |
| `charmm-gui/` | LiCl and NaCl system-builder outputs. |
| `md/` | GROMACS minimization, equilibration, 20 ns production, structural clustering, representative extraction, and MD-stage remote logs. |
| `umbrella/` | Umbrella sampling drivers, v2 reaction-coordinate setup, pull stages, window equilibration/production, synced window outputs, and umbrella diagnostics. |
| `pmf/` | WHAM, PMF QC, bootstrap/time-slice checks, Delta G estimates, and paired Delta Delta G analysis. |
| `analysis/` | Cross-stage computational interpretation and ranking work. |
| `data/` | Raw and processed computational data not tied to one workflow folder. |
