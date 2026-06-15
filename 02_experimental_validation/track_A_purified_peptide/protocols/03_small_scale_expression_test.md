# 03 Small-Scale Expression Test Protocol

## Purpose

Determine whether His6-SUMO-LiSPER fusion proteins express detectably and whether expression is soluble.

## Why This Matters

Track A depends on recovering enough fusion protein for cleavage and peptide assays. Small-scale testing prevents wasting time on a poor large-scale expression condition.

## Inputs

- Confirmed overnight culture.
- LB or TB medium with kanamycin.
- IPTG.
- Lysis buffer or simple sample-preparation reagents.
- SDS-PAGE or Tris-Tricine gel system.

## Suggested Initial Matrix

| Variable | Suggested values |
|---|---|
| IPTG | 0, 0.05, 0.1, 0.5 mM |
| Temperature | 16, 25, 30, 37 C |
| Time | 4 h, overnight |
| Fraction | total, soluble, insoluble |

For DKU undergraduate feasibility, begin with fewer conditions:

- 0.1 mM IPTG at 25 C overnight.
- 0.1 mM IPTG at 30 C for 4-6 h.
- uninduced control.

## Step-by-Step Workflow

1. Dilute overnight culture into fresh antibiotic medium.
2. Grow to mid-log phase.
3. Record OD600 at induction.
4. Add IPTG according to matrix.
5. Continue incubation under selected temperatures/times.
6. Harvest equal OD600-equivalent cells.
7. Prepare total-cell samples.
8. Lyse a matched aliquot to separate soluble and insoluble fractions.
9. Run gel optimized for ~13-14 kDa His6-SUMO-LiSPER fusion.
10. Compare induced vs uninduced and soluble vs insoluble.

## Expected Outcome

- A visible induced band near expected fusion size.
- Preferably much of the band appears in soluble fraction.

## Common Failure Modes

| Problem | Likely cause | Solution |
|---|---|---|
| No induced band | induction failed or expression too low | Verify host, IPTG, antibiotic, construct; use anti-His western if available. |
| Mostly insoluble | aggregation/inclusion bodies | Lower temperature, lower IPTG, shorter induction. |
| Strong degradation | proteolysis | Lower temperature, add protease inhibitors during lysis, shorten induction. |
| Band hard to see | small protein and stain sensitivity | Use Tris-Tricine/high-percentage gel and load normalized samples. |

## Decision Criteria

Advance a condition if:

- fusion band is detectable,
- soluble fraction is acceptable,
- cells grow reasonably,
- condition is simple enough to reproduce.

