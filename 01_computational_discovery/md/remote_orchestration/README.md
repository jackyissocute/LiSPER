# Remote GROMACS Orchestration

This folder contains the active remote-execution code for the revised **8-candidate** LiSPER MD workflow. MD-stage orchestration remains here; umbrella drivers and synced umbrella outputs are organized in `../../umbrella/`, and WHAM/PMF/Delta G QC is organized in `../../pmf/`.

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
-> handoff to umbrella sampling
-> WHAM / PMF / Delta Delta G
```

New GROMACS tasks should start only for candidates with final-name ESMFold PDBs and matched CHARMM-GUI systems.

## Active Remote Workdirs

Use [`SYNC_PATHS.md`](SYNC_PATHS.md) as the canonical path map.

| Worker | Remote workdir | Active role |
|---|---|---|
| Worker A replacement, 18 cores | `/root/LiSPER_remote/LiSPER_8cand_LiCl` | LiCl production/clustering and LiCl umbrella backfill |
| Worker A replacement, 18 cores | `/root/LiSPER_remote/LiSPER_8cand_NaCl_overflow_workerA` | NaCl backfill for candidates moved off Worker B |
| Worker B, 12 cores | `/root/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker` | NaCl production/clustering and NaCl umbrella backfill |

Do not sync active 8-candidate products into older remote workdirs.

## Active Scripts

| Script | Role |
|---|---|
| `scripts/run_lisper_minimize.py` | Shared minimization driver for a prepared LiCl or NaCl workdir. |
| `scripts/run_lisper_equilibrate.py` | Shared equilibration driver for minimized systems. |
| `scripts/run_lisper_production_cluster.py` | Shared 20 ns production and clustering driver for equilibrated systems. |
| `scripts/run_lisper_parallel_production_cluster.py` | Parallel candidate-level production and clustering driver for a fully equilibrated workdir. |
| `scripts/start_equilibration.sh` | Small shell wrapper for launching equilibration on the active workdir. |

The umbrella driver was moved to `../../umbrella/remote_orchestration/scripts/run_lisper_umbrella_sampling.py` so new umbrella work is visible under the top-level umbrella step.

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
  LISPER_JOBS=6 \
  LISPER_NTHREAD_PER_JOB=2 \
  python3 run_lisper_parallel_production_cluster.py
```

Current scheduling treats the two AutoDL machines as one non-oversubscribed pool: Worker A replacement is capped at 18 active GROMACS threads, and Worker B is capped at 12. Count actual `gmx mdrun -ntomp/-nt` threads before launching new work.

Umbrella sampling is condition-specific: a LiCl or NaCl condition can enter umbrella window design and sampling immediately after that condition has completed production, clustering, and representative extraction. It does not need to wait for the matched ion condition. Local umbrella files should be synced to `../../umbrella/`; WHAM/PMF outputs should be synced to `../../pmf/`.

## Versioned PMF Repair Loop

For every candidate-condition, monitoring follows this loop:

```text
V(n) result finishes
-> sync small outputs
-> review WHAM logs, PMF, histogram, bootstrap, and time slices
-> classify PASS / REPAIR / WAIT-RUNNING / BLOCKED
```

`PASS` promotes a reliable Delta G and allows paired Delta Delta G. `WAIT-RUNNING` protects active jobs until the next heartbeat. `BLOCKED` records the concrete blocker. `REPAIR` means the monitor must infer the smallest justified extra compute from QC warnings/results, write or update a short manifest, and launch `V(n+1)` when safe capacity and real inputs exist. If cores are full, queue the exact `V(n+1)` plan and launch it as soon as capacity opens.

Repair work should be generated from real GROMACS inputs and checkpoints, never invented locally. Valid repairs include extending weak/edge/tail windows, adding or interpolating denser windows around poor-overlap coordinates, rerunning equilibration/production for suspect windows, correcting coordinate/PBC setup, rerunning WHAM with bootstrap plus multiple burn-ins, or full rerun only when the protocol/coordinate is invalid. Dashboard and status surfaces should show cumulative current protocol counts, for example `V3 22/24 -> 23/24 -> 24/24`, not separate `+ repair` wording.

The monitor should stop modifying a candidate-condition only after the reliability gate passes or a real blocker is documented. Final Delta G requires no material empty bins, no material weak bins in the bound basin/transition/reference plateau, reasonable overlap, stable time-sliced PMF basin-to-plateau difference, acceptable bootstrap/error, and comparable LiCl/NaCl protocols.

## Completed Asset Policy

Three final candidates already have completed upstream assets:

| Final candidate | Source record | Active rule |
|---|---|---|
| `LiD3-Flex` | `LiD3-1` | Treat completed assets as final-name inputs. |
| `LiND-Hybrid` | `LiND-1` | Treat completed assets as final-name inputs. |
| `LiLC-1` | `LowCharge-Li` | Treat completed upstream assets as final-name inputs; production/clustering still pending. |

Public and active workflow surfaces should present the final 8-candidate names and simple done/pending states.
