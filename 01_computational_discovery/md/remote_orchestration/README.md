# Remote GROMACS Orchestration

This folder preserves the Python and shell scripts used to run LiSPER molecular-dynamics work on the AutoDL remote computer.

The scripts are copied from:

```text
/root/LiSPER_remote
```

They are kept here so the repository records not only the scientific outputs, but also the computational workflow used to generate them.

## Organization Choice

The scripts are stored in one shared `remote_orchestration/` folder instead of being duplicated under `li_cl/` and `na_cl/`.

This is intentional:

- `li_cl/` and `na_cl/` should stay focused on scientific inputs, logs, summaries, and results.
- `remote_orchestration/` should hold reusable code that can operate on either condition.
- The active condition is selected with `LISPER_WORKDIR`, so one script can run LiCl or NaCl without maintaining duplicate files.

This keeps the repository closer to a real computational project: code is reusable, results are condition-specific, and remote execution history remains easy to audit.

## Execution Model

The remote workflow is controlled by lightweight Python orchestration scripts. These scripts do not replace GROMACS. Instead, they:

1. Read candidate manifests and status summaries.
2. Prepare clean working folders for each peptide system.
3. Repair simple CHARMM-GUI/GROMACS setup issues when possible.
4. Generate or update `.mdp` and index files.
5. Launch GROMACS commands through `subprocess`.
6. Write per-step logs and summary TSV files.
7. Queue later stages with `WAIT_FOR_PID` so long jobs run sequentially.

Typical remote launch pattern:

```bash
cd /root/LiSPER_remote
nohup env LISPER_WORKDIR=/root/LiSPER_remote/LiSPER_LiCl \
  python3 /root/LiSPER_remote/run_lisper_production_cluster.py \
  > /root/LiSPER_remote/LiSPER_LiCl/remote_runs/licl_production_cluster_20ns.log 2>&1 &
```

The active GROMACS environment is:

```bash
source /root/miniconda3/etc/profile.d/conda.sh
conda activate lisper-gmx
```

Examples:

```bash
# LiCl minimization
env LISPER_WORKDIR=/root/LiSPER_remote/LiSPER_LiCl \
  python3 run_lisper_minimize.py

# NaCl minimization with the same script
env LISPER_WORKDIR=/root/LiSPER_remote/LiSPER_NaCl \
  python3 run_lisper_minimize.py
```

## Script Inventory

| Script | Role |
|---|---|
| `scripts/run_lisper_minimize.py` | Shared LiCl/NaCl minimization driver. Reads `ready_gromacs_systems.tsv`, repairs overlapping TIP3 waters when possible, runs `gmx grompp` and `gmx mdrun`, and writes minimization summaries. Uses `LISPER_WORKDIR`. |
| `scripts/run_lisper_equilibrate.py` | Shared LiCl/NaCl equilibration driver. Builds `SOLU`, `SOLV`, and `SYSTEM` index groups, runs step4.1 equilibration, and writes equilibration summaries. Uses `LISPER_WORKDIR`. |
| `scripts/run_lisper_production_cluster.py` | Shared LiCl/NaCl 20 ns production and clustering driver. Uses `LISPER_WORKDIR`, runs production MD, then attempts trajectory centering and `gmx cluster`. |
| `scripts/queue_nacl_add2.py` | Handles the late-added revised NaCl `LiD3-1` and `StrongBind-Li` systems, then merges their summaries back into the full NaCl queue. |
| `scripts/run_lid31_pipeline.py` | Earlier focused LiD3-1 repair/minimization/equilibration pipeline used during the revised one-chain LiD3-1 setup. |
| `scripts/start_equilibration.sh` | Small shell launcher for the LiCl equilibration script. |

## Current Caveats

These are historical execution scripts copied from the remote machine. Some paths are intentionally remote-specific, especially:

```text
/root/LiSPER_remote
/root/miniconda3
```

For local reuse, continue migrating hard-coded paths into command-line arguments or environment variables.

The current production/clustering script exposed two useful lessons:

- `LiD3-1` production finished cleanly, but clustering failed because the full `SYSTEM` index did not match the trajectory atom count by one atom.
- `LiND-1` production setup failed because the production working context could not resolve `toppar/forcefield.itp`.

Those issues are post-processing/setup issues, not evidence that the completed LiD3-1 MD trajectory is unusable.

## Scientific Handoff

```mermaid
flowchart LR
    A["CHARMM-GUI systems"] --> B["Python orchestration"]
    B --> C["gmx grompp"]
    C --> D["gmx mdrun"]
    D --> E["20 ns trajectory"]
    E --> F["trajectory centering"]
    F --> G["gmx cluster"]
    G --> H["representative_top_cluster.pdb"]
    H --> I["umbrella sampling setup"]
```

The next code improvement should be a safer clustering repair script that builds a trajectory-compatible peptide-only index before running `gmx trjconv` and `gmx cluster`.
