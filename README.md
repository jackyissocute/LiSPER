# LiSPER

## Lithium Selective Protein Engineering and Recovery

### Project Title

**Engineering Lithium Recognition through De Novo Design of Intrinsically Disordered Peptides Inspired by Lithium-Binding Motifs**

---

# Project Vision

LiSPER is a computational and experimental protein engineering project aimed at designing novel lithium-selective peptides capable of preferentially recognizing and binding Li⁺ over Na⁺ in aqueous environments.

The long-term application is sustainable lithium recovery from lithium-ion battery recycling streams.

The scientific objective is to establish whether intrinsically disordered peptide architectures inspired by known lithium-binding motifs can achieve measurable Li⁺/Na⁺ selectivity.

---

# Scientific Hypothesis

Two independent observations motivate this project:

## 1. Lithium-Binding Peptide (LBP) Literature

Previous studies reported short lithium-binding peptide motifs including:

GPGNP

and improved variants such as:

GPGDP

These motifs demonstrated lithium-binding capability and lithium recovery potential.

---

## 2. Intrinsically Disordered Proteins (IDPs)

Intrinsically disordered proteins do not possess a single stable structure.

Instead, they exist as dynamic structural ensembles capable of adapting to molecular binding events.

The project hypothesis is that:

- lithium-binding motifs provide Li⁺ recognition
- intrinsic disorder provides conformational flexibility
- combining both may improve lithium selectivity

---

# Core Research Question

Can de novo designed intrinsically disordered peptides inspired by lithium-binding motifs selectively bind Li⁺ over Na⁺ in aqueous solution?

---

# Selected Candidate Library

Current first-round peptide library:

## LiD3-1

GPGDPGSGPGDPGSGPGDP

## LiND-1

GPGNPGSGPGDPGSGPGNP

## LowCharge-Li

GPGDPGSGNPGSGDP

## IDP-Li-1

SGDSGPGDPGDSG

## IDP-Li-2

GDSGSGPGDPGSGDS

## Control-Negative

GPGAPGSGPGAPGSGPGAP

These sequences constitute the primary screening set.

Previous discarded sequences are not part of the current project.

---

# Computational Strategy

The objective is NOT merely strong lithium binding.

The objective is:

Li⁺ selectivity over Na⁺.

Therefore every candidate must be evaluated against BOTH ions.

---

# Computational Workflow

Sequence
↓
ESMFold
↓
CHARMM-GUI
↓
Molecular Dynamics Equilibration
↓
Structural Clustering
↓
Representative Structures
↓
Umbrella Sampling
↓
PMF
↓
ΔG(Li⁺)
ΔG(Na⁺)
↓
ΔΔG Selectivity

where:

ΔΔG = ΔG(Li⁺) - ΔG(Na⁺)

More negative values indicate stronger lithium preference.

---

# Important Simulation Decisions

## Water Model

TIP3P

## Force Field

CHARMM36m

## Simulation Box

Cubic

20 Å padding

## Ions

Use separate systems:

Protein + LiCl

Protein + NaCl

DO NOT perform first-round umbrella sampling using mixed Li⁺/Na⁺ systems.

Mixed systems are reserved for later validation.

---

# Why Separate Li⁺ and Na⁺ Simulations?

The project seeks a rigorous free-energy comparison.

Separate systems provide:

- cleaner PMF calculations
- cleaner ΔG estimates
- direct Li⁺/Na⁺ comparison
- easier interpretation

Mixed-ion competition simulations may be performed after top candidates are identified.

---

# Experimental Workflow

Candidate Selection
↓
Gene Design
↓
Codon Optimization
↓
Plasmid Construction
↓
E. coli Expression
↓
Protein Purification
↓
Li⁺ Binding Assay
↓
Na⁺ Competition Assay
↓
Li⁺/Na⁺ Selectivity Measurement

---

# Intended Application

Battery Recycling Process:

Spent Battery
↓
Hydrometallurgical Processing
↓
Removal of Co/Ni/Mn
↓
Li⁺ + Na⁺ Solution
↓
LiSPER Protein
↓
Selective Li⁺ Capture
↓
Elution
↓
Li₂CO₃ Production

The project does NOT currently focus on Co²⁺, Ni²⁺, or Mn²⁺ selectivity because these ions are expected to be removed upstream.

The primary challenge is Li⁺ vs Na⁺ separation.

---

# Repository Structure

LiSPER/

├── literature/
├── sequences/
├── esmfold/
├── charmm-gui/
├── md/
├── umbrella/
├── pmf/
├── plasmids/
├── wetlab/
├── figures/
├── manuscript/
└── README.md

---

# Project Philosophy

This project is a de novo protein engineering effort.

The goal is not to rediscover existing lithium-binding proteins.

The goal is to create and validate a new class of lithium-selective intrinsically disordered peptides through computational design and experimental verification.

---

Project: LiSPER

Lithium Selective Protein Engineering and Recovery