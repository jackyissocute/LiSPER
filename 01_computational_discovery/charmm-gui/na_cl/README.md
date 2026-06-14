# NaCl CHARMM-GUI Systems

CHARMM-GUI Solution Builder outputs for peptide + NaCl systems.

## QC Status

| Metric | Status |
|---|---|
| Candidates present | 10/10 |
| Sequence matches | 10/10 |
| Single protein molecule topology | 10/10 |
| Na+ ion present as `SOD` | 10/10 |
| Cl- ion present as `CLA` | 10/10 |
| GROMACS files present | 10/10 |

## Layout

| Path | Purpose |
|---|---|
| `raw_archives/` | Original CHARMM-GUI `.tgz` files |
| `systems/` | Extracted CHARMM-GUI systems |
| `metadata/archive_mapping.tsv` | Download-to-candidate mapping |
| `metadata/qc_manifest.tsv` | QC table for sequence, topology, ions, and files |
| `metadata/input_order_charmm_gui_na.png` | Upload-order screenshot |

## Provenance Note

The first NaCl exports for LiD3-1 and StrongBind-Li lacked the `gromacs/` folder. Those incomplete versions are preserved under `systems/replaced/` and `raw_archives/replaced/`. The canonical folders contain revised GROMACS-ready exports.

## Handoff

GROMACS-ready paths are listed in:

`../../md/na_cl/ready_gromacs_systems.tsv`
