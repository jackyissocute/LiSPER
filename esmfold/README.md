# ESMFold

Store ESMFold structure-prediction inputs and outputs here.

Current layout:

- `inputs/`: sequence files used for ESMFold prediction.
- `raw_zips/`: original downloaded ESMFold zip files.
- `runs/`: canonical extracted ESMFold run folder for each candidate.
- `pdb/`: flat set of CHARMM-GUI-ready PDB files, one per candidate.
- `pae/`: flat set of predicted aligned error matrices.
- `plots/`: flat set of ESMFold confidence plots.
- `manifest.tsv`: sequence validation and file-location manifest.

Each predicted structure should remain traceable to a candidate ID in `../sequences/candidates.tsv`.

## CHARMM-GUI Handoff

Upload the PDB files from `pdb/` to CHARMM-GUI Solution Builder.

Recommended first subset:

- `pdb/LiD3-1.pdb`
- `pdb/LiND-1.pdb`
- `pdb/IDP-Li-1.pdb`
- `pdb/LowCharge-Li.pdb`
- `pdb/Control-Negative.pdb`

Complete first-round set:

- `pdb/LiD3-1.pdb`
- `pdb/LiND-1.pdb`
- `pdb/IDP-Li-1.pdb`
- `pdb/IDP-Li-2.pdb`
- `pdb/LowCharge-Li.pdb`
- `pdb/LiD2-IDP.pdb`
- `pdb/StrongBind-Li.pdb`
- `pdb/SoftCage-Li.pdb`
- `pdb/IDP-Rich-Li.pdb`
- `pdb/Control-Negative.pdb`

For first-round free-energy comparison, create separate downstream systems for each candidate:

- peptide + LiCl
- peptide + NaCl

Do not use mixed Li+/Na+ systems for first-round umbrella sampling.

## Validation Notes

All 10 original ESMFold zip files were decompressed into 10 canonical run folders. All PDB files in `pdb/` were checked against `../sequences/candidates.tsv`; each PDB sequence matched the expected candidate sequence.

The `ptm` value in ESMFold filenames is low for these short, flexible peptides and should not be interpreted as a final design score. Use the structures as starting conformations for simulation, then evaluate Li+/Na+ selectivity through paired MD, umbrella sampling, PMF, and Delta Delta G analysis.
