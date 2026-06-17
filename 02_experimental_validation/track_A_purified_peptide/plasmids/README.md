# Plasmids

This folder is the active plasmid-design workspace for the **final 8-candidate** LiSPER library.

## Current State

The old 10-candidate His6-SUMO construct package has been archived under:

```text
archive/legacy_10_candidate_library/02_experimental_validation/track_A_purified_peptide/plasmids/
```

Those files are preserved for reference only. They should not be treated as the current vendor-ready set because the active candidate library has changed.

## Active Rule

Regenerate plasmid and codon-optimization files only after the final 8-candidate computational intake is stable.

Planned order:

```text
final 8 candidates
-> ESMFold intake
-> CHARMM-GUI / MD prioritization
-> codon optimization
-> His6-SUMO construct design
-> GenBank / SnapGene / vendor package
```

## Expected Final 8

| Candidate | Plasmid status |
|---|---|
| `LiD3-Core` | Pending codon optimization |
| `LiD3-Flex` | Pending codon optimization |
| `LiND-Hybrid` | Pending codon optimization |
| `LiLC-1` | Pending codon optimization |
| `LiDS-1` | Pending codon optimization |
| `LiDA-1` | Pending codon optimization |
| `LiN3-Core` | Pending codon optimization |
| `LiA3-Ref` | Pending codon optimization |

## Vector Map

| Path | Purpose |
|---|---|
| `vector_maps/pET28a_plus.dna` | Source pET-28a(+) SnapGene vector map used as the backbone reference |

## Notes

Exact-sequence reuse from the old candidate set may help with design review, but final plasmid files should use the final candidate names and final 8-candidate manifest.
