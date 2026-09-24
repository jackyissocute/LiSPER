# Molecular Dynamics

MD stage for the 8-candidate library: min → eq → 20 ns prod → clustering → representative handoff.

## Status

| Condition | State |
|---|---|
| LiCl | Complete — 8/8 production + reps |
| NaCl | Complete — 8/8 production + reps |
| Free energy | All 16 paired pulls and the eight paired PMF analyses complete; see `../pmf/` |

Fat trajectories / rebuild seeds: Jacky `ACTIVE/seeds/` (`../STORAGE_LAYOUT.md`).  
Historical paths and compute setup: `remote_orchestration/SYNC_PATHS.md`.

## Layout

| Path | Role |
|---|---|
| `li_cl/` `na_cl/` | Per-ion remote_runs (logs) + remote_results (lean systems) |
| `remote_orchestration/` | MD drivers + `SYNC_PATHS.md` |

Umbrella / WHAM live in sibling folders `../umbrella/` and `../pmf/`.
