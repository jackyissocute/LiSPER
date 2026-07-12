# Remote GROMACS Orchestration (MD stage)

MD-stage drivers for the 8-candidate library. Umbrella → `../../umbrella/`. PMF → `../../pmf/`.

## Canonical docs

| Doc | Role |
|---|---|
| [`SYNC_PATHS.md`](SYNC_PATHS.md) | Local / cold / remote paths + **EPYC 9554P** pick |
| [`LOCAL_BACKUP_AND_PROVIDER_SWITCH.md`](LOCAL_BACKUP_AND_PROVIDER_SWITCH.md) | GCP backup → Jacky |
| [`../../STORAGE_LAYOUT.md`](../../STORAGE_LAYOUT.md) | Part A git vs Part B cold |
| [`../../umbrella/PREFLIGHT_RUNBOOK.md`](../../umbrella/PREFLIGHT_RUNBOOK.md) | Pre-rent checklist |

## Rule

Do not launch mismatched-site umbrella or archived QuickPod resume scripts.  
Next compute: locked-site `VALIDATED_BOUND` only, on the host named in `SYNC_PATHS.md`.
