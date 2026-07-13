# LiSPER-Specific Umbrella and PMF QC Protocol

This protocol estimates Li/Na selectivity for flexible peptide binding sites. Window count and analysis range are therefore determined from the observed reaction-coordinate distributions and a physically justified unbound plateau, not copied from a generic GROMACS example.

## Current implementation boundary

- Fresh campaigns use `paired_site_manifests/<candidate>.tsv` so Li and Na are compared at the same named peptide site.
- The fixed 2.0 nm extension supplies a shared endpoint reference region; it is not claimed to prove a physical bulk plateau.
- The output is a radially corrected, endpoint-referenced PMF binding difference, not a 1 M standard binding free energy.
- Convergence and overlap quantities are reported as diagnostics. They are not universal binary promotion gates.

## Paired design

- Treat each candidate as a paired LiCl/NaCl block.
- Keep reaction-coordinate definition, `0.075 nm` spacing, `0.5 ns` equilibration, `2.0 ns` production, guard-window count, WHAM binning, burn-in, time blocks, and bound/reference regions identical within a pair.
- Do not compare protocols with different usable coordinate ranges. Extend the shorter condition to the shared range.

## Window design

- Generate the analysis range from the candidate's representative bound distance to a candidate-specific unbound plateau.
- Add three sequential guard windows beyond the intended reference endpoint. Guards stabilize endpoint overlap and are excluded from Delta G integration/region estimates.
- Before full production, require neighboring-window overlap throughout the bound basin, transition, and reference plateau. Add a midpoint window where adjacent distributions do not overlap; do not globally reduce spacing unless failures are widespread.
- Stop extending only when the reference region is flat in both ions and remains inside the PBC-safe limit.

## Reporting contract

The table is generated whenever all required GROMACS windows finish and `gmx wham` produces a profile. The report includes, without invented pass/fail thresholds:

1. histogram support and weak-bin count;
2. endpoint-region PMF span;
3. early/late difference;
4. burn-in sensitivity;
5. bootstrap uncertainty, explicitly labeled as conditional on the sampled histograms;
6. identical paired bound/reference regions and the sign convention.

A GROMACS fatal error, missing window, or failed WHAM calculation is a computational blocker because no estimate exists. Large or inconsistent diagnostics do not erase the estimate; they are shown as warnings and limit how strongly it can be interpreted.
