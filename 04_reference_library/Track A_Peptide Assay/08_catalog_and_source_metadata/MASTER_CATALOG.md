# Master Catalog — Track A Peptide Assay Literature

Retrieved / organized: 2026-07-11 for LiSPER Track A protocol design.

## How to cite from this library

Prefer DOI in manuscripts. Local files are working copies for protocol writing.

---

## 01 Lithium-binding peptide precedent

| File | Citation | DOI / ID | Access | Track A use |
|---|---|---|---|---|
| `Selvamani_2022_JECE_LBP_surface_display_construction.pdf` | Selvamani et al., *J. Environ. Chem. Eng.* 2022/2023, 11, 109029 | 10.1016/j.jece.2022.109029 | Local PDF (publisher paywalled online) | Motif GPGAP/GPGDP/GPGNP; assay endpoints for Li uptake |
| `Jeong_2024_JIMB_LBP_trimers_industrial_waste.pdf` | Jeong et al., *J. Ind. Microbiol. Biotechnol.* 2024, 51, kuae012 | 10.1093/jimb/kuae012 | Local PDF + OA (PMC11037431) | Trimer vs monomer capacity; competition vs Ni/Co/Mn |
| `Recycling_2026_biotech_strategies_Li_metal_binding_peptides_review.md` | *Recycling* 2026, 11(1), 4 | 10.3390/recycling11010004 | OA HTML capture | Broad review of peptide/microbe Li recovery |
| `Zhang_2024_MetaLATTE_metal_binding_prediction_bioRxiv.pdf` | Zhang et al., bioRxiv 2024 | 10.1101/2024.06.26.600843 | OA PDF | ML metal-binding prediction context |
| `Zhang_2025_Metalorian_de_novo_metal_binding_peptides_bioRxiv.pdf` | Zhang et al., bioRxiv 2025 | 10.1101/2025.07.10.664242 | OA PDF | De novo metal-binding peptides + wet validation ideas |

---

## 02 Immobilized peptide / bead assays (PRIMARY Track A format)

| File | Citation | DOI / ID | Access | Track A use |
|---|---|---|---|---|
| `Bhargawa_2024_Desalination_magnetic_beads_GPGDP.pdf` | Bhargawa, Hong, Yoo, *Desalination* 2024, 117412 | 10.1016/j.desal.2024.117412 | Local PDF (paywalled online) | **Core protocol precedent:** EDC/NHS bead conjugation, Langmuir isotherm, Li vs competitors, reuse cycles |
| `Xu_2020_ApplSci_magnetic_adsorbent_Pb_binding_peptide.md` | Xu & Yoo, *Appl. Sci.* 2020, 10(18), 6418 | 10.3390/app10186418 | OA HTML capture | Bead + selective peptide workflow (Pb case; method transferable) |

**Protocol takeaways from Bhargawa 2024**

- Conjugate peptide to magnetic beads (EDC/NHS).
- Compare monomer GPGDP vs trimer Pep-D3.
- Quantify adsorbed Li after magnetic separation.
- Test competition with other metal ions.
- Fit Langmuir `q_max` when isotherm saturates.

For LiSPER: replace Pb/Ni/Cu competitors with **Na⁺** as the primary selectivity competitor; keep Li-only and competition arms.

---

## 03 Dialysis / solution selectivity assays

| File | Citation | DOI / ID | Access | Track A use |
|---|---|---|---|---|
| `Adams_2026_ChemSci_Li_selective_tripeptide_gelators_dialysis_ICP.md` (+ `.fulltext.xml`) | Adams et al., *Chem. Sci.* 2026 (PMC13093460) | 10.1039/D6SC01183G | OA full text via Europe PMC | **Core free-solution method:** dialysis cassette, Li-only / Na-only / 1:1 Li+Na, ICP-OES of dialysate |

**Protocol takeaways**

- Put peptide (or peptide solution) inside dialysis membrane.
- External baths: LiCl, NaCl, or equimolar mix.
- Measure external [Li] and [Na] before/after by ICP-OES.
- Net decrease = uptake; Na increase with Li decrease can indicate exchange.

Validate peptide retention for ~1–2 kDa LiSPER peptides before trusting bound/free split.

---

## 04 ICP-OES / ICP-MS ion quantification

| File | Citation | Notes |
|---|---|---|
| `ICP_quantification_guidance_for_Track_A.md` | Curated method notes + DOI pointers | Practical Li/Na quantification checklist for protocol writing |

Key citable pointers (access often institutional):

- Doherty et al., *JAAS* — lithium isotope / matrix notes: 10.1039/b907122a
- Use **ICP-OES** for routine mM-range Li/Na; **ICP-MS** for trace.
- Matrix: high Na can affect Li measurement — dilute into calibration range; match acid matrix (typically 2% HNO₃).

---

## 05 NMR / ITC thermodynamic methods (optional)

| File | Citation | DOI / ID | Access | Track A use |
|---|---|---|---|---|
| `Brachvogel_2015_IJMS_NMR_Li_Na_K_cryptand.md` (+ xml + MDPI webpage md) | Brachvogel et al., *Int. J. Mol. Sci.* 2015, 16, 20641 | 10.3390/ijms160920641 | OA | ⁷Li / alkali NMR complexation precedent (cryptand, not peptide — method analogy) |

Use only if bead/dialysis show clear binding and you need K / stoichiometry support.

---

## 06 Peptide QC, counterions, handling

| File | Citation | DOI / ID | Access | Track A use |
|---|---|---|---|---|
| `AAPPTec_TSIB1085_Removing_TFA_from_peptides.pdf` | AAPPTec Technical Bulletin 1085 | vendor tech note | Local PDF | TFA→HCl / TFA→acetate exchange recipes |
| `Guzman_2025_Processes_peptide_purification_counterion_exchange_SPE.md` | Guzmán et al., *Processes* 2025, 13(1), 27 | 10.3390/pr13010027 | OA HTML | SPE one-step purify + counterion exchange |
| `Neelakantan_2012_Hindawi_TFA_to_acetate_exchange_anion_resin.md` | Neelakantan et al., *Int. J. Pept. Sci.* style Hindawi 2012 | 10.1155/2012/323907 | OA HTML | Anion-exchange TFA→acetate at scale |

Also useful PubMed record (no local full text yet):

- Roux et al., elimination/exchange of TFA counter-ion — PMID 18035848

**Why this matters for Li/Na assays:** vendor peptides often arrive as TFA salts; residual Na⁺/TFA can inflate blanks and distort ICP.

---

## 07 Surface display (Track B bridge only)

| File | Citation | DOI / ID | Access | Use |
|---|---|---|---|---|
| `Jeong_2024_JIMB_surface_display_LBP_battery_waste.pdf` | same as Jeong 2024 | 10.1093/jimb/kuae012 | Local PDF | Track B design after Track A ranking |
| `Jeong_2024_JIMB_LBP_surface_display_battery_waste_EPMC.md` (+ xml) | same | PMC11037431 | OA full text | searchable text copy |
| `Selvamani_2022_JECE_LBP_surface_display_construction.pdf` | Selvamani 2022 | 10.1016/j.jece.2022.109029 | Local PDF | Display construction |
| `Sousa_1999_AEM_surface_display_metal_binding_peptides_PMC91149.md` | Sousa et al., *Appl. Environ. Microbiol.* 1999 | 10.1128/aem.65.3.1092-1098.1999 | PMC HTML | Classic short metal-binding peptide display |

---

## Suggested Track A reading order for protocol drafting

1. AAPPTec TFA bulletin + Guzmán 2025 (QC / counterion)
2. Bhargawa 2024 beads (primary assay)
3. Adams 2026 Chem Sci dialysis+ICP (optional free-solution confirmation)
4. Selvamani 2022 + Jeong 2024 (what “success” looks like for LBP motifs)
5. Recycling 2026 review (big-picture framing for intro/discussion)

---

## Paywall / missing PDF log

| Item | Status | Local substitute |
|---|---|---|
| Chem Sci PDF binary | Publisher blocked automated PDF; OA exists | Europe PMC `.md` + `.fulltext.xml` |
| MDPI PDF binaries | Often 403 to bots | HTML → `.md` captures |
| Desalination / JECE | Paywalled | Local PDFs already in repo from prior LBP collection |
| Braun 2018 peptides-as-biosorbents | Paywalled | Listed; obtain via campus library if needed (DOI 10.1016/j.resmic.2018.06.001) |
| Hindawi PDF | 403 | HTML capture stored |

Do **not** use unauthorized pirate sites. Prefer DOI + institutional access for any missing PDF.
