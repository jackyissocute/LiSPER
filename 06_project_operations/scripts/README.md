# Scripts

Reusable project scripts for preparation, conversion, analysis, plotting, and reporting.

## Promotion Rule

```mermaid
flowchart TD
    accTitle: Script Promotion Rule
    accDescr: One-off analysis commands become reusable project scripts only after the workflow is repeated and documented.

    command["One-off<br/>command"]
    analysis["Discovery<br/>analysis"]
    repeat["Repeated<br/>twice"]
    scripts["Reusable<br/>script"]
    protocol["Documented<br/>protocol"]

    command --> analysis
    analysis --> repeat
    repeat --> scripts
    scripts --> protocol
```

Keep scripts small, named by task, and parameterized enough to reuse across candidates and ion conditions.
