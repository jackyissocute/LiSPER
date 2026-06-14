# LiCl CHARMM-GUI Systems

CHARMM-GUI Solution Builder outputs for peptide + LiCl systems.

## QC Status

| Metric | Status |
|---|---|
| Candidates present | 10/10 |
| Sequence matches | 10/10 |
| Single protein molecule topology | 10/10 |
| Li+ ion present as `LIT` | 10/10 |
| Cl- ion present as `CLA` | 10/10 |
| GROMACS files present | 10/10 |

## Layout

| Path | Purpose |
|---|---|
| `raw_archives/` | Original CHARMM-GUI `.tgz` files |
| `systems/` | Extracted CHARMM-GUI systems |
| `metadata/archive_mapping.tsv` | Download-to-candidate mapping |
| `metadata/qc_manifest.tsv` | QC table for sequence, topology, ions, and files |
| `metadata/input_order_charmm_gui.png` | Upload-order screenshot |

## Provenance Note

The first LiD3-1 LiCl export had a split protein topology (`PROA` + `PROB`). It is preserved under `systems/replaced/` and `raw_archives/replaced/`. The canonical `systems/LiD3-1/` folder contains the corrected one-chain setup.

## Handoff

GROMACS-ready paths are listed in:

`../../md/li_cl/ready_gromacs_systems.tsv`
