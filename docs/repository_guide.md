# LiSPER Repository Guide

This repository is organized around the LiSPER project question:

Can de novo designed intrinsically disordered peptides inspired by lithium-binding motifs selectively bind Li+ over Na+ in aqueous solution?

## Main Data Flow

1. `sequences/`
   First-round peptide library and sequence metadata.

2. `esmfold/`
   Structure prediction outputs from candidate sequences.

   CHARMM-GUI-ready PDB files are in `esmfold/pdb/`, with the upload checklist in `esmfold/charmm_gui_upload_list.md`.

3. `charmm-gui/`
   System preparation for separate LiCl and NaCl simulations.

4. `md/`
   Equilibration, production runs, and structural clustering.

5. `umbrella/`
   Umbrella sampling setup and trajectories.

6. `pmf/`
   PMF analysis and Delta Delta G selectivity estimates.

7. `plasmids/` and `wetlab/`
   Experimental translation of selected computational candidates.

## Supporting Areas

- `inbox/`: temporary drop zone for files that need sorting or review
- `literature/`: papers and notes
- `docs/Literature Review/IDP`: intrinsically disordered protein literature PDFs
- `docs/Literature Review/LBP`: lithium-binding peptide/protein literature PDFs
- `data/`: raw and processed datasets
- `analysis/`: notebooks and exploratory analysis
- `protocols/`: repeatable computational and experimental methods
- `scripts/`: reusable project utilities
- `figures/`: plots, diagrams, and publication graphics
- `manuscript/`: writing and supplementary materials

## Naming Convention

Use the candidate IDs from `sequences/candidates.tsv` consistently across folders:

- `LiD3-1`
- `LiND-1`
- `IDP-Li-1`
- `IDP-Li-2`
- `LowCharge-Li`
- `LiD2-IDP`
- `StrongBind-Li`
- `SoftCage-Li`
- `IDP-Rich-Li`
- `Control-Negative`

The strongest recommended starting subset is:

- `LiD3-1`
- `LiND-1`
- `IDP-Li-1`
- `LowCharge-Li`
- `Control-Negative`

For ion-specific computational folders or files, include the ion condition explicitly, for example:

- `LiD3-1_LiCl`
- `LiD3-1_NaCl`

This keeps the central comparison, Li+ versus Na+, visible throughout the project.

## Inbox Workflow

Use `inbox/` for files that are not yet classified.

Typical process:

1. Put a new file in `inbox/`.
2. Ask Codex to process the inbox.
3. Codex inspects the file, summarizes what it is, recommends a destination, and moves or copies it into the appropriate project folder.

The inbox is temporary. Once a file is processed, it should usually leave `inbox/` and live in a permanent project folder.

## First-Round Design Logic

The first-round library is based on three linked inspirations:

- GPGDP/GPGNP motifs provide lithium-binding precedent from the LBP literature.
- Gly/Ser/Pro-rich sequence design provides IDP-like flexibility.
- Asp/Glu oxygen donors may coordinate Li+, but charge is intentionally limited to reduce nonspecific Na+/Ca2+ binding.

The computational screen should evaluate every candidate against both Li+ and Na+, even when a design is expected to be a negative control.
