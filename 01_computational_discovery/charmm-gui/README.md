# CHARMM-GUI

This folder will store CHARMM-GUI Solution Builder outputs for the active 8-candidate LiSPER library.

## Current State

The old 10-candidate CHARMM-GUI outputs were archived under:

`archive/legacy_10_candidate_library/01_computational_discovery/charmm-gui/`

The active 8-candidate CHARMM-GUI stage has not started yet. It should begin only after ESMFold PDBs are prepared in:

`01_computational_discovery/esmfold/charmm_gui_pdb/`

## Conditions

| Condition | Status | Next action |
|---|---|---|
| LiCl | Awaiting revised ESMFold PDBs | Upload each safe PDB to CHARMM-GUI Solution Builder |
| NaCl | Awaiting revised ESMFold PDBs | Build matched NaCl systems after LiCl setup logic is confirmed |

## Reuse Note

`LiD3-Flex`, `LiND-Hybrid`, and `LiLC-1` are sequence-identical to legacy candidates. Their old CHARMM-GUI materials may be used as provenance or emergency fallback, but the active workflow should prefer regenerated systems from the final 8-candidate ESMFold intake.
