# NaCl Molecular Dynamics Handoff

This folder tracks NaCl systems that passed CHARMM-GUI QC and are ready for GROMACS minimization/equilibration.

Ready-system index:

- `ready_gromacs_systems.tsv`

Source QC:

- `../../charmm-gui/na_cl/metadata/qc_manifest.tsv`

Current status:

- 10 NaCl systems are ready for GROMACS.
- The first 8 ready systems were already launched on the remote.
- `LiD3-1` and `StrongBind-Li` have been updated with revised GROMACS-ready CHARMM-GUI exports and are queued to run after the active 8-system NaCl batch finishes.

The ready GROMACS folders remain in `../../charmm-gui/na_cl/systems/<candidate>/gromacs/` to avoid duplicating setup files.
