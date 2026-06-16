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

The repository now follows a clear program model:

- `01-03` are the active research pipeline.
- `04-06` are support layers for evidence, communication, and operations.
- `assets/` stores reusable branding and media.
- `archive/` preserves non-current material without presenting it as active work.

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
flowchart TD
    accTitle: LiSPER Scientific Thesis
    accDescr: LiSPER combines motif precedent, peptide flexibility, and oxygen-donor chemistry to generate candidates that are tested for Li over Na selectivity.

    motifs["💡 Li-binding<br/>motifs"]
    flexibility["🔄 IDP-like<br/>flexibility"]
    donors["⚙️ Oxygen-donor<br/>residues"]
    candidates["🧪 LiSPER<br/>candidate peptides"]
    ensembles["📊 Simulated<br/>ensembles"]
    comparison["🔍 Li+ vs Na+<br/>comparison"]
    selectivity["🎯 Selectivity<br/>ranking"]

    motifs --> candidates
    flexibility --> candidates
    donors --> candidates
    candidates --> ensembles
    ensembles --> comparison
    comparison --> selectivity

    classDef idea fill:#fef9c3,stroke:#ca8a04,stroke-width:2px,color:#713f12
    classDef peptide fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#3b0764
    classDef result fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d

    class motifs,flexibility,donors idea
    class candidates,ensembles,comparison peptide
    class selectivity result
```

## 🧭 Program roadmap

LiSPER is organized as a three-stage program: discover the molecular principle, validate it experimentally, then translate the best peptide systems into capture materials.

```mermaid
flowchart TD
    accTitle: LiSPER Three-Phase Roadmap
    accDescr: LiSPER moves from computational discovery to two parallel experimental validation tracks and then to industrial translation.

    phase_one["🔍 Phase I<br/>Computational<br/>discovery"]
    rank["📊 Li/Na<br/>ranking"]
    phase_two["🧪 Phase II<br/>Experimental<br/>validation"]
    track_a["Track A<br/>purified peptide"]
    track_b["Track B<br/>surface display"]
    phase_three["📦 Phase III<br/>Industrial<br/>translation"]

    phase_one --> rank
    rank --> phase_two
    phase_two --> track_a
    phase_two --> track_b
    track_a --> phase_three
    track_b --> phase_three

    classDef computational fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f
    classDef experimental fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    classDef industrial fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#7c2d12
    class phase_one,rank computational
    class phase_two,track_a,track_b experimental
    class phase_three industrial
```

| Phase | Goal | Status | Near-term gate |
|---|---|---|---|
| **I. Computational discovery** | Rank LiSPER candidates by Li+/Na+ selectivity | Active | Finish production MD, clustering, umbrella sampling, PMF |
| **II. Experimental validation** | Test whether designed peptides show measurable selectivity | Preparing | Express purified-peptide constructs and prepare surface-display validation |
| **III. Industrial translation** | Convert validated peptides into capture media | Concept stage | Select immobilization and column prototype strategy |

## 📊 Progress monitor dashboard

> [!IMPORTANT]
> **Live project control panel.** This cover-page dashboard compresses the active LiSPER workflow into two views: a process matrix and a remaining-time horizon. Detailed logs remain in the linked MD status files so the README stays readable.
>
> ![Computational discovery](https://img.shields.io/badge/Phase_I-computational_discovery_active-2563eb)
> ![Remote MD](https://img.shields.io/badge/remote_MD-LiND--1_running-0f766e)
> ![NaCl queue](https://img.shields.io/badge/NaCl_queue-waiting-f59e0b)
> ![PMF](https://img.shields.io/badge/PMF-planned-0f766e)

<p align="center">
  <a href="https://jackyissocute.github.io/LiSPER-Dashboard/"><strong>Open LiSPER Dashboard</strong></a>
</p>

**Last synchronized monitor snapshot:** `2026-06-16 13:30 CST`

### Process matrix

<table>
  <thead>
    <tr>
      <th>Track</th>
      <th>Process</th>
      <th>Progress</th>
      <th>Status</th>
      <th>Gate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3"><strong>Program roadmap</strong></td>
      <td>Phase I computational discovery</td>
      <td><code>🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜</code> 70%</td>
      <td><img alt="active" src="https://img.shields.io/badge/active-2563eb"></td>
      <td>ΔΔG ranking</td>
    </tr>
    <tr>
      <td>Phase II experimental validation</td>
      <td><code>🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜</code> 20%</td>
      <td><img alt="preparing" src="https://img.shields.io/badge/preparing-16a34a"></td>
      <td>Expression + assays</td>
    </tr>
    <tr>
      <td>Phase III Bio-DLE translation</td>
      <td><code>🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜</code> 10%</td>
      <td><img alt="concept" src="https://img.shields.io/badge/concept-ea580c"></td>
      <td>Immobilized format</td>
    </tr>
    <tr>
      <td rowspan="4"><strong>System preparation</strong></td>
      <td>Candidate library</td>
      <td><code>🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩</code> 10/10</td>
      <td><img alt="complete" src="https://img.shields.io/badge/complete-16a34a"></td>
      <td>Library locked</td>
    </tr>
    <tr>
      <td>ESMFold structures</td>
      <td><code>🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩</code> 10/10</td>
      <td><img alt="complete" src="https://img.shields.io/badge/complete-16a34a"></td>
      <td>MD starting models</td>
    </tr>
    <tr>
      <td>CHARMM-GUI systems</td>
      <td><code>🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩</code> 20/20</td>
      <td><img alt="complete" src="https://img.shields.io/badge/complete-16a34a"></td>
      <td>LiCl + NaCl ready</td>
    </tr>
    <tr>
      <td>Minimization + equilibration</td>
      <td><code>🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩</code> 20/20</td>
      <td><img alt="complete" src="https://img.shields.io/badge/complete-16a34a"></td>
      <td>Production-ready</td>
    </tr>
    <tr>
      <td rowspan="2"><strong>LiCl branch</strong></td>
      <td>20 ns production MD</td>
      <td><code>🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜</code> 3 complete + 1 active</td>
      <td><img alt="LiND-1 running" src="https://img.shields.io/badge/LiND--1-0.00_ns_%2F_20_ns-2563eb"></td>
      <td><a href="01_computational_discovery/md/li_cl/remote_runs/remote_status.md">LiCl status</a></td>
    </tr>
    <tr>
      <td>Structural clustering</td>
      <td><code>🟪🟪🟪⬜⬜⬜⬜⬜⬜⬜</code> 3/10 representatives</td>
      <td><img alt="active" src="https://img.shields.io/badge/active-7c3aed"></td>
      <td>Representative set</td>
    </tr>
    <tr>
      <td><strong>NaCl branch</strong></td>
      <td>Production + clustering</td>
      <td><code>🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜</code> queued</td>
      <td><img alt="queued" src="https://img.shields.io/badge/queued-after_LiCl-f59e0b"></td>
      <td><a href="01_computational_discovery/md/na_cl/remote_runs/remote_status.md">NaCl status</a></td>
    </tr>
    <tr>
      <td><strong>Free energy</strong></td>
      <td>Umbrella sampling + PMF</td>
      <td><code>⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜</code> planned</td>
      <td><img alt="planned" src="https://img.shields.io/badge/planned-after_representatives-0f766e"></td>
      <td>ΔG and ΔΔG</td>
    </tr>
  </tbody>
</table>

### Protein-focused matrix

<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>Setup</th>
      <th>LiCl production</th>
      <th>LiCl clustering</th>
      <th>NaCl branch</th>
      <th>Free-energy gate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>LiD3-1</strong></td>
      <td>✅ complete</td>
      <td>✅ 20 ns</td>
      <td>✅ representative<br><sub>top cluster 15.69%</sub></td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
    <tr>
      <td><strong>LiND-1</strong></td>
      <td>✅ complete</td>
      <td>▶️ running<br><sub>0.00 ns / 20 ns</sub></td>
      <td>⏳ next</td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
    <tr>
      <td><strong>IDP-Li-1</strong></td>
      <td>✅ complete</td>
      <td>✅ 20 ns</td>
      <td>✅ representative<br><sub>top cluster 7.00%</sub></td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
    <tr>
      <td><strong>IDP-Li-2</strong></td>
      <td>✅ complete</td>
      <td>🔁 rerun queued</td>
      <td>⏳ waiting</td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
    <tr>
      <td><strong>LowCharge-Li</strong></td>
      <td>✅ complete</td>
      <td>🔁 rerun queued</td>
      <td>⏳ waiting</td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
    <tr>
      <td><strong>LiD2-IDP</strong></td>
      <td>✅ complete</td>
      <td>🔁 rerun queued</td>
      <td>⏳ waiting</td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
    <tr>
      <td><strong>StrongBind-Li</strong></td>
      <td>✅ complete</td>
      <td>✅ 20 ns</td>
      <td>✅ representative<br><sub>top cluster 3.45%</sub></td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
    <tr>
      <td><strong>SoftCage-Li</strong></td>
      <td>✅ complete</td>
      <td>⏳ queued</td>
      <td>⏳ waiting</td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
    <tr>
      <td><strong>IDP-Rich-Li</strong></td>
      <td>✅ complete</td>
      <td>⏳ queued</td>
      <td>⏳ waiting</td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
    <tr>
      <td><strong>Control-Negative</strong></td>
      <td>✅ complete</td>
      <td>⏳ queued</td>
      <td>⏳ waiting</td>
      <td>⏳ queued</td>
      <td>⏳ PMF pending</td>
    </tr>
  </tbody>
</table>

### Remaining-time horizon

<table>
  <thead>
    <tr>
      <th>Gate</th>
      <th>Time remaining</th>
      <th>What clears the gate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Active LiND-1 LiCl production</strong></td>
      <td align="center"><strong><code>~18-25 hours</code></strong><br><sub>current run</sub></td>
      <td>Finish the current 20 ns production and hand off to clustering.</td>
    </tr>
    <tr>
      <td><strong>LiCl production + clustering set</strong></td>
      <td align="center"><strong><code>~7-9 days</code></strong><br><sub>LiCl branch</sub></td>
      <td>Complete repaired LiCl reruns, queued LiCl systems, and representatives.</td>
    </tr>
    <tr>
      <td><strong>NaCl production + clustering set</strong></td>
      <td align="center"><strong><code>~10 additional days</code></strong><br><sub>NaCl branch</sub></td>
      <td>Run matched NaCl production and clustering after LiCl releases the queue.</td>
    </tr>
    <tr>
      <td><strong>PMF / ΔG extraction</strong></td>
      <td align="center"><strong><code>~3-7 days</code></strong><br><sub>after representatives</sub></td>
      <td>Build umbrella windows, run sampling, then perform WHAM/PMF QC.</td>
    </tr>
    <tr>
      <td><strong>First ΔΔG selectivity table</strong></td>
      <td align="center"><strong><code>~3-4 weeks total</code></strong><br><sub>first selectivity table</sub></td>
      <td>Complete LiCl and NaCl PMFs, then compute ΔΔG = ΔG(Na+) - ΔG(Li+).</td>
    </tr>
  </tbody>
</table>

> Time estimates are CPU-only planning ranges from the current AutoDL/GROMACS pace. They will tighten after LiND-1 completes and the corrected LiCl queue advances.

<details>
<summary><strong>Current MD interpretation</strong></summary>

- `LiD3-1`, `IDP-Li-1`, and `StrongBind-Li` completed 20 ns LiCl production and now have repaired peptide-only representative structures.
- Their top-cluster populations are low (`15.69%`, `7.00%`, and `3.45%`), which supports the IDP-like design hypothesis and argues for comparing additional representatives before relying on a single umbrella-sampling start.
- `LiND-1` is the active LiCl production run through the corrected topology-path workflow.
- `IDP-Li-2`, `LowCharge-Li`, and `LiD2-IDP` were previously blocked by a topology include-path setup issue, not by peptide physics; corrected production logic is now advancing candidate by candidate.

</details>

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
    accDescr: The computational workflow keeps LiCl and NaCl systems parallel so the final PMF comparison supports Li over Na selectivity ranking.

    sequences["📋 Candidate<br/>sequences"]
    structures["🔍 ESMFold<br/>structures"]
    systems["⚙️ CHARMM-GUI<br/>systems"]

    subgraph li_branch["Li+ branch"]
        li_md["📊 LiCl<br/>MD"]
        li_cluster["🔍 Li+<br/>clustering"]
        li_pmf["⚙️ Li+<br/>PMF"]
    end

    subgraph na_branch["Na+ branch"]
        na_md["📊 NaCl<br/>MD"]
        na_cluster["🔍 Na+<br/>clustering"]
        na_pmf["⚙️ Na+<br/>PMF"]
    end

    ranking["✅ Li/Na<br/>selectivity"]

    sequences --> structures
    structures --> systems
    systems --> li_md
    systems --> na_md
    li_md --> li_cluster --> li_pmf
    na_md --> na_cluster --> na_pmf
    li_pmf --> ranking
    na_pmf --> ranking

    classDef input fill:#f3f4f6,stroke:#6b7280,stroke-width:2px,color:#1f2937
    classDef simulation fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f
    classDef analysis fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#3b0764
    classDef result fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d

    class sequences,structures,systems input
    class li_md,na_md,li_pmf,na_pmf simulation
    class li_cluster,na_cluster analysis
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
| **Track A: purified peptide** | Intrinsic LiSPER binding behavior | Li+ binding, Na+ competition, selectivity trend |
| **Track A: His6-SUMO fusion** | Expressible peptide production route | Soluble expression, purification, cleavage |
| **Track B: surface display** | LiSPER as biological capture interface | Whole-cell Li capture and Na competition |

The first experimental subset is `LiD3-1`, `LiND-1`, `IDP-Li-1`, `LowCharge-Li`, and `Control-Negative`.

## 🏭 Industrial outlook

The long-term deployment concept is an immobilized peptide capture process rather than a free peptide in solution.

```mermaid
flowchart TD
    accTitle: Bio-DLE Translation Path
    accDescr: The industrial translation path converts validated LiSPER peptides into immobilized capture media for column operation and lithium recovery.

    peptide["🧪 Validated<br/>LiSPER peptide"]
    immobilization["⚙️ Immobilization<br/>chemistry"]
    beads["📦 Magnetic bead<br/>prototype"]
    resin["📦 Resin capture<br/>media"]
    column["⚙️ Packed-bed<br/>column"]
    recovery["✅ Li2CO3<br/>recovery path"]

    peptide --> immobilization
    immobilization --> beads
    beads --> resin
    resin --> column
    column --> recovery

    classDef experimental fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    classDef industrial fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#7c2d12
    classDef result fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f

    class peptide experimental
    class immobilization,beads,resin,column industrial
    class recovery result
```

**Vision:** LiSPER peptides -> Li+/Na+ selectivity -> experimental validation -> immobilized peptide systems -> peptide-enabled Direct Lithium Extraction.

## 📍 Repository navigation

The repository is organized as a research pipeline plus support layers. Folders `01-03` hold the active scientific program, while folders `04-06` hold references, communication outputs, and project operations.

```mermaid
flowchart TD
    accTitle: Repository Organization Model
    accDescr: The repository is organized as a three-stage research pipeline with reference, communication, and operations support layers.

    A["01 Computational Discovery"] --> B["02 Experimental Validation"]
    B --> C["03 Industrial Translation"]
    D["04 Reference Library"] --> E["Evidence base"]
    F["05 Outputs and Communication"] --> G["Manuscripts<br/>figures<br/>decks"]
    H["06 Project Operations"] --> I["Guides<br/>scripts<br/>inbox"]
    E -.-> A
    E -.-> B
    E -.-> C
    A --> F
    B --> F
    C --> F
    H -.-> A
    H -.-> B
    H -.-> C

    classDef phase fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a
    classDef support fill:#fef9c3,stroke:#ca8a04,stroke-width:2px,color:#713f12
    classDef output fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#3b0764
    class A,B,C phase
    class D,E,H,I support
    class F,G output
```

| Directory | Purpose |
|---|---|
| [`01_computational_discovery/`](01_computational_discovery/) | Candidate sequences, ESMFold structures, CHARMM-GUI systems, MD, umbrella sampling, PMF, and analysis |
| [`02_experimental_validation/`](02_experimental_validation/) | Plasmids, wet-lab planning, purified-peptide validation, surface-display validation, and assay protocols |
| [`03_industrial_translation/`](03_industrial_translation/) | Immobilized capture formats, packed-bed process design, and deployment architecture |
| [`04_reference_library/`](04_reference_library/) | External evidence base: papers, patents, source metadata, citation exports, and reading notes |
| [`05_outputs_and_communication/`](05_outputs_and_communication/) | Manuscripts, figures, presentations, milestone summaries, and reviewer-facing materials |
| [`06_project_operations/`](06_project_operations/) | Repository guides, reusable scripts, decision records, and temporary intake inbox |
| [`assets/`](assets/) | Official LiSPER branding assets and reusable non-data media |
| [`archive/`](archive/) | Superseded designs and preserved legacy materials |

## 🔗 Key project documents

- [Repository guide](06_project_operations/docs/repository_guide.md)
- [Candidate design rationale](06_project_operations/docs/candidate_design_rationale.md)
- [MD to PMF workflow](06_project_operations/docs/md_to_pmf_workflow.md)
- [LiCl MD status](01_computational_discovery/md/li_cl/remote_runs/remote_status.md)
- [NaCl MD status](01_computational_discovery/md/na_cl/remote_runs/remote_status.md)
- [Surface-display host selection report](02_experimental_validation/track_B_surface_display/research/surface_display_host_selection/reports/final_host_selection_report.md)
- [Deployment architecture report](03_industrial_translation/deployment_architecture/reports/final_deployment_architecture_report.md)
- [Repository reorganization report](06_project_operations/docs/repository_reorganization_report.md)
- [README polish report](06_project_operations/docs/readme_polish_report_2026-06-15.md)
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
