# PMF Analysis

Future folder for potential-of-mean-force analysis, Delta G estimates, and Li+/Na+ selectivity ranking.

## Selectivity Equation

`Delta Delta G = Delta G(Li+) - Delta G(Na+)`

More negative Delta Delta G indicates stronger Li+ preference.

## Expected Outputs

| Output | Purpose |
|---|---|
| `pmf_li.tsv` | Li+ PMF curve |
| `pmf_na.tsv` | Na+ PMF curve |
| `delta_g_summary.tsv` | Per-condition free energies |
| `selectivity_summary.tsv` | Delta Delta G candidate ranking |
| convergence plots | Check whether PMFs are reliable |

```mermaid
flowchart TD
    accTitle: PMF Ranking Logic
    accDescr: PMF analysis compares Li and Na umbrella-sampling free energies to compute selectivity and rank candidate peptides.

    li_umbrella["Li+ umbrella<br/>sampling"]
    na_umbrella["Na+ umbrella<br/>sampling"]
    li_delta_g["Delta G<br/>Li+"]
    na_delta_g["Delta G<br/>Na+"]
    selectivity["Delta Delta G<br/>selectivity"]
    ranking["Candidate<br/>ranking"]

    li_umbrella --> li_delta_g
    na_umbrella --> na_delta_g
    li_delta_g --> selectivity
    na_delta_g --> selectivity
    selectivity --> ranking
```
