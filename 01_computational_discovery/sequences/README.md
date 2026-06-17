# Sequences

This folder defines the active 8-candidate LiSPER peptide library.

## Files

| File / Folder | Purpose |
|---|---|
| `candidates.tsv` | Ranked 8-candidate metadata, design logic, and reuse status |
| `candidates.fasta` | FASTA input for ESMFold |
| `reuse_map.tsv` | Links sequence-identical revised candidates to legacy 10-candidate assets |
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

## Reuse Rule

`LiD3-Flex`, `LiND-Hybrid`, and `LiLC-1` are sequence-identical to old `LiD3-1`, `LiND-1`, and `LowCharge-Li`, respectively. Their old assets may be reused only with explicit provenance.

The active project should otherwise behave as an 8-candidate library. Retired 10-candidate materials live under:

`archive/legacy_10_candidate_library/`
