# CHARMM-GUI

This folder will store CHARMM-GUI Solution Builder outputs for the active 8-candidate LiSPER library.

## Current State

CHARMM-GUI LiCl systems are available for three final candidates. NaCl systems are imported for all eight candidates, with seven GROMACS-ready and one on QC hold because the downloaded archive lacks the `gromacs/` input folder. Eight safe PDBs are prepared in:

`01_computational_discovery/esmfold/charmm_gui_pdb/`

LiD3-Core replacement ESMFold files passed sequence QC and are now active.

## Conditions

| Condition | Status | Next action |
|---|---|---|
| LiCl | 3/8 systems done | Build the five remaining LiCl systems |
| NaCl | 7/8 GROMACS-ready; 1 QC hold | Re-download or repair the `LiN3-Core` NaCl GROMACS archive |

## Reuse Note

Keep active folder names aligned with the final 8-candidate library. Quiet provenance is tracked in `completed_assets_manifest.tsv`.
