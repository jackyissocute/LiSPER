# LiSPER storage layout (2026-07-12)

## Rule

| Layer | Path | Holds |
|---|---|---|
| **A — GitHub + Mac git worktree** | `~/Documents/GitHub/LiSPER` | Code, docs, site manifests, QC protocols, audit TSVs, lean `pullf`/`xvg`, ΔΔG tables when ready |
| **B — Jacky 1TB cold (optional mount)** | `/Volumes/Jacky 1TB/Research/LiSPER_cold/` | Fat runtime (`.xtc`, window piles, `.edr`, `.cpt`), WHAM packs, rebuild seeds, cold archive |

Live `git commit` / `git push` only from the **Mac** worktree. Do **not** put the live git root on ExFAT Jacky 1TB.

Disk is often **unplugged**. Automations and day-to-day syncs keep **lean Part A** on Mac/GitHub. Fat Part B lands on the 1TB the next time it is mounted.

## Cold disk map (open `ACTIVE/` first)

```
LiSPER_cold/
├── README.txt
├── ACTIVE/                          ← use this
│   ├── incoming/                    ★ NEW fat remote syncs
│   │   ├── umbrella/
│   │   ├── pmf/
│   │   └── md/
│   └── seeds/                       rebuild inputs (keep)
│       ├── charmm_gui_systems/
│       └── gcp_remote_backup_20260712/
└── ARCHIVE/                         ← cold archive only (not for ranking)
```

| Path | Role |
|---|---|
| `ACTIVE/incoming/` | Write target for new locked-site umbrella / WHAM / MD fat syncs |
| `ACTIVE/seeds/charmm_gui_systems/` | CHARMM-GUI LiCl + NaCl seeds for remote rebuild |
| `ACTIVE/seeds/gcp_remote_backup_20260712/` | GCP remote science snapshot (no `.xtc`/`.trr`) |
| `ARCHIVE/` | Cold archive — not for ΔΔG ranking |

## Sync policy

| When | What goes where |
|---|---|
| Always (disk optional) | Lean QC, manifests, ΔΔG tables → Mac git / GitHub |
| Disk plugged | Fat windows, trajectories, WHAM packs → `ACTIVE/incoming/{umbrella,pmf,md}/` |
| Disk unplugged | Skip fat copy; queue until next mount |

## Fresh umbrella restart

1. Reconstruct bound starts → record `GEOMETRY_SCREENED_BOUND_START` in `umbrella/paired_site_manifests/`; this is a geometry screen, not binding validation.
2. Launch locked-site umbrella (pilot: **LiLC-1**).
3. Sync new fat outputs to `ACTIVE/incoming/`; keep GitHub lean.

See `umbrella/remote_runs_umbrella_sampling_status.md` .
