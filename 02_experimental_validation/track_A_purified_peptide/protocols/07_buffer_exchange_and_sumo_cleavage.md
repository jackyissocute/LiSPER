# 07 Buffer Exchange and SUMO Cleavage Protocol

## Purpose

Remove purification-buffer components that interfere with SUMO protease and Li+/Na+ assays, then cleave His6-SUMO-LiSPER to release native LiSPER peptide.

## Why This Matters

Imidazole, nickel, salt, and incompatible pH can reduce cleavage efficiency or contaminate ion-binding measurements.

## Cleavage Design Check

The current plasmid design places each LiSPER peptide immediately after the Smt3 SUMO C-terminal `GG`.

```text
His6 - Smt3 SUMO - GG | LiSPER peptide
```

SUMO protease cleavage at this junction should release the native LiSPER peptide without His tag, SUMO residues, or vector-derived C-terminal residues.

Expected gel interpretation:

| Species | Approximate size | Gel visibility |
|---|---:|---|
| His6-SUMO-LiSPER fusion | ~13.2-13.8 kDa | Should be visible. |
| His6-SUMO after cleavage | ~12 kDa | Should be visible as the main post-cleavage protein band. |
| Native LiSPER peptide | ~1.0-1.6 kDa | May be weak or invisible by routine stain. |

## Step-by-Step Workflow

1. Pool purified His6-SUMO-LiSPER fusion fractions.
2. Buffer exchange into SUMO-protease-compatible cleavage buffer.
3. Measure or estimate fusion concentration.
4. Set up small analytical cleavage test first.
5. Add SUMO protease at recommended enzyme:substrate ratio.
6. Incubate under recommended temperature/time.
7. Analyze pre-cleavage and post-cleavage samples by gel.
8. Scale cleavage only after analytical cleavage works.

## Analytical Cleavage Setup

Before scaling, test a small reaction:

1. Prepare a no-protease control and a SUMO-protease reaction.
2. Incubate under the protease vendor's recommended condition.
3. Run pre-cleavage, no-protease, and protease-treated samples side by side.
4. Estimate cleavage by loss of the fusion band and appearance/enrichment of the SUMO-sized band.
5. Do not require visible native peptide on gel before proceeding; confirm peptide later by MS/HPLC or recovery assay.

## Expected Outcome

- Fusion band decreases.
- His6-SUMO band appears.
- Native LiSPER peptide may not be visible by ordinary gel because it is only ~1-2 kDa.

## Common Failure Modes

| Problem | Likely cause | Solution |
|---|---|---|
| No cleavage | wrong buffer or inactive protease | Verify protease on control substrate; buffer exchange again. |
| Partial cleavage | insufficient time/protease | Increase time or protease ratio. |
| Protein precipitates | buffer or concentration issue | Lower concentration, adjust salt/pH, cleave colder. |
| Peptide not visible | expected for small peptides | Use LC-MS/MALDI or downstream recovery assay. |

## Records To Keep

- Fusion concentration estimate.
- Buffer composition.
- Protease lot and amount.
- Cleavage time and temperature.
- Gel image.
- Percent cleavage estimate if possible.
