# Bacterial Surface-Display Platform Comparison

## Ranking Summary

| Rank | Platform | Best LiSPER role | Overall assessment |
|---:|---|---|---|
| 1 | eCPX / circularly permuted OmpX | First proof-of-concept peptide display and library screening | Best fit for small peptides, E. coli, flow sorting, and low implementation risk. |
| 2 | OmpX variants | Small peptide display with minimal scaffold complexity | Strong option if eCPX geometry is not required. |
| 3 | Lpp-OmpA | Simple E. coli display and metal-binding peptide precedent | Useful and established, but topology/exposure can be less tunable. |
| 4 | Autotransporters | Larger passenger or robust E. coli/Pseudomonas display | Powerful but may add burden; overbuilt for 1-2 kDa peptides. |
| 5 | Bacillus spore/vegetative display | Durable pilot adsorbent | Excellent robustness, but second-wave platform after peptide validation. |
| 6 | Ice nucleation protein systems | High-copy display and large surface exposure | Useful in some hosts, but expression burden and membrane effects are concerns. |

## eCPX

- Display efficiency: strong for peptide libraries and FACS-compatible screening.
- Small peptide compatibility: excellent; designed around short peptide insertion and biterminal display logic (S14).
- Stability: good in E. coli lab assays; industrial salt/pH stability must be tested.
- Expression burden: generally manageable for small peptides.
- Industrial practicality: good for discovery, less proven for large-scale adsorbent columns.
- Literature support: strong directed-evolution and peptide-display precedent.

Assessment: Best first LiSPER platform. It answers the most important early question: does a LiSPER peptide still bind/select Li+ when surface-presented?

## OmpX

- Display efficiency: strong outer-membrane scaffold.
- Small peptide compatibility: high.
- Stability: good in controlled E. coli conditions.
- Expression burden: low to moderate.
- Industrial practicality: similar to eCPX; requires immobilization and process validation.
- Literature support: strong as the parent family for eCPX.

Assessment: Good backup or simpler comparator to eCPX.

## Lpp-OmpA

- Display efficiency: historically important and experimentally accessible.
- Small peptide compatibility: good; used for peptides and antibody fragments.
- Stability: moderate to good.
- Expression burden: usually manageable.
- Industrial practicality: attractive because it is simple and familiar.
- Literature support: foundational E. coli display literature (S15).

Assessment: Good low-complexity benchmark. Include as a comparator if eCPX geometry produces ambiguous binding.

## Autotransporter Systems

- Display efficiency: can be high, especially for passenger proteins.
- Small peptide compatibility: compatible, but the system is often larger than needed.
- Stability: good when passengers fold properly; passenger sequence can affect translocation.
- Expression burden: moderate to high.
- Industrial practicality: good for robust whole-cell biocatalysis and larger display cargos.
- Literature support: strong review base (S16).

Assessment: Better for later robust display or host expansion than for first 1-2 kDa LiSPER peptide screening.

## Ice Nucleation Protein Systems

- Display efficiency: can expose proteins/peptides on Gram-negative surfaces at high copy.
- Small peptide compatibility: plausible.
- Stability: context-dependent.
- Expression burden: can perturb membranes due to large carrier size.
- Industrial practicality: mixed; high display but potential fitness cost.
- Literature support: long-standing display literature (S24).

Assessment: Keep as a later comparator, not first-line.

## Bacillus Surface and Spore Display

- Display efficiency: strong for spores and some vegetative-cell anchors.
- Small peptide compatibility: plausible, but each anchor-peptide combination needs empirical validation.
- Stability: excellent for spores; attractive for harsh sidestreams and nonliving adsorbents.
- Expression burden: manageable but less convenient for rapid library sorting than E. coli eCPX.
- Industrial practicality: high.
- Literature support: strong and growing (S17).

Assessment: Best pilot-scale robustness platform after LiSPER peptide function is established in E. coli.

## Recommended Display Development Path

1. Build eCPX-LiSPER fusions in E. coli K-12/MG1655.
2. Compare OmpX and Lpp-OmpA for one or two top peptides.
3. Test binding in Li/Na and residual-metal matrices.
4. If peptide function survives display, transfer top peptide(s) to Bacillus spore display and immobilized/killed E. coli formats.
5. Consider Halomonas/Pseudomonas/Cupriavidus display only if process-liquid stress defeats E. coli/Bacillus.

## Evidence Base

Key sources: S13-S17, S24 in `extracted_data/source_metadata.md`.

