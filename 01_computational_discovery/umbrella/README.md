# Umbrella Sampling

Future folder for pulling/umbrella windows, run inputs, trajectories, and convergence checks.

## Entry Requirement

Umbrella sampling should start from representative structures selected after production-MD clustering.

```mermaid
flowchart TD
    accTitle: Umbrella Sampling Setup
    accDescr: Production trajectories are clustered to select representative structures, define reaction coordinates, and build umbrella windows.

    trajectory["Production<br/>trajectory"]
    clustering["Structural<br/>clustering"]
    representative["Representative<br/>structure"]
    coordinate["Reaction<br/>coordinate"]
    windows["Umbrella<br/>windows"]

    trajectory --> clustering
    clustering --> representative
    representative --> coordinate
    coordinate --> windows
```

## Recommended Metadata

| Field | Why It Matters |
|---|---|
| Candidate ID | Links umbrella result to design |
| Ion condition | LiCl or NaCl comparison branch |
| Representative structure path | Ensures reproducible starting state |
| Reaction coordinate | Defines ion-peptide separation metric |
| Window centers | PMF coverage |
| Force constants | Bias strength |
| Sampling length | Convergence interpretation |
