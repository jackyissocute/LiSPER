# Data

Project data that is not tied to one specific workflow folder.

## Data Policy

| Folder | Rule |
|---|---|
| `raw/` | Original data exactly as generated or received |
| `processed/` | Cleaned, transformed, or analysis-ready data |

Avoid editing raw data in place. Put transformed versions in `processed/` and document the transformation in `../analysis/` or `../../06_project_operations/scripts/`.
