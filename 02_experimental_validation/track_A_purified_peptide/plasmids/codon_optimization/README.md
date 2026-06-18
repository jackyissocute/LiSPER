# IDT Codon Optimization

This folder stores the final IDT E. coli codon-optimization inputs used for the purified-peptide plasmid package.

## Files

| Path | Purpose |
|---|---|
| `idt_peptide_codon_optimization.csv` | Candidate-to-IDT optimized peptide DNA manifest used by the plasmid generator |
| `idt_downloads/` | Original IDT CSV downloads renamed by candidate |

## Usage

The vendor-ready plasmid generator reads this manifest and inserts the IDT-optimized peptide-coding DNA into the His6-SUMO-LiSPER expression cassette.

```text
06_project_operations/scripts/design_pet28a_SUMO_restriction_vendor_package.py
```

The His6 and Smt3 SUMO regions remain fixed in the generator. The LiSPER peptide region uses the IDT-optimized DNA exactly as listed in the manifest.

## QC

- All eight IDT peptide DNA sequences translate back to the expected LiSPER peptide sequences.
- IDT optimization changes the DNA codons but does not change the peptide products.
- The regenerated vendor package passes NdeI/XhoI boundary, internal-site, translation, and GenBank feature checks.
