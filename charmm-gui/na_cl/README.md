# NaCl CHARMM-GUI Systems

This folder contains CHARMM-GUI Solution Builder outputs for first-round peptide + NaCl systems.

## Layout

- `raw_archives/`: original downloaded CHARMM-GUI `.tgz` files, renamed by candidate.
- `systems/`: extracted CHARMM-GUI output folders, one per candidate.
- `metadata/archive_mapping.tsv`: maps download names and input order to candidate IDs.
- `metadata/qc_manifest.tsv`: sequence, ion, topology, and GROMACS-readiness checks.
- `metadata/input_order_charmm_gui_na.png`: screenshot documenting the upload order.

## QC Summary

Ready for GROMACS:

- LiD3-1
- LiND-1
- IDP-Li-1
- IDP-Li-2
- LowCharge-Li
- LiD2-IDP
- StrongBind-Li
- SoftCage-Li
- IDP-Rich-Li
- Control-Negative

All 10 first-round NaCl systems now pass the current GROMACS-readiness checks.

Note: the first NaCl exports for LiD3-1 and StrongBind-Li did not include the `gromacs/` input-generator folder. Those incomplete versions have been preserved under `systems/replaced/` and `raw_archives/replaced/`; the canonical folders now contain revised GROMACS-ready exports.

## Ready Criteria

A system is marked `ready_for_gromacs` when:

- final peptide sequence matches `../../sequences/candidates.tsv`
- `topol.top` contains exactly one protein molecule
- Na+ is present as `SOD`
- Cl- is present as `CLA`
- required GROMACS files are present
