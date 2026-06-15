<p align="center">
  <img src="assets/branding/banners/Dark_Banner.png" alt="LiSPER banner showing lithium-selective peptide engineering, Li+ coordination, Na+ exclusion, peptide design, and sustainable recovery" width="100%">
</p>

<h1 align="center">LiSPER</h1>

<p align="center">
  <strong>Lithium-Selective Peptide Engineering and Recovery</strong><br>
  A computational-to-experimental program for designing lithium-selective peptides and translating them toward bio-inspired Direct Lithium Extraction (Bio-DLE).
</p>

<p align="center">
  <img alt="Program status" src="https://img.shields.io/badge/status-active%20computational%20discovery-2563eb">
  <img alt="Project type" src="https://img.shields.io/badge/project-peptide%20ion%20selectivity-0f766e">
  <img alt="Simulation" src="https://img.shields.io/badge/MD-GROMACS%20%7C%20CHARMM36m-7c3aed">
  <img alt="Translation goal" src="https://img.shields.io/badge/vision-Bio--DLE-ea580c">
</p>

---

## 📋 Project overview

**LiSPER** is a scientific research and technology-development project for engineering short peptide systems that preferentially recognize lithium over sodium in aqueous environments.

The project combines **lithium-binding peptide inspiration**, **intrinsically disordered peptide principles**, and **computational protein engineering** to discover candidate Li+/Na+ selective peptide materials. The long-term aim is a deployable peptide-enabled lithium capture platform for battery recycling and Direct Lithium Extraction.

| What LiSPER is | Why it matters | Current focus |
|---|---|---|
| Lithium-selective peptide library | Li+/Na+ separation is central to lithium recovery | MD, clustering, PMF ranking |
| Computational discovery engine | Prioritizes candidates before wet-lab cost | LiCl vs NaCl free-energy comparison |
| Experimental validation program | Converts predictions into measurable assays | His6-SUMO peptide expression strategy |
| Bio-DLE translation roadmap | Connects molecular recognition to process design | Immobilized peptide capture concepts |

## 🎯 Scientific thesis

> **Flexible peptide motifs with oxygen-donor residues can form lithium coordination environments that differ measurably from sodium coordination under aqueous conditions.**

LiSPER does not only ask whether a peptide can bind Li+. It asks whether a peptide can prefer Li+ over Na+, and whether that preference can be carried from molecular simulation into experimental and eventually material formats.

```mermaid
flowchart LR
    accTitle: LiSPER Scientific Thesis
    accDescr: The diagram shows how motif inspiration, IDP-like flexibility, and oxygen-donor residues combine into LiSPER peptides that are evaluated for Li over Na selectivity.

    lithium_motifs[💡 Lithium-binding motifs] --> candidates[🧪 LiSPER peptides]
    idp_principles[🔄 IDP-like flexibility] --> candidates
    oxygen_donors[⚙️ Asp and Ser donors] --> candidates
    candidates --> ensembles[📊 Conformational ensembles]
    ensembles --> li_states[✅ Li+ coordination states]
    ensembles --> na_states[🔍 Na+ comparison states]
    li_states --> selectivity[🎯 Li+/Na+ selectivity]
    na_states --> selectivity

    classDef idea fill:#fef9c3,stroke:#ca8a04,stroke-width:2px,color:#713f12
    classDef peptide fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#3b0764
    classDef result fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d

    class lithium_motifs,idp_principles,oxygen_donors idea
    class candidates,ensembles,li_states,na_states peptide
    class selectivity result
```

## 🧭 Program roadmap

LiSPER is organized as a three-stage program: discover the molecular principle, validate it experimentally, then translate the best peptide systems into capture materials.

```mermaid
flowchart LR
    accTitle: LiSPER Three-Phase Roadmap
    accDescr: Three major phases move from computational discovery through experimental validation and into industrial translation.

    phase_one[🔍 Phase I<br/>Computational discovery<br/>sequence design, MD, clustering, PMF] --> phase_two[🧪 Phase II<br/>Experimental validation<br/>expression, purification, binding assays]
    phase_two --> phase_three[📦 Phase III<br/>Industrial translation<br/>immobilization, beads, resin, column]

    phase_one --> rank[📊 Li+/Na+ selectivity ranking]
    rank --> shortlist[🎯 wet-lab candidate subset]
    shortlist --> phase_two
    phase_two --> validated[✅ validated LiSPER peptides]
    validated --> phase_three

    classDef computational fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f
    classDef experimental fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    classDef industrial fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#7c2d12
    class phase_one,rank computational
    class phase_two,shortlist,validated experimental
    class phase_three industrial
```

| Phase | Goal | Status | Near-term gate |
|---|---|---|---|
| **I. Computational discovery** | Rank LiSPER candidates by Li+/Na+ selectivity | Active | Finish production MD, clustering, umbrella sampling, PMF |
| **II. Experimental validation** | Test whether designed peptides show measurable selectivity | Preparing | Express and purify His6-SUMO-LiSPER candidates |
| **III. Industrial translation** | Convert validated peptides into capture media | Concept stage | Select immobilization and column prototype strategy |

## 📊 Project dashboard

| Workstream | Progress | Evidence in repository | Next decision |
|---|---:|---|---|
| **Candidate design** | `complete` | 10-peptide first-round library | Keep library stable through first PMF round |
| **ESMFold structures** | `complete` | Predicted PDB, PAE, plots | Use as starting structures only |
| **CHARMM-GUI systems** | `complete` | 10 LiCl and 10 NaCl systems | Preserve QC manifests |
| **GROMACS equilibration** | `complete` | LiCl and NaCl equilibration summaries | Continue production queue |
| **Production MD + clustering** | `active` | 20 ns LiCl/NaCl queues | Select representative structures |
| **Umbrella sampling + PMF** | `planned` | Workflow documented | Launch after clustering |
| **Wet-lab validation** | `preparing` | His6-SUMO plasmid route | Begin expression/purification |
| **Bio-DLE translation** | `concept` | Deployment architecture notes | Prototype immobilized format |

```text
Computational discovery  [########--]  active
Wet-lab validation       [##--------]  preparing
Industrial translation   [#---------]  concept
```

## 🧪 Candidate library

The first-round LiSPER library is intentionally small: enough sequence diversity to test the design logic, but compact enough for simulation and wet-lab follow-through.

| Rank | Candidate | Sequence | Design role | First subset |
|---:|---|---|---|:---:|
| 1 | **LiD3-1** | `GPGDPGSGPGDPGSGPGDP` | Repeated GPGDP motif | Yes |
| 2 | **LiND-1** | `GPGNPGSGPGDPGSGPGNP` | Hybrid GPGNP/GPGDP motif | Yes |
| 3 | **IDP-Li-1** | `SGDSGPGDPGDSG` | Flexible acidic shell | Yes |
| 4 | **IDP-Li-2** | `GDSGSGPGDPGSGDS` | Symmetric disordered pocket | No |
| 5 | **LowCharge-Li** | `GPGDPGSGNPGSGDP` | Lower-charge risk control | Yes |
| 6 | **LiD2-IDP** | `GPGDPGSDGSGPGDP` | Dual motif with acidic spacer | No |
| 7 | **StrongBind-Li** | `GPGDPGSDGPGDPGSD` | Higher Asp-density binder | No |
| 8 | **SoftCage-Li** | `GSGDPGNGDPGSG` | Short oxygen-rich cage | No |
| 9 | **IDP-Rich-Li** | `DSGDSGPGDPGDSGS` | Highly disordered acidic design | No |
| 10 | **Control-Negative** | `GPGAPGSGPGAPGSGPGAP` | Weak/neutral control | Yes |

## ⚙️ Computational workflow

The computational pipeline is ensemble-aware because these peptides are short, flexible, and IDP-like. A single ESMFold structure is treated as a starting model, not as the final biological state.

```mermaid
flowchart TD
    accTitle: Computational Discovery Pipeline
    accDescr: The computational workflow moves from candidate sequences through structure prediction, CHARMM-GUI setup, LiCl and NaCl molecular dynamics, clustering, umbrella sampling, and final selectivity ranking.

    sequences[📋 Candidate sequences] --> esmfold[🔍 ESMFold structures]
    esmfold --> charmm[⚙️ CHARMM-GUI systems]
    charmm --> licl[🧪 LiCl MD system]
    charmm --> nacl[🧪 NaCl MD system]
    licl --> md_li[📊 20 ns production MD]
    nacl --> md_na[📊 20 ns production MD]
    md_li --> cluster_li[🔍 Li+ structural clustering]
    md_na --> cluster_na[🔍 Na+ structural clustering]
    cluster_li --> rep_li[🎯 Li+ representative structure]
    cluster_na --> rep_na[🎯 Na+ representative structure]
    rep_li --> pmf_li[⚙️ Li+ umbrella sampling]
    rep_na --> pmf_na[⚙️ Na+ umbrella sampling]
    pmf_li --> ranking[✅ Delta Delta G selectivity ranking]
    pmf_na --> ranking

    classDef input fill:#f3f4f6,stroke:#6b7280,stroke-width:2px,color:#1f2937
    classDef simulation fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f
    classDef analysis fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#3b0764
    classDef result fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d

    class sequences,esmfold,charmm input
    class licl,nacl,md_li,md_na,pmf_li,pmf_na simulation
    class cluster_li,cluster_na,rep_li,rep_na analysis
    class ranking result
```

<details>
<summary><strong>Why structural clustering is central</strong></summary>

LiSPER peptides are expected to sample many conformations during production MD. Structural clustering asks which conformations occur most often, then selects representative structures from populated states. This prevents umbrella sampling from starting from an arbitrary rare frame and makes the downstream PMF comparison more defensible.

</details>

---

## 🔬 Experimental validation

Phase II is designed to convert computational rankings into measurable biological evidence.

| Route | What it tests | Planned readout |
|---|---|---|
| **Purified peptide** | Intrinsic LiSPER binding behavior | Li+ binding, Na+ competition, selectivity trend |
| **His6-SUMO fusion** | Expressible peptide production route | Soluble expression, purification, cleavage |
| **Surface display** | LiSPER as biological capture interface | Whole-cell Li capture and Na competition |

The first experimental subset is `LiD3-1`, `LiND-1`, `IDP-Li-1`, `LowCharge-Li`, and `Control-Negative`.

## 🏭 Industrial outlook

The long-term deployment concept is an immobilized peptide capture process rather than a free peptide in solution.

```mermaid
flowchart LR
    accTitle: Bio-DLE Translation Path
    accDescr: The industrial translation path starts with validated LiSPER peptides and moves toward immobilized formats, column operation, lithium elution, and lithium recovery.

    peptide[🧪 Validated LiSPER peptide] --> immobilization[⚙️ Immobilization chemistry]
    immobilization --> beads[📦 Magnetic bead prototype]
    beads --> resin[📦 Resin capture media]
    resin --> column[⚙️ Packed-bed column]
    column --> elution[🔄 Li+ elution]
    elution --> recovery[✅ Lithium recovery process]

    classDef experimental fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    classDef industrial fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#7c2d12
    classDef result fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f

    class peptide experimental
    class immobilization,beads,resin,column,elution industrial
    class recovery result
```

**Vision:** LiSPER peptides -> Li+/Na+ selectivity -> experimental validation -> immobilized peptide systems -> peptide-enabled Direct Lithium Extraction.

## 📍 Repository navigation

The repository is organized by program phase rather than by file type.

| Directory | Purpose |
|---|---|
| [`01_computational_discovery/`](01_computational_discovery/) | Candidate sequences, ESMFold structures, CHARMM-GUI systems, MD, umbrella sampling, PMF, and analysis |
| [`02_experimental_validation/`](02_experimental_validation/) | Plasmids, wet-lab planning, purified-peptide validation, surface-display validation, and assay protocols |
| [`03_industrial_translation/`](03_industrial_translation/) | Immobilized capture formats, packed-bed process design, and deployment architecture |
| [`04_literature/`](04_literature/) | Background literature for lithium-binding peptides, IDPs, ion selectivity, and DLE |
| [`05_manuscript/`](05_manuscript/) | Manuscript drafts, figures, and publication planning |
| [`06_shared/`](06_shared/) | Shared docs, reusable scripts, temporary inbox, and visual assets |
| [`assets/`](assets/) | Official LiSPER branding assets for README and project presentation |
| [`archive/`](archive/) | Superseded designs and preserved legacy materials |

## 🔗 Key project documents

- [Repository guide](06_shared/docs/repository_guide.md)
- [Candidate design rationale](06_shared/docs/candidate_design_rationale.md)
- [MD to PMF workflow](06_shared/docs/md_to_pmf_workflow.md)
- [LiCl MD status](01_computational_discovery/md/li_cl/remote_runs/remote_status.md)
- [NaCl MD status](01_computational_discovery/md/na_cl/remote_runs/remote_status.md)
- [Surface-display host selection report](02_experimental_validation/track_B_surface_display/research/surface_display_host_selection/reports/final_host_selection_report.md)
- [Deployment architecture report](03_industrial_translation/deployment_architecture/reports/final_deployment_architecture_report.md)
- [Repository reorganization report](06_shared/docs/repository_reorganization_report.md)
- [Branding assets](assets/branding/README.md)

## 📈 Research vision

LiSPER is meant to become more than a peptide list. It is a staged research program for discovering whether selective ion recognition can be engineered into compact, experimentally tractable peptide materials.

If successful, the platform could support:

- selective Li+/Na+ separation in battery-recycling streams
- peptide-based polishing after upstream transition-metal removal
- immobilized Bio-DLE media for lithium-bearing aqueous streams
- broader design principles for peptide-enabled ion separations

---

<p align="center">
  <strong>LiSPER asks a simple hard question:</strong><br>
  Can engineered peptide ensembles make lithium recovery more selective, biological, and modular?
</p>
