# Remote GROMACS Orchestration

This folder contains the active remote-execution code for the revised **8-candidate** LiSPER workflow.

The previous 10-candidate remote run was stopped and archived after the candidate library changed. Its one-off recovery and repair scripts are preserved under:

```text
archive/legacy_10_candidate_library/01_computational_discovery/md/remote_orchestration/
```

Do not use those legacy scripts for the active 8-candidate workflow unless a specific provenance/reuse check requires it.

## Current Execution Rule

The active computational order is:

```text
8 candidate sequences
-> ESMFold intake
-> CHARMM-GUI LiCl and NaCl systems
-> minimization
-> equilibration
-> 20 ns production MD
-> structural clustering
-> representative structures
-> umbrella sampling / PMF / Delta Delta G
```

GROMACS should **not** be restarted until final 8-candidate ESMFold PDBs and matched CHARMM-GUI systems are available.

## Active Remote Workdirs

Use [`SYNC_PATHS.md`](SYNC_PATHS.md) as the canonical path map.

| Condition | Remote workdir |
|---|---|
| LiCl | `/root/LiSPER_remote/LiSPER_8cand_LiCl` |
| NaCl | `/root/LiSPER_remote/LiSPER_8cand_NaCl` |

The old `/root/LiSPER_remote/LiSPER_LiCl` and `/root/LiSPER_remote/LiSPER_NaCl` paths are legacy-only and should not receive new products.

## Active Scripts

| Script | Role |
|---|---|
| `scripts/run_lisper_minimize.py` | Shared minimization driver for a prepared LiCl or NaCl workdir. |
| `scripts/run_lisper_equilibrate.py` | Shared equilibration driver for minimized systems. |
| `scripts/run_lisper_production_cluster.py` | Shared 20 ns production and clustering driver for equilibrated systems. |
| `scripts/start_equilibration.sh` | Small shell wrapper for launching equilibration on the active workdir. |

All active scripts default to the 8-candidate LiCl workdir and can be redirected with `LISPER_WORKDIR`.

Examples:

```bash
# LiCl
env LISPER_WORKDIR=/root/LiSPER_remote/LiSPER_8cand_LiCl \
  python3 run_lisper_minimize.py

# NaCl
env LISPER_WORKDIR=/root/LiSPER_remote/LiSPER_8cand_NaCl \
  python3 run_lisper_minimize.py
```

## Reuse Policy

Three final candidates are sequence-identical to old designs:

| Final candidate | Legacy candidate | Reuse rule |
|---|---|---|
| `LiD3-Flex` | `LiD3-1` | Old ESMFold/CHARMM materials may be consulted with provenance. |
| `LiND-Hybrid` | `LiND-1` | Old ESMFold/CHARMM materials may be consulted with provenance. |
| `LiLC-1` | `LowCharge-Li` | Old ESMFold/CHARMM materials may be consulted with provenance. |

Reuse must be explicit. The public and active workflow should still present the final 8-candidate names.
