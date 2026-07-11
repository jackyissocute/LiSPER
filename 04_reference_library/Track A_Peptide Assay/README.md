# Track A Peptide Assay — Reference Library

External literature for designing and running **ordered synthetic peptide Li⁺/Na⁺ binding assays** (Track A).

Use this folder when writing `02_experimental_validation/track_A_purified_peptide/protocols/`. Do not treat this folder as a protocol itself.

## Folder Map

| Folder | What it supports in Track A |
|---|---|
| `01_lithium_binding_peptide_precedent` | GPGDP/GPGNP/GPGAP motif precedent; Li-binding peptide biology context |
| `02_immobilized_peptide_and_bead_assays` | **Primary assay format:** peptide on magnetic beads + adsorption / ICP |
| `03_dialysis_and_solution_selectivity_assays` | Free-solution / dialysis + ICP Li vs Na selectivity |
| `04_icp_oes_ms_ion_quantification` | How to quantify Li and Na reliably |
| `05_nmr_itc_thermodynamic_methods` | Optional upgrade: ⁷Li NMR / thermodynamics |
| `06_peptide_qc_counterions_and_handling` | Vendor peptide QC, TFA removal, counterion exchange |
| `07_surface_display_context_for_track_B_bridge` | Why Track A hits advance to display (not Track A protocol core) |
| `08_catalog_and_source_metadata` | Master citation table, DOI list, paywall notes |

## Protocol Priority (what to read first)

1. **QC first:** `06_peptide_qc_counterions_and_handling/`
2. **Main assay precedent:** `02_immobilized_peptide_and_bead_assays/Bhargawa_2024_...pdf`
3. **Solution selectivity method:** `03_dialysis_and_solution_selectivity_assays/Adams_2026_...md`
4. **Motif / ranking context:** `01_lithium_binding_peptide_precedent/`
5. Optional thermodynamics: `05_nmr_itc_thermodynamic_methods/`
6. Track B only later: `07_surface_display_context_for_track_B_bridge/`

## Access Notes

- **PDF present:** file is stored locally and citable from this repo copy.
- **`.md` / `.fulltext.xml`:** open-access full text captured from Europe PMC / publisher HTML when PDF download was blocked by publisher anti-bot rules.
- **Paywalled DOI-only records:** listed in `08_catalog_and_source_metadata/` with citation + access status. Local PDF copies of key paywalled LBP papers already exist from the earlier `protein_design/LBP/` collection and are copied into folders `01`, `02`, and `07`.

## Boundary

| Put here | Do not put here |
|---|---|
| External papers / reviews for Track A assays | Your own wet-lab protocol drafts |
| Citation metadata | Simulation trajectories |
| Vendor QC method refs | GenScript order CSVs (those stay in `ordering/`) |
