<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Now, I want to learn how to build my plasmids using the eCPX surface displaying system for E. coli K-12 / MG1655-compatible strain. Search for reliable sources and give me a detailed instruction on how to link the related display gene and my peptide and build a plasmid. Also, recommend the top two suitable vectors for this project.

I now have all the information needed to write a comprehensive plasmid construction guide. Let me compile the response.

***

## eCPX Surface Display Plasmid Construction in *E. coli* K-12 MG1655

The eCPX (Enhanced Circularly Permuted OmpX) system, developed by Rice and Daugherty (2008), is the gold standard for peptide surface display in *E. coli*. It circularly permutes the outer membrane protein OmpX so that **both N- and C-termini are exposed on the cell exterior**, allowing biterminal peptide fusion and quantitative FACS/MACS screening. Here is a step-by-step protocol to link your peptide gene to the eCPX display gene and build an MG1655-compatible plasmid.[^1][^2][^3]

***

## The eCPX Scaffold Architecture

Before cloning, you must understand the gene organization of eCPX, as this dictates exactly where your peptide is inserted.[^3]

The full eCPX gene (from 5′ to 3′) is organized as:

```
[OmpX signal peptide] → [SfiI site / GQSGQ linker] → [Peptide (N-term)]
→ [GGQSGQS linker] → [OmpX residues S54–F148]
→ [GSKSRR internal linker joining native termini] → [OmpX residues A1–S53]
→ [C-terminal peptide (optional)]
```

Key features:[^3]

- The **OmpX signal peptide** directs the protein to the outer membrane and is cleaved after translocation
- An **embedded SfiI restriction site** (encoding GQSGQ) sits immediately after the signal sequence — this is your peptide insertion point at the **N-terminus**
- The evolved linker **GSKSRR** joins the circularly permuted native termini; combined with substitutions **A165L and G166S**, this is what makes eCPX superior to the original CPX in display efficiency
- A secondary **C-terminal SfiI site** is used if you want dual-terminus display (e.g., with the P2X monitoring peptide)

***

## Step 1: Screen Your Peptide Sequence for Internal SfiI Sites

SfiI recognizes **5′-GGCCNNNNN↓GGCC-3′**. Before designing primers, run your peptide's DNA sequence through a restriction enzyme analysis tool (e.g., Addgene's Sequence Analyzer, SnapGene, or NEB Cutter) to confirm there are **no internal SfiI sites** in your peptide-coding sequence. If an internal site exists, introduce a silent codon mutation to eliminate it while preserving amino acid identity.[^4][^5]

***

## Step 2: Design the Peptide-Encoding Insert with Flanking SfiI Sites

The standard cloning strategy for pB33eCPX uses **two asymmetric SfiI sites** flanking the peptide insert for directional cloning. SfiI cuts **GGCCNNNNN↓GGCC** — since the five central bases can differ between the two sites, the resulting sticky ends are non-palindromic and incompatible with each other, enforcing correct insert orientation.[^3][^6][^7]

**Consensus linker used in original publications:**

- N-terminal side of peptide: `GGQSGQS` (encoded upstream of your peptide sequence)
- C-terminal side of peptide: reverts into the start of the circularly permuted S54 segment

**Designing your insert oligonucleotides:**

For a **defined peptide** (not a library), the cleanest approach is a two-oligo annealing strategy. Design a top-strand oligo and a bottom-strand reverse complement oligo encoding your peptide, flanked by the appropriate SfiI half-sites:[^8][^5]

```
5' TAAGCA-[GGCCATCTG]-{codon for peptide AA1}...{codons for peptide AAn}-[GGCCAACTG]-GCCAT 3'
```

The two bracketed segments are your SfiI.A and SfiI.B half-sites (the five variable nucleotides in each site are chosen to give you the correct reading-frame overhang that matches the cut pB33eCPX vector). If ordering as a single long oligo + short reverse primer (PCR approach):

**Forward primer** (for PCR-amplified insert):

```
5'-[6 bp clamp]-GGCCATCTG-[your peptide codons, ATG optional]-3'
```

**Reverse primer** (anneals to 3′ end of insert, includes second SfiI site):

```
5'-[6 bp clamp]-GGCCAACTG-[reverse complement of last peptide codons, no stop codon]-3'
```

> **Critical reading-frame note:** The SfiI site in the vector encodes GQSGQ (amino acids encoded upstream of S54 of OmpX). Your peptide codons must be in-frame with this context. Use a codon table to align the first codon of your peptide to the reading frame established by the linker.[^3]

***

## Step 3: Generate and Purify the Peptide Insert

**Via annealed oligos (for short peptides ≤ 60 bp):**

1. Resuspend both complementary oligos at 100 µM in annealing buffer (10 mM Tris pH 7.5–8.0, 50 mM NaCl, 1 mM EDTA)
2. Mix equimolar amounts, heat to 95 °C for 5 min, then cool to RT at ~1 °C/min
3. Dilute annealed product 1:10 before using in ligation[^8]

**Via PCR (for longer or codon-optimized peptides):**

1. PCR with your designed forward and reverse primers using a synthetic gene block or your peptide-coding template and a proofreading polymerase (e.g., KOD Hot Start, Q5)
2. Gel-purify the PCR product
3. Proceed to SfiI digest[^3]

***

## Step 4: Double-Digest Insert and Vector with SfiI

SfiI is a **thermophilic enzyme** that cuts optimally at **50 °C** (not 37 °C).[^5]

**Digest reaction (20 µL):**

- 500 ng–1 µg insert (or vector)
- 2 µL CutSmart Buffer (NEB)
- 1 µL SfiI (NEB R0123S, 5 U/µL)
- Nuclease-free water to 20 µL
- Incubate **50 °C, 1–4 h**

Run on 2% agarose gel to confirm digestion. Gel-purify both the digested insert and linearized pB33eCPX vector.

> **Optional:** Treat the digested vector with CIP/SAP phosphatase (37 °C, 30 min) to reduce self-ligation background, then heat-inactivate and column-purify.[^4]

***

## Step 5: Ligation

Use T4 DNA ligase with a **3:1 to 5:1 molar ratio of insert to vector**:[^4]

```
- 50–100 ng digested vector
- Insert: ~3× molar excess
- 2 µL T4 DNA Ligase Buffer (10×)
- 1 µL T4 DNA Ligase (NEB M0202)
- Nuclease-free water to 20 µL
```

Incubate 16 °C overnight (or room temperature 2 h with quick ligase). Heat-inactivate at 65 °C for 10 min. Desalt by drop dialysis on 0.025 µm membrane if electroporating.

***

## Step 6: Transform into *E. coli* K-12 MG1655

MG1655 contains the native **araC** gene on its chromosome, so the araBAD promoter on pBAD33 is functional in this strain without additional supplementation. Key points for successful transformation:[^9][^10]

1. **Electroporation** (preferred for highest efficiency): Transform 40–50 µL electrocompetent MG1655 cells with 1–2 µL of desalted ligation product; pulse at 1.8 kV (1 mm cuvette)[^11]
2. **Heat-shock** (chemical competent cells): ≥5 × 10⁶ cfu/µg using pUC19 as standard; thaw cells on ice, add 2 µL DNA, ice 30 min, 42 °C 60 s, ice 2 min, then recover in SOC 1 h[^11]
3. Plate on LB + **25 µg/mL chloramphenicol** (pB33eCPX selection)
4. Incubate at 37 °C overnight

**Negative control:** plate ligation of vector only (no insert) to assess self-ligation background.[^4]

***

## Step 7: Colony Screening and Sequence Verification

1. Pick 8–12 colonies → mini-prep cultures in LB + Cm 25 µg/mL overnight
2. Diagnostic restriction digest: a KpnI + HindIII double digest on pB33eCPX-derived constructs releases the entire insert-containing region for gel size verification[^12]
3. **Sanger sequence** using the pBAD-fwd primer (`5'-ATGCCATAGCATTTTTATCC-3'`) or the primer listed in the Addgene entry for pB33eCPX[^12]

***

## Step 8: Verify Surface Display by Flow Cytometry

1. Inoculate a single verified colony into 5 mL LB + Cm 25 µg/mL; grow at 37 °C to OD₆₀₀ ≈ 0.4–0.6
2. Induce with **L-arabinose to 0.04% (w/v)** for 30–60 min at 37 °C with shaking (250 rpm)[^13][^3]
3. Label cells with a fluorescent probe directed against your peptide (anti-tag antibody, target protein, streptavidin-PE if using SApep, etc.) on ice for 45 min in PBS
4. Wash ×2 with cold PBS, resuspend, and analyze by flow cytometry[^3]
5. The median fluorescence intensity should be well above the unfused eCPX control

***

## Recommended Vectors

### Vector 1 — **pB33eCPX** (Addgene \#23336) ✅ Top Choice

| Property | Detail |
| :-- | :-- |
| Backbone | pBAD33 |
| Promoter | araBAD (arabinose-inducible, tightly regulated) |
| Resistance | Chloramphenicol (25 µg/mL) |
| Origin | p15A (~10–12 copies/cell) |
| MG1655 compatible | ✅ Yes — araC is encoded in the MG1655 genome |
| Cloning method | SfiI directional RE cloning |
| Addgene status | Available (\$89, agar stab) |

This is the **canonical eCPX display vector** designed by the Daugherty lab. The p15A origin is compatible with ColE1/pMB1 plasmids, so it can be co-transformed with a second plasmid if needed. The araBAD promoter gives tight inducible control with minimal leaky expression when glucose is supplemented to the growth medium.[^12][^14][^15][^3][^16][^17]

***

### Vector 2 — **pQE80L** (Qiagen) for eCPX(-met) variant ✅ Alternative

| Property | Detail |
| :-- | :-- |
| Backbone | pQE80L |
| Promoter | T5 (strong, lacIq-repressed) |
| Resistance | Ampicillin (100 µg/mL) |
| Origin | ColE1 (high copy, ~20–40 copies/cell) |
| MG1655 compatible | ✅ Yes — carries its own lacIq repressor module |
| Cloning method | EcoRI / HindIII (for eCPX insert transfer) |
| Key advantage | Higher display levels; not dependent on glucose suppression |

The SPEED (Stabilized Peptide Evolution by *E. coli* Display) framework demonstrated that the pQE80L/T5 system outperforms pBAD33 for surface display under certain conditions (especially during non-canonical amino acid incorporation) and gives robust eCPX expression in K-12 strains. Since pQE80L carries its own lacIq module, it works in **any** *E. coli* K-12 strain including MG1655 without the need for a chromosomal lacI gene. The eCPX gene is transferred from pB33eCPX into pQE80L using **EcoRI and HindIII** sites. The ampicillin resistance is **compatible** with pB33eCPX's chloramphenicol resistance, so both can co-exist if you need dual plasmids.[^18][^19]

***

## Complete Construct Design Summary

```
[pBAD promoter] → [OmpX SS] → [SfiI site: GGCCATCTG] →
[GQSGQ] → [YOUR PEPTIDE] → [GGQSGQS] → [OmpX S54–F148] →
[GSKSRR linker] → [OmpX A1–S53 / A165L / G166S] → [C-term tag optional]
```

The linker GGQSGQS between the SfiI cloning site and the start of the circularly permuted OmpX body is **not removed** by cloning — it provides flexibility for your peptide to project outward from the outer membrane surface. For larger peptides (>15 aa), consider extending this linker with (GGGS)ₙ repeats to avoid steric clashes with the scaffold.[^3]

***

## Important Practical Notes

- **Suppress leaky expression** during overnight growth by adding **0.2% glucose** to LB media; remove glucose and add arabinose only at induction[^13]
- **Verify absence of internal SfiI sites** in your peptide-coding sequence before synthesis — SfiI recognition is common by chance and a missed internal site will destroy your cloning strategy[^5]
- The **original Daugherty lab strain** is MC1061, not MG1655; both are K-12 derivatives, and pBAD33 with its araC gene functions identically in MG1655 since it encodes araC on the plasmid itself[^15][^3]
- If your peptide contains disulfide bonds (e.g., Cys-constrained peptides), MG1655 can be used directly; no special reducing-environment strain is required for surface display since displayed peptides are extracellular[^3]
<span style="display:none">[^100][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^70][^71][^72][^73][^74][^75][^76][^77][^78][^79][^80][^81][^82][^83][^84][^85][^86][^87][^88][^89][^90][^91][^92][^93][^94][^95][^96][^97][^98][^99]</span>

<div align="center">⁂</div>

[^1]: https://pubmed.ncbi.nlm.nih.gov/18480093/?dopt=Abstract

[^2]: https://pubmed.ncbi.nlm.nih.gov/18480093/

[^3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2427320/

[^4]: https://www.addgene.org/protocols/pcr-cloning/

[^5]: http://rrresearch.fieldofscience.com/2007/08/troubleshooting-cloning-experiment.html

[^6]: https://pubmed.ncbi.nlm.nih.gov/2165017/

[^7]: https://pubmed.ncbi.nlm.nih.gov/2531695/

[^8]: https://www.addgene.org/protocols/annealed-oligo-cloning/

[^9]: https://www.sciencedirect.com/science/article/abs/pii/S0378111900002109

[^10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10399174/

[^11]: https://www.lifetechindia.com/pdf/MG1655-Chemically-Competent-Cells-Manual.pdf

[^12]: https://www.addgene.org/23336/

[^13]: https://www.intechopen.com/chapters/18186

[^14]: https://www.novoprolabs.com/vector/Vge3tmnbr

[^15]: https://rega.kuleuven.be/bac/economou/files/pdf/publications/j-bacteriol-1995-guzman-4121-30.pdf

[^16]: https://www.novopro.cn/vector/Vgezdoobs

[^17]: https://assets.thermofisher.com/TFS-Assets/LSG/brochures/710_01619_pBAD_bro.pdf

[^18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7304070/

[^19]: https://www.addgene.org/vector-database/3883/

[^20]: https://journals.plos.org/plosone/article/figures?id=10.1371%2Fjournal.pone.0080474

[^21]: https://mdpi-res.com/d_attachment/energies/energies-14-05389/article_deploy/energies-14-05389.pdf?version=1630323893

[^22]: https://www.addgene.org/61440/

[^23]: https://mednexus.org/doi/10.1097/JBR.0000000000000052

[^24]: https://www.sciencedirect.com/science/article/abs/pii/B9780123969620000045

[^25]: https://www.embl.org/groups/protein-expression-purification/services/strategy-and-construct-design/e-coli-expression-vectors/

[^26]: https://pubmed.ncbi.nlm.nih.gov/30971255/

[^27]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4274986/

[^28]: https://www.addgene.org/121907/

[^29]: https://journals.asm.org/doi/10.1128/cdli.6.4.499-503.1999

[^30]: https://pubmed.ncbi.nlm.nih.gov/16600968/

[^31]: https://www.genome.wisc.edu/resources/strains.htm

[^32]: https://www.thermofisher.com/us/en/home/life-science/protein-biology/protein-expression/membrane-protein-expression.html

[^33]: https://ecocyc.org/pathway?orgid=ECOLI\&id=LPSSYN-PWY

[^34]: https://www.addgene.org/22145/

[^35]: https://d-nb.info/1208010751/34

[^36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2791049/

[^37]: https://aiche.confex.com/aiche/2006/techprogram/P68749.HTM

[^38]: https://bio-protocol.org/exchange/minidetail?id=8455905\&type=30

[^39]: https://www.creative-biolabs.com/protease-substrate-identification-by-bacterial-display.html

[^40]: https://www.addgene.org/65098/

[^41]: https://is.muni.cz/el/sci/jaro2017/C8980/um/68028093/2017_Lecture7.pdf

[^42]: https://bio-protocol.org/exchange/minidetail?id=3947871\&type=30

[^43]: https://oaktrust.library.tamu.edu/items/1404c0e1-9575-4adf-ae50-054d4bfe742b

[^44]: https://journals.plos.org/plosone/article/figures?id=10.1371%2Fjournal.pone.0068674

[^45]: http://mbio.bas-net.by/cager/en/vectors?action=display\&vector_no=121.D.A1-2\&printv=1

[^46]: https://ecoliwiki.org/colipedia/index.php/pBAD33

[^47]: https://pubmed.ncbi.nlm.nih.gov/2551781/

[^48]: https://catalog.takara-bio.co.jp/PDFS/PT5018-1(012512).pdf

[^49]: https://www.sigmaaldrich.com/JP/ja/product/sigma/pp2379

[^50]: https://www.geneuniversal.com/company/newsDetail?id=88

[^51]: https://www.sigmaaldrich.com/PL/en/product/sigma/ogs106

[^52]: https://www.rsc.org/suppdata/c7/mb/c7mb00495h/c7mb00495h1.pdf

[^53]: https://www.novoprolabs.com/vector/Vgezdoobs

[^54]: https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2015.00191/full

[^55]: https://www.promega.com/-/media/files/resources/promega-notes/100/expression-of-fusion-proteins-how-to-get-started-with-the-halotag-technology.pdf?rev=8694aa6307214e80a014fefb8d7b0104\&sc_lang=en

[^56]: https://bio-protocol.org/exchange/minidetail?id=7332516\&type=30

[^57]: https://academic.oup.com/peds/article/21/7/435/1538582

[^58]: https://sites.chemengr.ucsb.edu/~ceweb/faculty/daugherty/images/17-rice.pdf

[^59]: https://bio-protocol.org/exchange/minidetail?id=11099943\&type=30

[^60]: https://pubmed.ncbi.nlm.nih.gov/15390265/?dopt=Citation

[^61]: https://techtransfer.universityofcalifornia.edu/NCD/Media/2003-460_Bacterial_Display_Science_Direct_2007.pdf

[^62]: https://www.neb.com/en-us/protocols/construction-of-the-fusion-plasmid-e6901

[^63]: https://bio-protocol.org/exchange/minidetail?id=8615624\&type=30

[^64]: https://bio-protocol.org/exchange/minidetail?id=334506\&type=30

[^65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4600428/

[^66]: https://www.novoprolabs.com/vector/V11005

[^67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12282077/

[^68]: https://synapse.patsnap.com/article/plasmid-vector-comparison-puc19-vs-pet-28a-for-protein-expression

[^69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7568196/

[^70]: https://2022.igem.wiki/korea-hs/parts

[^71]: https://www.snapgene.com/plasmids/qiagen_vectors/pQE-80L

[^72]: https://www.diva-portal.org/smash/get/diva2:1118023/FULLTEXT01.pdf

[^73]: https://infoscience.epfl.ch/server/api/core/bitstreams/b63884e0-e162-47b0-907e-ce71e05ae619/content

[^74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7567684/

[^75]: http://www.ulab360.com/files/prod/references/201301/07/427553001.pdf

[^76]: https://www.qiagen.com/en-us/resources/download/protocols/cis-repressed-pqe-vector-maps-en

[^77]: https://portals.broadinstitute.org/gpp/public/dir/download?dirpath=protocols%2Fproduction\&filename=cloning_of_oligos_for_sgRNA_shRNA_nov2019.pdf

[^78]: https://journals.plos.org/plosgenetics/article/figures?id=10.1371%2Fjournal.pgen.1010672

[^79]: https://journals.asm.org/doi/10.1128/jb.01007-13

[^80]: https://eureka.patsnap.com/patent-CN108676808A

[^81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC177046/

[^82]: https://www.studocu.com/en-ca/document/concordia-university/molecular-biology/biol367-final-exam-practice-students-copy/123562145

[^83]: https://wikis.mit.edu/confluence/download/export/pdfexport-20250402-020425-0915-194203/phage+display-+cloning+peptide+l_a452d16bf6b442edb775c4c57a7c991f-020425-0915-194204.pdf?contentType=application%2Fpdf

[^84]: https://www.origene.com/support/learning-resources/protocols/primer-design-and-pcr-amplification-of-orfs-protocol

[^85]: https://www.addgene.org/browse/article/3122/

[^86]: https://freegenes.github.io/genes/BBF10K_003302.html

[^87]: https://www.liverpool.ac.uk/~clague/local_html/molecular%20biology/primers.html

[^88]: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0111538

[^89]: https://www.neb.com/en/protocols/0001/01/01/primer-design-e6901?pdf=true

[^90]: http://www.protocol-online.org/biology-forums-2/posts/39300.html

[^91]: https://www.promega.ca/-/media/files/resources/cell-notes/cn011/clone-and-express-protein-coding-regions-using-the-flexi-vector-systems.pdf?la=en

[^92]: https://www.addgene.org/protocols/primer-design/

[^93]: https://www.sigmaaldrich.com/IN/en/technical-documents/technical-article/genomics/cloning-and-expression/restriction-site-positions-and-functions

[^94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5658595/

[^95]: https://www.neb.com/en-gb/-/media/nebus/files/manuals/manuale8101.pdf?rev=2b5c03b454244e469be51c339c3761cc\&la=en-gb\&hash=849CB2A78DEE9B130475E97A2605E194

[^96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2242469/

[^97]: https://www.rsc.org/suppdata/cc/c2/c2cc30531c/c2cc30531c.pdf

[^98]: https://www.creativebiomart.net/escherichia-coli-display-platform.htm

[^99]: https://journals.plos.org/plosone/article/file?type=printable\&id=10.1371%2Fjournal.pone.0325589

[^100]: https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000005845.2/

