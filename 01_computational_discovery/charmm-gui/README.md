# CHARMM-GUI

This folder will store CHARMM-GUI Solution Builder outputs for the active 8-candidate LiSPER library.

## Current State

CHARMM-GUI NaCl systems are GROMACS-ready for all eight candidates. LiCl systems are GROMACS-ready for seven candidates; `LiN3-Core` LiCl is the only remaining CHARMM-GUI system still needed. Eight safe PDBs are prepared in:

`01_computational_discovery/esmfold/charmm_gui_pdb/`

LiD3-Core replacement ESMFold files passed sequence QC and are now active.

## Conditions

| Condition | Status | Next action |
|---|---|---|
| LiCl | 7/8 GROMACS-ready | Build `LiN3-Core` LiCl |
| NaCl | 8/8 GROMACS-ready | Add `LiN3-Core` to the next NaCl MD queue |

## Reuse Note

Keep active folder names aligned with the final 8-candidate library. Quiet provenance is tracked in `completed_assets_manifest.tsv`.
