# Sequences

This folder defines the first-round LiSPER peptide library.

## Files

| File / Folder | Purpose |
|---|---|
| `candidates.tsv` | Ranked candidate metadata, design logic, and recommended-start flag |
| `candidates.fasta` | FASTA input for structure prediction |
| `candidates/` | Individual sequence records |

## Library Overview

```mermaid
flowchart TD
    accTitle: Candidate Design Inputs
    accDescr: LiSPER candidate sequences combine lithium-binding motif precedent, IDP-like flexibility, and limited acidic oxygen donors before Li versus Na screening.

    lbp["LBP motifs<br/>GPGNP / GPGDP"]
    idp["IDP-like<br/>flexibility"]
    donors["Limited acidic<br/>oxygen donors"]
    candidates["LiSPER<br/>candidates"]
    screen["Li+ vs Na+<br/>screen"]

    lbp --> candidates
    idp --> candidates
    donors --> candidates
    candidates --> screen
```

## Recommended Starting Subset

| Candidate | Why It Matters |
|---|---|
| `LiD3-1` | Strongest motif-repeat candidate |
| `LiND-1` | Balances original and improved LBP motifs |
| `IDP-Li-1` | Compact IDP-like acidic shell |
| `LowCharge-Li` | Selectivity risk-control design |
| `Control-Negative` | Weak/neutral binding control |

Discarded historical sequences should remain outside the primary library unless explicitly used for comparison.
