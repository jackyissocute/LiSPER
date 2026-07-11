# Construct-Purification Alignment Check

## Verdict

The current final-8 plasmid design is aligned with the future purified-peptide workflow.

The plasmids are suitable for:

```text
BL21(DE3) expression
-> His6-SUMO fusion purification by Ni-NTA
-> SUMO protease cleavage
-> native LiSPER peptide recovery
-> peptide QC
-> Li+/Na+ binding assays
```

## Construct Features That Support Purification

| Plasmid feature | Why it helps |
|---|---|
| pET-28a(+) T7 expression context | Standard expression route in BL21(DE3)-type strains. |
| Kanamycin marker | Routine bacterial selection. |
| N-terminal His6 tag | Enables first-pass Ni-NTA / IMAC purification. |
| Smt3 SUMO tag | Improves solubility and provides a precise cleavage junction. |
| LiSPER peptide immediately after SUMO `GG` | SUMO protease should release the native peptide without extra residues. |
| Stop codon before XhoI | Prevents vector-derived C-terminal residues. |

## Expected Molecular Sizes

| Candidate | Fusion MW (kDa) | Native peptide MW (kDa) |
|---|---:|---:|
| LiD3-Core | 13.486 | 1.288 |
| LiD3-Flex | 13.774 | 1.577 |
| LiND-Hybrid | 13.772 | 1.575 |
| LiLC-1 | 13.465 | 1.267 |
| LiDS-1 | 13.155 | 0.958 |
| LiDA-1 | 13.184 | 0.986 |
| LiN3-Core | 13.483 | 1.285 |
| LiA3-Ref | 13.354 | 1.156 |

## Main Obstacles To Expect

| Stage | Risk | Interpretation |
|---|---|---|
| Expression | weak or insoluble fusion | Optimize temperature/IPTG before judging candidate quality. |
| Ni-NTA | target in flow-through | Check pH, resin capacity, imidazole, and His-tag accessibility. |
| SUMO cleavage | incomplete cleavage | Optimize protease ratio, time, temperature, and buffer. |
| Native peptide recovery | peptide too small for standard concentrators | Avoid unvalidated MWCO filters; save flow-through/wash fractions. |
| QC | native peptide not visible by gel | Expected; use MS/HPLC when possible. |
| Binding assay | Li/Na contamination or imidazole/nickel carryover | Desalt, run process blanks, and use low-sodium buffers. |

## Minimum Bench Evidence Before Binding Assays

Do not interpret Li+/Na+ binding until each candidate has:

- confirmed plasmid / colony identity,
- detectable His6-SUMO-LiSPER expression,
- soluble fraction or an optimized expression condition,
- Ni-NTA enriched fusion fraction,
- evidence of SUMO cleavage,
- recovered peptide-containing fraction,
- peptide identity or recovery QC,
- buffer/process blanks for Li/Na background.

## Practical Readout Strategy

Track the fusion by gel.

```text
13.2-13.8 kDa His6-SUMO-LiSPER
```

Track the native peptide by MS/HPLC or assay-linked recovery.

```text
0.96-1.58 kDa LiSPER peptide
```

The native peptide may be scientifically present even when it is not visible by routine SDS-PAGE staining.
