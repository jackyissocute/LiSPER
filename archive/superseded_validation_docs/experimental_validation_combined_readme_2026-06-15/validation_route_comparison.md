# Validation Route Comparison: Track A vs Track B

## Summary

Track A and Track B are complementary, not interchangeable.

| Route | Core question | Evidence type |
|---|---|---|
| Track A: purified peptide validation | Does the LiSPER peptide itself selectively recognize Li+ over Na+? | Molecular-recognition evidence. |
| Track B: surface-display validation | Can LiSPER remain functional when displayed on a biological surface? | Biological-deployment evidence. |

## Detailed Comparison

| Dimension | Track A: Purified Peptide | Track B: Surface Display |
|---|---|---|
| Scientific question answered | Intrinsic peptide Li+/Na+ recognition. | Function of LiSPER on a cell surface. |
| What it proves | Binding can be attributed directly to peptide sequence, if purification/QC are strong. | Displayed LiSPER can capture Li+ in a whole-cell format. |
| What it does not prove | Surface display, immobilized performance, industrial deployment. | Intrinsic peptide-only selectivity independent of scaffold/cell surface. |
| Strengths | Strong attribution; reviewer-friendly molecular evidence; links directly to computational design. | Application-relevant; tests accessibility, display, whole-cell capture, and deployable format. |
| Weaknesses | Small peptide recovery and quantification may be difficult; yield may be low. | Scaffold, tag, and cell-envelope effects complicate attribution. |
| Publication value | High for fundamental design/biochemistry. | High for synthetic biology/biotechnology validation. |
| Technical difficulty | Moderate-high due to SUMO cleavage, peptide recovery, and small-peptide QC. | Moderate-high due to display verification, cell controls, and ion-background management. |
| Cost | Medium; purification consumables plus MS/ICP can cost. | Medium; antibodies/flow cytometry plus ICP can cost. |
| Main risk | Technical recovery failure mistaken for peptide failure. | Apparent binding caused by scaffold/cell surface rather than LiSPER. |
| Reviewer acceptance | Strong if identity, purity, and controls are clear. | Strong if scaffold/tag/cell-surface controls are rigorous. |
| Best first subset | Control-Negative plus 2-4 top candidates. | Empty scaffold, Control-Negative, 2-4 top candidates. |
| Key readout | Li/Na binding by purified peptide. | Whole-cell Li/Na uptake normalized by cells and display level. |

## Reviewer Acceptance Logic

Track A addresses:

- "How do you know the peptide itself binds lithium?"
- "Could binding come from the tag, protein fusion, cell surface, or material support?"
- "Does computational design correspond to molecular behavior?"

Track B addresses:

- "Can the peptide function when deployed on a biological surface?"
- "Is surface expression accessible?"
- "Can whole cells capture Li+ over Na+?"
- "Is this plausible as a Bio-DLE precursor?"

## Risk Interpretation

Track A technical failure does not mean LiSPER science failed.

Examples:

- peptide yield too low,
- cleavage inefficient,
- peptide lost during cleanup,
- assay separation unsuitable for 1-2 kDa peptide.

These are production and recovery problems.

Track B success does not replace Track A.

Surface-display success may involve:

- scaffold geometry,
- local avidity,
- cell-envelope chemistry,
- altered peptide conformation.

This evidence is valuable, but it does not fully isolate peptide-intrinsic selectivity.

## Recommended Strategic Framing

Do not describe Track B as a backup. Use this framing:

```text
Track A validates LiSPER as a molecular recognition element.
Track B validates LiSPER as a biological deployment interface.
Together, they connect computational design to both mechanism and application.
```

## Practical Sequencing

Ideal order:

1. Continue Track A because plasmids already exist.
2. Develop Track B assay logic and controls before eCPX plasmid design.
3. Use early Track A outcomes to prioritize Track B candidates when possible.
4. Use Track B outcomes to inform future immobilized or whole-cell formats.

If Track A becomes technically delayed:

- Continue Track B as a parallel scientific route.
- Be explicit that Track B answers a different question.
- Avoid claiming purified-peptide molecular recognition until Track A data exist.

If Track B succeeds before Track A:

- Claim biological surface-display selectivity, not intrinsic peptide-only selectivity.
- Use Track B success to justify renewed effort on Track A or an immobilized-peptide Track C.

