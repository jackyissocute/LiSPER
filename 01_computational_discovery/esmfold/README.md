# ESMFold

This folder stores structure-prediction outputs for the active 8-candidate LiSPER library.

## Current State

The 8-candidate library has been locked. Seven ESMFold structures are upload-ready under their final names. LiD3-Core needs a replacement ESMFold result after sequence QC.

Current ESMFold intake state:

| Candidate group | Count | State |
|---|---|
| ESMFold assets ready | 7 | PDB/PAE/plots available under final names |
| Replacement needed | 1 | LiD3-Core upload failed sequence QC |

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

## Next Step

Next, upload a replacement LiD3-Core ESMFold result. The other safe PDB names in `charmm_gui_pdb/` can be used to complete the remaining CHARMM-GUI LiCl and NaCl systems.
