# ESMFold

Store ESMFold structure-prediction inputs and outputs here.

Current layout:

- `inputs/`: sequence files used for ESMFold prediction.
- `raw_zips/`: original downloaded ESMFold zip files.
- `runs/`: canonical extracted ESMFold run folder for each candidate.
- `pdb/`: flat set of CHARMM-GUI-ready PDB files, one per candidate.
- `charmm_gui_pdb/`: upload-safe PDB copies with lowercase alphanumeric filenames.
- `pae/`: flat set of predicted aligned error matrices.
- `plots/`: flat set of ESMFold confidence plots.
- `manifest.tsv`: sequence validation and file-location manifest.

Each predicted structure should remain traceable to a candidate ID in `../sequences/candidates.tsv`.

## CHARMM-GUI Handoff

Upload the PDB files from `charmm_gui_pdb/` to CHARMM-GUI Solution Builder.

These copies avoid hyphens, underscores, spaces, and mixed capitalization in filenames. The mapping back to project candidate IDs is stored in `charmm_gui_pdb/filename_mapping.tsv`.

Recommended first subset:

- `charmm_gui_pdb/lid31.pdb`
- `charmm_gui_pdb/lind1.pdb`
- `charmm_gui_pdb/idpli1.pdb`
- `charmm_gui_pdb/lowchargeli.pdb`
- `charmm_gui_pdb/controlnegative.pdb`

Complete first-round set:

- `charmm_gui_pdb/lid31.pdb`
- `charmm_gui_pdb/lind1.pdb`
- `charmm_gui_pdb/idpli1.pdb`
- `charmm_gui_pdb/idpli2.pdb`
- `charmm_gui_pdb/lowchargeli.pdb`
- `charmm_gui_pdb/lid2idp.pdb`
- `charmm_gui_pdb/strongbindli.pdb`
- `charmm_gui_pdb/softcageli.pdb`
- `charmm_gui_pdb/idprichli.pdb`
- `charmm_gui_pdb/controlnegative.pdb`

For first-round free-energy comparison, create separate downstream systems for each candidate:

- peptide + LiCl
- peptide + NaCl

Do not use mixed Li+/Na+ systems for first-round umbrella sampling.

## Validation Notes

All 10 original ESMFold zip files were decompressed into 10 canonical run folders. All PDB files in `pdb/` were checked against `../sequences/candidates.tsv`; each PDB sequence matched the expected candidate sequence.

The `ptm` value in ESMFold filenames is low for these short, flexible peptides and should not be interpreted as a final design score. Use the structures as starting conformations for simulation, then evaluate Li+/Na+ selectivity through paired MD, umbrella sampling, PMF, and Delta Delta G analysis.
