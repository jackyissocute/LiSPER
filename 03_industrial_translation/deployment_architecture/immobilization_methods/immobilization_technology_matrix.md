# Immobilization Technology Matrix

## Summary Ranking for LiSPER

| Rank | Method | Best use | Industrial suitability |
|---:|---|---|---|
| 1 | Epoxy-functionalized acrylic/methacrylate resin | Stable packed-bed peptide adsorbent | High |
| 2 | NHS coupling on agarose or polymer resin | Rapid prototype and pilot affinity media | Medium-high |
| 3 | Oriented cysteine/maleimide or click chemistry | Controlled LiSPER orientation after peptide redesign | Medium-high |
| 4 | Glutaraldehyde coupling | Low-cost biomass/support crosslinking | Medium |
| 5 | Ni-NTA/His-tag immobilization | Reversible lab screening | Low-medium |
| 6 | Biotin-streptavidin | Analytical validation and high-affinity prototypes | Low for bulk industry |
| 7 | Physical adsorption/entrapment | Low-cost exploratory immobilized cells | Low-medium |

## Method Comparison

| Method | Binding strength | Reusability | Cost | Industrial fit | LiSPER notes |
|---|---|---:|---:|---|---|
| NHS coupling | Covalent amide bond to primary amines; strong. | Good if peptide and support survive regeneration. | Medium. | Good for prototype/pilot; hydrolysis requires fresh activated media. | Easy but random lysine/N-terminus attachment may bury Li-binding residues unless peptide is engineered with a spacer and terminal amine. |
| Epoxy-functionalized supports | Covalent, often multipoint after long contact; very stable. | High. | Medium to high depending resin. | Strong industrial enzyme precedent. | Recommended for final packed-bed peptide material if LiSPER tolerates covalent attachment and spacer design. |
| Glutaraldehyde coupling | Covalent Schiff base/reduced amine networks; strong but heterogeneous. | Medium to high. | Low. | Good for low-cost immobilized biomass/enzyme systems; chemistry less controlled. | Attractive for inactivated display cells or protein-coated supports, but random crosslinking may damage peptide presentation. |
| Biotin-streptavidin | Extremely strong noncovalent affinity. | High under mild conditions, lower under harsh regeneration. | High. | Poor for commodity lithium recovery due ligand cost. | Excellent for assay development and bead screening, not bulk sorbent. |
| Ni-NTA/His-tag | Reversible coordination. | Moderate; susceptible to imidazole, low pH, chelators, metal exchange. | Medium. | Better for purification than industrial adsorbent. | Useful because LiSPER wet-lab peptides may use His6-SUMO, but Ni leaching and competing metals make it a poor final deployment. |
| Agarose supports | Depends on functional group. | Medium. | Medium-high. | Strong in bioprocess affinity media; softer beads limit high-pressure industrial wastewater use. | Good pilot material when pressure drop is manageable. |
| Magnetic beads | Covalent or affinity depending surface. | Medium. | High per kg. | Excellent for lab/pilot separations; weak for bulk low-cost streams. | Valuable for LiSPER screening and small modular systems; 2024 Li-binding peptide magnetic bead precedent is directly relevant. |
| Silica supports | Covalent silane chemistry; mechanically rigid. | Medium-high. | Low-medium. | Good mechanical/thermal properties; pH can dissolve silica under alkaline conditions. | Useful for membranes/monoliths or moderate-pH columns; avoid strong alkaline carbonate service. |
| Acrylic/methacrylate resins | Covalent functionalization; robust. | High. | Medium-high. | Strongest packed-bed candidate. | Best support family for industrial LiSPER peptide resin. |
| Industrial affinity media | Mature bead/column formats. | High if chemistry is stable. | High but scalable. | Strong pilot path; cost must be justified by high selectivity and reuse. | Good for pilot before developing custom low-cost resin. |

## Recommendation

Use a two-stage immobilization strategy:

1. Near-term validation: NHS or maleimide magnetic beads/agarose for fast binding, selectivity, and regeneration assays.
2. Industrial architecture: terminally engineered LiSPER peptide with spacer, covalently coupled to epoxy-functionalized acrylic/methacrylate resin in a packed bed.

Avoid Ni-NTA as final deployment because Li recovery streams contain competing metals, regeneration may strip nickel, and His-tag affinity is not designed for repeated harsh industrial cycles.

