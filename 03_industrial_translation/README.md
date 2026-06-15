# 03 Industrial Translation

This stage contains LiSPER technology-translation studies: immobilized peptide deployment architecture, support-material analysis, packed-bed process design, and Bio-DLE reports.

```mermaid
flowchart TD
    accTitle: Industrial Translation Path
    accDescr: Industrial translation starts from validated LiSPER peptides, evaluates deployment architecture, selects immobilization media, and moves toward packed-bed Bio-DLE.

    peptide["Validated<br/>LiSPER peptide"]
    architecture["Deployment<br/>architecture"]
    immobilization["Immobilization<br/>strategy"]
    media["Resin or bead<br/>capture media"]
    column["Packed-bed<br/>Bio-DLE"]

    peptide --> architecture
    architecture --> immobilization
    immobilization --> media
    media --> column
```

## Contents

| Folder | Purpose |
|---|---|
| `deployment_architecture/` | Immobilization, support-material, and process-architecture assessment. |

The current translation hypothesis is that purified immobilized LiSPER peptide in a packed-bed column is the most realistic industrial endpoint, with inactivated display systems and magnetic beads as bridge technologies after validation.
