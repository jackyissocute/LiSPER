# Vendor-Ready Restriction-Cloning SUMO Plasmids

This folder contains the corrected purified-peptide plasmid vendor package for the final 8 LiSPER candidates.

Current project priority is to order synthetic LiSPER peptides directly for first-pass binding assays. This plasmid package is retained as a fallback/secondary route for in-house His6-SUMO expression and native peptide recovery.

If activated, the package follows the vendor-compatible rule: synthesize only the insert, then clone it into an original pET-28a(+) backbone by NdeI/XhoI restriction cloning.

The LiSPER peptide-coding regions use the IDT E. coli codon-optimized sequences stored in `../codon_optimization/idt_peptide_codon_optimization.csv`.

## Folder Contents

| Path | Purpose |
|---|---|
| `VENDOR_ORDER_INSTRUCTIONS.md` | Human-readable instructions to send/review with the vendor. |
| `vendor_order_table.csv` | Complete insert sequences and QC fields. |
| `genbank_final_constructs/` | Eight target final plasmid GenBank maps. |
| `insert_sequences/` | FASTA files for synthesis inserts and translated products. |

## Constructs

| Candidate | Plasmid | Product |
|---|---|---|
| `LiD3-Core` | `pET28a-SUMO-LiD3-Core` | His6-SUMO-`LiD3-Core` |
| `LiD3-Flex` | `pET28a-SUMO-LiD3-Flex` | His6-SUMO-`LiD3-Flex` |
| `LiND-Hybrid` | `pET28a-SUMO-LiND-Hybrid` | His6-SUMO-`LiND-Hybrid` |
| `LiLC-1` | `pET28a-SUMO-LiLC-1` | His6-SUMO-`LiLC-1` |
| `LiDS-1` | `pET28a-SUMO-LiDS-1` | His6-SUMO-`LiDS-1` |
| `LiDA-1` | `pET28a-SUMO-LiDA-1` | His6-SUMO-`LiDA-1` |
| `LiN3-Core` | `pET28a-SUMO-LiN3-Core` | His6-SUMO-`LiN3-Core` |
| `LiA3-Ref` | `pET28a-SUMO-LiA3-Ref` | His6-SUMO-`LiA3-Ref` |
