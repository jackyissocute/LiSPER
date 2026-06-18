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
| Lithium-selective peptide library | Li+/Na+ separation is central to lithium recovery | Final 8-candidate intake |
| Computational discovery engine | Prioritizes candidates before wet-lab cost | Full LiCl/NaCl MD setup gate |
| Experimental validation program | Converts predictions into measurable assays | Waiting for final codon/plasmid designs |
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
> **Live MD control panel.** The pre-MD intake gates are closed: final library, ESMFold structures, and paired LiCl/NaCl CHARMM-GUI systems are complete. LiCl setup is complete, and both LiCl and NaCl 20 ns production + clustering are now running on separate AutoDL workers.
>
> ![Setup QC](https://img.shields.io/badge/setup_QC-complete-16a34a)
> ![LiCl](https://img.shields.io/badge/LiCl-0.28--0.98_ns_of_20_ns-2563eb)
> ![NaCl](https://img.shields.io/badge/NaCl-0.02--0.12_ns_of_20_ns-2563eb)
> ![PMF](https://img.shields.io/badge/PMF-after_representatives-0f766e)

<p align="center">
  <a href="https://jackyissocute.github.io/LiSPER-Dashboard/"><strong>Open LiSPER Dashboard</strong></a>
</p>

**Last synchronized monitor snapshot:** `2026-06-18 20:07 CST`

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
      <td rowspan="2"><strong>Current gate</strong></td>
      <td>Paired production monitor</td>
      <td><code>🟩🟩🟩🟩🟩🟩🟩🟩</code> 16 active production jobs</td>
      <td><img alt="active" src="https://img.shields.io/badge/active-two_workers-2563eb"></td>
      <td>Monitor paired 20 ns production; clustering remains queued behind each job</td>
    </tr>
    <tr>
      <td>Production launch readiness</td>
      <td><code>🟩🟩🟩🟩🟩🟩🟩🟩</code> Both branches launched</td>
      <td><img alt="launched" src="https://img.shields.io/badge/launched-LiCl%2BNaCl-16a34a"></td>
      <td>Collect production logs first; representatives after clustering completes</td>
    </tr>
    <tr>
      <td rowspan="3"><strong>LiCl branch</strong></td>
      <td>Minimization + equilibration</td>
      <td><code>🟩🟩🟩🟩🟩🟩🟩🟩</code> 8 equilibrated</td>
      <td><img alt="running" src="https://img.shields.io/badge/complete-LiCl_setup-16a34a"></td>
      <td><a href="01_computational_discovery/md/li_cl/">LiCl setup complete</a></td>
    </tr>
    <tr>
      <td>20 ns production MD</td>
      <td><code>0.28-0.98 ns / 20 ns</code> across 8 active jobs</td>
      <td><img alt="LiCl production progress" src="https://img.shields.io/badge/active-8%2F8_jobs-2563eb"></td>
      <td>Li+ ensemble trajectories; current leader <code>LiDA-1</code> at <code>0.98 ns</code></td>
    </tr>
    <tr>
      <td>Structural clustering</td>
      <td><code>⬜⬜⬜⬜⬜⬜⬜⬜</code> queued after production</td>
      <td><img alt="queued" src="https://img.shields.io/badge/queued-after_20_ns-64748b"></td>
      <td>Li+ representative structures</td>
    </tr>
    <tr>
      <td rowspan="3"><strong>NaCl branch</strong></td>
      <td>Minimization + equilibration</td>
      <td><code>🟩🟩🟩🟩🟩🟩🟩🟩</code> 8 equilibrated</td>
      <td><img alt="complete" src="https://img.shields.io/badge/complete-setup_QC-16a34a"></td>
      <td><a href="01_computational_discovery/md/na_cl/">NaCl workspace</a></td>
    </tr>
    <tr>
      <td>20 ns production MD</td>
      <td><code>0.02-0.12 ns / 20 ns</code> across 8 active jobs</td>
      <td><img alt="NaCl production progress" src="https://img.shields.io/badge/active-8%2F8_jobs-2563eb"></td>
      <td>Matched Na+ comparison ensembles; current leader <code>LiDA-1</code> at <code>0.12 ns</code></td>
    </tr>
    <tr>
      <td>Structural clustering</td>
      <td><code>⬜⬜⬜⬜⬜⬜⬜⬜</code> planned after production</td>
      <td><img alt="planned" src="https://img.shields.io/badge/planned-after_20ns-0f766e"></td>
      <td>Na+ representative structures</td>
    </tr>
    <tr>
      <td rowspan="2"><strong>Free energy</strong></td>
      <td>Umbrella sampling</td>
      <td><code>⬜⬜⬜⬜⬜⬜⬜⬜</code> planned</td>
      <td><img alt="planned" src="https://img.shields.io/badge/planned-after_representatives-0f766e"></td>
      <td>Window design and biased sampling</td>
    </tr>
    <tr>
      <td>WHAM / PMF / ΔG</td>
      <td><code>⬜⬜⬜⬜⬜⬜⬜⬜</code> planned</td>
      <td><img alt="planned" src="https://img.shields.io/badge/planned-after_umbrella_sampling-0f766e"></td>
      <td>ΔG and ΔΔG selectivity ranking</td>
    </tr>
  </tbody>
</table>

### Protein-focused matrix

<sub>LiCl and NaCl setup are complete for all eight candidates, so this live matrix now focuses on active and upcoming production/free-energy gates.</sub>

<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>LiCl production / representative</th>
      <th>NaCl production / representative</th>
      <th>Umbrella sampling</th>
      <th>WHAM / PMF / ΔG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>LiD3-Core</strong></td>
      <td>🟦 <code>0.43 ns / 20 ns</code>; clustering queued</td>
      <td>🟦 <code>0.03 ns / 20 ns</code>; clustering queued</td>
      <td>🟪 planned after paired representatives</td>
      <td>🟪 planned after umbrella sampling</td>
    </tr>
    <tr>
      <td><strong>LiD3-Flex</strong></td>
      <td>🟦 <code>0.29 ns / 20 ns</code>; clustering queued</td>
      <td>🟦 <code>0.02 ns / 20 ns</code>; clustering queued</td>
      <td>🟪 planned after paired representatives</td>
      <td>🟪 planned after umbrella sampling</td>
    </tr>
    <tr>
      <td><strong>LiND-Hybrid</strong></td>
      <td>🟦 <code>0.28 ns / 20 ns</code>; clustering queued</td>
      <td>🟦 <code>0.04 ns / 20 ns</code>; clustering queued</td>
      <td>🟪 planned after paired representatives</td>
      <td>🟪 planned after umbrella sampling</td>
    </tr>
    <tr>
      <td><strong>LiLC-1</strong></td>
      <td>🟦 <code>0.44 ns / 20 ns</code>; clustering queued</td>
      <td>🟦 <code>0.06 ns / 20 ns</code>; clustering queued</td>
      <td>🟪 planned after paired representatives</td>
      <td>🟪 planned after umbrella sampling</td>
    </tr>
    <tr>
      <td><strong>LiDS-1</strong></td>
      <td>🟦 <code>0.67 ns / 20 ns</code>; clustering queued</td>
      <td>🟦 <code>0.08 ns / 20 ns</code>; clustering queued</td>
      <td>🟪 planned after paired representatives</td>
      <td>🟪 planned after umbrella sampling</td>
    </tr>
    <tr>
      <td><strong>LiDA-1</strong></td>
      <td>🟦 <code>0.98 ns / 20 ns</code>; clustering queued</td>
      <td>🟦 <code>0.12 ns / 20 ns</code>; clustering queued</td>
      <td>🟪 planned after paired representatives</td>
      <td>🟪 planned after umbrella sampling</td>
    </tr>
    <tr>
      <td><strong>LiN3-Core</strong></td>
      <td>🟦 <code>0.44 ns / 20 ns</code>; clustering queued</td>
      <td>🟦 <code>0.03 ns / 20 ns</code>; clustering queued</td>
      <td>🟪 planned after paired representatives</td>
      <td>🟪 planned after umbrella sampling</td>
    </tr>
    <tr>
      <td><strong>LiA3-Ref</strong></td>
      <td>🟦 <code>0.43 ns / 20 ns</code>; clustering queued</td>
      <td>🟦 <code>0.03 ns / 20 ns</code>; clustering queued</td>
      <td>🟪 planned after paired representatives</td>
      <td>🟪 planned after umbrella sampling</td>
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
      <td><strong>Setup QC completion</strong></td>
      <td align="center"><strong><code>Complete</code></strong><br><sub>LiCl and NaCl setup gate is closed</sub></td>
      <td>Setup gate is closed; continue production/clustering QC.</td>
    </tr>
    <tr>
      <td><strong>20 ns production + clustering</strong></td>
      <td align="center"><strong><code>~3-6 days</code></strong><br><sub>LiCl on worker A; NaCl on worker B</sub></td>
      <td>Collect production logs, cluster trajectories, and extract dominant representative structures.</td>
    </tr>
    <tr>
      <td><strong>Umbrella sampling</strong></td>
      <td align="center"><strong><code>~5-10 days after representatives</code></strong><br><sub>likely longest compute gate; depends on window count and sampling length</sub></td>
      <td>Design windows from paired representatives, run biased sampling, and check window overlap.</td>
    </tr>
    <tr>
      <td><strong>WHAM / PMF / ΔG extraction</strong></td>
      <td align="center"><strong><code>~1-2 days after umbrella sampling</code></strong><br><sub>analysis, convergence checks, and reruns if needed</sub></td>
      <td>Run WHAM/PMF analysis, inspect convergence, then extract ΔG for paired Li+/Na+ systems.</td>
    </tr>
    <tr>
      <td><strong>First ΔΔG selectivity table</strong></td>
      <td align="center"><strong><code>~10-18 days</code></strong><br><sub>first defensible table; full 8-candidate table may extend longer</sub></td>
      <td>Complete paired PMFs, then compute ΔΔG = ΔG(Na+) - ΔG(Li+) and rank candidates.</td>
    </tr>
  </tbody>
</table>

> Time estimates are conservative and will tighten after the first paired LiCl/NaCl production jobs finish and clustering reports are available.

<details>
<summary><strong>Current MD interpretation</strong></summary>

- `LiD3-Flex` and `LiND-Hybrid` already have LiCl production/clustering representatives available under the final candidate names.
- `LiLC-1` already has upstream setup/equilibration assets available and still needs LiCl production/clustering completion.
- LiCl minimization and equilibration are complete for all eight candidates.
- NaCl setup is complete for all eight candidates.
- LiCl and NaCl 20 ns production/clustering are running in parallel on separate workers.
- All eight LiCl and all eight NaCl CHARMM-GUI systems are GROMACS-ready.
- Active MD should continue only from final 8-candidate names and matched LiCl/NaCl systems.

</details>

## 🧪 Candidate library

The active LiSPER library contains 8 candidates selected from the updated LBP, IDP, and Li+ coordination design logic. All eight candidates have paired LiCl/NaCl systems in active 20 ns production MD.

| Rank | Candidate | Sequence | Design role | Current MD status |
|---:|---|---|---|---|
| 1 | **LiD3-Core** | `GPGDPGPGDPGPGDP` | Linker-free GPGDP trimer benchmark | LiCl `0.43/20 ns`; NaCl `0.03/20 ns` |
| 2 | **LiD3-Flex** | `GPGDPGSGPGDPGSGPGDP` | Flexible GSG-spaced GPGDP trimer | LiCl `0.29/20 ns`; NaCl `0.02/20 ns` |
| 3 | **LiND-Hybrid** | `GPGNPGSGPGDPGSGPGNP` | Mixed GPGNP/GPGDP donor environment | LiCl `0.28/20 ns`; NaCl `0.04/20 ns` |
| 4 | **LiLC-1** | `GPGDPGSGNPGSGDP` | Lower-charge selectivity-control design | LiCl `0.44/20 ns`; NaCl `0.06/20 ns` |
| 5 | **LiDS-1** | `DGDGPGDPGDG` | Asp/Gly Li+/Na+ geometry probe | LiCl `0.67/20 ns`; NaCl `0.08/20 ns` |
| 6 | **LiDA-1** | `DADGPGDPDAG` | Ala-supported Asp pocket probe | LiCl `0.98/20 ns`; NaCl `0.12/20 ns` |
| 7 | **LiN3-Core** | `GPGNPGPGNPGPGNP` | GPGNP trimer benchmark | LiCl `0.44/20 ns`; NaCl `0.03/20 ns` |
| 8 | **LiA3-Ref** | `GPGAPGPGAPGPGAP` | Low-donor GPGAP reference | LiCl `0.43/20 ns`; NaCl `0.03/20 ns` |

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

The first experimental subset will be chosen from the final 8-candidate computational ranking. A conservative early bench subset is expected to include `LiD3-Core`, `LiD3-Flex`, `LiND-Hybrid`, `LiLC-1`, and `LiA3-Ref`.

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
| [`archive/`](archive/) | Superseded working materials kept outside the active workflow |

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
