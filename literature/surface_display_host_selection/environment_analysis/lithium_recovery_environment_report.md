# Lithium Recovery Environment Report

## Executive Summary

LiSPER surface-display capture should be designed for a late-stage, metal-depleted lithium polishing stream, not raw spent-LIB acid leachate. The realistic process position is after Cu/Al/Fe removal and after Co/Mn/Ni recovery, before final sodium carbonate precipitation. At that point the stream is still chemically harsh for bacteria: high ionic strength, substantial sodium risk from neutralization/carbonation reagents, residual multivalent metals, and pH that can move from acidic/near-neutral to strongly alkaline depending on where capture is inserted.

The safest biologically plausible target is a clarified, cooled, pH-controlled sidestream upstream of Na2CO3 precipitation. A living-cell column should be treated as an engineered unit operation, not as a biological additive dropped into the main hot crystallizer.

## Process Context

Typical spent-LIB hydrometallurgy follows this logic:

1. Acid leaching dissolves Li, Ni, Co, Mn, Cu, Al, Fe, and other impurities into a strongly acidic liquor.
2. Cu/Al/Fe are removed by precipitation, cementation, solvent extraction, or pH-controlled impurity removal.
3. Co, Mn, and Ni are removed as higher-value products by solvent extraction, precipitation, crystallization, or combinations.
4. Lithium remains in the raffinate because it is monovalent, highly hydrated, and harder to selectively precipitate before transition metals.
5. Lithium is finally recovered by concentration and Na2CO3 precipitation as Li2CO3, or by adsorption/extraction followed by eluate conversion.

This sequence is consistent across spent-LIB recycling reviews and hydrometallurgical studies (S1-S5).

## Expected Chemistry at the Li Polishing Stage

| Variable | Expected LiSPER-relevant envelope | Design consequence |
|---|---:|---|
| Li+ | Often about 1-10 g/L in concentrated battery raffinates, but strongly process-dependent. | Screen LiSPER at low mM through high mM Li+, not only trace lithium. |
| Na+ | Potentially very high once NaOH/Na2CO3 are used; 0.1-2 M is a prudent challenge envelope. | Li/Na selectivity must be tested under sodium excess. |
| Residual Ni/Co/Mn | Ideally low mg/L to tens of mg/L; upset streams may be higher. | Multivalent-metal off-target binding is a critical failure mode. |
| Residual Fe/Al/Cu | Ideally removed before LiSPER; trace residuals still matter. | Include Fe3+/Al3+/Cu2+ interference screens. |
| pH before final Li recovery | Acidic to near-neutral depending process step; should be adjusted for biological columns. | Proof-of-concept should use pH 6-8, then expand to pH 5-9 if display remains intact. |
| pH during carbonate precipitation | Strongly alkaline, commonly pH 10-12. | Avoid living-cell operation here; immobilized dead cells or purified display particles could be explored later. |
| Temperature | Upstream adsorption can be ambient/moderate; carbonate precipitation often hot. | Surface-display host should target 20-40 C initially; thermostability is a later engineering constraint. |
| Ionic strength | High due to sulfate/chloride/nitrate/carbonate and sodium salts. | Include osmotic stress and membrane-integrity assays. |
| Residence time | Adsorption: minutes-hours; precipitation: tens of minutes-hours. | Column host needs immobilization, flow stability, and regeneration tolerance. |

## Existing Lithium Polishing Technologies

- Sodium carbonate precipitation remains the conventional endpoint for Li2CO3 production.
- Evaporation/concentration is used when Li concentration is too low for efficient precipitation.
- Lithium ion-sieves based on manganese oxide, titanium oxide, and related frameworks provide Li-selective adsorption in brines and wastewaters.
- Ion exchange, solvent extraction, membranes, and electrodialysis are used or proposed depending stream composition.
- DLE systems typically involve adsorption or ion-exchange contactors followed by washing, elution, sorbent regeneration, and lithium conversion (S6, S8, S9).

## Biosorption State of the Art

Biosorption is credible for metal removal generally but is immature for industrial lithium selectivity. A LiSPER display system must therefore be judged as an engineered affinity material rather than a drop-in replacement for mature inorganic sorbents. Its strongest niche is likely:

- high-specificity polishing after bulk impurity removal,
- modular columns with contained biomass,
- rapid peptide iteration and low-cost expression,
- operation in controlled sidestreams where pH, temperature, and bioburden can be managed.

## Industrial Operating Constraints

- Sterility cannot be assumed.
- Cells should be immobilized or otherwise contained.
- The process must tolerate high ionic strength and variable residual metals.
- Regeneration must not destroy the display scaffold.
- A host that grows well in the laboratory may still fail as an industrial adsorbent if outer-membrane integrity collapses under salt, pH, metals, or temperature.
- Biosafety and release risk matter because the unit would interface with industrial wastewater/recycling streams.

## Recommended Screening Matrix

Initial LiSPER display assays should use:

- pH: 6.0, 7.0, 8.0, 9.0, then stress tests at 5.0 and 10.0.
- Temperature: 20, 30, 37, and 45 C.
- Li+: 1, 10, 50, and 150 mM.
- Na+: 50, 250, 500, and 1000 mM.
- Competing metals: Ni2+, Co2+, Mn2+, Fe3+, Al3+, Cu2+ at low mg/L and upset-case concentrations.
- Contact time: 5, 15, 30, 60, and 180 min.

## Evidence Base

Key sources: S1-S9, S13, S17, S24 in `extracted_data/source_metadata.md`.

