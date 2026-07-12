# Umbrella Sampling Status

Last updated: 2026-07-12 16:55 CST

## Decision (authoritative)

**Clean restart.** All legacy umbrella v1/v2/v3/v4 data removed from this git worktree and archived to Jacky 1TB.

Cold path: `/Volumes/Jacky 1TB/Research/LiSPER_cold/ARCHIVE/legacy_umbrella_unreliable/`

Those campaigns remain **diagnostic only** (`0/8` same chemical site). Do **not** resume them for ΔΔG ranking.

| Item | Value |
|---|---|
| Repo US workdirs | Empty scaffolds under `remote_runs/` / `remote_results/` |
| Legacy resume / watchdog | **Obsolete — do not relaunch** |
| Next authorized work | Reconstruct/validate bound starts → `VALIDATED_BOUND` → locked-site pilot **LiLC-1** |
| Storage policy | Part A on GitHub/Mac; fat B+C on Jacky 1TB (`../STORAGE_LAYOUT.md`) |

## Paired site-lock audit (still required before launch)

| Candidate | Classification | Proposed locked site | Next action |
|---|---|---|---|
| `LiD3-Core` | `SITE_MISMATCH_PARTIAL_OVERLAP_REVIEW` | central Asp9 | reconstruct/validate both bound starts |
| `LiD3-Flex` | `SITE_MISMATCH_RERUN_REQUIRED` | central Asp11 | reconstruct/validate both bound starts |
| `LiND-Hybrid` | `SITE_MISMATCH_RERUN_REQUIRED` | central Asp11 | reconstruct/validate both bound starts |
| `LiLC-1` | `SITE_MISMATCH_PARTIAL_OVERLAP_REVIEW` | terminal Asp14 | **preferred first locked-site pilot** |
| `LiDS-1` | `SITE_MISMATCH_PARTIAL_OVERLAP_REVIEW` | central Asp7 | reconstruct/validate both bound starts |
| `LiDA-1` | `SITE_MISMATCH_RERUN_REQUIRED` | central Asp7/Asp9 | reconstruct Na-bound central pocket |
| `LiN3-Core` | `SITE_MISMATCH_PARTIAL_OVERLAP_REVIEW` | central Asn9 | reconstruct/validate both bound starts |
| `LiA3-Ref` | `SITE_MISMATCH_RERUN_REQUIRED` | central Ala9 backbone | reconstruct low-donor control starts |

## Keep in this repo (Part A)

- `paired_site_manifests/*.tsv`
- `paired_binding_site_audit.tsv` / `paired_binding_site_design.tsv`
- `LISPER_UMBRELLA_QC_PROTOCOL.md`
- `remote_orchestration/scripts/` (site-lock gated driver)
- Empty `remote_runs/` / `remote_results/` for new campaigns

## Next science steps

Follow `PREFLIGHT_RUNBOOK.md` (do **not** rent until Phase A–B pass).

1. Run readiness inventory (`check_campaign_readiness.py`) — expect MISSING_XTC / BLOCKED_SITE_LOCK today.
2. Reconstruct LiLC-1 LiCl/NaCl bound starts on locked Asp14 donors; `validate_bound_start.py --promote`.
3. Rent AMD EPYC **9554P** (128t); use `launch_locked_site.env.example` (`GLOBAL_MDRUN_LIMIT=124`).
4. Pilot LiLC-1 only → WHAM → `evaluate_paired_pmf_qc.py`; scale other 7 only after PASS.
5. Sync fat → Jacky `ACTIVE/incoming/`; lean QC + ΔΔG → GitHub.
