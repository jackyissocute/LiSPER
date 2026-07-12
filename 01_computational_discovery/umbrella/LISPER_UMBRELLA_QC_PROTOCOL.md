# LiSPER-Specific Umbrella and PMF QC Protocol

This protocol estimates Li/Na selectivity for flexible peptide binding sites. Window count and analysis range are therefore determined from the observed reaction-coordinate distributions and a physically justified unbound plateau, not copied from a generic GROMACS example.

## Current implementation boundary

- Delta G promotion is frozen until paired binding-site identity, regions, and the estimator are machine-locked.
- Existing V2/V3 campaigns chose donors independently and are diagnostic unless the paired audit explicitly rules them equivalent.
- Fresh campaigns require `paired_site_manifests/<candidate>.tsv`; the driver maps residue number/name/atom name into each topology and refuses a missing or mismatched manifest.
- Candidate-specific plateau selection and the central PASS evaluator are P2/P3 work. The current fixed 2.0 nm analysis extension must not be described as plateau-selected.

## Paired design

- Treat each candidate as a paired LiCl/NaCl block.
- Keep reaction-coordinate definition, `0.075 nm` spacing, `0.5 ns` equilibration, `2.0 ns` production, guard-window count, WHAM binning, burn-in, time blocks, and bound/reference regions identical within a pair.
- Do not compare protocols with different usable coordinate ranges. Extend the shorter condition to the shared range.

## Window design

- Generate the analysis range from the candidate's representative bound distance to a candidate-specific unbound plateau.
- Add three sequential guard windows beyond the intended reference endpoint. Guards stabilize endpoint overlap and are excluded from Delta G integration/region estimates.
- Before full production, require neighboring-window overlap throughout the bound basin, transition, and reference plateau. Add a midpoint window where adjacent distributions do not overlap; do not globally reduce spacing unless failures are widespread.
- Stop extending only when the reference region is flat in both ions and remains inside the PBC-safe limit.

## Reliability gate

A paired result is `PASS` only when both ions satisfy all gates over the declared analysis range:

1. No empty bins and no bins supported by only one window in the bound basin, transition, or reference plateau.
2. Reference plateau slope is indistinguishable from a practically flat profile: absolute change no greater than `1.0 kJ/mol` across the declared plateau.
3. Independent early/late production halves give bound-to-reference Delta G values within `1.0 kJ/mol`.
4. Burn-in variants are reported separately and agree within `1.0 kJ/mol`; they are not called time slices.
5. Bootstrap uncertainty is read from the `xydy` bootstrap profile. The conservative combined bound/reference uncertainty must be no more than `1.0 kJ/mol` and no more than 25% of the paired Li/Na effect once Delta Delta G is available.
6. Bound and reference regions have physical interpretations and are identical for paired LiCl/NaCl analysis.
7. Guard-only weak bins are documented but do not fail the result. Any warned bin inside the declared analysis range triggers `REPAIR`.

Thresholds are predeclared practical-resolution targets for this LiSPER comparison. They may be tightened after replicate evidence, but must not be relaxed after seeing a desired selectivity result.

## LiD3-Flex V3 guard repair

- Existing analysis endpoint: base window `026` (`2.0583 nm` NaCl; `2.20 nm` LiCl).
- Add guard windows `027-029` at the same `0.075 nm` spacing, sequentially initialized from the preceding completed guard.
- Keep the current base windows; do not restart or overwrite them.
- After both guard sequences finish, define one shared paired analysis endpoint no farther than the smaller condition's last base-window center, then run full, burn-in, independent-half, histogram, and bootstrap QC.
- The present NaCl warnings at `2.221-2.255 nm` are guard-edge diagnostics, not automatically acceptable: they become non-material only if they lie outside the shared declared reference region and all interior gates pass.
