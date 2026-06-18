# 06 Ni-NTA Purification Protocol

## Purpose

Purify His6-SUMO-LiSPER fusion protein through its N-terminal His6 tag.

## Why This Matters

SUMO cleavage and peptide recovery require enriched fusion protein. Contaminants, imidazole, and nickel carryover can interfere with downstream Li+/Na+ assays, so purification fractions must be tracked carefully.

## Inputs

- Clarified lysate.
- Ni-NTA resin or column.
- Bind/wash/elution buffers.
- SDS-PAGE or Tris-Tricine gel setup.

## Target and Fraction Logic

| Species | His tag? | Expected behavior |
|---|---|---|
| His6-SUMO-LiSPER fusion | Yes | Binds Ni-NTA and elutes with imidazole. |
| Host proteins | Mostly no | Mostly flow-through/wash, with some nonspecific binders. |
| Free native LiSPER peptide | No | Not expected before cleavage; after cleavage it should not bind Ni-NTA strongly. |

Expected fusion size is approximately 13.2-13.8 kDa. Use Tris-Tricine or high-percentage SDS-PAGE and include a low-molecular-weight marker.

## Step-by-Step Workflow

1. Equilibrate Ni-NTA resin with binding buffer.
2. Apply clarified lysate to resin.
3. Collect flow-through.
4. Wash resin with wash buffer.
5. Collect wash fractions.
6. Elute His6-SUMO-LiSPER with imidazole-containing elution buffer.
7. Analyze input, flow-through, wash, and elution by gel.
8. Pool fractions containing target fusion.
9. Buffer exchange pooled fusion before SUMO cleavage.

## Recommended Fraction QC

Run at minimum:

- input lysate,
- soluble flow-through,
- final wash,
- each elution fraction,
- pooled elution before buffer exchange.

Estimate fusion purity from the gel before cleavage. If the target band is weak or heavily contaminated, optimize expression/wash conditions before committing to peptide recovery.

## Expected Outcome

- Target fusion enriched in elution fractions.
- Reduced host-cell protein background.

## Common Failure Modes

| Problem | Likely cause | Solution |
|---|---|---|
| Target in flow-through | resin overloaded, poor binding, wrong pH | Reduce load, increase binding time, verify pH and imidazole. |
| Many contaminants | weak wash | Increase wash imidazole or wash volume. |
| Low elution | target insoluble/degraded | Check soluble lysate and expression. |
| Downstream assay contamination | imidazole/nickel carryover | Buffer exchange thoroughly before binding assays. |

## Fraction Tracking

Keep labeled aliquots:

- input lysate,
- flow-through,
- wash 1,
- wash 2,
- elution fractions,
- pooled elution.

## DKU Feasibility Tip

For first attempts, use small-scale batch Ni-NTA purification because it is easier to troubleshoot than a packed gravity column.
