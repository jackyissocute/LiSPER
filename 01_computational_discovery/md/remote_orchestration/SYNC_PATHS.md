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

## Remote Roots

| Purpose | Path |
|---|---|
| Remote project root | `/root/LiSPER_remote` |
| Active LiCl workdir | `/root/LiSPER_remote/LiSPER_8cand_LiCl` |
| Active NaCl setup workdir | `/root/LiSPER_remote/LiSPER_8cand_NaCl` |
| Active NaCl production workdir | `/root/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker` |
| Active NaCl overflow workdir | `/root/LiSPER_remote/LiSPER_8cand_NaCl_overflow_workerA` |
| Legacy 10-candidate archive | `/root/LiSPER_remote/legacy_10_candidate_runs/` |

## Rule

Do not sync new active products into the old `/root/LiSPER_remote/LiSPER_LiCl` or `/root/LiSPER_remote/LiSPER_NaCl` paths. Those old workdirs were archived after the library changed from 10 candidates to 8 candidates.
