# LiSPER Whole-Cell Assay Decision Matrix

## Core Decisions

| Decision | Recommended choice | Why | Risk | Mitigation |
|---|---|---|---|---|
| Primary validation format | Live and chemically fixed cells side-by-side | Separates true surface binding from physiology/metabolism. | Fixation may damage display. | Compare display signal and binding before/after fixation. |
| Final quantitative format | Fixed cells if binding is retained | Better reproducibility and lower biological variability. | Reduced peptide flexibility. | Keep live-cell data as comparator. |
| Heat inactivation | Control only | Heat can denature eCPX/LiSPER. | False negative. | Do not use as main assay format. |
| Buffer | HEPES or PIPES adjusted with KOH | Low sodium background and biological compatibility. | Buffer-metal interactions or contamination. | Use high-purity reagents and blanks. |
| Osmotic support | KCl, not NaCl | Maintains cells without adding sodium background. | K+ may affect binding weakly. | Include KCl-only controls. |
| Separation | Centrifugation | Lowest cost and most accessible. | Pellet disturbance, carryover. | Validate with filtration subset. |
| Main readout | ICP-OES | Publishable Li/Na quantification at practical concentrations. | Facility access/cost. | Batch samples and outsource if needed. |
| Screening readout | Li/Na kits or small outsourced ICP batch | Fast candidate triage. | Matrix interference. | Confirm all hits by ICP. |
| Selectivity condition | Mixed Li+Na solution | Directly tests Li over Na. | High sodium matrix can exceed kit range. | Dilute samples or use ICP. |
| Application-like condition | Synthetic raffinate after Level 2 success | Tests industrial relevance. | Residual metals may dominate binding. | Add residual metals stepwise. |

## Assay Level Comparison

| Feature | Level 1 screening | Level 2 quantitative validation | Level 3 application-like raffinate |
|---|---|---|---|
| Purpose | Rank candidates quickly | Publishable selectivity evidence | Deployment-relevant stress test |
| Candidates | All 10 plus controls | Top 2-4 plus controls | Top 1-2 plus controls |
| Cell format | Live, optional fixed | Live and fixed | Fixed preferred, live comparator optional |
| Display QC | Tag staining subset | Flow cytometry every replicate | Before/after exposure |
| Matrix | Simple Li/Na buffer | Concentration/time/pH matrix | Li + high Na + residual metals |
| Readout | Kit or small ICP batch | ICP-OES/ICP-MS | ICP-OES/ICP-MS |
| Main metric | Percent Li removal vs controls | Uptake and selectivity ratio | Selectivity retained under competition |
| Output | Go/no-go candidate shortlist | Publication-quality data | Translation feasibility data |

## Analytical Method Decision

| Analytical method | Cost | Accessibility | Li/Na suitability | Publication strength | Recommendation |
|---|---:|---:|---:|---:|---|
| Lithium colorimetric kit | Low-medium | High | Medium | Low-medium | Use only for Level 1. |
| Sodium colorimetric kit | Low-medium | High | Medium | Low-medium | Use only for Level 1 and controls. |
| Conductivity | Low | High | Low | Low | Sanity check only. |
| Flame photometry | Low-medium | Medium | Medium | Medium | Backup if available. |
| Ion chromatography | Medium | Medium | Medium-high | Medium-high | Good if a local method exists. |
| ICP-OES | Medium | Medium-high through core/outsourcing | High | High | Preferred validation method. |
| ICP-MS | High | Medium through core/outsourcing | Very high | High | Use for trace metals/low Li, not routine screens. |

## Cell Format Decision

| Format | Pros | Cons | Use |
|---|---|---|---|
| Live cells | Tests authentic surface display; easy from induction culture. | Metabolism, ion transport, growth state, leakage, biosafety variability. | Initial biological relevance. |
| Mildly fixed cells | More stable, less metabolic artifact, easier batching. | Fixation can alter proteins or surface charge. | Preferred if validated. |
| Heat-killed cells | Simple nonliving control. | Denatures display proteins and changes envelope. | Negative/stress control only. |
| Inactivated immobilized cells | Relevant to future deployment. | Requires extra method development. | Later bridge after core assay works. |

## Go/No-Go Criteria

Advance a LiSPER candidate from Level 1 to Level 2 if:

- Li uptake is above empty eCPX and LiA3-Ref controls.
- Na uptake is low in Na-only and mixed Li+Na conditions.
- Display signal is detectable and not grossly toxic to cells.
- Replicates agree qualitatively.

Advance from Level 2 to Level 3 if:

- Li/Na selectivity is statistically above controls.
- Uptake is measurable by both depletion and pellet-associated ion analysis.
- Binding is not explained by OD600, cell death, or display level alone.
- At least one nonliving format retains meaningful Li selectivity.

Advance toward construct optimization if:

- The assay shows that display level, linker geometry, or detection tag placement materially affects binding.

