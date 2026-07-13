# LiSPER Remote MD Monitor Update Report

Date: 2026-06-15

## Automation Updated

Automation: `lisper-remote-md-monitor`

Cadence remains unchanged:

```text
Every 2 hours
```

The heartbeat prompt was polished to make each monitor pass more robust to repository changes.

## New Automation Priorities

The monitor now explicitly checks for:

- Current repository organization before syncing or launching remote tasks.
- Canonical sync-path guidance in `01_computational_discovery/md/remote_orchestration/SYNC_PATHS.md`.
- Active MD workspace under `01_computational_discovery/md/`.
- Correct LiCl and NaCl local destinations:
  - `01_computational_discovery/md/li_cl/remote_runs/`
  - `01_computational_discovery/md/li_cl/remote_results/`
  - `01_computational_discovery/md/na_cl/remote_runs/`
  - `01_computational_discovery/md/na_cl/remote_results/`
- Avoidance of old root-level destinations such as `md/`, `charmm-gui/`, `esmfold/`, `sequences/`, `docs/`, and `scripts/`.
- Small-file sync first, avoiding repeated transfer of active large trajectories.
- QC distinction between:
  - real MD instability,
  - topology/setup problems,
  - post-processing or clustering handoff failures.
- Conservative repair jobs that preserve original failure diagnostics.

## Repository Path Alignment

Added:

- `01_computational_discovery/md/remote_orchestration/SYNC_PATHS.md`

Updated:

- `01_computational_discovery/md/remote_orchestration/README.md`
- `01_computational_discovery/md/README.md`
- `01_computational_discovery/md/remote_orchestration/scripts/queue_nacl_add2.py`
- `01_computational_discovery/md/remote_orchestration/scripts/run_lid31_pipeline.py`
- `01_computational_discovery/md/remote_orchestration/scripts/start_equilibration.sh`
- `01_computational_discovery/md/na_cl/remote_runs/queue_nacl_add2.py`
- `01_computational_discovery/md/na_cl/remote_runs/remote_status.md`

Remote scripts were synced to `/root/LiSPER_remote`.

Old NaCl-only scripts were moved out of the active remote root into:

```text
/root/LiSPER_remote/legacy_scripts/
```

## Current MD Task Summary

### LiD3-1

- 20 ns LiCl production completed cleanly.
- Original full-system clustering failed because the `SYSTEM` index and trajectory atom counts differed by one atom.
- Repaired peptide-only clustering succeeded.
- Representative structure exists:

```text
01_computational_discovery/md/li_cl/remote_results/systems/LiD3-1/gromacs/cluster_20ns_repair/representative_top_cluster.pdb
```

- Top cluster: 314 / 2001 frames = 15.69%.

### IDP-Li-1

- 20 ns LiCl production completed cleanly.
- Original full-system clustering failed by the same one-atom index mismatch pattern.
- Repaired peptide-only clustering succeeded.
- Representative structure exists:

```text
01_computational_discovery/md/li_cl/remote_results/systems/IDP-Li-1/gromacs/cluster_20ns_repair/representative_top_cluster.pdb
```

- Top cluster: 140 / 2001 frames = 7.00%.

### StrongBind-Li

- Currently active LiCl production run on the remote computer.
- Last synced checkpoint: 1.82 ns / 20 ns.
- QC markers were healthy at last check.

### Blocked Production Setup

These LiCl candidates were skipped by the production queue because `gmx grompp` could not resolve `toppar/forcefield.itp`:

- `LiND-1`
- `IDP-Li-2`
- `LowCharge-Li`
- `LiD2-IDP`

This appears to be a topology include path/setup issue, not a peptide physics failure.

### NaCl

- NaCl production/clustering remains queued behind the LiCl workflow.
- NaCl local/remote sync paths are now documented in `SYNC_PATHS.md`.

## Scientific Interpretation

The repaired clustering succeeded, but the top-cluster populations for `LiD3-1` and `IDP-Li-1` are low. This supports the IDP-like/flexible-peptide hypothesis, but it also means umbrella sampling should be planned carefully.

Recommended next decision:

- Use the largest-cluster representative as a first umbrella-sampling starting point, or
- compare several representative clusters before choosing umbrella starting structures.

For highly flexible peptides, the second option is scientifically stronger if time allows.
