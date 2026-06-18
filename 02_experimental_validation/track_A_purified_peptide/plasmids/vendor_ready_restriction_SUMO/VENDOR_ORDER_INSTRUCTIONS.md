# Vendor Order Instructions: pET-28a(+)-His6-SUMO-LiSPER Inserts

## Critical Clarification

Please **do not synthesize a redesigned full pET-28a plasmid**. Please use a standard/original pET-28a(+) backbone and synthesize only the listed inserts. Each insert should be restriction-cloned into the original pET-28a(+) MCS using **NdeI and XhoI**.

## Cloning Strategy

- Backbone: original pET-28a(+), kanamycin resistance.
- Expression host after delivery: E. coli BL21(DE3).
- 5' cloning site: NdeI (`CATATG`). The ATG start codon is inside the NdeI site.
- 3' cloning site: XhoI (`CTCGAG`) downstream of a TAA stop codon.
- Insert architecture: `NdeI -> His6 -> Smt3 SUMO -> LiSPER peptide -> TAA stop -> XhoI`.
- LiSPER peptide-coding segments use the IDT E. coli codon-optimized sequences in `codon_optimization/idt_peptide_codon_optimization.csv`.
- Important: do not duplicate the ATG after NdeI. Use the exact insert sequences in the order table.
- Please sequence-verify the complete insert and both vector-insert junctions.

## Why This Fixes the Previous Problem

The previous style of design changed too much of the pET-28a MCS/expression region and did not match a normal insert-into-backbone vendor workflow. This package instead keeps the vector as pET-28a(+) and defines only a restriction-cloned insert between the existing NdeI and XhoI sites.

## Construct Summary

| Candidate | Plasmid | Peptide | Insert length (bp) | QC |
|---|---|---|---:|---|
| LiD3-Core | pET28a-SUMO-LiD3-Core | `GPGDPGPGDPGPGDP` | 372 | PASS: no internal NdeI/XhoI in ORF; PASS |
| LiD3-Flex | pET28a-SUMO-LiD3-Flex | `GPGDPGSGPGDPGSGPGDP` | 384 | PASS: no internal NdeI/XhoI in ORF; PASS |
| LiND-Hybrid | pET28a-SUMO-LiND-Hybrid | `GPGNPGSGPGDPGSGPGNP` | 384 | PASS: no internal NdeI/XhoI in ORF; PASS |
| LiLC-1 | pET28a-SUMO-LiLC-1 | `GPGDPGSGNPGSGDP` | 372 | PASS: no internal NdeI/XhoI in ORF; PASS |
| LiDS-1 | pET28a-SUMO-LiDS-1 | `DGDGPGDPGDG` | 360 | PASS: no internal NdeI/XhoI in ORF; PASS |
| LiDA-1 | pET28a-SUMO-LiDA-1 | `DADGPGDPDAG` | 360 | PASS: no internal NdeI/XhoI in ORF; PASS |
| LiN3-Core | pET28a-SUMO-LiN3-Core | `GPGNPGPGNPGPGNP` | 372 | PASS: no internal NdeI/XhoI in ORF; PASS |
| LiA3-Ref | pET28a-SUMO-LiA3-Ref | `GPGAPGPGAPGPGAP` | 372 | PASS: no internal NdeI/XhoI in ORF; PASS |

## Files

- `vendor_order_table.csv`: insert sequences and construct QC.
- `insert_sequences/`: FASTA files for synthesis inserts, translated fusion products, and post-cleavage peptides.
- `genbank_final_constructs/`: target final plasmid maps for review and sequence verification.

## Protein Product

Each construct expresses an N-terminal His6-Smt3 SUMO fusion. SUMO protease cleavage after the SUMO C-terminal `GG` should release the native LiSPER peptide exactly, with no extra N-terminal or C-terminal residues.
