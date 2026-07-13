# Umbrella Sampling Status

Last updated: 2026-07-13 08:09 CST

## Decision (authoritative)

Locked-site umbrella campaign is live on a remote EPYC 9554P worker.

| Item | Value |
|---|---|
| Active host | EPYC 9554P 128t worker |
| Active campaign | **LiLC-1** locked-site pilot (LiCl + NaCl) |
| Stage | Pull + 0.5 ns window eq complete; 2.0 ns window production ~42% (≈832 ps LiCl / 838 ps NaCl average; 30 windows/ion; 0 failed) |
| Drivers | 2 alive; 60 `mdrun -deffnm umbrella` (30 LiCl + 30 NaCl) |
| Bound starts | **8/8** `VALIDATED_BOUND` |
| Next after windows | Finish umbrella prod (2.0 ns) → WHAM → `evaluate_paired_pmf_qc.py`; scale other 7 only on PASS |
| Capacity | 60/124 real one-thread `mdrun`; 64 slots idle because the pilot has no additional distinct ready windows |

## Paired site-lock status

| Candidate | Classification | Locked site | Status |
|---|---|---|---|
| `LiLC-1` | preferred pilot | terminal Asp14 | **VALIDATED_BOUND** — window production ~42% |
| `LiD3-Core` | scale queue | central Asp9 | **VALIDATED_BOUND** — await pilot PASS |
| `LiD3-Flex` | scale queue | central Asp11 | **VALIDATED_BOUND** — await pilot PASS |
| `LiND-Hybrid` | scale queue | central Asp11 | **VALIDATED_BOUND** — await pilot PASS |
| `LiDS-1` | scale queue | central Asp7 | **VALIDATED_BOUND** — await pilot PASS |
| `LiDA-1` | scale queue | central Asp7/Asp9 | **VALIDATED_BOUND** — await pilot PASS |
| `LiN3-Core` | scale queue | central Asn9 | **VALIDATED_BOUND** — await pilot PASS |
| `LiA3-Ref` | scale queue | central Ala9 backbone | **VALIDATED_BOUND** — await pilot PASS |

## Keep in this repo (Part A)

- `paired_site_manifests/*.tsv`
- `paired_binding_site_audit.tsv` / `paired_binding_site_design.tsv`
- `LISPER_UMBRELLA_QC_PROTOCOL.md`
- `remote_orchestration/scripts/` (site-lock gated driver)
- Empty `remote_runs/` / `remote_results/` for new campaigns

## Next science steps

1. Let LiLC-1 window production finish → WHAM.
2. Run `evaluate_paired_pmf_qc.py`; promote only on PASS.
3. Scale remaining 7 under same locked-site protocol toward 124/124.
4. Write `selectivity_summary.tsv` (ΔΔG table).
5. Sync fat → Jacky `ACTIVE/incoming/`; lean QC + ΔΔG → GitHub.
