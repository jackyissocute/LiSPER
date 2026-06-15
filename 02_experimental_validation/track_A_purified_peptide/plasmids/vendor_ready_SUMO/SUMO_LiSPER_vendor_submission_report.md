# SUMO LiSPER Vendor Submission Report

## Construct Rationale

The deprecated direct His/T7-LiSPER constructs have been archived and should not be used for vendor submission. The redesigned constructs express each LiSPER peptide as an N-terminal His6-Smt3 SUMO fusion under the pET-28a(+) T7/RBS cassette. SUMO improves expression and protects the 1-2 kDa peptides during production, while SUMO protease cleavage after the SUMO C-terminal diglycine releases the exact native peptide.

Required architecture: `T7 promoter -> RBS -> His6 -> Smt3 SUMO -> LiSPER peptide -> STOP`.

No T7 tag, thrombin remnant, vector-derived linker, or extra residue is present between SUMO and the LiSPER peptide.

## Construct Summary

| Candidate | Peptide sequence | Fusion protein MW (kDa) | Native peptide MW (kDa) | Predicted expressed protein sequence | Post-cleavage peptide sequence |
|---|---|---:|---:|---|---|
| LiD3-1 | GPGDPGSGPGDPGSGPGDP | 13.774 | 1.577 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGGPGDPGSGPGDPGSGPGDP` | `GPGDPGSGPGDPGSGPGDP` |
| LiND-1 | GPGNPGSGPGDPGSGPGNP | 13.772 | 1.575 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGGPGNPGSGPGDPGSGPGNP` | `GPGNPGSGPGDPGSGPGNP` |
| IDP-Li-1 | SGDSGPGDPGDSG | 13.302 | 1.104 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGSGDSGPGDPGDSG` | `SGDSGPGDPGDSG` |
| IDP-Li-2 | GDSGSGPGDPGSGDS | 13.446 | 1.248 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGGDSGSGPGDPGSGDS` | `GDSGSGPGDPGSGDS` |
| LowCharge-Li | GPGDPGSGNPGSGDP | 13.465 | 1.267 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGGPGDPGSGNPGSGDP` | `GPGDPGSGNPGSGDP` |
| LiD2-IDP | GPGDPGSDGSGPGDP | 13.466 | 1.268 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGGPGDPGSDGSGPGDP` | `GPGDPGSDGSGPGDP` |
| StrongBind-Li | GPGDPGSDGPGDPGSD | 13.581 | 1.383 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGGPGDPGSDGPGDPGSD` | `GPGDPGSDGPGDPGSD` |
| SoftCage-Li | GSGDPGNGDPGSG | 13.271 | 1.073 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGGSGDPGNGDPGSG` | `GSGDPGNGDPGSG` |
| IDP-Rich-Li | DSGDSGPGDPGDSGS | 13.504 | 1.306 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGDSGDSGPGDPGDSGS` | `DSGDSGPGDPGDSGS` |
| Control-Negative | GPGAPGSGPGAPGSGPGAP | 13.642 | 1.445 | `MHHHHHHMSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGGGPGAPGSGPGAPGSGPGAP` | `GPGAPGSGPGAPGSGPGAP` |

## Cloning Strategy

Use seamless/Gibson-compatible synthesis and cloning into pET-28a(+), replacing the native N-terminal His/T7/MCS coding region with the synthetic His6-Smt3SUMO-LiSPER-STOP ORF while retaining the vector T7 promoter, RBS, lac operator, KanR, ori, lacI, and T7 terminator. Sequence-verify the full synthetic ORF and both vector junctions.

## Expression Strategy

Transform sequence-verified plasmids into E. coli BL21(DE3). Express under T7 induction using kanamycin selection. Because the fusion products are approximately 13.3-13.8 kDa, use Tris-Tricine SDS-PAGE or high-percentage gels for expression checks.

## Purification Strategy

Purify the His6-SUMO-LiSPER fusion by Ni-NTA under native conditions. Buffer exchange or dilute imidazole before cleavage as needed. Retain samples of soluble lysate, flow-through, wash, and elution for analytical gels.

## SUMO Cleavage Workflow

Digest purified fusion with SUMO protease. The LiSPER peptide begins immediately after the SUMO C-terminal `GG`, so cleavage should release the exact native peptide. After cleavage, run the reaction over Ni-NTA again: His6-SUMO and His-tagged SUMO protease should bind resin, while the untagged LiSPER peptide should be collected in the flow-through.

## Downstream Peptide Recovery and Assay Concerns

The liberated peptides are only about 1.1-1.6 kDa. Do not expect standard 3 kDa, 10 kDa, or 30 kDa MWCO devices to retain them. Collect low-MW flow-through fractions intentionally. Verify identity by LC-MS or MALDI-TOF; A280 detection is not suitable because the peptides lack aromatic residues. Use metal-controlled, low-salt, low-contamination buffers for Li+/Na+ assays and remove imidazole, nickel, SUMO, and protease carryover before binding measurements.

## Vendor Ordering Recommendations

Order the GenBank designs in `genbank/` or the synthetic ORF sequences in `insert_sequences/`. Request plasmid DNA, final plasmid maps, full sequence files, and Sanger verification across the full ORF and both junctions. Do not order the archived direct His/T7-LiSPER constructs for final binding assays.
