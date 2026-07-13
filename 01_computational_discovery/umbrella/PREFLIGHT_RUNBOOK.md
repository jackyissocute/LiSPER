# Locked-site campaign preflight runbook

Date: 2026-07-12  
Purpose: avoid the old mess (rent → blast parallel → fail QC → repair forever).

**Hard rule:** Do **not** rent CPU to “finish ranking” until Phase A–B evidence is complete. Renting early is how the last campaign burned days.

## Why last run felt awful

| Failure | What happened | Fix before next rent |
|---|---|---|
| Wrong estimand | Dynamic-nearest donors → Li/Na different pockets | Locked manifests + geometry-screened starts only |
| Parallel everything | 8×2 campaigns + repairs interleaved | One pilot pair first; scale only after method review |
| QC after burn | WHAM diagnostics checked after days of windows | Evidence plan + diagnostic analysis before scale-up |
| Thin local inputs | Mac lean sync; no prod `.xtc` | Restore seeds / re-produce before umbrella |
| Thread ceiling | Driver default `GLOBAL_MDRUN_LIMIT=28` | Set `~threads−4` on 100-core host |

## Phases (do in order)

### Phase A — Inventory (no rent)

```bash
python3 01_computational_discovery/umbrella/remote_orchestration/scripts/check_campaign_readiness.py \
  --pilot \
  --out 01_computational_discovery/umbrella/preflight_readiness_pilot.tsv

python3 01_computational_discovery/umbrella/remote_orchestration/scripts/check_campaign_readiness.py \
  --out 01_computational_discovery/umbrella/preflight_readiness_all.tsv
```

Expect today: **not READY**. Typical blockers: `MISSING_XTC`, `MISSING_TOPOL`, `BLOCKED_SITE_LOCK`.

Also plug Jacky 1TB and confirm:

| Path | Need |
|---|---|
| `ACTIVE/seeds/charmm_gui_systems/` | NaCl topologies / rebuild seeds |
| `ACTIVE/seeds/gcp_remote_backup_20260712/` | System trees (no xtc by design) |
| Cold-disk seed archive | Optional hunt for prior `representative_full_system.gro` if rebuilding starts |

### Phase B — Bound starts (still mostly local / short remote)

For each ion of **LiLC-1**:

1. Obtain full-system start `representative_full_system.gro` at locked Asp14 pocket.
   - Preferred: extract cluster-rep frame from recovered/re-run prod `.xtc`.
   - If ion too far from locked centroid: short steered placement + brief eq (document it).
2. Validate:

```bash
python3 .../validate_bound_start.py \
  --gro /path/to/representative_full_system.gro \
  --manifest 01_computational_discovery/umbrella/paired_site_manifests/LiLC-1.tsv \
  --ion-resname LI \
  --record
```

Repeat for `SOD`. The current `distance ≤ 0.55 nm` check records starting geometry only; it is not proof of binding, convergence, or PMF reliability.

Driver still refuses launch until `starting_state_status=GEOMETRY_SCREENED_BOUND_START`; this is an operational geometry check, not proof of binding.

### Phase C — Rent AMD EPYC 9554P (128 threads)

Host: see `remote_orchestration/PROVIDER.md` + `launch_locked_site.env.example`.

```bash
export LISPER_GLOBAL_MDRUN_LIMIT=124   # 128 − 4 reserve
export LISPER_JOBS=32
```

Reject: 9575F (2× price), dual-socket ~$0.72 boxes (thin disk / older), 9754 unless you want max parallel and accept higher $/hr.
### Phase D — Pilot only (LiLC-1 LiCl + NaCl)

```bash
# estimate first
python3 .../estimate_umbrella_campaign.py --threads 128 --candidates 1
```

Launch **one candidate, both ions**, locked-site driver only.

After windows complete → WHAM →:

```bash
python3 01_computational_discovery/pmf/remote_orchestration/scripts/record_paired_analysis_plan.py \
  --li-metadata .../LiCl/umbrella_metadata.tsv \
  --na-metadata .../NaCl/umbrella_metadata.tsv \
  --bound-min ... --bound-max ... --ref-min ... --ref-max ... \
  --bound-rationale "..." --reference-rationale "..." \
  --out .../pmf/LiLC-1/paired_regions.tsv

python3 01_computational_discovery/pmf/remote_orchestration/scripts/run_wham_qc.py \
  --umbrella-dir .../LiLC-1/gromacs/umbrella_sampling \
  --out .../pmf/LiLC-1/LiCl

python3 01_computational_discovery/pmf/remote_orchestration/scripts/summarize_paired_pmf_evidence.py \
  --candidate LiLC-1 \
  --li-profile ... --na-profile ... \
  --li-bootstrap-profiles ... --na-bootstrap-profiles ... \
  --li-time-profiles ... ... --na-time-profiles ... ... \
  --li-histo ... --na-histo ... \
  --li-iact ... --na-iact ... \
  --bootstrap-method traj_with_gmx_iact \
  --wham-log-files ... \
  --regions .../pmf/LiLC-1/paired_regions.tsv \
  --out .../LiLC-1_paired_evidence.tsv
```

The summary contains measurements and limitations, not a binary verdict. Use the
overlap, IACT, time-block, replica, and sensitivity evidence to decide the next
scientific action. Do not redesign the site or estimator after seeing a preferred
selectivity result.

### Phase E — Scale remaining 7 (only after documented pilot method review)

Same protocol, same spacing/eq/prod/guards, same shared regions rule. Fan out across 124 mdrun slots.

Fat sync → Jacky `ACTIVE/incoming/{umbrella,pmf}/`  
Lean QC + ΔΔG table → Mac git / GitHub.

### Phase F — ΔΔG table

Only after the estimand and uncertainty evidence support each stated row:

- `pmf/.../delta_g_summary.tsv`
- `pmf/.../selectivity_summary.tsv`
- Release / delete `DELTA_G_PROMOTION_HOLD.md`

## Anti-mess rules (non-negotiable)

1. No dynamic-nearest `umbrella_sampling_binding_site_v2`.
2. No resume/watchdog scripts.
3. No promoting ΔG while hold file exists.
4. No “fix while seven others still running” chaos — pilot gate first.
5. No changing bound/ref regions after seeing a preferred selectivity contrast.
6. Disk unplugged OK for lean sync; fat waits for Jacky mount.

## Confidence checklist before you pay for the VM

- [ ] Readiness TSV reviewed (pilot blockers known)
- [ ] Jacky seeds confirmed mounted at least once
- [ ] LiLC-1 both ions `GEOMETRY_SCREENED_BOUND_START` + geometry logs
- [ ] Launch env uses `GLOBAL_MDRUN_LIMIT=124` on EPYC 9554P, 1 thread/window
- [ ] WHAM evidence summarizer and IACT-aware analysis path known
- [ ] Sync plan: lean→git, fat→`ACTIVE/incoming/`
- [ ] Emotional contract: pilot method evidence before all-8 blast
