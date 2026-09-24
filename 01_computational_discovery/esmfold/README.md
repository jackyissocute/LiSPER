# ESMFold

This folder stores structure-prediction outputs for the active 8-candidate LiSPER library.

## Current State

The 8-candidate library has been locked. All eight ESMFold structures are now upload-ready under their final names.

Current ESMFold intake state:

| Candidate group | Count | State |
|---|---|
| ESMFold assets ready | 8 | PDB/PAE/plots available under final names |
| Replacement needed | 0 | LiD3-Core replacement passed sequence QC |

## Layout

| Path | Contents |
|---|---|
| `inputs/` | Active 8-candidate FASTA and metadata |
| `raw_zips/` | Incoming ESMFold zip files after inbox triage |
| `runs/` | Extracted run folder for each candidate |
| `pdb/` | Candidate-named PDB collection |
| `charmm_gui_pdb/` | Upload-safe lowercase PDB names |
| `pae/` | Predicted aligned error matrices |
| `plots/` | ESMFold confidence plots |
| `manifest.tsv` | Intake and validation status |
| `completed_assets_manifest.tsv` | Quiet provenance for candidates with completed upstream assets |
| `reuse_map.tsv` | Internal exact-match traceability |

The LiN3-Core replacement passed sequence QC; all eight LiCl and NaCl systems have since completed the downstream MD and PMF workflow. These models were starting structures, not claims of a single stable peptide conformation.

## Duplication Policy

The ESMFold folder intentionally keeps a few derived views of the same prediction:

| View | Why it stays |
|---|---|
| `runs/` | Original extracted ESMFold job folders |
| `pdb/`, `pae/`, `plots/` | Candidate-named canonical working copies |
| `charmm_gui_pdb/` | Upload-safe lowercase PDB names for CHARMM-GUI |
| `charmm_gui_pdb_original_esmfold_format/` | Historical upload-format reference |
| `raw_zips/` | Original downloaded archives |

Confirmed duplicate prior raw ZIPs were removed after content comparison; the remaining copies have distinct workflow roles.
