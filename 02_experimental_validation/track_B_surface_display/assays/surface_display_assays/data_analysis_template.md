# LiSPER Whole-Cell Binding Data Analysis Template

Use this file as the analysis specification for spreadsheets, notebooks, or scripts.

## Required Raw Data Columns

| Column | Description |
|---|---|
| `experiment_id` | Unique experiment identifier. |
| `date` | Experiment date. |
| `operator` | Person performing assay. |
| `candidate` | LiSPER candidate or control. |
| `construct_type` | Candidate display, empty scaffold, non-display, LiA3-Ref, positive control. |
| `cell_format` | Live, fixed, heat-killed. |
| `biological_replicate` | Independent culture number. |
| `technical_replicate` | Technical replicate number. |
| `display_signal_mfi` | Flow cytometry median fluorescence intensity, if available. |
| `display_positive_percent` | Percent display-positive cells, if available. |
| `od600_equivalent` | OD600 equivalent used in assay. |
| `dry_cell_weight_mg` | Dry cell weight equivalent, if measured. |
| `buffer` | Buffer identity and pH. |
| `pH` | Assay pH. |
| `temperature_C` | Incubation temperature. |
| `incubation_min` | Binding time. |
| `initial_Li_mM` | Initial Li concentration. |
| `initial_Na_mM` | Initial Na concentration. |
| `supernatant_Li_mM` | Li measured after incubation. |
| `supernatant_Na_mM` | Na measured after incubation. |
| `wash_Li_mM` | Li in wash, if collected. |
| `wash_Na_mM` | Na in wash, if collected. |
| `pellet_release_Li_mM` | Li released/digested from pellet. |
| `pellet_release_Na_mM` | Na released/digested from pellet. |
| `sample_volume_mL` | Binding reaction volume. |
| `elution_volume_mL` | Elution/digestion volume. |
| `notes` | Observations: precipitation, pellet loss, turbidity, abnormal OD. |

## Unit Conversions

Moles in supernatant:

```text
Li_supernatant_umol = supernatant_Li_mM * sample_volume_mL
Na_supernatant_umol = supernatant_Na_mM * sample_volume_mL
```

Because 1 mM x 1 mL = 1 umol.

Moles initially added:

```text
Li_initial_umol = initial_Li_mM * sample_volume_mL
Na_initial_umol = initial_Na_mM * sample_volume_mL
```

Moles released from pellet:

```text
Li_pellet_umol = pellet_release_Li_mM * elution_volume_mL
Na_pellet_umol = pellet_release_Na_mM * elution_volume_mL
```

## Core Metrics

### Percent Li Removal

```text
percent_Li_removal = 100 * (Li_initial_umol - Li_supernatant_umol) / Li_initial_umol
```

### Percent Na Removal

```text
percent_Na_removal = 100 * (Na_initial_umol - Na_supernatant_umol) / Na_initial_umol
```

### Li Uptake by Depletion

```text
Li_uptake_depletion_umol = Li_initial_umol - Li_supernatant_umol - Li_wash_umol
```

If wash is not measured:

```text
Li_uptake_depletion_umol = Li_initial_umol - Li_supernatant_umol
```

### Na Uptake by Depletion

```text
Na_uptake_depletion_umol = Na_initial_umol - Na_supernatant_umol - Na_wash_umol
```

### Uptake Normalized by OD600

```text
Li_uptake_umol_per_OD = Li_uptake_umol / od600_equivalent
Na_uptake_umol_per_OD = Na_uptake_umol / od600_equivalent
```

### Uptake Normalized by Dry Cell Weight

```text
Li_uptake_umol_per_g_DCW = Li_uptake_umol / (dry_cell_weight_mg / 1000)
Na_uptake_umol_per_g_DCW = Na_uptake_umol / (dry_cell_weight_mg / 1000)
```

### Uptake Normalized by Display Level

If flow cytometry display signal is available:

```text
display_normalized_Li = Li_uptake_umol / (od600_equivalent * display_signal_mfi)
display_normalized_Na = Na_uptake_umol / (od600_equivalent * display_signal_mfi)
```

Alternative:

```text
display_normalized_Li = Li_uptake_umol / (od600_equivalent * display_positive_percent / 100)
```

Use display-normalized metrics only as secondary interpretation because fluorescence is not an absolute peptide copy number unless calibrated.

## Selectivity Metrics

### Li/Na Uptake Ratio

```text
Li_Na_uptake_ratio = Li_uptake_umol / Na_uptake_umol
```

If Na uptake is near zero, report as greater than a detection-limit-based lower bound rather than infinity.

### Selectivity Ratio Relative to Solution Composition

```text
selectivity_ratio = (Li_uptake_umol / Na_uptake_umol) / (Li_initial_umol / Na_initial_umol)
```

Interpretation:

- `selectivity_ratio > 1`: cells enrich Li relative to solution composition.
- `selectivity_ratio = 1`: no Li/Na preference beyond solution ratio.
- `selectivity_ratio < 1`: Na is favored relative to Li.

### Li Enrichment Factor Over Empty Scaffold

```text
Li_enrichment_vs_empty = Li_uptake_candidate / Li_uptake_empty_scaffold
```

### Li/Na Selectivity Improvement Over Empty Scaffold

```text
selectivity_improvement = selectivity_ratio_candidate / selectivity_ratio_empty_scaffold
```

## Mass Balance

For quantitative validation:

```text
Li_mass_balance_percent = 100 * (Li_supernatant_umol + Li_wash_umol + Li_pellet_umol) / Li_initial_umol
Na_mass_balance_percent = 100 * (Na_supernatant_umol + Na_wash_umol + Na_pellet_umol) / Na_initial_umol
```

Acceptable pilot target:

- 80-120% mass balance during method development.
- 90-110% for publication-quality claims, if practical.

## Recommended Statistical Comparisons

Primary comparisons:

- Candidate vs empty eCPX scaffold.
- Candidate vs LiA3-Ref peptide.
- Candidate vs non-displaying E. coli.

Recommended tests:

- For simple candidate ranking: mean +/- SD across biological replicates.
- For publication: ANOVA or linear model with candidate/control and condition as factors, followed by corrected pairwise comparisons.
- Report effect sizes, not only p-values.

## Interpretation Rules

Strong candidate:

- Li uptake above all controls.
- Na uptake close to controls or lower.
- Selectivity ratio greater than controls.
- Reproducible across biological replicates.
- Display signal present and not dramatically lower than controls.

Ambiguous candidate:

- Li uptake above controls but Na uptake also high.
- Good depletion but poor pellet recovery.
- Strong binding in live cells but not fixed cells.
- High residual metal uptake in raffinate matrix.

Failed candidate:

- No Li uptake above empty scaffold.
- Li and Na uptake both match non-displaying cells.
- Display is absent or severely toxic.
- Apparent Li loss occurs in no-cell or filter blanks.

