# LiSPER project instructions

## Scientific figures

- Use `paper-narrative` for manuscript figure story and order,
  `scientific-visualization` for design, styling, integrity, provenance, and
  final export, and `scipilot-figure-skill` for supplementary layout QA/CJK.
  These skills share canonical directories under `~/.agents/skills`.
- Reuse `06_project_operations/scripts/analyze_selectivity.py` and its
  source-validation workflow. Preserve raw data, existing estimators, source
  references, and numerical transformations; do not change them for appearance.
- Preserve `Delta Delta G = Delta G(Li+) - Delta G(Na+)`: negative values mean
  Li+ preference. Preserve units, bootstrap SD definitions and propagation
  assumptions, and numerical sampling diagnostics.
- Describe current estimates as radially corrected, endpoint-referenced,
  within-protocol comparisons, not 1 M standard-state binding free energies.
- Candidates, trajectory frames, umbrella windows, and bootstrap draws are not
  automatically independent replicates. Do not invent raw replicates,
  significance tests, or confidence intervals from these counts.
- Prefer authoritative numerical products and validation results over stale
  stage READMEs. Keep sampling limitations and diagnostic warnings visible.
- Prioritize publication plots. Until a target journal is known, prepare
  provisional general figures; verify its current official requirements once
  the journal, article type, figure type, and submission phase are established.
- Missing evidence is a recommendation, not authorization to run new HPC jobs,
  spend compute allocation, delete source artifacts, or install dependencies.
