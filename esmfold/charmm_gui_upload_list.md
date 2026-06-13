# CHARMM-GUI Upload List

Use these PDB files for CHARMM-GUI Solution Builder.

## Recommended Starting Subset

| Rank | Candidate | PDB |
| --- | --- | --- |
| 1 | LiD3-1 | `pdb/LiD3-1.pdb` |
| 2 | LiND-1 | `pdb/LiND-1.pdb` |
| 3 | IDP-Li-1 | `pdb/IDP-Li-1.pdb` |
| 5 | LowCharge-Li | `pdb/LowCharge-Li.pdb` |
| 10 | Control-Negative | `pdb/Control-Negative.pdb` |

## Complete First-Round Library

| Rank | Candidate | PDB |
| --- | --- | --- |
| 1 | LiD3-1 | `pdb/LiD3-1.pdb` |
| 2 | LiND-1 | `pdb/LiND-1.pdb` |
| 3 | IDP-Li-1 | `pdb/IDP-Li-1.pdb` |
| 4 | IDP-Li-2 | `pdb/IDP-Li-2.pdb` |
| 5 | LowCharge-Li | `pdb/LowCharge-Li.pdb` |
| 6 | LiD2-IDP | `pdb/LiD2-IDP.pdb` |
| 7 | StrongBind-Li | `pdb/StrongBind-Li.pdb` |
| 8 | SoftCage-Li | `pdb/SoftCage-Li.pdb` |
| 9 | IDP-Rich-Li | `pdb/IDP-Rich-Li.pdb` |
| 10 | Control-Negative | `pdb/Control-Negative.pdb` |

## CHARMM-GUI Setup Reminder

For each candidate, prepare two separate systems:

- peptide + LiCl
- peptide + NaCl

Use the project defaults from the root README:

- water model: TIP3P
- force field: CHARMM36m
- box: cubic with 20 A padding
