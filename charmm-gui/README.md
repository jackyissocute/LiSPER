# CHARMM-GUI

Store CHARMM-GUI system setup files here.

Current organized batch:

- `li_cl/`: CHARMM-GUI Solution Builder outputs for peptide + LiCl systems.
- `na_cl/`: CHARMM-GUI Solution Builder outputs for peptide + NaCl systems.
- `li_cl/raw_archives/`: original downloaded `.tgz` archives, renamed by candidate.
- `li_cl/systems/`: extracted CHARMM-GUI outputs, one folder per candidate.
- `li_cl/metadata/`: input order image, archive mapping, and QC manifest.

First-round systems should be prepared separately for each peptide and ion condition:

- protein + LiCl
- protein + NaCl

Project defaults:

- water model: TIP3P
- force field: CHARMM36m
- box: cubic with 20 A padding

Mixed Li+/Na+ competition systems are reserved for later validation, not first-round umbrella sampling.

## LiCl Batch QC

See `li_cl/metadata/qc_manifest.tsv`.

All 10 LiCl systems are ready for GROMACS setup and have completed minimization/equilibration on the remote CPU GROMACS workflow.

## NaCl Batch QC

See `na_cl/metadata/qc_manifest.tsv`.

All 10 NaCl systems are ready for GROMACS setup. The first NaCl exports for `LiD3-1` and `StrongBind-Li` lacked the `gromacs/` folder, but revised GROMACS-ready archives have replaced them.
