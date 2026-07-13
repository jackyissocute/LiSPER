# Remote Sync Path Map

Canonical paths for the 8-candidate LiSPER workflow. Updated 2026-07-12.

## Local (always)

| Purpose | Path |
|---|---|
| Git worktree (Part A lean) | `/Users/jackylin/Documents/GitHub/LiSPER` |
| MD | `01_computational_discovery/md/` |
| Umbrella | `01_computational_discovery/umbrella/` |
| PMF / ΔΔG | `01_computational_discovery/pmf/` |
| Storage policy | `01_computational_discovery/STORAGE_LAYOUT.md` |
| Campaign status | `01_computational_discovery/umbrella/remote_runs_umbrella_sampling_status.md` |
| Pre-rent checklist | `01_computational_discovery/umbrella/PREFLIGHT_RUNBOOK.md` |

## Cold disk (optional mount)

| Purpose | Path |
|---|---|
| Cold root | `/Volumes/Jacky 1TB/Research/LiSPER_cold/` |
| New fat syncs | `.../ACTIVE/incoming/{umbrella,pmf,md}/` |
| Rebuild seeds | `.../ACTIVE/seeds/charmm_gui_systems/` |
| GCP snapshot | `.../ACTIVE/seeds/gcp_remote_backup_20260712/` |
| Cold archive | `.../ARCHIVE/` |

Disk often unplugged → lean sync to git only; fat waits for next mount.

## Next compute host (live)

| Item | Value |
|---|---|
| **Pick** | **AMD EPYC 9554P** (64c / 128t, 3.1–3.75 GHz) |
| SSH | `ssh lisper-epyc` → `root@84.32.71.226` |
| GROMACS | `/opt/gromacs/2026.0` (AVX_512, CPU-only) |
| Remote root | `/data/LiSPER_remote/` |
| Why | Modern Genoa, 128 threads, 384 GB RAM, 2×1 TB NVMe RAID1, **10 Gbps**, **~$1.34/hr** |
| Reject | 9575F (~2× $/hr); dual-socket older boxes (thin disk); 9754 unless wall-clock dominates |
| Env | `umbrella/remote_orchestration/launch_locked_site.env.example` |
| Scheduler | `LISPER_GLOBAL_MDRUN_LIMIT=124`, 1 thread / window |
| Window plan | `umbrella/WINDOW_ASSIGNMENT_PLAN.md` |

## Remote layout (on rented host)

```
/data/LiSPER_remote/
  LiSPER_8cand_LiCl/
  LiSPER_8cand_NaCl_prod_worker/
  scripts/
  paired_binding_sites/     # copy of umbrella/paired_site_manifests/
```

## Retired providers (do not launch)

| Provider | Status |
|---|---|
| QuickPod | Destroyed / abandoned (unstable SSH). Ops stubs archived under Jacky cold `ARCHIVE/` |
| GCP `lisper-runner-32v` | Soft-stop OK after backup; science copy on Jacky seeds |
| AutoDL workers | Backup only |

Historical remote path names (`/data/LiSPER_remote/...`) stay as the **template** for the next host — not a live QuickPod box.
