# LiSPER storage layout (2026-07-12)

## Rule

| Layer | Path | Holds |
|---|---|---|
| **A — GitHub + Mac git worktree** | `~/Documents/GitHub/LiSPER` | Code, docs, site manifests, QC protocols, audit TSVs, ΔΔG tables when ready |
| **B+C — Jacky 1TB cold** | `/Volumes/Jacky 1TB/Research/LiSPER_cold/` | Fat runtime (`.xtc`, logs, `.edr`, `.cpt`, window piles), analysis packs (`pullf`/`pullx`/`tpr`), GCP backup, CHARMM-GUI seeds |

Live `git commit` / `git push` only from the **Mac** worktree. Do **not** put the live git root on ExFAT Jacky 1TB.

## Cold archive map

| Folder | Contents |
|---|---|
| `01_gcp_remote_backup_20260712/` | Full GCP remote science backup (no `.xtc`/`.trr`) |
| `02_legacy_umbrella_unreliable/` | All legacy US v1/v2/v3/v4 window dumps — **not for ranking** |
| `03_legacy_pmf_diagnostic/` | Legacy WHAM/PMF products — diagnostic only |
| `04_charmm_gui_systems/` | CHARMM-GUI system seeds for remote rebuild |
| `05_future_remote_sync/` | Empty; land new remote fat syncs here |
| `06_repo_archive_legacy_10_candidate_library/` | Superseded 10-candidate library |

## Fresh umbrella restart

1. Reconstruct bound starts → mark `VALIDATED_BOUND` in `umbrella/paired_site_manifests/`.
2. Launch locked-site umbrella (pilot: **LiLC-1**).
3. Sync new fat outputs to `05_future_remote_sync/`, keep GitHub lean.

See `umbrella/remote_runs_umbrella_sampling_status.md` and `pmf/LEGACY_DATA_EVALUATION.md`.
