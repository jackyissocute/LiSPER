# Final Host Selection Report

## Bottom Line

Do not choose a single industrial host yet. The evidence supports a staged decision:

- Best proof-of-concept host: E. coli K-12 derivative, preferably MG1655 or a closely related display-friendly K-12 strain.
- Best academic-research host: E. coli MG1655/K-12 with eCPX first, plus BL21(DE3) only if expression yield becomes limiting.
- Best pilot-scale host: Bacillus subtilis spore or immobilized vegetative display, after LiSPER peptide function is validated.
- Best industrial host direction: Bacillus subtilis spore/killed-cell adsorbent for contained columns; Halomonas is the best high-salt industrial research backup if sodium-rich operation becomes mandatory.

This recommendation optimizes for feasibility, engineering realism, and low implementation risk, not novelty.

## 1. Real Industrial Lithium-Recovery Environment

LiSPER is unlikely to operate in raw acid leachate. The realistic target is a late-stage lithium raffinate after Cu/Al/Fe and Co/Mn/Ni removal but before Na2CO3 precipitation.

Key features:

- Li+ may be in the g/L range after concentration, but exact values are process-specific.
- Na+ can become very high if NaOH and Na2CO3 are used.
- Residual Ni/Co/Mn/Cu/Fe/Al should be low after purification but can still interfere with acidic or chelating peptides.
- Raw leachate is strongly acidic; final Li2CO3 precipitation is strongly alkaline.
- Ionic strength is high.
- Industrial sterility is unrealistic.
- Adsorption columns need immobilization, containment, regeneration, and consistent pressure/flow behavior.

Therefore, LiSPER should target a cooled, clarified, pH-adjusted sidestream upstream of carbonate precipitation.

## 2. Lithium Capture Operating Conditions

Lithium adsorption and lithium carbonate precipitation are different unit operations:

- Adsorption/DLE: often ambient to moderately warm, commonly compatible with 20-60 C depending sorbent and stream.
- Li2CO3 precipitation: commonly elevated temperature, often 60-95 C and frequently around 80-90 C, because Li2CO3 solubility decreases as temperature rises.
- Biological display should not be forced into the hot carbonate crystallizer during early development.

The first LiSPER process model should be:

1. Purified Li raffinate.
2. pH adjustment to a biological/material-compatible range.
3. Immobilized LiSPER display adsorption.
4. Wash/elution/regeneration.
5. Conventional Li2CO3 precipitation from enriched eluate.

## 3. Candidate Host Ranking

| Rank | Host | Score | Rationale |
|---:|---|---:|---|
| 1 | E. coli K-12 / MG1655 | 8.5/10 | Lowest-risk genetics and display; ideal for measuring LiSPER function. Weakness is industrial robustness. |
| 2 | E. coli BL21(DE3) | 7.8/10 | Strong expression host; useful backup. Less clean as a baseline selection chassis. |
| 3 | Bacillus subtilis | 7.6/10 | Best robust/pilot candidate, especially spore display; needs transfer after peptide validation. |
| 4 | Pseudomonas putida KT2440 | 6.8/10 | Robust and engineerable; display path less direct. |
| 5 | Halomonas spp. | 6.5/10 | Best high-salt industrial direction; display/libraries less mature. |
| 6 | Cupriavidus spp. | 6.0/10 | Excellent metal tolerance; less direct for LiSPER display engineering. |
| 7 | Acidithiobacillus spp. | 4.8/10 | Fits upstream acidic bioleaching, not Li polishing. |
| 8 | DH5alpha-derived systems | 4.0/10 | Cloning host, not production/display deployment host. |

## 4. Display Technology Ranking

| Rank | Platform | Score | Rationale |
|---:|---|---:|---|
| 1 | eCPX | 9.0/10 | Best match for small peptides, E. coli, FACS/library screening, and low-risk first experiments. |
| 2 | OmpX | 8.0/10 | Strong small-peptide scaffold and simple comparator. |
| 3 | Lpp-OmpA | 7.5/10 | Established and simple; good benchmark. |
| 4 | Autotransporter | 6.8/10 | Powerful but overbuilt for 1-2 kDa peptides. |
| 5 | Bacillus spore/vegetative display | 6.7/10 now, higher for pilot | Excellent durability; less ideal for first peptide discovery. |
| 6 | Ice nucleation protein | 6.0/10 | High exposure possible, but carrier burden and membrane effects are concerns. |

## 5. Recommendations

### Best Proof-of-Concept Host

Use E. coli K-12/MG1655 with eCPX.

Justification: It offers the fastest, cleanest route to test whether LiSPER peptides still bind lithium selectively when displayed on a bacterial surface. It also keeps the first experiment close to established bacterial-display literature rather than entangling peptide performance with an exotic host.

### Best Academic-Research Host

Use E. coli MG1655/K-12 as the main chassis, with BL21(DE3) as an expression-yield backup.

Justification: Academic research needs iteration speed, reproducibility, cheap genetics, FACS-compatible display, and interpretable controls. K-12 strains beat industrial robustness candidates on those criteria.

### Best Pilot-Scale Host

Move top peptides into Bacillus subtilis spore or immobilized display after E. coli validation.

Justification: Bacillus offers a stronger industrial safety and robustness story, especially with spores. It is a better candidate for contained, non-growing, reusable adsorbent columns than live E. coli, but it should not be the first place to debug peptide-display chemistry.

### Best Industrial Host

Prioritize a Bacillus subtilis spore/killed-cell adsorbent format. Keep Halomonas as the high-sodium/high-salt industrial backup.

Justification: Industrial Li raffinate will not be sterile and may be salt-rich. A living engineered E. coli column is regulatory and operationally fragile. Bacillus spores or killed/immobilized biomass better match containment, durability, and cost. If the key stressor turns out to be sodium/osmotic load rather than metals or pH, Halomonas deserves a dedicated display-tooling program.

## 6. Decision Rule Applied

The recommendation deliberately avoids novelty. Acidithiobacillus, Cupriavidus, and Halomonas are scientifically interesting, but the evidence does not support making them first-line hosts before LiSPER peptide function is proven on a mature display platform.

The low-risk development path is:

1. E. coli K-12/MG1655 + eCPX for initial binding/selectivity.
2. OmpX and Lpp-OmpA comparison for display-geometry sensitivity.
3. Matrix stress testing in synthetic Li raffinate.
4. Immobilized or killed E. coli column test.
5. Bacillus spore-display transfer for pilot durability.
6. Halomonas or Cupriavidus only if process-specific salt or metal stress defeats the simpler chassis.

## Required Next Experiments

- Measure LiSPER binding in Na-rich matrices, not just clean LiCl.
- Include Ni2+, Co2+, Mn2+, Fe3+, Al3+, and Cu2+ competition.
- Test pH 6-9 before attempting more extreme pH.
- Compare live, fixed, and immobilized cells.
- Measure display level, cell integrity, and Li uptake separately.
- Run desorption/regeneration cycles before calling any host pilot-ready.

## Evidence Base

See:

- `extracted_data/source_metadata.md`
- `extracted_data/operating_envelope_table.md`
- `environment_analysis/lithium_recovery_environment_report.md`
- `environment_analysis/lithium_capture_conditions_report.md`
- `candidate_hosts/candidate_hosts.md`
- `display_systems/display_platform_comparison.md`

