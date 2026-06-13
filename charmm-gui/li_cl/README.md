# LiCl CHARMM-GUI Systems

This folder contains CHARMM-GUI Solution Builder outputs for the first-round peptide + LiCl systems.

## Layout

- `raw_archives/`: original downloaded CHARMM-GUI `.tgz` files, renamed by candidate.
- `systems/`: extracted CHARMM-GUI output folders, one per candidate.
- `metadata/archive_mapping.tsv`: maps the original download filenames and input order to candidate IDs.
- `metadata/qc_manifest.tsv`: sequence, ion, topology, and GROMACS-readiness checks.
- `metadata/input_order_charmm_gui.png`: screenshot documenting the upload order.

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

All 10 first-round LiCl systems now pass the current GROMACS-readiness checks.

Note: the first LiD3-1 CHARMM-GUI export contained two protein molecules, `PROA` and `PROB`, from an earlier split-chain upload. It has been preserved under `systems/replaced/` and `raw_archives/replaced/`; the canonical `systems/LiD3-1/` folder now contains the revised one-chain setup generated from `../../esmfold/charmm_gui_pdb/lid31.pdb`.

## Ready Criteria

A system is marked `ready_for_gromacs` when:

- final peptide sequence matches `../../sequences/candidates.tsv`
- `topol.top` contains exactly one protein molecule
- Li+ is present as `LIT`
- Cl- is present as `CLA`
- water is present as `TIP3`
- required GROMACS files are present
- no fatal CHARMM-GUI output messages were detected
