# Construct Design Implications from the Whole-Cell Assay Plan

This file translates assay requirements into future eCPX plasmid-design constraints. It does not design plasmids.

## Assay-First Design Principle

The future eCPX constructs should be designed to satisfy two needs simultaneously:

1. Display LiSPER peptides on the outside of E. coli in a way that preserves Li+/Na+ binding.
2. Allow independent verification that surface display occurred before interpreting binding data.

## Detection Tag Requirement

A detection tag is recommended.

Why:

- Whole-cell Li uptake cannot be interpreted if display level is unknown.
- Flow cytometry or immunostaining is the most direct way to compare display across candidates.
- Display-normalized uptake may help distinguish poor binding from poor expression/display.

Risk:

- A charged or bulky tag may alter Li+/Na+ binding or nonspecific ion adsorption.

Design implication:

- Use a small epitope tag rather than a large fluorescent protein for first-generation constructs.
- Include an empty eCPX scaffold with the same tag.
- Include LiA3-Ref LiSPER with the same tag and linker context.

## Detection Tag Placement

Tag placement must respect eCPX topology and LiSPER binding logic.

Recommended logic:

- Place the detection tag at a position that remains surface-exposed but is spatially separated from the LiSPER peptide.
- If the tag must be near LiSPER, separate it with a flexible Gly/Ser linker.
- Avoid placing His-tags, polyacidic tags, polybasic tags, or metal-binding tags next to LiSPER in the displayed region.

Reason:

- His-rich or charged tags can bind metal ions or alter local electrostatics, confounding Li+/Na+ selectivity.

## Linker Requirement

Flexible linkers are recommended.

Recommended linker properties:

- Gly/Ser-rich.
- Short initial set, such as 1-2 linker lengths, to avoid overcomplicating the first library.
- No extra Asp/Glu/His/Cys clusters unless intentionally tested.

Why:

- LiSPER peptides are short and flexible; they may need spacing from the OmpX scaffold to access ions.
- Linkers reduce steric interference from the scaffold and detection tag.

Design implication:

- Keep linker sequence identical across candidates wherever possible.
- If testing linker length, use the same candidate across linkers rather than changing all variables at once.

## Live vs Fixed Cell Compatibility

The assay plan recommends testing both live and chemically fixed cells.

Construct implications:

- The displayed peptide and epitope tag should tolerate mild fixation.
- Avoid detection strategies requiring live-cell enzymatic activity.
- Avoid constructs where binding interpretation depends on active transport or metabolism.

Controls:

- Live empty scaffold.
- Fixed empty scaffold.
- Live LiA3-Ref.
- Fixed LiA3-Ref.
- Heat-killed control as stress/nonliving comparator.

## Plasmid-Encoded Controls Required

Future plasmid set should include:

| Construct class | Purpose |
|---|---|
| Empty eCPX scaffold with detection tag | Measures scaffold and tag background. |
| eCPX-LiA3-Ref | Controls for peptide length/context without Li-binding motif. |
| eCPX-LiSPER candidates | Tests candidate-specific Li/Na selectivity. |
| Positive LBP display construct, if feasible | Confirms assay can detect lithium-binding behavior. |
| Optional non-display tagged construct | Helps distinguish surface display from total expression. |

Non-plasmid controls still required:

- non-displaying host cells,
- no-cell blanks,
- buffer blanks,
- killed-cell controls.

## Features to Avoid

Avoid these design features in the first-generation eCPX plasmids:

- His6 tag in the surface-exposed binding region.
- Large fluorescent proteins fused near LiSPER.
- Strongly acidic/basic detection tags near LiSPER.
- Cys-rich tags or motifs that may bind metals or form uncontrolled disulfides.
- Linkers containing EDTA-like chelating motifs or repeated His/Asp/Glu clusters.
- Different tags/linkers for different candidates in the same comparison set.
- Constructs that require sodium-containing buffers for detection or induction during the binding step.

## Display Verification Strategy Built Into Construct Design

Future constructs should support:

1. Flow cytometry:
   - epitope tag accessible on intact cells,
   - same tag across candidates,
   - fluorescence signal separable from autofluorescence.
2. Immunofluorescence microscopy:
   - surface-localized staining pattern.
3. Protease accessibility:
   - tag or display region should be externally accessible.
4. Western/dot blot:
   - total expression confirmation.

## How Assay Design Guides Construct Priority

First-generation construct set should prioritize interpretability:

1. Empty eCPX scaffold.
2. LiA3-Ref peptide.
3. LiD3-Core.
4. LiND-Hybrid.
5. LiD3-Flex.
6. LiLC-1.
7. Optional known lithium-binding peptide positive control.

Only after the assay works should the full final 8-candidate display panel be built.

## Key Design Question for Future Plasmid Work

Before plasmid design, decide:

- exact eCPX insertion site/topology,
- tag identity and tag position,
- linker sequence and length,
- whether constructs are optimized for live-cell display, fixed-cell display, or both,
- which minimal control plasmids are required for the first assay.

The assay plan makes one point clear: future plasmids should be designed for measurable, normalized, and controllable ion-binding experiments, not merely for surface expression.
