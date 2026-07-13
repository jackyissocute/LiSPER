# Locked-site campaign preflight runbook

Date: 2026-07-12  
Purpose: run paired Li/Na umbrella campaigns without duplicate work or hidden analysis assumptions.

**Hard rule:** real GROMACS failures and missing inputs stop the affected scope; numerical convergence diagnostics are reported, not converted into invented universal PASS gates.

## Why last run felt awful

| Failure | What happened | Fix before next rent |
|---|---|---|
| Wrong estimand | Dynamic-nearest donors → Li/Na different pockets | Locked manifests + `VALIDATED_BOUND` only |
| Unsafe parallelism | Process-count limiter ignored multi-thread pulls | Thread-aware 124-thread ceiling shared by all campaigns |
| QC after burn | WHAM gates checked after days of windows | Predeclared gates + automated evaluator |
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
  --promote
```

Repeat for `SOD`. Only promote when **both** ions PASS (`distance ≤ 0.55 nm` default).

Driver still refuses launch until `starting_state_status=VALIDATED_BOUND`.

### Phase C — Rent AMD EPYC 9554P (128 threads)

Host: see `remote_orchestration/PROVIDER.md` + `launch_locked_site.env.example`.

```bash
export LISPER_GLOBAL_MDRUN_LIMIT=124   # 128 − 4 reserve
export LISPER_JOBS=32
```

Reject: 9575F (2× price), dual-socket ~$0.72 boxes (thin disk / older), 9754 unless you want max parallel and accept higher $/hr.
### Phase D — Paired production

```bash
# estimate first
python3 .../estimate_umbrella_campaign.py --threads 128 --candidates 1
```

Launch all eight candidates for both ions with the locked-site driver and the node-wide 124-thread ceiling. After windows complete → WHAM →:

```bash
python3 01_computational_discovery/pmf/remote_orchestration/scripts/lock_paired_regions.py \
  --li-metadata .../LiCl/umbrella_metadata.tsv \
  --na-metadata .../NaCl/umbrella_metadata.tsv \
  --out .../pmf/LiLC-1/paired_regions.tsv

python3 01_computational_discovery/pmf/remote_orchestration/scripts/run_wham_qc.py \
  --umbrella-dir .../LiLC-1/gromacs/umbrella_sampling \
  --out .../pmf/LiLC-1/LiCl

python3 01_computational_discovery/pmf/remote_orchestration/scripts/evaluate_paired_pmf_qc.py \
  --candidate LiLC-1 \
  --li-profile ... --na-profile ... \
  --li-bootstrap ... --na-bootstrap ... \
  --li-half-early ... --li-half-late ... \
  --na-half-early ... --na-half-late ... \
  --li-burnin ... ... --na-burnin ... ... \
  --li-histo ... --na-histo ... \
  --wham-warning-files ... \
  --regions .../pmf/LiLC-1/paired_regions.tsv \
  --out .../LiLC-1_paired_qc.tsv
```

The evaluator writes `ESTIMATE_READY` or `ESTIMATE_WITH_WARNINGS`; both retain the numerical Delta G and Delta Delta G. Missing windows or a fatal WHAM error have no estimate and must be repaired.

### Phase E — Diagnostics and table

Use the same spacing/eq/prod/guards and shared endpoint regions within each Li/Na pair. Fan out across at most 124 real mdrun threads.

Fat sync → Jacky `ACTIVE/incoming/{umbrella,pmf}/`  
Lean QC + ΔΔG table → Mac git / GitHub.

### Phase F — ΔΔG table

After paired WHAM profiles exist:

- `pmf/.../delta_g_summary.tsv`
- `pmf/.../selectivity_summary.tsv`

## Anti-mess rules (non-negotiable)

1. No dynamic-nearest `umbrella_sampling_binding_site_v2`.
2. No resume/watchdog scripts.
3. Do not hide overlap, time-sensitivity, or uncertainty diagnostics.
4. Fix only the failed scope while unrelated campaigns continue.
5. Do not change bound/ref regions after seeing a preferred ΔΔG.
6. Disk unplugged OK for lean sync; fat waits for Jacky mount.

## Confidence checklist before you pay for the VM

- [ ] Readiness TSV reviewed (pilot blockers known)
- [ ] Jacky seeds confirmed mounted at least once
- [ ] LiLC-1 both ions `VALIDATED_BOUND` + validation logs
- [ ] Launch env uses `GLOBAL_MDRUN_LIMIT=124` on EPYC 9554P, 1 thread/window
- [ ] WHAM estimator and diagnostic paths known
- [ ] Sync plan: lean→git, fat→`ACTIVE/incoming/`
- [ ] All campaign launches share the 124-thread ceiling and reject duplicates
