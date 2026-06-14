# LiSPER Repository Reorganization Report

Date: 2026-06-14

## Reasoning

LiSPER has evolved from a computational peptide-design repository into a three-stage research and technology-development program:

1. Computational Discovery
2. Experimental Validation
3. Industrial Translation

The old structure placed major workflow areas directly at the repository root. That was serviceable during early computational work, but it became harder to navigate once plasmid design, wet-lab planning, surface-display research, immobilization studies, deployment architecture, literature collection, and manuscript preparation were added.

The new structure groups files by program stage while preserving the internal workflow folders that already worked well.

## What Changed

| Old location | New location | Reason |
|---|---|---|
| `sequences/` | `01_computational_discovery/sequences/` | Candidate sequence library belongs to discovery. |
| `esmfold/` | `01_computational_discovery/esmfold/` | Structure prediction belongs to discovery. |
| `charmm-gui/` | `01_computational_discovery/charmm-gui/` | System setup belongs to discovery. |
| `md/` | `01_computational_discovery/md/` | MD simulation belongs to discovery. |
| `umbrella/` | `01_computational_discovery/umbrella/` | Umbrella sampling belongs to discovery. |
| `pmf/` | `01_computational_discovery/pmf/` | PMF/selectivity analysis belongs to discovery. |
| `analysis/` | `01_computational_discovery/analysis/` | Computational interpretation belongs to discovery. |
| `data/` | `01_computational_discovery/data/` | Current data are discovery-stage computational data. |
| `plasmids/` | `02_experimental_validation/plasmids/` | Plasmids support wet-lab validation. |
| `wetlab/` | `02_experimental_validation/wetlab/` | Wet-lab planning belongs to validation. |
| `protocols/` | `02_experimental_validation/protocols/` | Current protocols are primarily experimental/validation-facing. |
| `literature/surface_display_host_selection/` | `03_industrial_translation/surface_display_host_selection/` | Surface display host selection is an applied translation study. |
| `literature/deployment_architecture/` | `03_industrial_translation/deployment_architecture/` | Deployment architecture is an industrial translation study. |
| `literature/protein_design/` | `04_literature/protein_design/` | Foundational design literature remains a literature collection. |
| `manuscript/` | `05_manuscript/manuscript/` | Manuscript preparation gets its own stage area. |
| `figures/` | `05_manuscript/figures/` | Publication/report figures belong with manuscript materials. |
| `docs/` | `06_shared/docs/` | Cross-project documentation supports all stages. |
| `scripts/` | `06_shared/scripts/` | Reusable scripts support multiple stages. |
| `inbox/` | `06_shared/inbox/` | Inbox is a shared temporary intake area. |

## What Was Archived

| Archived material | New location | Reason |
|---|---|---|
| Deprecated direct His/T7-LiSPER pET-28a(+) construct package | `archive/superseded_plasmid_designs/archive_v1_without_SUMO/` | Superseded by the His6-SUMO-LiSPER design, which is better suited for expression, purification, SUMO cleavage, and native peptide recovery. |
| `.DS_Store` filesystem artifacts | `archive/system_files/` | Non-scientific system files moved out of active science folders and preserved rather than deleted. |

## Documentation Updated

- Root `README.md` now describes the stage-based structure.
- `06_shared/docs/repository_guide.md` now shows the new workflow paths.
- Stage-level README files were added for:
  - `01_computational_discovery/`
  - `02_experimental_validation/`
  - `03_industrial_translation/`
  - `05_manuscript/`
  - `06_shared/`
  - `archive/`
- Active operational docs were updated for new paths, including plasmid generation and MD status references.
- The SUMO plasmid generator now reads and writes from the new locations.

## Why The New Structure Is Better

- It mirrors the current LiSPER roadmap: discovery, validation, translation.
- It reduces root-level clutter and makes first-time navigation easier.
- It keeps computational files together, which protects the MD/PMF workflow from being mixed with wet-lab or business-facing materials.
- It separates foundational literature from applied industrial-translation studies.
- It preserves superseded work without presenting it as current.
- It creates a clear place for future expansion: new assays go under validation, new process studies go under translation, and reusable tooling goes under shared resources.

## Current Top-Level Map

```text
LiSPER/
├── 01_computational_discovery/
├── 02_experimental_validation/
├── 03_industrial_translation/
├── 04_literature/
├── 05_manuscript/
├── 06_shared/
└── archive/
```

