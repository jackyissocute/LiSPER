# Extracted Operating Envelope

The ranges below are design envelopes for LiSPER host-screening, not universal constants. Industrial streams vary strongly with cathode chemistry, leachant, liquid/solid ratio, solvent-extraction train, precipitation reagents, washing, and recycle loops.

| Parameter | Practical range for Li polishing sidestream | Evidence notes |
|---|---:|---|
| Lithium concentration | Commonly about 1-10 g/L Li in concentrated hydrometallurgical raffinates; brines and DLE feeds can be much lower. | Acid leaching dissolves Li with Ni/Co/Mn/Al/Cu/Fe (S1-S4). Li is typically left in raffinate after valuable transition metals are removed, then concentrated or precipitated (S2, S4, S5). |
| Sodium concentration | Low before NaOH/Na2CO3 dosing if upstream reagents are not sodium-rich; can become high after neutralization/carbonation, plausibly 0.1-2 M Na+ in alkaline carbonate/sulfate/nitrate liquors. | NaOH and Na2CO3 are common pH/carbonation reagents (S2, S5, S7). LiSPER testing should include Na-rich matrices because Li/Na selectivity is central to deployment. |
| Residual transition metals | Target: low mg/L to tens of mg/L after Cu/Al/Fe/Co/Mn/Ni removal; upset conditions may be higher. | Metal precipitation/solvent extraction removes Ni/Co/Mn before Li recovery (S1-S4). Residual metals matter because surface-displayed acidic peptides may bind multivalent cations more strongly than Li+. |
| pH before Li recovery | Acid leachate starts around pH <2; purified Li raffinate before carbonate precipitation may be mildly acidic to near-neutral depending on extraction/neutralization. | Hydrometallurgical leaching uses strong acid; downstream purification changes pH stepwise (S1-S4). |
| pH during Li2CO3 precipitation | Alkaline carbonate conditions, commonly around pH 10-12. | Sodium carbonate addition and lithium carbonate crystallization require alkaline carbonate chemistry (S5, S7). |
| Temperature for adsorption/capture | Ambient to moderately warm, commonly about 20-60 C for many adsorbent tests; some industrial DLE systems operate at brine temperature. | DLE adsorbents and ion sieves operate over broad brine/process conditions (S6, S8, S9). |
| Temperature for Li2CO3 precipitation | Elevated temperature is common, often 60-95 C and frequently near 80-90 C in lab and industrial crystallization studies. | Li2CO3 solubility decreases with increasing temperature, so heating improves precipitation yield (S5, S7). |
| Ionic strength | High relative to laboratory biological media once sulfate/chloride/nitrate/carbonate and sodium salts accumulate; should be treated as a high-salt process liquid. | DLE and battery-recycling raffinates involve concentrated salts; sodium carbonate dosing further raises ionic strength (S5-S8). |
| Residence time | Adsorption columns: minutes to hours depending bed depth and kinetics. Precipitation/crystallization: tens of minutes to hours. | DLE columns require contact, loading, wash, elution, and regeneration cycles (S6); crystallization studies vary mixing and aging times (S5, S7). |
| Existing polishing technologies | Na2CO3 precipitation, evaporative concentration, solvent extraction, ion exchange, manganese/titanium/aluminum lithium ion sieves, membrane/electrodialysis, DLE adsorption. | Summarized in lithium recovery reviews and industry DLE reports (S2, S6, S8). |
| Biosorption status | Much less mature than inorganic adsorbents; mostly lab-scale biomass or engineered-cell demonstrations. | Biosorption literature supports metal binding, but lithium-selective whole-cell capture in spent-LIB raffinate is not industrially established (S13, S17, S24). |

## Design Implication

The biologically realistic deployment point is not the hot, pH 11 carbonate crystallizer. It is a cooled, clarified, pH-adjusted lithium-polishing sidestream upstream of Na2CO3 precipitation, or an immobilized adsorption column with controlled pH and wash/elution conditions. Direct operation in raw acid leachate or hot carbonate precipitation liquor is a poor initial target for living surface-display cells.

