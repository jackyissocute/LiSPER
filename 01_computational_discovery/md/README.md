# Molecular Dynamics

MD stage for the 8-candidate library: min → eq → 20 ns prod → clustering → representative handoff.

## Status (2026-07-12)

| Condition | State |
|---|---|
| LiCl | Complete — 8/8 production + reps |
| NaCl | Clustering done; lean Mac sync (some topols restored from Jacky seeds) |
| Free energy | Locked-site restart — see `../umbrella/PREFLIGHT_RUNBOOK.md` |

Fat trajectories / rebuild seeds: Jacky `ACTIVE/seeds/` (`../STORAGE_LAYOUT.md`).  
Paths / next CPU: `remote_orchestration/SYNC_PATHS.md` (**EPYC 9554P**).

## Layout

| Path | Role |
|---|---|
| `li_cl/` `na_cl/` | Per-ion remote_runs (logs) + remote_results (lean systems) |
| `remote_orchestration/` | MD drivers + `SYNC_PATHS.md` |

Umbrella / WHAM live in sibling folders `../umbrella/` and `../pmf/`.
