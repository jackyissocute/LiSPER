# 04 Expression Optimization Protocol

## Purpose

Improve soluble His6-SUMO-LiSPER fusion yield before purification.

## Strategy

Optimize for usable soluble protein, not maximum total expression.

## Variables To Test

| Variable | Practical range |
|---|---|
| Induction temperature | 16, 20-25, 30 C |
| IPTG | 0.02-0.5 mM |
| Induction time | 4 h, 6 h, overnight |
| Medium | LB first; TB if yield is low |
| Harvest OD600 | 0.5-0.8 initial target |

## Step-by-Step Workflow

1. Choose top 2-4 conditions from small-scale expression test.
2. Repeat with biological duplicate cultures.
3. Normalize samples by OD600.
4. Assess total, soluble, and insoluble fusion.
5. Select the simplest condition with reproducible soluble expression.
6. Document final expression condition for each candidate.

## Expected Outcome

- A candidate-specific or shared expression condition suitable for 50-500 mL purification scale.

## Common Failure Modes

| Problem | Likely cause | Solution |
|---|---|---|
| High total but low soluble expression | folding burden | Lower temperature and IPTG. |
| Low biomass | induction too early or toxic | Induce later or reduce IPTG. |
| Candidate-to-candidate variability | peptide sequence affects expression | Optimize priority candidates individually. |
| No condition works | construct/host issue | Consider alternative host later; do not call peptide nonfunctional. |

## Records To Keep

- OD600 at induction and harvest.
- Temperature.
- IPTG.
- Induction time.
- Gel image.
- Solubility assessment.
- Selected condition.

