# Umbrella Sampling Status

Last updated: 2026-07-12 20:30 CST

## Decision (authoritative)

**Locked-site restart is live.** Legacy umbrella v1–v4 stays diagnostic only (`0/8` same chemical site). Do **not** resume those for ΔΔG ranking.

| Item | Value |
|---|---|
| Active host | EPYC 9554P 128t (`lisper-epyc`) |
| Active campaign | **LiLC-1** locked-site pilot (LiCl + NaCl) |
| Stage | Pull ~3% (29 ps / 1000 ps both ions) |
| Drivers | 2 alive; 2 `mdrun -deffnm pull` |
| Legacy resume / watchdog | **Obsolete — do not relaunch** |
| Next after windows | WHAM → `evaluate_paired_pmf_qc.py`; scale other 7 only on PASS |
| Storage policy | Part A on GitHub/Mac; fat B+C on Jacky 1TB (`../STORAGE_LAYOUT.md`) |

## Paired site-lock status

| Candidate | Classification | Locked site | Status |
|---|---|---|---|
| `LiLC-1` | preferred pilot | terminal Asp14 | **VALIDATED_BOUND** — pull running |
| `LiD3-Core` | review | central Asp9 | await pilot PASS then reconstruct |
| `LiD3-Flex` | rerun required | central Asp11 | await pilot PASS then reconstruct |
| `LiND-Hybrid` | rerun required | central Asp11 | await pilot PASS then reconstruct |
| `LiDS-1` | review | central Asp7 | await pilot PASS then reconstruct |
| `LiDA-1` | rerun required | central Asp7/Asp9 | await pilot PASS then reconstruct |
| `LiN3-Core` | review | central Asn9 | await pilot PASS then reconstruct |
| `LiA3-Ref` | rerun required | central Ala9 backbone | await pilot PASS then reconstruct |

## Keep in this repo (Part A)

- `paired_site_manifests/*.tsv`
- `paired_binding_site_audit.tsv` / `paired_binding_site_design.tsv`
- `LISPER_UMBRELLA_QC_PROTOCOL.md`
- `remote_orchestration/scripts/` (site-lock gated driver)
- Empty `remote_runs/` / `remote_results/` for new campaigns

## Next science steps

1. Let LiLC-1 pull finish → windows (0.075 nm spacing) → WHAM.
2. Run `evaluate_paired_pmf_qc.py`; promote only on PASS.
3. Scale remaining 7 under same locked-site protocol.
4. Write `selectivity_summary.tsv` (ΔΔG table).
5. Sync fat → Jacky `ACTIVE/incoming/`; lean QC + ΔΔG → GitHub.
