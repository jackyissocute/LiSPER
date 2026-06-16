# NaCl Molecular Dynamics

Remote GROMACS workflow and synced results for peptide + NaCl systems.

## Status

| Stage | Status |
|---|---|
| CHARMM-GUI QC | 10/10 ready |
| Minimization | 10/10 complete |
| Equilibration | 10/10 complete |
| 20 ns production | Queued after LiCl production/clustering; currently waiting while `LiND-1` LiCl production runs at 0.00 ns / 20 ns |
| Structural clustering | Queued after NaCl production runs |

Last synchronized monitor snapshot: `2026-06-16 13:30 CST`.

## Key Files

| File / Folder | Purpose |
|---|---|
| `ready_gromacs_systems.tsv` | Systems passed from CHARMM-GUI QC |
| `remote_runs/` | Remote scripts, logs, and status snapshots |
| `remote_results/` | Synced GROMACS outputs |
| `remote_runs/current_remote_snapshot.md` | Completed minimization/equilibration status |
| `remote_runs/remote_status.md` | Current remote status |

## Handoff Logic

```mermaid
flowchart TD
    accTitle: NaCl MD Path
    accDescr: Equilibrated NaCl systems proceed through production MD, clustering, representative-structure selection, and Na umbrella sampling.

    equilibrated["Equilibrated<br/>NaCl systems"]
    production["20 ns<br/>production"]
    clustering["gmx<br/>cluster"]
    representative["Top-cluster<br/>PDB"]
    umbrella["Na+ umbrella<br/>sampling"]

    equilibrated --> production
    production --> clustering
    clustering --> representative
    representative --> umbrella
```
