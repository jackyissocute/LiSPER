# Remote Sync Path Map

This file is the canonical path reference for LiSPER remote GROMACS work.

Use these paths when uploading scripts to AutoDL or syncing products back into the repository. Do not sync new MD products into old root-level folders such as `md/`, `charmm-gui/`, `esmfold/`, `sequences/`, `docs/`, or `scripts/`.

## Local Repository Roots

| Purpose | Local path |
|---|---|
| Repository root | `/Users/jackylin/Documents/GitHub/LiSPER` |
| Active MD workspace | `01_computational_discovery/md/` |
| LiCl MD status/logs | `01_computational_discovery/md/li_cl/remote_runs/` |
| LiCl synced outputs | `01_computational_discovery/md/li_cl/remote_results/` |
| NaCl MD status/logs | `01_computational_discovery/md/na_cl/remote_runs/` |
| NaCl synced outputs | `01_computational_discovery/md/na_cl/remote_results/` |
| Remote orchestration code | `01_computational_discovery/md/remote_orchestration/scripts/` |

## Remote Roots

| Purpose | Remote path |
|---|---|
| Remote project root | `/root/LiSPER_remote` |
| LiCl GROMACS workdir | `/root/LiSPER_remote/LiSPER_LiCl` |
| NaCl GROMACS workdir | `/root/LiSPER_remote/LiSPER_NaCl` |
| Remote script staging | `/root/LiSPER_remote/*.py` |
| Remote legacy scripts | `/root/LiSPER_remote/legacy_scripts/` |
| LiCl remote logs | `/root/LiSPER_remote/LiSPER_LiCl/remote_runs/` |
| NaCl remote logs | `/root/LiSPER_remote/LiSPER_NaCl/remote_runs/` |

## Uploading Orchestration Scripts

Upload only the scripts needed for the next task:

```bash
scp -P 37049 \
  01_computational_discovery/md/remote_orchestration/scripts/run_lisper_production_cluster.py \
  root@connect.westb.seetacloud.com:/root/LiSPER_remote/
```

Shared scripts use `LISPER_WORKDIR`, so the same script can run LiCl or NaCl:

```bash
env LISPER_WORKDIR=/root/LiSPER_remote/LiSPER_LiCl python3 /root/LiSPER_remote/run_lisper_minimize.py
env LISPER_WORKDIR=/root/LiSPER_remote/LiSPER_NaCl python3 /root/LiSPER_remote/run_lisper_minimize.py
```

The old NaCl-only scripts are no longer active launch targets:

```text
/root/LiSPER_remote/legacy_scripts/run_lisper_nacl_minimize.py
/root/LiSPER_remote/legacy_scripts/run_lisper_nacl_equilibrate.py
```

## Syncing LiCl Results Back

Use these local destinations:

```bash
# Queue-level summaries
scp -P 37049 \
  root@connect.westb.seetacloud.com:/root/LiSPER_remote/LiSPER_LiCl/production_clustering_summary.tsv \
  01_computational_discovery/md/li_cl/remote_runs/

scp -P 37049 \
  root@connect.westb.seetacloud.com:/root/LiSPER_remote/LiSPER_LiCl/remote_runs/clustering_repair_summary.tsv \
  01_computational_discovery/md/li_cl/remote_runs/

# Per-candidate small products
scp -P 37049 \
  root@connect.westb.seetacloud.com:/root/LiSPER_remote/LiSPER_LiCl/systems/<candidate>/gromacs/run_prod_20ns/step5_production_20ns.log \
  01_computational_discovery/md/li_cl/remote_results/systems/<candidate>/gromacs/run_prod_20ns/

scp -P 37049 \
  root@connect.westb.seetacloud.com:/root/LiSPER_remote/LiSPER_LiCl/systems/<candidate>/gromacs/cluster_20ns_repair/representative_top_cluster.pdb \
  01_computational_discovery/md/li_cl/remote_results/systems/<candidate>/gromacs/cluster_20ns_repair/
```

## Syncing NaCl Results Back

Use the NaCl mirror paths:

```bash
scp -P 37049 \
  root@connect.westb.seetacloud.com:/root/LiSPER_remote/LiSPER_NaCl/production_clustering_summary.tsv \
  01_computational_discovery/md/na_cl/remote_runs/

scp -P 37049 \
  root@connect.westb.seetacloud.com:/root/LiSPER_remote/LiSPER_NaCl/systems/<candidate>/gromacs/run_prod_20ns/step5_production_20ns.log \
  01_computational_discovery/md/na_cl/remote_results/systems/<candidate>/gromacs/run_prod_20ns/
```

## Large Trajectory Rule

Avoid repeatedly syncing active `.xtc`, `.trr`, or full trajectory files.

Sync large trajectories only when:

- the run is complete,
- the file is needed for local QC or archiving,
- or the user explicitly asks.

For routine monitoring, sync small files first: `.log`, `.grompp.log`, `.mdrun.stdout.log`, summary TSVs, representative PDBs, and cluster logs.
