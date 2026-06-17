# ESMFold

This folder stores structure-prediction outputs for the active 8-candidate LiSPER library.

## Current State

The 8-candidate library has been locked. ESMFold assets are available for all 8 candidates under their final names.

Current ESMFold intake state:

| Candidate group | Count | State |
|---|---|
| ESMFold assets done | 8 | PDB/PAE/plots available under final names |
| New uploads needed | 0 | ESMFold intake complete |

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

Next, use the safe PDB names in `charmm_gui_pdb/` to complete the remaining CHARMM-GUI LiCl and NaCl systems.
