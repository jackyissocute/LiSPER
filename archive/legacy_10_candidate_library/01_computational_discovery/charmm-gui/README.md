# CHARMM-GUI Systems

This folder stores CHARMM-GUI Solution Builder outputs for the paired LiSPER ion systems.

```mermaid
flowchart TD
    accTitle: CHARMM-GUI System Setup
    accDescr: ESMFold peptide structures are prepared in CHARMM-GUI as parallel LiCl and NaCl GROMACS systems for remote molecular dynamics.

    pdb["ESMFold<br/>PDB"]
    builder["CHARMM-GUI<br/>Solution Builder"]
    li_system["LiCl<br/>system"]
    na_system["NaCl<br/>system"]
    inputs["GROMACS<br/>inputs"]
    remote_md["Remote<br/>MD"]

    pdb --> builder
    builder --> li_system
    builder --> na_system
    li_system --> inputs
    na_system --> inputs
    inputs --> remote_md
```

## Organized Conditions

| Condition | Folder | QC Status | MD Status |
|---|---|---|---|
| LiCl | `li_cl/` | 10/10 ready | Minimization and equilibration complete |
| NaCl | `na_cl/` | 10/10 ready | Minimization and equilibration complete |

## Shared Setup

| Setting | Value |
|---|---|
| Force field | CHARMM36m |
| Water model | TIP3P |
| Box setup | Cubic, 20 A padding |
| Li+ residue name | `LIT` |
| Na+ residue name | `SOD` |
| Cl- residue name | `CLA` |

## Folder Pattern

| Path | Contents |
|---|---|
| `<condition>/raw_archives/` | Original CHARMM-GUI `.tgz` downloads, renamed by candidate |
| `<condition>/systems/` | Extracted CHARMM-GUI output, one folder per candidate |
| `<condition>/metadata/` | Archive mapping, upload order, and QC manifest |
| `<condition>/systems/replaced/` | Preserved superseded setup folders |

Mixed Li+/Na+ competition systems are intentionally excluded from the first-round PMF workflow. The first comparison uses separate LiCl and NaCl systems.
