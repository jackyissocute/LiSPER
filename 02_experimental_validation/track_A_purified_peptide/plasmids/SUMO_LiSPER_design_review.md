# SUMO-LiSPER Construct Design Review

## Recommendation

The current direct pET-28a(+) LiSPER designs are sequence-correct but not wet-lab robust because the expressed products are only about 4.6-5.1 kDa and retain vector-derived His/T7/linker residues on the assay molecule. Redesign all constructs as:

`T7 promoter -> His6 tag -> SUMO tag -> SUMO protease cleavage junction -> LiSPER peptide -> STOP`

Use a seamless/Gibson-compatible vendor cloning strategy in pET-28a(+), preserving the T7 expression cassette and kanamycin selection while replacing the current N-terminal His/T7 peptide fusion with a full His6-SUMO-LiSPER ORF.

## Critical Junction Requirement

The LiSPER peptide must begin immediately after the C-terminal `GG` of SUMO. SUMO protease cleaves after the SUMO C-terminal diglycine, so this design can release the native LiSPER peptide with no residual His-tag, T7 tag, linker, protease-site residue, or vector-derived residue.

Do not include the native pET-28a(+) T7 tag/linker between SUMO and the LiSPER peptide.

## Size Estimates

Masses are approximate average molecular weights. The fusion size assumes `MHHHHHH` plus a standard yeast Smt3/SUMO tag ending in `GG`, followed directly by the LiSPER peptide.

| candidate_id | liberated peptide sequence | peptide aa | peptide kDa | fusion aa | fusion kDa | cleavage product after SUMO protease |
|---|---|---:|---:|---:|---:|---|
| LiD3-1 | GPGDPGSGPGDPGSGPGDP | 19 | 1.577 | 124 | 13.774 | GPGDPGSGPGDPGSGPGDP |
| LiND-1 | GPGNPGSGPGDPGSGPGNP | 19 | 1.575 | 124 | 13.772 | GPGNPGSGPGDPGSGPGNP |
| IDP-Li-1 | SGDSGPGDPGDSG | 13 | 1.104 | 118 | 13.302 | SGDSGPGDPGDSG |
| IDP-Li-2 | GDSGSGPGDPGSGDS | 15 | 1.248 | 120 | 13.446 | GDSGSGPGDPGSGDS |
| LowCharge-Li | GPGDPGSGNPGSGDP | 15 | 1.267 | 120 | 13.465 | GPGDPGSGNPGSGDP |
| LiD2-IDP | GPGDPGSDGSGPGDP | 15 | 1.268 | 120 | 13.466 | GPGDPGSDGSGPGDP |
| StrongBind-Li | GPGDPGSDGPGDPGSD | 16 | 1.383 | 121 | 13.581 | GPGDPGSDGPGDPGSD |
| SoftCage-Li | GSGDPGNGDPGSG | 13 | 1.073 | 118 | 13.271 | GSGDPGNGDPGSG |
| IDP-Rich-Li | DSGDSGPGDPGDSGS | 15 | 1.306 | 120 | 13.504 | DSGDSGPGDPGDSGS |
| Control-Negative | GPGAPGSGPGAPGSGPGAP | 19 | 1.445 | 124 | 13.642 | GPGAPGSGPGAPGSGPGAP |

## Expected Expression Advantages

The His6-SUMO architecture should improve expression, protect the small acidic/disordered LiSPER peptides from proteolysis, increase apparent product size for SDS-PAGE detection, improve solubility, and enable robust Ni-NTA capture before cleavage.

After cleavage, pass the reaction over Ni-NTA again. His6-SUMO and His-tagged SUMO protease should bind the resin, while the untagged LiSPER peptide should be collected in the flow-through.

## SUMO vs MBP

SUMO is recommended over MBP for this 1-2 kDa peptide panel.

SUMO advantages:
- Compact fusion partner, keeping fusion proteins near 13-14 kDa rather than about 43-45 kDa.
- Strong track record for improving expression of small peptides.
- SUMO protease can release peptides with a native N-terminus when the junction is designed directly after SUMO `GG`.
- Easier downstream cleanup because the mass difference between SUMO and the peptide is large but not as operationally bulky as MBP.

MBP advantages:
- Often stronger solubility enhancement than SUMO.
- May be useful if SUMO fusions express poorly or aggregate.

MBP disadvantages for LiSPER:
- Much larger fusion partner can dominate purification behavior.
- Cleavage/removal burden is higher.
- More risk of carryover into binding assays.
- Native peptide release depends on the chosen protease site and usually leaves more design constraints than SUMO.

Conclusion: use His6-SUMO as the primary vendor submission architecture. Keep MBP as a backup only if His6-SUMO expression fails.

## Downstream Concerns

Peptide recovery after cleavage is the main remaining risk. These peptides are only about 1.1-1.6 kDa, so standard dialysis or centrifugal filters with common 3 kDa, 10 kDa, or 30 kDa MWCO membranes can lose the peptide into the filtrate or dialysate. Design the purification workflow around collecting and assaying the low-MW flow-through/fractions, not retaining the peptide above a membrane cutoff.

Recommended verification and handling:
- Verify fusion expression by Tris-Tricine SDS-PAGE or high-percentage gel rather than standard SDS-PAGE alone.
- Verify liberated peptide by LC-MS or MALDI-TOF; UV A280 may be poor because these peptides lack aromatic residues.
- Use peptide-compatible quantification such as amino acid analysis, LC-MS peak calibration, fluorescamine/OPA-type amine assays, or quantitative HPLC if available.
- Avoid storage conditions that introduce lithium/sodium contamination before selectivity assays.
- Desalt into metal-controlled buffer using LC/HPLC, SPE, or carefully validated low-binding workflows.
- Use low-bind tubes and minimize transfers because very short peptides can adsorb or disappear during cleanup.
- Confirm SUMO, SUMO protease, imidazole, and nickel carryover are removed before Li+/Na+ binding assays.

## Vendor-Ready Design Set

Proceed to redesign each candidate as a pET-28a(+)-compatible T7 expression plasmid carrying a synthetic `His6-SUMO-LiSPER-STOP` ORF. The vendor instructions should require full insert and junction sequence verification and should explicitly state that the SUMO C-terminal `GG` is fused directly to the first residue of each LiSPER peptide.

Do not order the current direct His/T7-LiSPER constructs for final binding assays.
