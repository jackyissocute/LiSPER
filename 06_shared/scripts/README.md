# Scripts

Reusable project scripts for preparation, conversion, analysis, plotting, and reporting.

## Promotion Rule

```mermaid
flowchart LR
    A["One-off command"] --> B["01_computational_discovery/analysis/"]
    B --> C["Repeated twice"]
    C --> D["scripts/"]
    D --> E["Documented protocol"]
```

Keep scripts small, named by task, and parameterized enough to reuse across candidates and ion conditions.
