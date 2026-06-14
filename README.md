# LiSPER

## Lithium-Selective Peptide Engineering and Recovery

**Engineering selective lithium-recognition peptides through computational design, experimental validation, and industrial translation.**

LiSPER is a research and technology-development program for designing **de novo lithium-selective peptides** and translating them into a future protein-based Direct Lithium Extraction platform.

```mermaid
flowchart LR
    A["Computational Discovery"] --> B["Experimental Validation"]
    B --> C["Industrial Translation"]

    A --> A1["Peptide design<br/>MD simulation<br/>PMF ranking"]
    B --> B1["His6-SUMO-LiSPER<br/>binding assays<br/>surface display"]
    C --> C1["immobilized peptide media<br/>packed-bed capture<br/>Bio-DLE process"]

    classDef phase fill:#e0f2fe,stroke:#0369a1,stroke-width:2px,color:#0c4a6e
    classDef detail fill:#f8fafc,stroke:#64748b,stroke-width:1px,color:#0f172a
    class A,B,C phase
    class A1,B1,C1 detail
```

---

## Project Vision

Current lithium recovery technologies face persistent challenges in **selectivity, cost, energy use, chemical intensity, and sustainability**, especially when Li+ must be separated from chemically similar or highly abundant ions such as Na+.

LiSPER aims to develop short lithium-recognition peptides inspired by:

| Inspiration | Role in LiSPER |
|---|---|
| Lithium-binding peptide motifs | Provide motif-level precedent for Li+-associated peptide behavior. |
| Intrinsically disordered peptide principles | Enable flexible conformational sampling and adaptive ion coordination. |
| Computational protein engineering | Enables rapid design, simulation, ranking, and experimental prioritization. |

The ultimate goal is a **protein-based Direct Lithium Extraction platform**, or **Bio-DLE**, in which engineered LiSPER peptides selectively capture lithium from battery-recycling or lithium-processing streams and feed conventional lithium carbonate production.

---

## Project Roadmap

```mermaid
flowchart TD
    A["Phase I: Computational Discovery"] --> B["Phase II: Experimental Validation"]
    B --> C["Phase III: Industrial Translation"]

    subgraph P1["Phase I: Computational Discovery"]
        A1["Sequence Design"] --> A2["ESMFold Structure Prediction"]
        A2 --> A3["CHARMM-GUI System Building"]
        A3 --> A4["GROMACS Equilibration"]
        A4 --> A5["Production MD"]
        A5 --> A6["Structural Clustering"]
        A6 --> A7["Representative Structures"]
        A7 --> A8["Umbrella Sampling"]
        A8 --> A9["PMF Analysis"]
        A9 --> A10["Delta G(Li+) and Delta G(Na+)"]
        A10 --> A11["Li/Na Selectivity Ranking"]
    end

    subgraph P2["Phase II: Experimental Validation"]
        B1["Construct Design"] --> B2["His6-SUMO-LiSPER Plasmids"]
        B2 --> B3["E. coli Expression"]
        B3 --> B4["Protein Purification"]
        B4 --> B5["SUMO Cleavage"]
        B5 --> B6["Native Peptide Recovery"]
        B6 --> B7["Li+/Na+ Binding Assays"]
        B7 --> B8["Selectivity Validation"]

        B9["Surface Display System"] --> B10["Display LiSPER on Cell Surface"]
        B10 --> B11["Whole-Cell Li Capture Assays"]
        B11 --> B12["Li/Na Selectivity Assessment"]
    end

    subgraph P3["Phase III: Industrial Translation"]
        C1["Best LiSPER Candidate"] --> C2["Immobilization Strategy"]
        C2 --> C3["Magnetic Bead Prototype"]
        C3 --> C4["Resin-Based Capture Media"]
        C4 --> C5["Packed-Bed Column Development"]
        C5 --> C6["Synthetic Raffinate Testing"]
        C6 --> C7["Pilot Process Evaluation"]
        C7 --> C8["Patent Development"]
    end

    A11 --> B1
    A11 --> B9
    B8 --> C1
    B12 --> C1

    classDef computational fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a
    classDef experimental fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    classDef industrial fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#7c2d12
    class A,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11 computational
    class B,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12 experimental
    class C,C1,C2,C3,C4,C5,C6,C7,C8 industrial
```

### Phase I: Computational Discovery

**Goal:** identify the most promising LiSPER candidates computationally.

**Current status:** active.

Phase I uses ensemble-aware molecular simulation to avoid overinterpreting a single folded model. The intended comparison is:

`Delta Delta G = Delta G(Li+) - Delta G(Na+)`

More negative values indicate stronger predicted lithium preference.

### Phase II: Experimental Validation

**Goal:** experimentally validate computational predictions.

**Expected outcome:** publication-quality biological evidence showing whether designed LiSPER peptides exhibit measurable Li+/Na+ selectivity.

Phase II includes two complementary validation routes:

1. **Purified peptide route:** His6-SUMO-LiSPER expression, purification, SUMO cleavage, native peptide recovery, and binding assays.
2. **Surface-display route:** cellular display of LiSPER peptides followed by whole-cell capture and selectivity assays.

### Phase III: Industrial Translation

**Goal:** transform LiSPER from a peptide into a deployable lithium-capture technology.

Phase III evaluates immobilized peptides, magnetic bead prototypes, resin capture media, packed-bed columns, synthetic raffinate testing, and patentable process architecture.

---

## Scientific Hypothesis

> **Hybridization of lithium-binding motifs and intrinsically disordered peptide properties can generate peptides with measurable lithium selectivity over sodium in aqueous solution.**

```mermaid
flowchart LR
    A["Lithium-binding motifs<br/>GPGNP / GPGDP"] --> D["LiSPER candidate peptides"]
    B["IDP-like flexibility<br/>Gly / Ser / Pro-rich sequence space"] --> D
    C["Oxygen donor residues<br/>Asp / Glu coordination sites"] --> D
    D --> E["Conformational ensemble"]
    E --> F["Li+ coordination states"]
    E --> G["Na+ coordination states"]
    F --> H["Measured Li/Na selectivity"]
    G --> H

    classDef idea fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef peptide fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef result fill:#dcfce7,stroke:#16a34a,color:#14532d
    class A,B,C idea
    class D,E,F,G peptide
    class H result
```

The goal is not simply strong Li+ binding. The goal is **selective Li+ recognition over Na+** under aqueous conditions relevant to lithium recovery.

---

## Current Candidate Library

| Candidate | Sequence family | Status | MD complete? | Umbrella sampling complete? | Wet-lab complete? |
|---|---|---|---:|---:|---:|
| LiD3-1 | Repeated GPGDP motif | Primary computational and wet-lab candidate | In progress | No | No |
| LiND-1 | Mixed GPGNP/GPGDP motif | Primary computational and wet-lab candidate | In progress | No | No |
| IDP-Li-1 | IDP-like acidic shell | Primary computational and wet-lab candidate | In progress | No | No |
| IDP-Li-2 | Symmetric disordered pocket | Screening candidate | In progress | No | No |
| LiD2-IDP | Dual GPGDP with acidic spacer | Screening candidate | In progress | No | No |
| StrongBind-Li | Higher Asp-density design | Screening candidate | In progress | No | No |
| SoftCage-Li | Short oxygen-rich flexible cage | Screening candidate | In progress | No | No |
| IDP-Rich-Li | Strongly disordered acidic design | Screening candidate | In progress | No | No |
| LowCharge-Li | Reduced-charge motif design | Primary computational and wet-lab candidate | In progress | No | No |
| Control-Negative | Neutral motif-related control | Negative control | In progress | No | No |

Recommended starting wet-lab subset:

`LiD3-1`, `LiND-1`, `IDP-Li-1`, `LowCharge-Li`, `Control-Negative`

---

## Computational Workflow

```mermaid
flowchart TD
    A["Candidate sequences"] --> B["ESMFold prediction"]
    B --> C["CHARMM-GUI setup"]
    C --> D1["LiCl system"]
    C --> D2["NaCl system"]
    D1 --> E1["Minimization and equilibration"]
    D2 --> E2["Minimization and equilibration"]
    E1 --> F1["Production MD"]
    E2 --> F2["Production MD"]
    F1 --> G1["Structural clustering"]
    F2 --> G2["Structural clustering"]
    G1 --> H1["Representative Li+ structures"]
    G2 --> H2["Representative Na+ structures"]
    H1 --> I1["Li+ umbrella sampling"]
    H2 --> I2["Na+ umbrella sampling"]
    I1 --> J1["PMF and Delta G(Li+)"]
    I2 --> J2["PMF and Delta G(Na+)"]
    J1 --> K["Li/Na selectivity ranking"]
    J2 --> K
```

Why clustering matters: LiSPER peptides are flexible and IDP-like. A random trajectory frame may represent a rare state. Clustering identifies populated conformational families, making umbrella sampling and PMF comparison more meaningful.

### Simulation Choices

| Decision | Current value | Rationale |
|---|---|---|
| Force field | CHARMM36m | Compatible with peptide and IDP-oriented CHARMM workflows. |
| Water model | TIP3P | Standard CHARMM-GUI setup for these systems. |
| Ion systems | Separate LiCl and NaCl systems | Enables clean Li+ vs Na+ free-energy comparison. |
| First production length | 20 ns | Provides an initial ensemble for clustering and representative-state selection. |
| Mixed-ion systems | Later validation round | Reserved for competition assays after single-ion behavior is understood. |

---

## Experimental Validation Strategy

```mermaid
flowchart TD
    A["Computational ranking"] --> B["Construct design"]
    B --> C["His6-SUMO-LiSPER plasmids"]
    C --> D["E. coli expression"]
    D --> E["Protein purification"]
    E --> F["SUMO cleavage"]
    F --> G["Native peptide recovery"]
    G --> H["Li+ binding assay"]
    H --> I["Na+ competition assay"]
    I --> J["Li/Na selectivity validation"]

    A --> K["Surface-display construct"]
    K --> L["Cell-surface LiSPER display"]
    L --> M["Whole-cell Li capture"]
    M --> N["Displayed-peptide selectivity"]
    N --> J
```

The purified-peptide track tests the intrinsic binding behavior of LiSPER candidates. The surface-display track tests whether LiSPER can function as a biological capture interface.

---

## Industrial Translation Concept

```mermaid
flowchart TD
    A["Spent LIB or Li+/Na+ process stream"] --> B["Upstream impurity removal"]
    B --> C["Li+/Na+ raffinate"]
    C --> D["LiSPER capture step"]
    D --> E["Na-rich effluent"]
    D --> F["Li+ elution"]
    F --> G["Concentrated Li+ stream"]
    G --> H["Na2CO3 precipitation"]
    H --> I["Li2CO3 product"]

    D --> J["Possible formats:<br/>immobilized peptide resin<br/>magnetic beads<br/>inactivated display cells<br/>packed-bed column"]
```

Current literature assessments in this repository favor **purified immobilized LiSPER peptide in a packed-bed adsorption column** as the most realistic industrial endpoint, with inactivated surface-display biomass and magnetic bead systems as useful bridge technologies.

---

## Repository Structure

```text
LiSPER/
├── analysis/          # Analysis notebooks, scripts, and derived interpretation
├── charmm-gui/        # CHARMM-GUI system-builder outputs for LiCl and NaCl systems
├── data/              # Raw and processed data
├── docs/              # Design rationale and workflow documentation
├── esmfold/           # Structure prediction inputs, outputs, PAE, plots, and PDBs
├── figures/           # Figures for reports, manuscripts, and presentations
├── literature/        # Literature reviews and technology assessments
├── manuscript/        # Publication drafts and manuscript assets
├── md/                # GROMACS equilibration, production, logs, and clustering work
├── plasmids/          # His6-SUMO-LiSPER plasmid design and vendor-ready records
├── pmf/               # Potential of mean force analysis outputs
├── protocols/         # Experimental and computational protocols
├── scripts/           # Utility scripts for design, setup, and analysis
├── sequences/         # Candidate peptide sequences and metadata
├── umbrella/          # Umbrella sampling setup and windows
└── wetlab/            # Expression, purification, assay, and validation planning
```

| Folder | Purpose |
|---|---|
| `analysis/` | Downstream analysis, summary calculations, and interpretation. |
| `charmm-gui/` | System-builder outputs for solvated LiCl and NaCl peptide simulations. |
| `esmfold/` | Structure prediction pipeline outputs and CHARMM-GUI-ready PDBs. |
| `md/` | GROMACS simulation scripts, remote run logs, equilibration, production, and clustering. |
| `umbrella/` | Umbrella sampling setups for ion-peptide separation coordinates. |
| `pmf/` | PMF analysis and Delta G comparison for Li+ and Na+. |
| `plasmids/` | His6-SUMO-LiSPER plasmid designs, vector maps, and vendor-ready files. |
| `wetlab/` | Experimental planning for expression, purification, cleavage, and binding assays. |
| `literature/` | Literature-driven assessments for protein design, host selection, and deployment architecture. |
| `protocols/` | Reproducible protocols for computational and experimental workflows. |
| `manuscript/` | Manuscript drafts, figures, and publication planning. |

---

## Current Status

```text
Computational Discovery:  ████████░░ 80%
Experimental Validation:  ██░░░░░░░░ 20%
Industrial Translation:   ░░░░░░░░░░ 0%
```

| Program area | Status | Near-term gate |
|---|---|---|
| Computational Discovery | Active | Complete clustering, representative structure selection, umbrella sampling, and PMF ranking. |
| Experimental Validation | In preparation | Express and purify His6-SUMO-LiSPER candidates; establish Li+/Na+ binding assays. |
| Industrial Translation | Literature and concept stage | Convert validated peptides into immobilized capture formats and column concepts. |

---

## Key Documents

- [Repository guide](docs/repository_guide.md)
- [Candidate design rationale](docs/candidate_design_rationale.md)
- [MD to PMF workflow](docs/md_to_pmf_workflow.md)
- [LiCl MD status](md/li_cl/remote_runs/remote_status.md)
- [NaCl MD status](md/na_cl/remote_runs/remote_status.md)
- [Surface-display host selection report](literature/surface_display_host_selection/reports/final_host_selection_report.md)
- [Deployment architecture report](literature/deployment_architecture/reports/final_deployment_architecture_report.md)

---

## Long-Term Impact

LiSPER is designed as a platform technology for selective ion recognition and sustainable resource recovery.

Potential applications include:

- **Direct Lithium Extraction (DLE):** selective lithium capture from complex aqueous streams.
- **Battery Recycling:** late-stage lithium polishing after transition-metal removal.
- **Lithium Purification:** improved Li+/Na+ separation before lithium carbonate production.
- **Resource Recovery:** bio-inspired recovery of critical minerals from waste streams.
- **Selective Ion Separation:** generalizable peptide-engineering principles for difficult ion separations.

```mermaid
mindmap
  root((LiSPER Impact))
    Direct Lithium Extraction
      Bio-DLE
      Lower chemical intensity
    Battery Recycling
      Spent LIB streams
      Lithium polishing
    Lithium Purification
      Li/Na selectivity
      Li2CO3 feed preparation
    Resource Recovery
      Critical minerals
      Circular economy
    Selective Ion Separation
      Peptide engineering
      Bio-inspired materials
```

---

## Team

### LiSPER Team

**Lithium-Selective Peptide Engineering and Recovery**

**Mission:** designing the next generation of bio-inspired lithium capture technologies.

LiSPER is built for collaboration across computational protein design, molecular simulation, biochemistry, synthetic biology, hydrometallurgy, and technology translation. The repository is intended to support researchers, student team members, faculty advisors, DKU Innovation & Entrepreneurship reviewers, potential investors, and future collaborators.

---

## Working Principle

For LiSPER, the scientifically careful path is:

`ESMFold -> CHARMM-GUI -> equilibration -> production MD -> clustering -> representative structures -> umbrella sampling -> PMF -> selectivity`

The project should avoid the shortcut:

`ESMFold -> umbrella sampling`

because flexible peptides require ensemble-aware structure selection before free-energy calculations.
