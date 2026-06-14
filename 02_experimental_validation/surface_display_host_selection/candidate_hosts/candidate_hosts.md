# Candidate Microbial Host Assessment

## Ranking Summary

| Rank | Host | Best use case | Overall assessment |
|---:|---|---|---|
| 1 | E. coli K-12 derivatives / MG1655 | Proof-of-concept and academic research | Lowest implementation risk, strong genetics, compatible with eCPX/OmpX/Lpp-OmpA, BSL-1; weak industrial robustness. |
| 2 | E. coli BL21(DE3) | Expression-heavy proof-of-concept | Excellent expression strain; less ideal for environmental robustness and containment than K-12 lab chassis. |
| 3 | Bacillus subtilis | Pilot-scale dead/immobilized or spore-display exploration | Robust, GRAS history, strong secretion/spore-display literature; peptide display possible but less directly matched to eCPX-style LiSPER screening. |
| 4 | Pseudomonas putida KT2440 | Robust academic/pilot chassis | Strong stress tolerance and genetics; surface-display literature exists but is less plug-and-play for small peptide libraries. |
| 5 | Halomonas / H. bluephagenesis-like chassis | High-salt industrial research | Excellent salt/open-process fit; less mature for surface-display peptide discovery. |
| 6 | Cupriavidus metallidurans / C. necator | Metal-rich sidestream research | Metal tolerance is attractive; slower, less standardized display and deployment toolkit. |
| 7 | Acidithiobacillus species | Raw acidic leachate/bioleaching research only | Fits low-pH metal-rich leaching, not late Li polishing; genetic/display systems are high-risk for LiSPER. |
| 8 | DH5alpha-derived systems | Cloning and library maintenance | Useful cloning host but not a good production/display or industrial adsorption host. |

## Host-by-Host Review

### E. coli BL21(DE3)

- Growth temperature: typically 30-37 C; can be run lower for folding.
- pH tolerance: best near neutral; poor under strong acid or high alkalinity.
- Salt tolerance: moderate; high NaCl imposes osmotic stress.
- Metal tolerance: limited compared with environmental metal-resistant bacteria.
- Lithium tolerance: LiCl inhibits E. coli growth and translation at sufficiently high concentration; lithium stress must be measured directly for LiSPER strains (S11).
- Genetic engineering: excellent.
- Surface display: excellent compatibility with OmpX/eCPX, Lpp-OmpA, autotransporters, and INP-derived systems.
- Industrial history: strong recombinant protein host, weak as live environmental adsorbent.
- Cost: very low.
- Scale-up: excellent for fermentation; adsorption-column survival under Li raffinate requires validation.
- Biosafety: BSL-1 lab strain, but live release containment still required.
- Immobilization potential: good; many E. coli immobilization precedents.
- Suitability for adsorption column: strong for proof of concept, moderate for pilot only after immobilization and killed-cell options.

Assessment: BL21(DE3) is attractive if high expression is the bottleneck. It is not the best first host if the key assay is clean surface-display genotype-phenotype screening rather than protein yield.

### E. coli MG1655

- Growth temperature: 30-37 C typical.
- pH tolerance: near-neutral preferred.
- Salt/metal/lithium tolerance: moderate to weak under industrial salt/metals.
- Genetic engineering: excellent; clean K-12 genetic background.
- Surface display: strong compatibility with E. coli display platforms.
- Industrial deployment: excellent lab chassis, limited environmental robustness.
- Biosafety: BSL-1 K-12 derivative.
- Immobilization potential: good.
- Column suitability: best early academic host where controllability and clean genetics matter.

Assessment: MG1655 is the best baseline academic host for measuring whether LiSPER peptides retain Li selectivity on a bacterial surface without BL21-specific expression artifacts.

### E. coli K-12 Derivatives

- Growth temperature/pH/salt: similar to MG1655, depending derivative.
- Engineering: best-in-class toolkit.
- Display: best-in-class for eCPX/OmpX/Lpp-OmpA peptide screening.
- Biosafety: favorable, especially nonpathogenic auxotrophic or containment-engineered strains.
- Column suitability: good proof-of-concept; industrial use should likely shift to immobilized/killed cells or transferred peptide materials.

Assessment: Overall lowest-risk proof-of-concept chassis family.

### DH5alpha-Derived Systems

- Strength: plasmid construction and library propagation.
- Weakness: not optimized for surface-display stress, protein expression, or industrial operation.
- Display: possible but not preferred.

Assessment: Use for cloning, not as the LiSPER display workhorse.

### Bacillus subtilis

- Growth temperature: typically 30-37 C; some strains tolerate broader ranges.
- pH tolerance: broader than E. coli in many industrial contexts, but not an acidophile.
- Salt tolerance: strain-dependent; generally better environmental resilience than E. coli but not a halophile.
- Metal/lithium tolerance: not a dedicated metal-resistant chassis.
- Genetic engineering: strong.
- Surface display: strong literature for vegetative-cell and spore display; spores add durability (S17).
- Industrial history: excellent; enzyme production, GRAS/QPS reputation, secretion, spores.
- Cost/scale-up: excellent.
- Biosafety: favorable.
- Immobilization potential: excellent, especially spores.
- Column suitability: attractive for pilot-scale robust adsorbents, particularly if LiSPER can be displayed on spores or killed biomass.

Assessment: Best candidate to evaluate after E. coli proof of peptide function, especially for more rugged immobilized formats.

### Pseudomonas Species

Best representative: Pseudomonas putida KT2440.

- Growth temperature: mesophilic, typically around 30 C.
- pH/salt tolerance: generally more stress-tolerant than E. coli, but strain-dependent.
- Metal tolerance: better than E. coli for many environmental stresses, but not as metal-specialized as Cupriavidus.
- Genetic engineering: good and improving.
- Surface display: possible using autotransporters and outer-membrane systems; less standardized for LiSPER-style peptide libraries.
- Industrial deployment: growing chassis for biomanufacturing; KT2440 has a favorable safety profile.
- Column suitability: promising pilot research host if E. coli fails in process liquor.

Assessment: A strong second-wave research chassis for more realistic salt/metal exposure.

### Cupriavidus Species

Representatives: Cupriavidus metallidurans CH34 and Cupriavidus necator H16.

- Growth temperature: mesophilic.
- pH/salt: moderate, strain-dependent.
- Metal tolerance: excellent for C. metallidurans; CH34 is a model heavy-metal-resistant bacterium (S20, S21).
- Lithium tolerance: not the main known strength; must test.
- Genetic engineering: feasible but less convenient than E. coli/Bacillus/Pseudomonas.
- Surface display: less mature for small peptide display.
- Industrial history: C. necator has industrial PHA/bioprocess history; C. metallidurans is more bioremediation-focused.
- Column suitability: useful if residual Ni/Co/Mn/Cu toxicity dominates.

Assessment: Keep as a contingency host for metal-rich sidestreams, not as the primary LiSPER path.

### Acidithiobacillus Species

- Growth temperature: mesophilic to moderately thermophilic depending species.
- pH tolerance: excellent under acidic bioleaching conditions.
- Metal tolerance: excellent in leaching liquors.
- Genetic engineering: harder and slower than mainstream chassis.
- Surface display: not mature for rapid LiSPER peptide iteration.
- Industrial history: strong in biomining/bioleaching.
- Column suitability: relevant to upstream leachate, not post-metal-removal Li polishing.

Assessment: Scientifically interesting but mismatched to the selected LiSPER deployment point.

### Halophilic Hosts

Representatives: Halomonas bluephagenesis and related Halomonas spp.

- Growth temperature: mesophilic, strain-dependent.
- pH/salt tolerance: excellent salt tolerance; some tolerate alkaline conditions.
- Metal/lithium tolerance: likely better osmotic compatibility in brine-like streams, but lithium-specific tolerance must be measured.
- Genetic engineering: improving; less mature than E. coli.
- Surface display: less established for small peptide display and library sorting.
- Industrial deployment: strong open/unsterile fermentation promise (S23).
- Column suitability: attractive for high-sodium Li raffinate after the peptide/display concept is validated.

Assessment: Best high-salt industrial research direction, but not the lowest-risk first chassis.

## Candidate Discovered During Review: Shewanella oneidensis

Shewanella has strong metal-reduction and environmental biotechnology literature, biofilm/immobilization potential, and genetic tools. However, it is not a top LiSPER host because lithium polishing needs Li/Na selectivity and surface peptide presentation more than extracellular electron transfer. It remains a possible biofilm-material host if column immobilization becomes central.

## Recommendation by Phase

- Cloning: DH5alpha or equivalent.
- First surface-display assay: E. coli K-12/MG1655 with eCPX/OmpX.
- Expression-heavy backup: E. coli BL21(DE3).
- Robust biological adsorbent follow-up: Bacillus subtilis spore/vegetative display.
- High-salt industrial research: Halomonas.
- Metal-rich contingency: Cupriavidus.

## Evidence Base

Key sources: S11-S23 in `extracted_data/source_metadata.md`.

