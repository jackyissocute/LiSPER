# Plasmids

This folder is the secondary/fallback plasmid-design workspace for the **final 8-candidate** LiSPER purified-peptide library.

Current wet-lab priority has shifted to ordering synthetic LiSPER peptides directly for first-pass Li+/Na+ binding assays. These plasmid designs are retained for optional in-house His6-SUMO peptide production if later needed.

## Current State

The current vendor-ready fallback package is:

```text
vendor_ready_restriction_SUMO/
```

It contains eight corrected pET-28a(+)-His6-SUMO-LiSPER construct maps, synthesis insert FASTA files, and a vendor order instruction document.

The LiSPER peptide-coding regions now use the IDT E. coli codon-optimized DNA downloaded for the final 8 candidates.

## Vendor-Compatible Design Rule

Use this section only if the project chooses to pursue in-house expression and purification instead of, or in addition to, ordered synthetic peptides.

The vendor should **not synthesize a redesigned full pET-28a plasmid**.

Use the original pET-28a(+) backbone and synthesize only the expression insert:

```text
NdeI -> His6 -> Smt3 SUMO -> LiSPER peptide -> stop codon -> XhoI
```

The generated final plasmid GenBank maps preserve the original pET-28a(+) backbone and replace only the NdeI/XhoI cloning interval.

## Final 8 Constructs

| Candidate | Plasmid status |
|---|---|
| `LiD3-Core` | Vendor-ready GenBank + insert sequence generated |
| `LiD3-Flex` | Vendor-ready GenBank + insert sequence generated |
| `LiND-Hybrid` | Vendor-ready GenBank + insert sequence generated |
| `LiLC-1` | Vendor-ready GenBank + insert sequence generated |
| `LiDS-1` | Vendor-ready GenBank + insert sequence generated |
| `LiDA-1` | Vendor-ready GenBank + insert sequence generated |
| `LiN3-Core` | Vendor-ready GenBank + insert sequence generated |
| `LiA3-Ref` | Vendor-ready GenBank + insert sequence generated |

## Vendor Package

| Path | Purpose |
|---|---|
| `vendor_ready_restriction_SUMO/VENDOR_ORDER_INSTRUCTIONS.md` | Concise ordering instructions for the cloning vendor |
| `vendor_ready_restriction_SUMO/vendor_order_table.csv` | Insert names, insert sequences, lengths, and QC fields |
| `vendor_ready_restriction_SUMO/genbank_final_constructs/` | Eight final circular plasmid maps in GenBank format |
| `vendor_ready_restriction_SUMO/insert_sequences/` | FASTA files for synthesis inserts, fusion products, and released peptides |
| `codon_optimization/idt_peptide_codon_optimization.csv` | Final IDT peptide codon-optimization manifest used by the plasmid generator |
| `codon_optimization/idt_downloads/` | Original IDT CSV downloads renamed by candidate |

## Vector Map

| Path | Purpose |
|---|---|
| `vector_maps/pET28a_plus.dna` | Source pET-28a(+) SnapGene vector map used as the backbone reference |

## QC Summary

- All eight inserts start with NdeI and end with XhoI.
- The NdeI site supplies the start codon; the insert does not duplicate an extra ATG after NdeI.
- No internal NdeI or XhoI sites were detected inside the coding ORFs.
- All IDT peptide-coding sequences translate back to the expected LiSPER peptide sequences.
- Each GenBank file is circular and contains annotated cloning sites, vendor insert, His6 tag, Smt3 SUMO tag, candidate peptide, and stop codon.
- SUMO protease cleavage is designed to release the native LiSPER peptide without extra residues.

## Reproducibility

The generator used for this package is:

```text
06_project_operations/scripts/design_pet28a_SUMO_restriction_vendor_package.py
```

Earlier full-cassette replacement scripts are superseded for vendor ordering because the synthesis vendor workflow requires insert cloning into a standard backbone rather than redesigning the surrounding MCS.
