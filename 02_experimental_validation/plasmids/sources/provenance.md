# Frozen sequence sources

Retrieved or copied 2026-09-08.

| File | Origin | Use |
|---|---|---|
| GenScript_pET28a.fasta | https://www.genscript.com/tools/vector-design/queryLibraryList ; entry pET-28a(+), 5369 bp | Exact public vendor reference, retrieved through web access. |
| pET28a_annotated_reference.gb | Same vendor DNA; annotations transferred from `/Users/jackylin/Desktop/SW tmp/Plasmid Building/pET-28a(+).dna` | Local sequence is an exact circular reverse-complement match. Reverse-complement local sequence equals vendor sequence rotated to 0-based offset 406. Noncoding T7 RBS/operator/terminator annotation direction normalized to the expression direction. |
| eCPX_scaffold_precursor.fasta | Isolated CDS from the previous local digital scaffold reference | 567 nt including stop; 188-aa precursor containing signal, leader, N linker and eCPX core. The obsolete whole-vector source has been removed. Protein identity was independently checked against native OmpX and the published permutation/mutations. |
| OmpX_P0A917.fasta | https://rest.uniprot.org/uniprotkb/P0A917.fasta | Native OmpX sequence used for independent protein-level verification of permutation and mutations. |
| candidates.fasta | `01_computational_discovery/sequences/candidates.fasta` | Frozen active peptide library. Only LiDA-1 and LiND-Hybrid used. |

Scaffold architecture was checked against Rice & Daugherty (2008), DOI 10.1093/protein/gzn020, full-text XML from https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2427320/fullTextXML . Additional architecture reference: Li et al. (2023), https://elifesciences.org/articles/82345v2 . See the main README for interpretation and other sources.
