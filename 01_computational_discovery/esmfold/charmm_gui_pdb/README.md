# CHARMM-GUI-Safe PDB Copies

Upload these PDB files to CHARMM-GUI.

## Filename Rules

| Rule | Applied |
|---|---|
| lowercase letters | yes |
| numbers allowed | yes |
| hyphens | no |
| underscores | no |
| spaces | no |
| extension | `.pdb` |

## Formatting Normalization

| Edit | Reason |
|---|---|
| Remove nonstandard ESMFold headers | CHARMM-GUI compatibility |
| One chain ID, `A` | Prevent accidental split-chain systems |
| Sequential residue numbering | Cleaner topology generation |
| Backbone atoms first | Standard protein formatting |
| Explicit `TER` and `END` | PDB completeness |

Use `filename_mapping.tsv` to map upload-safe filenames back to project candidate IDs.

Recommended first uploads: `lid31.pdb`, `lind1.pdb`, `idpli1.pdb`, `lowchargeli.pdb`, `controlnegative.pdb`.
