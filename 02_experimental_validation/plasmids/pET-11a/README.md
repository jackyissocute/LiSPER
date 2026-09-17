# pET-11a surface-display plasmids

Eight native SnapGene files, updated 2026-09-17. All retain the GenScript forward strand and bp-1 origin (`AGATCT…`), use uppercase DNA, and have annotated backbone, expression and display features. The display CDS starts at bp 109 in every engineered construct. Reverse-strand backbone genes retain their biological orientation. The full display CDS is purple; the eCPX core remains green.

| File | Plasmid length | Display |
| --- | ---: | --- |
| pET11a_LiDA-1_N.dna | 6,268 bp | N-side DADGPGDPDAG; C-side His6 |
| pET11a_LiDA-1_C.dna | 6,268 bp | C-side DADGPGDPDAG; N-side His6 |
| pET11a_LiND-Hybrid_N.dna | 6,292 bp | N-side GPGNPGSGPGDPGSGPGNP; C-side His6 |
| pET11a_LiND-Hybrid_C.dna | 6,292 bp | C-side GPGNPGSGPGDPGSGPGNP; N-side His6 |
| pET11a_Empty_eCPX.dna | 6,217 bp | Tag-free scaffold control, byte-unchanged |
| pET11a_Empty_eCPX_N-His6.dna | 6,235 bp | Scaffold-only N-side His6 control |
| pET11a_Empty_eCPX_C-His6.dna | 6,235 bp | Scaffold-only C-side His6 control |
| pET-11a.dna | 5,677 bp | Original GenScript backbone, unchanged sequence |

## Restriction-cloning boundaries

Use **NdeI / BamHI**, each unique in the reference and every final plasmid. Original reference sites are bp 106–111 and 145–150, respectively (1-based, inclusive). The original bp 109–144 coding segment, including its start codon and T7-tag cassette, is replaced by the full display CDS. Both boundary restriction sites are rebuilt unchanged; the CDS begins with the ATG inside NdeI and ends with TAA before BamHI. No vector-derived tag is translated into eCPX.

The synthesis workbook has one tab and four columns. Its insert strings are complete site-flanked cassettes (`CAT` + full CDS + `GGATCC`), replacing original bp 106–150; the rest of the backbone is unchanged. Distinct restriction ends set the forward orientation. A top-strand restriction-ligation simulation reproduces each final sequence exactly.

## Display rationale and limits

Layouts, shown as translated precursor proteins:

- N display: OmpX signal – GQSGQ – peptide – GGQSGQ – eCPX core – GGS – His6 – stop.
- C display: OmpX signal – GQSGQ – His6 – GGQSGQ – eCPX core – GGS – peptide – stop.
- N-His6 control: OmpX signal – GQSGQ – His6 – GGQSGQ – eCPX core – GGS – stop.
- C-His6 control: OmpX signal – GQSGQ – GGQSGQ – eCPX core – GGS – His6 – stop.
- Tag-free control: OmpX signal – GQSGQ – GGQSGQ – eCPX core – GGS – stop.

The native 23-aa OmpX secretion signal remains first. The 154-aa circularly permuted core is mature OmpX S54–F148, then GSKSRR, then A1–S53, with the eCPX A165L/G166S stabilizing substitutions (original precursor numbering). The N-display leader/linker follows Getz; the C-side GGS linker follows Kenrick. Each tagged construct adds only `CATCACCATCACCATCAC` (18 nt, HHHHHH), with no extra linker residues or stop codon. Candidate sequences, existing leaders/linkers, core and retained backbone are unchanged. N-side display is **not a free peptide N-terminus** because GQSGQ precedes it; the C-displayed candidate has no translated residues after it.

His6 is on the opposite display side from each candidate peptide. Anti-His Western blot can support fusion-expression detection; intact-cell anti-His accessibility does not directly prove exposure or function of the peptide on the opposite side. Tag effects on folding, display and ion binding need experimental checks. The three scaffold controls separate scaffold and tag-associated backgrounds; they do not establish successful display by themselves.

These are sequence-checked designs, **not experimentally validated surface-display or lithium-binding constructs**. Kenrick and Getz use pBAD33/MC1061, not pET-11a/BL21. Van Bloois reviews bacterial display and does not validate this particular combination. Moving eCPX into a T7 backbone is an extrapolation; secretion, accessible surface display, cell fitness and lithium-binding specificity remain to be demonstrated. Use BL21(DE3) or another T7-RNA-polymerase host, not ordinary BL21 without a T7-polymerase source. See the [Novagen host documentation](https://b2b.sigmaaldrich.com/US/en/product/mm/69450m).

## Sources and verification

- [Kenrick & Daugherty, 2009/2010](../../../06_project_operations/inbox/kenrick2009.pdf): *Bacterial display enables efficient and quantitative peptide affinity maturation*, doi:10.1093/protein/gzp065; Methods p. 11, eCPX terminal display and C-side GGS.
- [Getz et al., 2012](../../../06_project_operations/inbox/getz2012.pdf): *Bacterial Display of Peptide Libraries for Screening against Biological Targets*, doi:10.1016/B978-0-12-396962-0.00004-5; §2.1.2 / Fig. 4.3, N-side display architecture.
- [Van Bloois et al., 2011](../../../06_project_operations/inbox/vanbloois2011.pdf): *Decorating microbes: surface display of proteins on Escherichia coli*, doi:10.1016/j.tibtech.2010.11.003; secretion/display limitations.
- [GenScript vector bank](https://www.genscript.com/vector/library_list): pET-11a, ID 47, 5,677 bp, retrieved 2026-09-16. Its raw sequence and [official map](https://www.genscript.com/gsfiles/vector-map/bacteria/pET-11a.pdf) are retained in `sources/`. GenScript supplies the reference sequence/map; it was converted to native `.dna` in SnapGene without changing its nucleotide sequence.
- Backbone annotations from [SnapGene resources](https://www.snapgene.com/plasmids/pet_and_duet_vectors_%28novagen%29/pET-11a), transferred only after exact circular-sequence identity verification against GenScript. Promoter/operator/RBS/terminator feature directions follow forward T7 transcription.
- Canonical core cross-check: [Rice et al., 2008](https://academic.oup.com/peds/article/21/7/435/1538582), doi:10.1093/protein/gzn020, and the inventors' [published sequence descriptions](https://patents.google.com/patent/US20090062142A1/en). Candidate identities and the OmpX reference protein are retained in `sources/`.

Run `python check_designs.py` with Biopython installed. It verifies all eight native files, peptide/His6 translations, preserved vector features, unique restriction sites, exact ligation products, and seven literal Excel insert sequences matched by construct name. Sequence insertion and native saving were performed in SnapGene; checked GenBank intermediates were subsequently imported there to normalize annotations without further sequence changes. Temporary GenBank files are not retained in this package.
