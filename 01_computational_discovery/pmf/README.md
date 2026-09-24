# PMF and selectivity analysis

All eight candidates have completed paired LiCl/NaCl PMF estimates. The authoritative values are in [selectivity_summary.tsv](selectivity_summary.tsv); [delta_g_summary.tsv](delta_g_summary.tsv) holds the 16 ion-level estimates. The [completed archive](../umbrella/analysis_archive_20260725/README.md) retains profiles, histograms, ACF/IACT evidence, bootstrap outputs, sensitivity variants, and logs.

`ΔΔG = ΔG(Li⁺) − ΔG(Na⁺)`. A negative estimate indicates nominal Li⁺ preference. These are **radially corrected, endpoint-referenced, within-protocol PMF binding differences**, not 1 M standard-state binding free energies and not measured adsorption capacities.

The paired uncertainty is propagated from the ion-level bootstrap SDs under the analysis workflow's assumptions. It is not a confidence interval or a biological-replicate estimate. Keep histogram overlap, endpoint span, time sensitivity, burn-in sensitivity, and autocorrelation diagnostics visible; do not convert them into an unsupported binary quality label. Some estimates have SD large enough that their sign remains uncertain.

Use [analyze_selectivity.py](../../06_project_operations/scripts/analyze_selectivity.py) and its source-validation workflow for figures or downstream summaries. Do not change raw profiles, numerical transformations, source references, or estimators for presentation.
