# AGENTS.md

## Cursor Cloud specific instructions

LiSPER is a research monorepo: mostly Markdown documentation plus Python 3 orchestration scripts that drive GROMACS molecular-dynamics runs on a remote HPC cluster. There is no local application service, no package manager, and no build/lint step. The orchestration and self-check scripts use only the Python standard library.

- Runnable self-check tests live in `01_computational_discovery/umbrella/remote_orchestration/scripts/` (no GROMACS required):
  - `python3 test_umbrella_design.py` — passes.
  - `python3 test_preflight_helpers.py` — `test_validate_bound_geometry` fails as-is: the test writes ions with resname `LI` but calls `validate_bound_start.py --ion-resname LIT`, so it never matches (pre-existing test-data mismatch, unrelated to the environment).
- Real MD / umbrella-sampling / PMF work requires GROMACS 2026.0 (`/opt/gromacs/2026.0/bin`) on a remote EPYC cluster and is not reproducible in this VM. Do not attempt to install GROMACS locally.
- Archived plasmid-design scripts under `archive/` are the only code needing extra deps (`biopython`, `snapgene_reader`); install on demand only if editing them.
- The public web dashboard lives in the separate `LiSPER-Dashboard` repository, not here.
