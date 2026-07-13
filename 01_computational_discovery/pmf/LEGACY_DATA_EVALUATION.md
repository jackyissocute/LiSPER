# Legacy umbrella / PMF evaluation (2026-07-12)

Goal: publishable paired ΔΔG with **same chemical binding-site definition** for Li+ and Na+.

Verdict: **stop legacy dynamic-nearest campaigns**. Do not finish them for ranking. Restart only under locked-site `VALIDATED_BOUND` manifests.

## Keep (needed for locked-site rebuild)

| Asset | Why |
|---|---|
| 20 ns LiCl/NaCl production + clustering + representatives | Inputs for reconstructing validated bound starts |
| `umbrella/paired_binding_site_audit.tsv` | Evidence: `0/8 SITE_LOCKED`; mismatch classification |
| `umbrella/paired_binding_site_design.tsv` + `paired_site_manifests/*.tsv` | Proposed locked donors (status still `PROPOSED_REQUIRES_RECONSTRUCTION`) |
| `umbrella/LISPER_UMBRELLA_QC_PROTOCOL.md` + drivers with site-lock gates | Method for next campaigns |
| Compact QC summary TSVs / warning excerpts | Show why legacy WHAM is not promoted |

## Diagnostic only (not publishable paired selectivity)

| Asset | Why not final |
|---|---|
| All `umbrella_sampling_binding_site_v2` Li/Na campaigns | Donors chosen independently per ion → site identity broken |
| Existing WHAM/PMF under `pmf/remote_results/gcp_*` and `pmf/remote_runs/` | Estimands not same-site; outer-tail / burn-in issues secondary |
| Legacy resume / watchdog scripts | Would burn CPU on mismatched RC; **do not relaunch** |

## Discard from GitHub (keep on remote disk only if useful)

Bulky GROMACS binaries and raw WHAM curves from mismatched campaigns mislead reviewers if treated as results. Untracked via `.gitignore`. Fat copies live on Jacky:

`/Volumes/Jacky 1TB/Research/LiSPER_cold/ARCHIVE/legacy_{umbrella_unreliable,pmf_diagnostic}/`

Patterns: window `*.gro` / `*.edr` / `*.cpt` / `*.tpr` / `*.log` / `*.xvg` / `*.mdp`.

## Required before the new ΔG / ΔΔG table

1. Reconstruct bound starts that sit in the **proposed locked chemical site** for both ions.
2. Mark manifests `VALIDATED_BOUND` (logs of site check).
3. New umbrella + WHAM under the paired site definition.
4. Report overlap, time sensitivity, endpoint span, and uncertainty numerically alongside every estimate.

## Compute policy

- Legacy resume / watchdog: **archived** (Jacky `ARCHIVE/legacy_ops_docs_20260712/`). Do not relaunch.
- Active host: AMD EPYC **9554P**. Fresh paired campaigns run in parallel; mismatched v2/v3/v4 sets remain diagnostic only.
