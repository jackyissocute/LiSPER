# Remote Sync Path Map

Canonical path reference for the revised 8-candidate LiSPER workflow.

## Local Roots

| Purpose | Path |
|---|---|
| Main repo | `/Users/jackylin/Documents/GitHub/LiSPER` |
| Active MD workspace | `01_computational_discovery/md/` |
| LiCl status/logs | `01_computational_discovery/md/li_cl/remote_runs/` |
| LiCl synced outputs | `01_computational_discovery/md/li_cl/remote_results/` |
| NaCl status/logs | `01_computational_discovery/md/na_cl/remote_runs/` |
| NaCl synced outputs | `01_computational_discovery/md/na_cl/remote_results/` |
| Orchestration scripts | `01_computational_discovery/md/remote_orchestration/scripts/` |
| Umbrella workspace | `01_computational_discovery/umbrella/` |
| Umbrella status/logs | `01_computational_discovery/umbrella/remote_runs/` |
| Umbrella synced outputs | `01_computational_discovery/umbrella/remote_results/` |
| PMF workspace | `01_computational_discovery/pmf/` |
| PMF QC/results | `01_computational_discovery/pmf/remote_runs/` and `01_computational_discovery/pmf/remote_results/` |

## Remote Roots

| Worker | SSH | CPU quota | Primary role |
|---|---|---:|---|
| **QuickPod (primary)** | `ssh quickpod-lisper` (`root@217.254.101.12 -p 63014`) | 126 threads | Locked-site rebuild host; legacy resume stopped |
| GCP `lisper-runner-32v` | `ssh gcp-lisper` (`jackieeelin929@34.84.148.249`) | 32 vCPU | Soft-stopped 2026-07-12; keep disk as backup archive |
| Worker A / AutoDL | `ssh -p 27815 root@connect.westc.seetacloud.com` | 18 cores | Backup/comparison only |
| Worker B / AutoDL | `ssh -p 43418 root@connect.westd.seetacloud.com` | 12 cores | Backup/comparison only |

### QuickPod paths (use these)

| Purpose | Path |
|---|---|
| Remote project root | `/data/LiSPER_remote` |
| Active LiCl workdir | `/data/LiSPER_remote/LiSPER_8cand_LiCl` |
| Active NaCl production workdir | `/data/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker` |
| Active NaCl overflow workdir | `/data/LiSPER_remote/LiSPER_8cand_NaCl_overflow_workerA` |
| Scripts | `/data/LiSPER_remote/scripts` |
| Paired site manifests | `/data/LiSPER_remote/paired_binding_sites` |

### Legacy GCP paths (backup only; do not launch new jobs here)

| Purpose | Path |
|---|---|
| GCP project root | `/mnt/lisper_data/LiSPER_remote` |
| Legacy AutoDL roots | `/root/LiSPER_remote/LiSPER_8cand_*` |

## Rule

Do not sync new active products into the old `/root/LiSPER_remote/LiSPER_LiCl` or `/root/LiSPER_remote/LiSPER_NaCl` paths. Those old workdirs were archived after the library changed from 10 candidates to 8 candidates.

Remote workdirs are unchanged by the local folder split. Locally, production/clustering artifacts go to `md/`, umbrella artifacts go to `umbrella/`, and WHAM/PMF/Delta G artifacts go to `pmf/`.
