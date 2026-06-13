# Sequences

This folder contains designed peptide sequences and sequence metadata.

Current first-round library:

- `candidates.fasta`: FASTA input for structure prediction and downstream modeling.
- `candidates.tsv`: ranked sequence metadata with design logic, prediction, and recommended-start flag.

The complete first-round library contains 10 designed peptides. The recommended initial subset is:

- `LiD3-1`
- `LiND-1`
- `IDP-Li-1`
- `LowCharge-Li`
- `Control-Negative`

The core design logic is to combine GPGDP/GPGNP lithium-binding precedent with Gly/Ser/Pro-driven flexibility and oxygen donor residues, while limiting charge to reduce nonspecific Na+/Ca2+ binding risk.

Keep previous discarded sequences out of the primary library unless they are being analyzed for historical comparison.
