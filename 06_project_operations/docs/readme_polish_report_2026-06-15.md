# README Polish Report

Date: 2026-06-15

## Purpose

This pass updated the repository README system after the latest LiSPER organizational changes.

The main goals were:

- make the root `README.md` match the current research-program logic,
- improve readability of Mermaid diagrams,
- clarify folder-level navigation,
- merge or archive duplicated markdown only where that improved clarity.

## What Changed

| Area | Change |
|---|---|
| Root README | Updated the overview to explain `01-03` as the research pipeline and `04-06` as support layers. |
| Root README diagrams | Reworked diagrams into top-down layouts with shorter node labels and line breaks. |
| Active README diagrams | Added `accTitle` and `accDescr` to active README Mermaid diagrams. |
| Computational READMEs | Converted compressed left-to-right workflow diagrams into top-down readable diagrams. |
| Experimental validation READMEs | Clarified Track A and Track B as parallel validation routes. |
| Protocol indexes | Kept detailed protocols modular but made the README indexes more clickable and easier to scan. |
| Surface-display assays | Expanded the assay README into a real navigation page for the assay package. |
| Archive | Moved a duplicate hidden candidate-host pointer markdown into the archive. |

## Merge Decisions

| Folder | Decision | Reason |
|---|---|---|
| `02_experimental_validation/track_A_purified_peptide/protocols/` | Do not merge | The files are bench protocols and are clearer as ordered, modular steps. |
| `02_experimental_validation/track_B_surface_display/assays/surface_display_assays/` | Do not merge | The files cover distinct assay-planning functions: design, decision matrix, reagents, data analysis, and construct implications. |
| `06_project_operations/docs/` | Do not merge | These are decision records and guides with different purposes. |
| `candidate_hosts/.md` | Archive | It duplicated the active `candidate_hosts.md` and added clutter. |

## Readability Standard

Active README diagrams now use:

- top-down flow where possible,
- short node labels,
- line breaks inside longer labels,
- accessibility titles and descriptions,
- no compressed left-to-right workflow chains.

## Verification

After the edits, the repository should pass:

- active README Mermaid accessibility check,
- markdown relative-link check,
- active README horizontal-flow check.
