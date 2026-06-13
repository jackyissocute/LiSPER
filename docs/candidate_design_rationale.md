# Candidate Design Rationale

LiSPER's first-round library tests whether lithium-binding peptide motifs can be embedded in flexible, IDP-like sequence contexts to improve Li+/Na+ selectivity.

## Three Inspirations

1. Lithium-binding peptide precedent

   The LBP literature motivates the use of GPGNP and GPGDP motifs as lithium-recognition elements.

2. Intrinsically disordered peptide behavior

   Gly/Ser/Pro-rich designs are intended to avoid a rigid folded pocket and instead sample flexible ensembles that can adapt around small ions.

3. Controlled oxygen-donor chemistry

   Asp/Glu and backbone/side-chain oxygen donors may support Li+ coordination, but excessive negative charge may increase nonspecific Na+/Ca2+ binding.

## Complete First-Round Library

| Rank | Name | Sequence | Main design logic | Prediction | Recommended start |
| --- | --- | --- | --- | --- | --- |
| 1 | LiD3-1 | GPGDPGSGPGDPGSGPGDP | Uses the best literature motif GPGDP, repeated 3x, with Gly/Ser flexibility. | Best first candidate | Yes |
| 2 | LiND-1 | GPGNPGSGPGDPGSGPGNP | Combines original LBP GPGNP with improved GPGDP. | Balanced affinity/selectivity | Yes |
| 3 | IDP-Li-1 | SGDSGPGDPGDSG | IDP-like flexible acidic shell around GPGDP. | Good Li+ binding, moderate selectivity | Yes |
| 4 | IDP-Li-2 | GDSGSGPGDPGSGDS | More symmetric disordered binding pocket. | Good screening candidate | No |
| 5 | LowCharge-Li | GPGDPGSGNPGSGDP | Lower negative charge to avoid nonspecific Na+/Ca2+ binding. | Better selectivity risk-control | Yes |
| 6 | LiD2-IDP | GPGDPGSDGSGPGDP | Two GPGDP motifs plus IDP acidic spacer. | Strong but not overcharged | No |
| 7 | StrongBind-Li | GPGDPGSDGPGDPGSD | Higher Asp density for stronger Li+ capture. | High affinity, lower selectivity risk | No |
| 8 | SoftCage-Li | GSGDPGNGDPGSG | Short flexible oxygen-rich Li+ cage. | Small, cheap, easy to test | No |
| 9 | IDP-Rich-Li | DSGDSGPGDPGDSGS | More IDP-like, many carboxylate/Ser donors. | Strong binding, may bind other metals | No |
| 10 | Control-Negative | GPGAPGSGPGAPGSGPGAP | Literature-related weak/neutral control. | Should bind Li+ weaker | Yes |

## Recommended Initial Subset

- LiD3-1
- LiND-1
- IDP-Li-1
- LowCharge-Li
- Control-Negative

This subset balances one strong literature-motif repeat design, one mixed-motif design, one IDP-shell design, one selectivity risk-control design, and one negative control.

## Screening Principle

Every candidate should be evaluated against both Li+ and Na+.

The main metric is:

Delta Delta G = Delta G(Li+) - Delta G(Na+)

More negative Delta Delta G values indicate stronger lithium preference.
