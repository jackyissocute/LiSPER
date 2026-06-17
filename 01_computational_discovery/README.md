# 01 Computational Discovery

This stage contains the in silico LiSPER discovery workflow: candidate sequences, structure prediction, CHARMM-GUI system construction, GROMACS simulations, umbrella sampling, PMF analysis, data, and analysis outputs.

## Current State

The active computational library is the final **8-candidate** panel in `sequences/candidates.tsv`. Six candidates have ESMFold assets under their final names. Three candidates also have matched LiCl/NaCl CHARMM-GUI systems available. The remaining near-term work is two ESMFold uploads plus five matched CHARMM-GUI system pairs.

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
```

## Contents

| Folder | Purpose |
|---|---|
| `sequences/` | Candidate peptide sequences and metadata. |
| `esmfold/` | ESMFold predictions and CHARMM-GUI-ready PDBs. |
| `charmm-gui/` | LiCl and NaCl system-builder outputs. |
| `md/` | GROMACS minimization, equilibration, production, clustering, and remote logs. |
| `umbrella/` | Umbrella sampling setup and future windows. |
| `pmf/` | PMF and Delta G analysis. |
| `analysis/` | Cross-stage computational interpretation and ranking work. |
| `data/` | Raw and processed computational data not tied to one workflow folder. |
