# Window assignment plan — lisper-epyc (EPYC 9554P, 128 threads)

Date: 2026-07-12  
Host: `lisper-epyc`
GROMACS: `/opt/gromacs/2026.0` (target), 1 thread per window

## Hardware budget

| Resource | Value |
|---|---|
| Threads | 128 |
| Reserve (SSH / WHAM / rsync / OS) | 4 |
| **Concurrent `gmx mdrun`** | **`LISPER_GLOBAL_MDRUN_LIMIT=126`** |
| Pull threads (16 paired campaigns) | `LISPER_PULL_NTHREADS=7`; thread-aware global limiter keeps the node at or below 126 |
| Per-window threads | `-ntmpi 1 -ntomp 1` (`LISPER_NTHREADS=1`) |
| Per-driver queue depth | `LISPER_JOBS=126` (global lock caps at 126) |

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

### Phase D — All paired campaigns

| Track | Workdir | Ion | Campaigns |
|---|---|---|---:|
| A | `LiSPER_8cand_LiCl` | LIT | 8 |
| B | `LiSPER_8cand_NaCl_prod_worker` | SOD | 8 |

**Assignment:** run all 16 pulls under the thread-aware 126-thread pool, then fan their windows into the same pool. Pulls use 7 threads; windows use one thread and automatically backfill toward **126/126**. When several distinct windows are ready, give newly free slots to the campaigns with the most remaining atom-weighted work; never interrupt a healthy `mdrun` to rebalance.

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

### Phase E — Window production

8 candidates × 2 ions = **16 conditions** × ~31 windows = **~496 window jobs**.

| Mode | How | Peak mdrun | Est. wall |
|---|---|---:|---:|
| **Recommended** | Fan all incomplete windows into global 126-slot pool (multiple drivers) | 126 | shortest safe wall time |
| Conservative | 2 candidates at a time (4 conditions) | ≤126 | longer, safer ops |

## WHAM / ΔG slotting

After a condition’s windows finish:

1. Build `tpr-files.dat` + `pullf-files.dat` (analysis windows only; guards optional/excluded per QC protocol).
2. Run `gmx wham` on **1–2 cores** only when the total MD plus analysis use remains at or below 126.
3. Reserve ~4 threads always free so WHAM + SSH never starve.

Paired estimator: `evaluate_paired_pmf_qc.py` on Mac or remote after both ions are ready. It writes the estimate and numerical diagnostics without universal PASS thresholds.

## Anti-thrash rules

1. Never exceed `LISPER_GLOBAL_MDRUN_LIMIT=126`.
2. Never use >1 thread per window on this host (benchmarked).
3. Never launch without `VALIDATED_BOUND` manifest.
4. Use locked-site workdirs only (`umbrella_sampling` under current campaign roots).
5. Keep every candidate×ion driver unique; do not duplicate windows.

## Remote paths

```
/data/LiSPER_remote/
  scripts/                      drivers + env
  paired_binding_sites/         manifests
  LiSPER_8cand_LiCl/systems/<Cand>/gromacs/
  LiSPER_8cand_NaCl_prod_worker/systems/<Cand>/gromacs/
```
