# Umbrella Sampling Status

Last updated: 2026-07-12 23:32 CST

## Decision (authoritative)

**Locked-site restart is live.** Legacy umbrella v1–v4 stays diagnostic only (`0/8` same chemical site). Do **not** resume those for ΔΔG ranking.

| Item | Value |
|---|---|
| Active host | EPYC 9554P 128t (`lisper-epyc`) |
| Active campaign | **LiLC-1** locked-site pilot (LiCl + NaCl) |
| Stage | Pull complete; window eq ~50% (≈249 ps / 500 ps; 30 windows/ion; 0 failed) |
| Drivers | 2 alive; 60 real `gmx mdrun -deffnm umbrella_eq` (30 LiCl + 30 NaCl) |
| Slot occupancy | **60 active / 124** (64 free held for Phase D — do not fan other candidates yet) |
| Rate | ~126 ps/h ≈ **3.0 ns/day** per 1-thread mdrun |
| ETA | eq rem ~2.0 h → prod 2.0 ns ≈ 16 h → first ΔΔG row **~0.8 d** after WHAM/QC |
| Legacy resume / watchdog | **Obsolete — do not relaunch** |
| Next after windows | Finish eq → umbrella prod (2.0 ns) → WHAM → `evaluate_paired_pmf_qc.py`; scale other 7 only on PASS |
| Storage policy | Part A on GitHub/Mac; fat B+C on Jacky 1TB (`../STORAGE_LAYOUT.md`) |

## Paired site-lock status

| Candidate | Classification | Locked site | Status |
|---|---|---|---|
| `LiLC-1` | preferred pilot | terminal Asp14 | **VALIDATED_BOUND** — window eq ~50% (both ions) |
| `LiD3-Core` | review | central Asp9 | **VALIDATED_BOUND** (both ions; queued post-pilot) |
| `LiD3-Flex` | rerun required | central Asp11 | **VALIDATED_BOUND** (both ions; queued post-pilot) |
| `LiND-Hybrid` | rerun required | central Asp11 | **VALIDATED_BOUND** (both ions; queued post-pilot) |
| `LiDS-1` | review | central Asp7 | **VALIDATED_BOUND** (both ions; queued post-pilot) |
| `LiDA-1` | rerun required | central Asp7/Asp9 | **VALIDATED_BOUND** (both ions; queued post-pilot) |
| `LiN3-Core` | review | central Asn9 | **VALIDATED_BOUND** (both ions; queued post-pilot) |
| `LiA3-Ref` | rerun required | central Ala9 backbone | **VALIDATED_BOUND** (both ions; queued post-pilot) |

## Keep in this repo (Part A)

- `paired_site_manifests/*.tsv`
- `paired_binding_site_audit.tsv` / `paired_binding_site_design.tsv`
- `LISPER_UMBRELLA_QC_PROTOCOL.md`
- `remote_orchestration/scripts/` (site-lock gated driver)
- Empty `remote_runs/` / `remote_results/` for new campaigns

## Next science steps

1. Let LiLC-1 window eq finish → umbrella prod (2.0 ns) → WHAM.
2. Run `evaluate_paired_pmf_qc.py`; promote only on PASS.
3. Scale remaining 7 (already `VALIDATED_BOUND`) under same locked-site protocol toward 124/124.
4. Write `selectivity_summary.tsv` (ΔΔG table).
5. Sync fat → Jacky `ACTIVE/incoming/`; lean QC + ΔΔG → GitHub.
