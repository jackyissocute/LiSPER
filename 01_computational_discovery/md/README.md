# Molecular Dynamics

This folder tracks the MD-stage GROMACS work for the active 8-candidate LiSPER library after ESMFold and CHARMM-GUI preparation. It owns minimization, equilibration, 20 ns production, structural clustering, and representative extraction. Umbrella sampling and PMF/Delta G artifacts now live in sibling workflow folders.

## Current State

The active MD workflow now uses the final 8-candidate names. All eight ESMFold structures are ready. All LiCl and NaCl CHARMM-GUI systems are GROMACS-ready. LiCl and NaCl setup are complete for all eight candidates. LiCl and NaCl 20 ns production plus clustering are running across two AutoDL workers without duplicate candidate-condition-stage jobs. Clustered representatives are handed to `../umbrella/`; WHAM/PMF/Delta G QC is tracked in `../pmf/`.

Latest production/free-energy handoff snapshot: `2026-06-26 13:20 CST`.

| Condition | Folder | Current state |
|---|---|---|
| LiCl | `li_cl/` | 8/8 production jobs complete and 8/8 representatives ready; refined umbrella work has moved to `../umbrella/` |
| NaCl | `na_cl/` | 6/8 production jobs complete and 6/8 representatives ready; Worker A backfill continues for `LiN3-Core` and `LiND-Hybrid` |
| Handoff | `../umbrella/` and `../pmf/` | Paired `LiDA-1`, `LiDS-1`, and `LiD3-Flex` refined umbrella work is active; PMF/Delta G remains preliminary until WHAM/bootstrap/time-slice QC passes |

Remote 8-candidate workspaces were initialized on AutoDL:

| Condition | Remote workspace |
|---|---|
| LiCl | `/root/LiSPER_remote/LiSPER_8cand_LiCl` |
| NaCl setup | `/root/LiSPER_remote/LiSPER_8cand_NaCl` |
| NaCl production | `/root/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker` |
| NaCl backfill | `/root/LiSPER_remote/LiSPER_8cand_NaCl_overflow_workerA` |

## Workflow

```mermaid
flowchart TD
    accTitle: Revised 8-Candidate MD Workflow
    accDescr: The final library moves from ESMFold and CHARMM-GUI into minimization, equilibration, production MD, clustering, and representative handoff.

    sequences["8 candidate sequences"]
    esmfold["ESMFold intake"]
    charmm["CHARMM-GUI LiCl/NaCl systems"]
    minimization["Energy minimization"]
    equilibration["Equilibration"]
    production["20 ns production MD"]
    clustering["Structural clustering"]
    handoff["Representative handoff"]

    sequences --> esmfold --> charmm --> minimization --> equilibration --> production --> clustering --> handoff
```

## What Belongs Here

| Sub-area | Purpose |
|---|---|
| `remote_orchestration/` | Scripts and sync maps for the 8-candidate remote workflow |
| `li_cl/remote_runs/` | LiCl launch/status logs for the 8-candidate workflow |
| `li_cl/remote_results/` | Synced LiCl outputs for the 8-candidate workflow |
| `na_cl/remote_runs/` | NaCl launch/status logs for the 8-candidate workflow |
| `na_cl/remote_results/` | Synced NaCl outputs for the 8-candidate workflow |

Umbrella sampling files are organized in `../umbrella/`. WHAM, PMF QC, Delta G, and Delta Delta G files are organized in `../pmf/`.

Do not launch new GROMACS work for a candidate until that candidate has final-name ESMFold and matched CHARMM-GUI inputs ready.
