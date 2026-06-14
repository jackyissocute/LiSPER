# Inbox

Temporary drop zone for files that need classification.

```mermaid
flowchart LR
    A["Downloaded file"] --> B["06_shared/inbox/"]
    B --> C["Inspect"]
    C --> D["Move to permanent folder"]
    D --> E["Update README or manifest"]
```

## Put Here

| File Type | Final Destination Usually |
|---|---|
| New papers | `04_literature/` or a study folder under `03_industrial_translation/` |
| CHARMM-GUI archives | `01_computational_discovery/charmm-gui/<condition>/` |
| ESMFold downloads | `01_computational_discovery/esmfold/` |
| Plasmid/vector files | `02_experimental_validation/plasmids/` |
| Screenshots | `05_manuscript/figures/` or condition metadata |
| One-off notes | `06_shared/docs/`, `02_experimental_validation/protocols/`, or `05_manuscript/manuscript/` |

This folder should usually be empty after processing.
