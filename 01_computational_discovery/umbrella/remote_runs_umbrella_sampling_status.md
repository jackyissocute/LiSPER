# Umbrella Sampling Status

Last updated: 2026-07-12 14:10 CST

## Decision (authoritative)

**Stop legacy umbrella.** Dynamic-nearest v2/v3/v4 Li/Na campaigns are **diagnostic only** (`0/8` same chemical site). Do not finish them for ΔΔG ranking.

Full evaluation: [`../pmf/LEGACY_DATA_EVALUATION.md`](../pmf/LEGACY_DATA_EVALUATION.md). Promotion hold: [`../pmf/DELTA_G_PROMOTION_HOLD.md`](../pmf/DELTA_G_PROMOTION_HOLD.md).

| Item | Value |
|---|---|
| Host | QuickPod `quickpod-lisper` (`root@217.254.101.12:63014`) |
| Remote root | `/data/LiSPER_remote` |
| Legacy resume / watchdog | **Obsolete — do not relaunch** |
| Next authorized work | Reconstruct/validate bound starts → `VALIDATED_BOUND` → locked-site pilot **LiLC-1** |
| GCP | Soft-stopped backup disk only |

If QuickPod still runs legacy `gmx mdrun`, kill them (host may be too loaded for SSH banner — reboot from QuickPod UI if needed, then confirm `pgrep -af 'gmx mdrun'` is empty).

## Paired site-lock audit

| Candidate | Current paired classification | Proposed locked site | Next action |
|---|---|---|---|
| `LiD3-Core` | `SITE_MISMATCH_PARTIAL_OVERLAP_REVIEW` | central Asp9 | reconstruct/validate both bound starts |
| `LiD3-Flex` | `SITE_MISMATCH_RERUN_REQUIRED` | central Asp11 | reconstruct/validate both bound starts |
| `LiND-Hybrid` | `SITE_MISMATCH_RERUN_REQUIRED` | central Asp11 | reconstruct/validate both bound starts |
| `LiLC-1` | `SITE_MISMATCH_PARTIAL_OVERLAP_REVIEW` | terminal Asp14 | **preferred first locked-site pilot** |
| `LiDS-1` | `SITE_MISMATCH_PARTIAL_OVERLAP_REVIEW` | central Asp7 | reconstruct/validate both bound starts |
| `LiDA-1` | `SITE_MISMATCH_RERUN_REQUIRED` | central Asp7/Asp9 | reconstruct Na-bound central pocket |
| `LiN3-Core` | `SITE_MISMATCH_PARTIAL_OVERLAP_REVIEW` | central Asn9 | reconstruct/validate both bound starts |
| `LiA3-Ref` | `SITE_MISMATCH_RERUN_REQUIRED` | central Ala9 backbone | reconstruct low-donor control starts |

## Legacy campaign archive (not ranking inputs)

Completed or partial mismatched-site windows remain on remote disk for forensics. Git keeps audit TSVs and QC summaries only; bulky `.gro`/`.xvg`/logs are gitignored.

| Candidate | Condition | Legacy set (approx) | Publishable paired ΔΔG? |
|---|---|---|---|
| `LiDA-1` | LiCl / NaCl | V4 complete + WHAM | No — site mismatch |
| `LiDS-1` | LiCl / NaCl | V2 complete + WHAM | No — site mismatch |
| `LiD3-Flex` | LiCl / NaCl | V3 partial + NaCl V2 WHAM | No — site mismatch |
| Others | LiCl / NaCl | V2 incomplete | No — stop; do not finish for ranking |

## Next science steps (only)

1. Stop any remaining legacy mdrun on QuickPod.
2. Reconstruct bound starts into proposed locked chemical donors for **LiLC-1** (both ions).
3. Log site validation; set manifests to `VALIDATED_BOUND`.
4. Launch new locked-site umbrella for LiLC-1 only; expand after pilot passes QC.
