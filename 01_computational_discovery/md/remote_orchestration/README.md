# Remote GROMACS Orchestration

This folder contains the active remote-execution code for the revised **8-candidate** LiSPER workflow.

One-off scripts from earlier development rounds are preserved under:

```text
archive/legacy_10_candidate_library/01_computational_discovery/md/remote_orchestration/
```

Do not use those archived scripts for the active 8-candidate workflow unless a specific traceability check requires it.

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

New GROMACS tasks should start only for candidates with final-name ESMFold PDBs and matched CHARMM-GUI systems.

## Active Remote Workdirs

Use [`SYNC_PATHS.md`](SYNC_PATHS.md) as the canonical path map.

| Condition | Remote workdir |
|---|---|
| LiCl | `/root/LiSPER_remote/LiSPER_8cand_LiCl` |
| NaCl | `/root/LiSPER_remote/LiSPER_8cand_NaCl` |
| NaCl production worker | `/root/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker` |

Do not sync active 8-candidate products into older remote workdirs.

## Active Scripts

| Script | Role |
|---|---|
| `scripts/run_lisper_minimize.py` | Shared minimization driver for a prepared LiCl or NaCl workdir. |
| `scripts/run_lisper_equilibrate.py` | Shared equilibration driver for minimized systems. |
| `scripts/run_lisper_production_cluster.py` | Shared 20 ns production and clustering driver for equilibrated systems. |
| `scripts/run_lisper_parallel_production_cluster.py` | Parallel candidate-level production and clustering driver for a fully equilibrated workdir. |
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

# NaCl production worker, candidate-parallel
env LISPER_WORKDIR=/root/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker \
  LISPER_JOBS=8 \
  LISPER_NTHREAD_PER_JOB=16 \
  python3 run_lisper_parallel_production_cluster.py
```

## Completed Asset Policy

Three final candidates already have completed upstream assets:

| Final candidate | Source record | Active rule |
|---|---|---|
| `LiD3-Flex` | `LiD3-1` | Treat completed assets as final-name inputs. |
| `LiND-Hybrid` | `LiND-1` | Treat completed assets as final-name inputs. |
| `LiLC-1` | `LowCharge-Li` | Treat completed upstream assets as final-name inputs; production/clustering still pending. |

Public and active workflow surfaces should present the final 8-candidate names and simple done/pending states.
