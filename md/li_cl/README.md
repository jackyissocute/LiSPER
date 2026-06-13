# LiCl Molecular Dynamics Handoff

This folder tracks LiCl systems that passed CHARMM-GUI QC and are ready for GROMACS minimization/equilibration.

Ready-system index:

- `ready_gromacs_systems.tsv`

Source QC:

- `../../charmm-gui/li_cl/metadata/qc_manifest.tsv`

Current status:

- 10 LiCl systems are ready for GROMACS.
- `LiD3-1` has been updated with the revised one-chain CHARMM-GUI setup and is included in `ready_gromacs_systems.tsv`.

The ready GROMACS folders remain in `../../charmm-gui/li_cl/systems/<candidate>/gromacs/` to avoid duplicating large setup files.
