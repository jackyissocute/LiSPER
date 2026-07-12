# Window assignment plan — lisper-epyc (EPYC 9554P, 128 threads)

Date: 2026-07-12  
Host: `lisper-epyc` → `root@84.32.71.226`  
GROMACS: `/opt/gromacs/2026.0` (target), 1 thread per window

## Hardware budget

| Resource | Value |
|---|---|
| Threads | 128 |
| Reserve (SSH / WHAM / rsync / OS) | 4 |
| **Concurrent `gmx mdrun`** | **`LISPER_GLOBAL_MDRUN_LIMIT=124`** |
| Pull threads (2 jobs only) | `LISPER_PULL_NTHREADS=60` each → use CPU while pull runs |
| Per-window threads | `-ntmpi 1 -ntomp 1` (`LISPER_NTHREADS=1`) |
| Per-driver queue depth | `LISPER_JOBS=124` (global lock caps at 124) |

## Protocol (fixed — do not change mid-campaign)

| Param | Value |
|---|---|
| Pull | 1.0 ns (serial per condition, before windows) |
| Window eq | 0.5 ns |
| Window prod | 2.0 ns |
| Spacing | 0.075 nm |
| Analysis extension | 2.00 nm (PBC-capped) |
| Guard windows | 3 |
| Force constant | 1000 kJ/mol/nm² |

Typical windows/condition ≈ **31** (analysis + guards from ~0.45 nm bound start).

## Phase schedule

### Phase D — Pilot (LiLC-1 only)

| Track | Workdir | Ion | Windows | Threads used |
|---|---|---|---:|---:|
| A | `LiSPER_8cand_LiCl` | LI | ~31 | up to 31 |
| B | `LiSPER_8cand_NaCl_prod_worker` | SOD | ~31 | up to 31 |

**Assignment:** after pull, fan both tracks into the global 124-slot pool. LiLC-1 alone ≈ 62 window jobs (fills what exists). After pilot PASS, launch more candidates so occupancy approaches **124/124**.

Wall estimate @ ~4.6 ns/day/thread: **~0.5 day** (pull + windows).

Launch pattern:

```bash
source /data/LiSPER_remote/scripts/launch_locked_site.env
# terminal 1 (tmux)
export LISPER_WORKDIR=.../LiSPER_8cand_LiCl LISPER_CANDIDATE=LiLC-1 LISPER_ION_RESNAME=LI
python3 /data/LiSPER_remote/scripts/run_lisper_umbrella_sampling.py
# terminal 2
export LISPER_WORKDIR=.../LiSPER_8cand_NaCl_prod_worker LISPER_CANDIDATE=LiLC-1 LISPER_ION_RESNAME=SOD
python3 /data/LiSPER_remote/scripts/run_lisper_umbrella_sampling.py
```

### Phase E — Scale (only after LiLC-1 paired QC PASS)

8 candidates × 2 ions = **16 conditions** × ~31 windows = **~496 window jobs**.

| Mode | How | Peak mdrun | Est. wall |
|---|---|---:|---:|
| **Recommended** | Fan all incomplete windows into global 124-slot pool (multiple drivers) | 124 | ~2.4 days |
| Conservative | 2 candidates at a time (4 conditions) | ≤124 | longer, safer ops |

Do **not** start Phase E until Phase D WHAM QC = PASS.

## WHAM / ΔG slotting

After a condition’s windows finish:

1. Build `tpr-files.dat` + `pullf-files.dat` (analysis windows only; guards optional/excluded per QC protocol).
2. Run `gmx wham` on **1–2 cores** (not 124) while other umbrella tracks continue.
3. Reserve ~4 threads always free so WHAM + SSH never starve.

Paired QC: `evaluate_paired_pmf_qc.py` on Mac or remote after both ions ready.

## Anti-thrash rules

1. Never exceed `LISPER_GLOBAL_MDRUN_LIMIT=124`.
2. Never use >1 thread per window on this host (benchmarked).
3. Never launch without `VALIDATED_BOUND` manifest.
4. Never mix legacy `umbrella_sampling_binding_site_v2` with locked-site dirs.
5. Pilot PASS before blasting remaining 7.

## Remote paths

```
/data/LiSPER_remote/
  scripts/                      drivers + env
  paired_binding_sites/         manifests
  LiSPER_8cand_LiCl/systems/<Cand>/gromacs/
  LiSPER_8cand_NaCl_prod_worker/systems/<Cand>/gromacs/
```
