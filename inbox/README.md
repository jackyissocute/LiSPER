# Inbox

Temporary drop zone for files that need classification.

```mermaid
flowchart LR
    A["Downloaded file"] --> B["inbox/"]
    B --> C["Inspect"]
    C --> D["Move to permanent folder"]
    D --> E["Update README or manifest"]
```

## Put Here

| File Type | Final Destination Usually |
|---|---|
| New papers | `literature/` |
| CHARMM-GUI archives | `charmm-gui/<condition>/` |
| ESMFold downloads | `esmfold/` |
| Plasmid/vector files | `plasmids/` |
| Screenshots | `figures/` or condition metadata |
| One-off notes | `docs/`, `protocols/`, or `manuscript/` |

This folder should usually be empty after processing.
