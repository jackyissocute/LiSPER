# Computational discovery

This folder contains the eight peptide sequences, structural models, original
CHARMM-GUI systems, and the current free-energy method.

## Current workflow

Snapshot: `2026-07-13 22:06 CST`.

`sequence ensemble -> model validation -> mixed-ion site discovery -> matched bulk/site Li-to-Na cycle -> standard-state affinity -> experimental comparison`

The original CHARMM-GUI inputs are retained as provenance. Derived trajectory,
clustering, and free-energy outputs are generated only by the current method
and must carry input hashes, engine versions, independent seeds, and declared
estimands.

| Folder | Role |
|---|---|
| `sequences/` | Candidate identities and design rationale |
| `esmfold/` | Structural starting models |
| `md/` | CHARMM-GUI LiCl/NaCl system inputs |
| `free_energy/` | Model validation and binding/selectivity calculations |
| `analysis/` | Final evidence tables after estimators are complete |

Current scientific result count: `0/8` peptide affinity rows and `0/8`
selectivity rows.
