# eCPX display plasmid design for BL21(DE3)

## Recommended architecture

Use a pET-28a(+)-type backbone with a T7/lac promoter, kanamycin selection, and IPTG induction. The core fusion should be:

```text
T7 promoter – lac operator – RBS – His6 – eCPX – flexible linker – DADGPGDPDAG – stop – T7 terminator
```

A practical first construct is:

```text
His6–eCPX–(Gly-Ser)2–DADGPGDPDAG
```

The peptide is placed at the eCPX C terminus because eCPX was engineered as a circularly permuted OmpX scaffold with surface-exposed N- and C-termini, and the eCPX variant improved outer-membrane localization and peptide presentation relative to the parent scaffold [^1]. The short (Gly-Ser)2 linker should reduce steric restriction while keeping the 11-residue peptide close to the bacterial surface; retain a no-linker version as a backup if the peptide must remain maximally proximal to the scaffold.

## Tag placement and cloning logic

The N-terminal His6 tag is suitable for checking expression and, if accessible, nickel-affinity capture of the fusion. Because eCPX was designed with surface-exposed N- and C-termini, the His6 tag may also be exposed on intact cells [^1]; therefore, do not assume that whole-cell Ni binding reports total expression. Confirm expression by anti-His western blot of whole-cell lysate and confirm external localization separately by antibody labeling of intact, non-permeabilized cells.

Use the native pET-28a(+) N-terminal His6/thrombin region only if its reading frame and the supplied eCPX sequence have been verified. Otherwise, synthesize the complete fusion as one codon-optimized insert for *E. coli* and clone it between the vector's NdeI and XhoI sites, preserving the start codon, reading frame, and stop codon. Avoid adding a second stop codon inside the insert. These are construct-design recommendations; the exact DNA sequence should be generated only after the eCPX allele, vector map, restriction sites, and desired protease-cleavage sites are confirmed.

Suggested construct set:

1. **Primary:** His6–eCPX–(G4S)2–DADGPGDPDAG.
2. **Proximity control:** His6–eCPX–DADGPGDPDAG.
3. **Display-negative control:** His6–eCPX with no peptide extension.
4. **Surface-labeling control:** His6–eCPX–(G4S)2–a short antibody-recognized epitope, if an established detection reagent is available.

## Expression host and induction pilot

Transform the plasmid into BL21(DE3) and retain a non-induced culture as a negative control. Run a small induction matrix rather than starting with a single condition: low, intermediate, and high IPTG; two post-induction temperatures; and at least two harvest times. Lower temperature and weaker induction are reasonable first choices for an outer-membrane fusion because excessive synthesis can overload export/folding pathways and reduce viability or apparent display; this is an optimization hypothesis to test rather than a guaranteed condition. Keep antibiotic selection identical across all conditions.

Measure four outputs separately:

- total fusion abundance by anti-His western blot;
- intact-cell surface accessibility using fluorescent anti-His or anti-peptide antibody without permeabilization;
- total-cell fluorescence after permeabilization, if needed;
- cell density and viability.

A successful condition is not simply the one with the strongest western-band signal: the decision metric is high surface-accessible signal with acceptable growth and low signal in the eCPX-only control. eCPX supports display from both surface-exposed termini and has been used to present diverse peptides and mini-proteins on *E. coli* [^1].

## Verification plan

1. Sequence-verify both insert junctions and the entire peptide-coding region; the peptide is acidic and glycine-rich, so confirm that no synthesis or sequencing frameshift occurred. This is a construct-quality control rather than a literature-derived benchmark.
2. Check the expected fusion size by SDS–PAGE and anti-His western blot. Interpret size cautiously because outer-membrane proteins can migrate anomalously.
3. Label intact, non-permeabilized cells with anti-His or an anti-peptide reagent, wash, and quantify by flow cytometry or whole-cell fluorescence.
4. Repeat labeling after membrane permeabilization. Surface display should produce a higher intact-cell signal than the eCPX-only negative control, while permeabilization can reveal intracellular or total fusion.
5. Confirm that the peptide is exposed rather than merely associated with lysed cells by testing culture supernatant, applying a viability/dye-exclusion gate, and including a no-primary-antibody control.

## Main risks and mitigations

- **Poor outer-membrane localization:** reduce induction strength, lower the induction temperature, shorten the induction window, or compare the no-linker and (G4S)2 designs.
- **Proteolysis of the peptide or linker:** compare the full-length anti-His band with surface signal; use a protease-deficient host only if the chosen strain and downstream application permit it.
- **His tag is inaccessible or misleading:** use anti-peptide detection as the primary surface assay and use anti-His mainly for lysate expression.
- **Display signal reflects damaged cells:** gate on intact cells, monitor viability, and compare non-permeabilized with permeabilized staining.
- **Peptide conformation is not preserved:** this sequence is short, acidic, and glycine-rich, so interpret positive binding as presentation of the linear sequence unless a conformational assay demonstrates otherwise.
- **Vector-specific frame errors:** verify the pET-28a map and insert junctions in the exact commercial vector before ordering DNA.

The most defensible first experiment is therefore a small IPTG/temperature/time matrix using the primary fusion, the eCPX-only control, and the no-linker variant, with anti-His western blot plus intact-cell anti-peptide flow cytometry as orthogonal readouts. The orthogonal surface-readout logic follows the demonstrated use of quantitative cell-surface display and labeling for eCPX constructs [^1].


[^1]: Rice & Daugherty, 2008. Directed evolution of a biterminal bacterial display scaffold enhances the display of diverse peptides. Protein engineering, design & selection : PEDS.