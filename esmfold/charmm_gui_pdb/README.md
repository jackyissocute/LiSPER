# CHARMM-GUI-Safe PDB Copies

Use these files for CHARMM-GUI upload.

Filename rule used here:

- lowercase letters only
- numbers allowed
- no hyphens
- no underscores
- no spaces
- `.pdb` extension

These files are normalized copies of the corresponding PDB files in `../pdb/`. The original coordinates are retained, while the upload copies use CHARMM-GUI-friendly formatting:

- nonstandard ESMFold header lines removed
- one chain ID, `A`
- sequential residue numbering
- standard residue atom ordering with backbone atoms first
- explicit `TER` and `END` records

Use `filename_mapping.tsv` to map each upload-safe filename back to the project candidate ID.

Recommended first uploads:

- `lid31.pdb`
- `lind1.pdb`
- `idpli1.pdb`
- `lowchargeli.pdb`
- `controlnegative.pdb`
