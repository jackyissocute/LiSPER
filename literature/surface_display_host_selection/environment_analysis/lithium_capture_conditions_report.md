# Lithium Capture Conditions Report

## Executive Summary

Lithium capture and lithium carbonate production should be separated conceptually. Adsorption/capture can often be run near room temperature or moderately warm, especially when using ion sieves, ion exchangers, or DLE-style contactors. Lithium carbonate precipitation is commonly run hotter, often around 60-95 C, because Li2CO3 has retrograde solubility: precipitation is favored at elevated temperature.

For LiSPER, this means the best biological deployment point is before carbonate precipitation and after major metal removal, with pH and temperature adjusted for the host/display material. The carbonate crystallizer itself is a poor first deployment target for living bacteria.

## Temperature Regimes

| Operation | Common temperature logic | LiSPER implication |
|---|---|---|
| Adsorption / DLE loading | Ambient to brine/process temperature; often 20-60 C in lab and industrial concepts. | A mesophilic display host can be tested realistically at 20-40 C. |
| Adsorbent elution/regeneration | Depends on material: acid, salt, water, or pH swing; temperature may be ambient or warm. | Regeneration compatibility is as important as one-cycle binding. |
| Li2CO3 precipitation | Frequently elevated; 60-95 C and often 80-90 C in crystallization studies. | Do not require live-cell survival here for initial LiSPER proof of concept. |
| Evaporative concentration | Often heated and energy-intensive. | A biological unit should be upstream or in a cooled bypass unless using dead/immobilized biomass. |

## Does Elevated Temperature Improve Lithium Separation?

For Li2CO3 precipitation, yes. Lithium carbonate solubility decreases as temperature increases, so higher temperature improves precipitation yield and crystallization kinetics. Sources on battery-derived Li2CO3 crystallization and Li-rich brine precipitation repeatedly use hot conditions or discuss temperature as a favorable crystallization variable (S5, S7).

For adsorption, the answer is material-specific. Some adsorbents show faster kinetics at higher temperature, but biological surface display adds new constraints: membrane stability, protein folding, peptide presentation, and cell viability. A peptide-display host should therefore not be selected solely for heat tolerance unless the process demands direct hot-stream contact.

## Is Room-Temperature Operation Common?

Room-temperature adsorption tests are common in lithium ion-sieve and DLE literature because they simplify screening and because many brines/process streams can be contacted without boiling. Industrial operation may still use native brine temperatures, heated streams, or cooled sidestreams. For LiSPER, room-temperature operation is realistic for proof of concept and early column testing.

Room-temperature Li2CO3 precipitation is less attractive because yield is lower unless lithium is concentrated or residence time/chemistry is adjusted.

## pH Sequence: Before or After pH Adjustment?

Lithium adsorption systems are commonly operated after some degree of pretreatment: solids removal, impurity removal, oxidation/reduction control, and pH adjustment. For LiSPER, this is not optional. Raw leachate pH and metal content would create severe off-target binding and host damage.

Recommended LiSPER insertion point:

1. After bulk transition-metal removal.
2. Before Na2CO3 precipitation.
3. In a pH-controlled sidestream near pH 6-8 initially.
4. With post-capture elution or desorption feeding conventional Li2CO3 production.

## Advantages and Disadvantages by Temperature

| Regime | Advantages | Disadvantages |
|---|---|---|
| 20-30 C | Best for E. coli screening, low energy, easy analytics, preserves proteins. | Slower kinetics for some adsorbents; may not match warm industrial streams. |
| 30-40 C | Compatible with common mesophiles; closer to many industrial warm processes. | Higher stress under salt/metals; expression burden can worsen. |
| 45-60 C | May improve mass transfer and kinetics; useful for robust immobilized/dead biomass. | E. coli display is unlikely to be stable long-term; fewer genetic chassis options. |
| 80-95 C | Strongly favorable for Li2CO3 precipitation. | Incompatible with living bacterial hosts and most peptide-display membranes. |

## Decision Consequence

LiSPER should optimize for a controlled adsorption column, not for live survival in carbonate precipitation. The biological host should be chosen for display reliability, engineering speed, containment, and moderate salt/metal tolerance. Industrial robustness can then be added by immobilization, killed-cell formats, host switching, or peptide transfer to nonliving supports.

## Evidence Base

Key sources: S2, S5-S9 in `extracted_data/source_metadata.md`.

