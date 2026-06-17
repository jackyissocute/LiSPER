# ESMFold

This folder stores structure-prediction outputs for the active 8-candidate LiSPER library.

## Current State

The 8-candidate library has been locked, and the workflow is waiting for the new ESMFold result zip files. Upload those zip files into the repository-level `inbox/` folder first.

Three revised candidates are sequence-identical to legacy candidates and may reuse old ESMFold outputs if needed:

| Revised candidate | Legacy candidate |
|---|---|
| `LiD3-Flex` | `LiD3-1` |
| `LiND-Hybrid` | `LiND-1` |
| `LiLC-1` | `LowCharge-Li` |

The remaining five candidates require new ESMFold outputs.

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
| `reuse_map.tsv` | Legacy ESMFold outputs that may be reused |

## Next Step

After the 8 ESMFold zip files are uploaded, validate sequence identity, normalize PDB filenames for CHARMM-GUI, and update `manifest.tsv`.
