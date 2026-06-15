# 09 Peptide QC, Storage, and Stability Protocol

## Purpose

Confirm peptide identity and develop storage conditions that preserve assay reliability.

## Why This Matters

Binding results are not interpretable if peptide identity, concentration, purity, or storage condition is unknown.

## Recommended QC

| QC method | Purpose |
|---|---|
| LC-MS or MALDI-TOF | Confirms peptide mass. |
| Analytical HPLC | Estimates purity if available. |
| Tris-Tricine gel | Tracks fusion/SUMO/protease but may miss native peptide. |
| ICP blank of peptide buffer | Detects Li/Na contamination before binding assays. |
| Conductivity or desalting check | Detects salt/imidazole carryover. |

## Concentration Estimation

LiSPER peptides may lack aromatic residues, so A280 is likely not useful.

Possible approaches:

- dry mass after lyophilization,
- HPLC peak calibration,
- amino-acid analysis if available,
- quantitative MS method if available,
- conservative estimate from starting fusion and cleavage/recovery yield.

## Storage Plan

| Storage format | Use |
|---|---|
| 4 C short term | Same-day or next-day handling only. |
| -80 C aliquots | Preferred for recovered peptide fractions. |
| Lyophilized aliquots | Best if cleanup buffer is compatible. |

Avoid repeated freeze-thaw cycles.

## Stability Test

1. Prepare matched aliquots.
2. Store at 4 C, -20 C, and -80 C if feasible.
3. Test at day 0, day 1, day 7, and day 30.
4. Measure peptide recovery/QC and a simple Li binding readout.

## Common Failure Modes

| Problem | Likely cause | Solution |
|---|---|---|
| Peptide concentration changes | adsorption or precipitation | Use low-bind tubes; test buffer and pH. |
| Binding varies by storage | degradation or aggregation | Use fresh aliquots and reduce freeze-thaw. |
| Li/Na background in peptide fraction | buffer contamination | Desalt and run ICP blanks. |

