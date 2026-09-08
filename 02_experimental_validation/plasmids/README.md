# LiSPER pET-28a(+) surface-display designs

Prepared 8 September 2026. **Six plasmids: four candidate fusions, one His-tagged eCPX-only control, and unmodified pET-28a(+).** These are sequence-defined experimental designs. Surface display and lithium selectivity have not been established for these constructs.

## What to give GenScript

- `LiSPER_GenScript_plasmid_designs.xlsx`: construct table, full synthesis sequences, exact insertion boundaries, and validation notes.
- `sequences/synthesis_fragments.fasta`: five complete synthesis fragments, each with 30 bp of backbone overlap at each end.
- `genbank/`: six annotated full-plasmid reference sequences readable in SnapGene.
- `sequences/coding_sequences.fasta`: the five coding sequences alone, including their terminal stop codon.

Ask GenScript Nanjing to supply its own pET-28a(+) backbone, synthesize the five fragments, assemble the specified final plasmids, sequence-verify the complete insert and both junctions, and supply the sixth plasmid as unmodified empty vector. The eCPX scaffold CDS is supplied as a standalone digital sequence in `sources/eCPX_scaffold_precursor.fasta`.

The public GenScript library record lists pET-28a(+) at 5,369 bp. Its DNA is identical to the existing local SnapGene backbone after reversing the strand and rotating the circular origin. All coordinates here use the **GenScript reference**, beginning `AGATCTCGATCCCGCG...`. The vendor should match its production backbone to this reference and return the final sequence with its quote. Public listing does not confirm current Nanjing stock, turnaround, or acceptance of a particular assembly method. [GenScript vector library](https://www.genscript.com/vector/library_list), [sequence-bearing library record](https://www.genscript.com/tools/vector-design/queryLibraryList).

## Exact insertion boundary

Use **seamless replacement of reference nucleotides 108–243 inclusive**, starting at the native initiation `ATG` and ending immediately before `XhoI`. Insert the full synthetic CDS, which starts with the OmpX signal and ends with `TAA`. This replaces 136 bp of the original start/tag/MCS segment. The T7 promoter, lac operator, RBS, downstream terminator and maintenance genes remain.

```text
retained backbone nt 1–107 | ATG ... complete fusion ... TAA | retained backbone nt 244–5369

left overlap, nt 78–107:  TTTTGTTTAACTTTAAGAAGGAGATATACC
right overlap, nt 244–273: CTCGAGCACCACCACCACCACCACTGAGAT
```

Each synthesis FASTA entry is `left overlap + CDS with stop + right overlap`, written 5′→3′ on the coding strand. **The overlaps occur once in the assembled plasmid.** They are not extra translated sequence. Full GenBank files specify the exact final products, independent of the vendor's choice of assembly chemistry.

| Site | Recognition sequence | Reference coordinates | Design consequence |
|---|---|---|---|
| NcoI | CCATGG | 106–111 | Overlaps the native start. Seamless replacement destroys this site. |
| NdeI | CATATG | 165–170 | Lies downstream of the original N-His/thrombin region. Removed. |
| XhoI | CTCGAG | 244–249 | Retained immediately after the synthetic stop. |

**Do not substitute routine NdeI/XhoI cloning:** it retains upstream vector-encoded residues before the export signal. Do not preserve NcoI by changing the second signal residue: `CCATGG` constrains the base after `ATG`, whereas the native signal begins Met-Lys. Seamless assembly preserves the native signal without adding an amino acid. The residual vector C-His DNA after XhoI is untranslated because of the insert stop; it is not a second fusion tag. These conclusions follow from translation of the actual backbone, not from the vector name alone. [GenScript map](https://www.genscript.com/gsfiles/vector-map/bacteria/pET-28a.pdf).

All five inserts run in the **same direction as T7 transcription**. N versus C refers to the peptide's position in the protein, not to reversing its amino-acid sequence or cloning the DNA in the opposite direction.

## Protein arrangement and sequence provenance

`P` is LiDA-1 (`DADGPGDPDAG`, 11 aa) or LiND-Hybrid (`GPGNPGSGPGDPGSGPGNP`, 19 aa). Candidate sequences were copied from the active repository FASTA.

```text
N-display: SP–GQSGQ–P–GGQSGQ–eCPX(core)–GGQSGQ–His6–GSG–STOP
C-display: SP–GQSGQ–GGQSGQ–eCPX(core)–GGQSGQ–His6–GSG–P–STOP
Control:   SP–GQSGQ–GGQSGQ–eCPX(core)–GGQSGQ–His6–GSG–STOP
```

Here `SP = MKKIACLSALAAVLAFTAGTSVA` (23 aa). It is at the absolute precursor N terminus. Expected processing removes SP and leaves the mature chain beginning `GQSGQ`. Sec-dependent export and subsequent outer-membrane assembly are required; the signal does not by itself prove successful surface localization.

The 154-aa core is the circularly permuted OmpX scaffold, not an unmodified ompX gene. It contains mature OmpX S54–F148, the internal joining linker `GSKSRR`, and mature OmpX A1–S53. The A165L/G166S substitutions use **native precursor numbering**, including its 23-aa signal, and must not be applied at positions 165/166 of the permuted core. The local reference matches this reconstruction exactly. The original eCPX study demonstrated both exposed termini in MC1061; it did not validate the current pET/BL21(DE3) designs. [Rice & Daugherty, 2008](https://doi.org/10.1093/protein/gzn020).

The standalone `sources/eCPX_scaffold_precursor.fasta` contains a 567-nt CDS encoding the 188-aa precursor and terminal stop. Its signal, leader, N linker and core nucleotide sequences were retained from the previous digital scaffold reference; the obsolete whole vector has been removed. Core identity was independently checked against [UniProt OmpX P0A917](https://www.uniprot.org/uniprotkb/P0A917/entry) after the stated permutation and two substitutions.

Published display work also uses the SP–GQSGQ–passenger–GGQSGQ–eCPX architecture and a C-terminal GGQSGQ-linked detection tag. Our **His6/GSG cassette and these candidate fusions are design choices**, not a previously validated LiSPER construct. [Li et al., 2023, Methods](https://elifesciences.org/articles/82345v2).

The five inserts retain the same core, linkers and single His6 cassette. The scaffold control is exactly the shared fusion with both candidate slots empty. His6 stays on the core's C-terminal extension; in the C-display constructs it precedes the peptide and is therefore internal to the full protein. Select an anti-His reagent documented to recognize internal His tags. This arrangement avoids moving the tag between the N and C series while keeping the requested single scaffold control.

Native scaffold codons were retained. Newly added segments use explicit synonymous codons, with alternating His codons. **No quantitative codon-optimization score or expression improvement is claimed.** If GenScript recodes for synthesis, require identical protein translations, unchanged assembly boundaries, and revised final sequence files. Do not treat a recoded DNA sequence as identical to the supplied reference.

## Are both peptide orientations worthwhile?

**Yes, as a four-construct comparison.** This tests whether fusion context changes display and ion-removal performance, without assuming one orientation is best. It is not required for eCPX to function, and equal total expression will not imply equal surface presentation.

There is an important terminus qualification: in the N-series, the peptide is followed by its scaffold linker but preceded by `GQSGQ`, so it does **not** have its exact native free N terminus. In the C-series, the peptide is the last translated segment and has a free C-terminal carboxyl group. Thus this panel tests N-side versus C-side display; it is not a rigorously isolated comparison of free native N and C termini. Retaining the established post-signal leader avoids silently assuming that changing the signal-cleavage context is harmless.

Fusion linkers, the His cassette and free terminal groups may affect a short ion-binding peptide's behavior. Tag proximity also differs between placements even though the shared cassette is fixed. These are reasons to measure both and interpret differences as **construct-context effects**, rather than attributing them solely to orientation. Computational results on isolated peptides cannot establish the behavior of these fusions. If an exact free N terminus is a future mechanistic requirement, that needs a separate processing design and confirmation of cleavage.

His6 may alter surface chemistry or metal interactions. The His-tagged scaffold control estimates the shared background but cannot remove nonadditive tag–peptide effects. A later tag-free confirmation is appropriate if a candidate appears promising; it is outside this six-plasmid set.

## Host and expression interpretation

Use **BL21(DE3)**, or another documented T7-RNA-polymerase host, for these pET constructs. Ordinary BL21 lacks the T7 polymerase gene. GenScript may ship DNA propagated in a cloning host; that does not establish that the shipping strain is suitable for expression. [NEB strain comparison](https://www.neb.com/en-us/faqs/what-is-the-difference-between-bl21-and-bl21-de3-competent-e-coli-cells).

The original paper does not validate these exact pET/BL21(DE3) fusions. Treat expression strength as a pilot variable and choose conditions by intact-cell surface signal plus cell integrity, not by the darkest lysate band. Excess total synthesis can exceed export/assembly capacity. No induction concentration, temperature, or duration is designated as a proven condition for this panel.

## His Western blot, SDS–PAGE and surface proteolysis

SDS–PAGE and anti-His Western blot detect the **whole fusion**, not a separately produced 11- or 19-aa peptide. Predicted masses are listed below and in the workbook. Mature masses assume removal of the 23-aa signal. Gel mobility can differ from calculated mass; N/C pairs have the same composition and mass, so a gel cannot identify their orientation. Sequencing does.

| Fusion | Precursor mass | Predicted mature mass |
|---|---:|---:|
| LiDA-1 N or C | 22.825 kDa | 20.605 kDa |
| LiND-Hybrid N or C | 23.413 kDa | 21.194 kDa |
| His-eCPX-only | 21.857 kDa | 19.637 kDa |

Use anti-His lysate blots to establish expression, with comparable cell input and an independent loading readout. Intact, non-permeabilized anti-His labeling provides an orthogonal test of tag accessibility. The **His-eCPX-only control is expected to be anti-His positive** if it displays; it is peptide-negative, not tag-negative. Empty-vector cells, non-induced samples and antibody-background controls address different backgrounds. Empty pET retains its native short tag-coding region, so do not assume zero anti-His signal at every molecular weight.

Your protease idea is sound, but “slight proteinase” is not sufficient evidence of an intact barrier. Consider proteinase K for an initial accessibility assessment and establish a condition that preserves the cell envelope. Neither candidate contains Lys or Arg, so trypsin is not a reliable direct-cleavage test of these peptides. Proteinase K has broader specificity, but accessibility and digestion must still be demonstrated. [NEB protease specificities](https://www.neb.com/en/products/protein-tools/proteases).

Use these comparisons for each expressed fusion:

| Sample | Required interpretation |
|---|---|
| Intact cells, no protease | Baseline fusion, surface-labeling signal and integrity markers. |
| Intact cells, protease | Accessible external signal should decline while validated intracellular/periplasmic markers remain protected. |
| Disrupted cells, no protease | Controls for effects of disruption on detection. |
| Disrupted cells, protease | Shows the enzyme can digest the fusion and the chosen protected markers when access is allowed. |

Include a periplasmic marker as well as a cytoplasmic marker: outer-membrane leakage can expose periplasmic proteins while the cytoplasm remains protected. Choose markers and antibodies available in the lab, and first show that each marker is susceptible in the disrupted-cell control. Do not assume resistance means protection; protease-resistant reporters can mislead. Cell viability/dye exclusion and supernatant leakage are supporting readouts, not substitutes for checking the outer-membrane barrier. [Besingi & Clark, extracellular protease-digestion method](https://pmc.ncbi.nlm.nih.gov/articles/PMC4838181/).

Stop or remove the protease **before lysis for Western analysis** and verify the stopping step; otherwise intracellular digestion during sample preparation invalidates the localization inference. Label with antibody after protease treatment and quenching so antibody digestion or antibody shielding does not masquerade as loss of surface display. Use matched handling controls.

Loss of anti-His signal establishes accessibility of the **tag-bearing region** under the integrity controls. It does not by itself prove that LiDA-1 or LiND-Hybrid was intact and exposed, particularly when the candidate is on the opposite terminus. Candidate-specific intact-cell detection or identification of released candidate-containing fragments would strengthen that claim. If those readouts are unavailable, report “fusion/tag surface accessibility consistent with the design,” rather than claiming direct proof of peptide exposure. Small cleavage fragments and ~1–2 kDa differences may be poorly resolved on a routine gel.

For subsequent ion assays compare all candidates with the His-eCPX scaffold control and empty-vector cells under matched culture/induction handling. Keep no-cell analytical blanks. Untransformed host may remain an additional culture control but is not a substitute for empty-vector cells. Normalize biomass and assess surface abundance separately; whole-cell ion removal does not alone prove peptide-specific lithium coordination.

## Corrections to the two supplied reports

Both reports were read in full. They are background references; this package defines the current constructs.

- `eCPX_bacterial_surface_peptide_display.md` correctly describes the general biterminal concept, but its T7/IPTG/BL21 statements are not established by the cited 2008 study, which used MC1061 with a different expression system.
- `Elicit - eCPX–DADGPGDPDAG BL21 surface-display plasmid design.md` omits the signal in its headline His6–eCPX architecture and suggests NdeI without accounting for retained upstream pET tags. Its short-linker descriptions also vary between `(Gly-Ser)2` and `(G4S)2`. The exact sequences here resolve those ambiguities.
- A His-tagged scaffold-only construct is not a negative control for anti-His accessibility. Expression, exposed tag, intact candidate peptide, and lithium-binding activity are distinct claims.

## Reproducibility and status

`sequence_QC.md` records the checks and exact lengths. `build_sequences.py` recreates sequence outputs from the frozen `sources/` files and checks source identity, scaffold permutation/mutations, translation, junctions and backbone preservation. `constructs.tsv` and `constructs.json` carry the same sequence data as the Excel workbook. Full-plasmid SHA-256 hashes identify the exact designs.

The LiDA-1 N GenBank design was opened successfully in SnapGene at 5,878 bp. A native SnapGene export of the scaffold-only control matched the GenBank sequence and feature count; that redundant QC copy was removed during cleanup. Batch export of the complete native-format set did not complete, so the six delivered plasmids are provided consistently in annotated GenBank format. The saved Excel DNA, protein and hash fields were independently compared with the sequence records and matched exactly.

This package is suitable for a concrete vendor design review and quotation. Final vendor acceptance, production sequence confirmation, and experimental surface-display verification remain outstanding. No order or external message has been sent.
