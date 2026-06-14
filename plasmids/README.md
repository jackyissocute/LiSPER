# Plasmids

Vector maps, construct planning, codon optimization records, and cloning notes.

## Current Vector Map

| File | Purpose |
|---|---|
| `vector_maps/pET28a_plus.dna` | Uploaded pET28a(+) map for future expression design |

## Construct Flow

```mermaid
flowchart LR
    A["Selected peptide"] --> B["Gene design"]
    B --> C["Codon optimization"]
    C --> D["pET28a(+) cloning"]
    D --> E["Expression construct"]
```

This folder should eventually connect computational candidate IDs to wet-lab construct IDs.
