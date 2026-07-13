# Compute provider

**Live host:** AMD **EPYC 9554P** — `ssh lisper-epyc` (`root@84.32.71.226`)

| Item | Value |
|---|---|
| GROMACS | `/opt/gromacs/2026.0` (AVX_512) |
| Data root | `/data/LiSPER_remote/` |
| Window plan | `../WINDOW_ASSIGNMENT_PLAN.md` |
| Launch env | `launch_locked_site.env.example` → remote `scripts/launch_locked_site.env` |

Paths: `../md/remote_orchestration/SYNC_PATHS.md`  
Preflight: `../PREFLIGHT_RUNBOOK.md`

Operational prerequisite: no umbrella until manifests record `GEOMETRY_SCREENED_BOUND_START`; this does not validate binding.
