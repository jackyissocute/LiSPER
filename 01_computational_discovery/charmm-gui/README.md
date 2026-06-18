# CHARMM-GUI

This folder will store CHARMM-GUI Solution Builder outputs for the active 8-candidate LiSPER library.

## Current State

CHARMM-GUI systems are now GROMACS-ready for all eight candidates in both LiCl and NaCl conditions. Eight safe PDBs are prepared in:

`01_computational_discovery/esmfold/charmm_gui_pdb/`

LiD3-Core replacement ESMFold files passed sequence QC and are now active.

## Conditions

| Condition | Status | Next action |
|---|---|---|
| LiCl | 8/8 GROMACS-ready | Launch/monitor LiCl MD setup |
| NaCl | 8/8 GROMACS-ready | Add `LiN3-Core` to NaCl setup results |

## Reuse Note

Keep active folder names aligned with the final 8-candidate library. Quiet provenance is tracked in `completed_assets_manifest.tsv`.
