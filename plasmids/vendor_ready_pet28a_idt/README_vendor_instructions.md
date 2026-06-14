# pET-28a(+) LiSPER Vendor Instructions

Please synthesize the listed codon-optimized inserts and clone each one into pET-28a(+) for E. coli BL21(DE3) expression. Preserve the N-terminal His-tag expression frame of pET-28a(+). Include a stop codon after each candidate coding sequence to avoid expression of unwanted C-terminal vector-derived residues/tags. Please sequence-verify the full insert and junction regions. Deliver plasmid DNA, final plasmid maps, full sequences, and Sanger sequencing reports.

## Files

- `idt_optimizer_exports/`: archived IDT codon optimizer exports and the optimization-order screenshot.
- `idt_file_mapping.csv`: mapping from rank/candidate to the archived IDT export.
- `plasmid_order_table.csv`: vendor order table with IDT-optimized insert sequences and design notes.
- `plasmid_qc_report.csv`: per-construct translation, frame, stop-codon, and restriction-site QC.
- `plasmid_qc_report.md`: compact human-readable QC summary.
- `genbank/*.gb`: annotated circular GenBank plasmid maps for each construct.

## Cloning Design

Use seamless/Gibson cloning into pET-28a(+) after the retained BamHI-derived `GS` linker in the N-terminal His/T7 expression frame. The expected N-terminal vector-derived leader is `MGSSHHHHHHSSGLVPRGSHMASMTGGQQMGRGS`, followed immediately by the candidate sequence and a `TAA` stop codon.
