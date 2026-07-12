# Sequences

This folder defines the active 8-candidate LiSPER peptide library.

## Files

| File / Folder | Purpose |
|---|---|
| `candidates.tsv` | Ranked 8-candidate metadata, design logic, and intake status |
| `candidates.fasta` | FASTA input for ESMFold |
| `reuse_map.tsv` | Internal exact-match traceability for completed upstream assets |
| `candidates/` | Individual sequence records |

## Active Library

| Rank | Candidate | Role |
|---:|---|---|
| 1 | `LiD3-Core` | Linker-free GPGDP trimer benchmark |
| 2 | `LiD3-Flex` | Flexible GSG-spaced GPGDP trimer |
| 3 | `LiND-Hybrid` | GPGNP/GPGDP hybrid |
| 4 | `LiLC-1` | Lower-charge mixed donor control |
| 5 | `LiDS-1` | Asp/Gly Li+/Na+ geometry probe |
| 6 | `LiDA-1` | Ala-supported Asp pocket probe |
| 7 | `LiN3-Core` | GPGNP trimer benchmark |
| 8 | `LiA3-Ref` | GPGAP low-donor reference |

## Completed Upstream Assets

`LiD3-Flex`, `LiND-Hybrid`, and `LiLC-1` already have upstream computational assets available under their final candidate names.

The active project should read and operate as a final 8-candidate library. Superseded working materials are kept outside the active workflow under:

`archive/` (prior library snapshot)
