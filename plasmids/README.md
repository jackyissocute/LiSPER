# Plasmids

Vector maps, construct planning, codon optimization records, and cloning notes.

## Current Vector Map

| File | Purpose |
|---|---|
| `vector_maps/pET28a_plus.dna` | Uploaded pET28a(+) map for future expression design |
| `vendor_ready_pet28a_idt/genbank/` | Text-source GenBank maps for the 10 LiSPER constructs |
| `vendor_ready_pet28a_idt/snapgene_dna/` | SnapGene `.dna` copies for visual inspection and editing |

## Construct Flow

```mermaid
flowchart LR
    A["Selected peptide"] --> B["Gene design"]
    B --> C["Codon optimization"]
    C --> D["pET28a(+) cloning"]
    D --> E["Expression construct"]
```

This folder should eventually connect computational candidate IDs to wet-lab construct IDs.
