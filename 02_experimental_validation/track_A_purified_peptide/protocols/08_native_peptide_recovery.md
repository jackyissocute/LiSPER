# 08 Native LiSPER Peptide Recovery Protocol

## Purpose

Separate native untagged LiSPER peptide from His6-SUMO, His-tagged protease, uncleaved fusion, and cleavage-buffer components.

## Key Constraint

LiSPER peptides are very small, approximately 1-2 kDa. Standard protein recovery assumptions often fail.

## Recommended First Recovery Logic

Use post-cleavage Ni-NTA subtraction:

- His6-SUMO binds Ni-NTA.
- His-tagged SUMO protease binds Ni-NTA if applicable.
- Uncleaved His6-SUMO-LiSPER binds Ni-NTA.
- Untagged native LiSPER peptide should appear in the flow-through.

## Step-by-Step Workflow

1. Equilibrate small Ni-NTA resin volume.
2. Apply cleavage reaction to resin.
3. Collect flow-through carefully; this is the expected native peptide fraction.
4. Wash resin with low-imidazole or cleavage-compatible buffer.
5. Collect wash fractions separately.
6. Elute resin to check retained His-tagged material.
7. Analyze retained proteins by gel.
8. Send flow-through/wash fractions for peptide QC if possible.

## Optional Cleanup

| Method | Use | Caution |
|---|---|---|
| C18 SPE | Desalt/concentrate peptide | Requires organic solvent handling and method development. |
| HPLC | Best purity assessment and cleanup | Requires instrument access. |
| Lyophilization | Concentrate peptide | Only after volatile/compatible buffer cleanup. |
| MWCO filters | Generally risky | Many filters will not retain 1-2 kDa peptides. |

## Common Failure Modes

| Problem | Likely cause | Solution |
|---|---|---|
| Peptide lost | stuck to resin/tube/filter | Use low-bind tubes; collect all fractions; avoid wrong MWCO. |
| SUMO contamination in flow-through | overloaded resin or poor binding | Increase resin or binding time. |
| No detectable peptide by gel | small peptide expected | Use MS/HPLC. |
| Low recovery | too many handling steps | Simplify workflow and quantify each fraction. |

## Records To Keep

- Cleavage reaction ID.
- Resin volume.
- Flow-through volume.
- Wash volumes.
- Fraction labels.
- QC submission IDs.

