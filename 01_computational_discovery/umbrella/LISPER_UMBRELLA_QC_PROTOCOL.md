# LiSPER umbrella-sampling evidence protocol

This protocol has **no automatic scientific PASS/FAIL gate**. The former fixed
`1.0 kJ/mol` and `25% of |Delta Delta G|` rules were LiSPER heuristics, not
GROMACS or umbrella-sampling theory, and are retired.

## Scientific scope

Umbrella sampling reconstructs a potential of mean force (PMF) along the chosen
reaction coordinate. Reliability depends on equilibrium sampling within every
window, connected overlap between windows, adequate sampling of slow coordinates,
and an estimator consistent with the stated thermodynamic quantity. A smooth PMF
or a small software-generated error bar alone does not establish reliability.

The current distance-coordinate profiles support **diagnostic paired state
contrasts only**. They do not support claims of absolute or standard binding free
energy until restraint, coordinate-measure/Jacobian, state-volume, and standard-
state corrections are explicitly derived and validated.

## Evidence that must be reported

1. **Reaction-coordinate and state definition**
   - Use the same locked chemical site, pull geometry, force constant, coordinate
     range, and analysis plan for LiCl and NaCl.
   - Record bound/reference regions and their physical rationale explicitly. Do
     not derive them automatically from a fixed cutoff or the last `0.30 nm`.
   - Selectivity is not calculated from arithmetic means of PMF values. The
     diagnostic estimator is the difference between Boltzmann-integrated region
     probability contrasts, with its non-standard-state scope stated.
2. **Histogram overlap**
   - Publish the per-window histograms and report empty bins, support counts, and
     any adjacent window pair with zero common support.
   - Do not convert overlap into an invented universal numeric threshold.
     GROMACS requires inspection of whether histograms sufficiently overlap.
3. **Time correlation and uncertainty**
   - Run `gmx wham -ac` and retain per-window integrated autocorrelation-time
     estimates.
   - Use the GROMACS trajectory bootstrap with those IACT estimates as one
     conditional uncertainty diagnostic. State its limitation: finite sampling
     can miss unsampled slow modes and underestimate uncertainty.
   - Propagate bootstrap uncertainty through the declared state estimator by
     evaluating every bootstrap PMF, not by averaging pointwise PMF standard
     deviations.
4. **Time dependence**
   - Report cumulative and disjoint time-block PMFs/contrasts. Contiguous halves
     are time blocks, not independent replicas.
   - Do not assign a universal kJ/mol cutoff. Inspect whether estimates stabilize
     with additional sampling and whether observed changes are compatible with
     their uncertainty.
5. **Independent sampling**
   - Report the number of independent replicas per window and between-replica
     variation. One trajectory per window cannot establish reproducibility or
     reveal all orthogonal slow modes.
   - Add independent replicas from independently equilibrated/seeded starts when
     the existing data cannot characterize between-replica variation.
6. **Sensitivity and limitations**
   - Report sensitivity to bin count, analysis start time, region definition, and
     bootstrap treatment.
   - Report WHAM warnings, failed calculations, PBC limits, and any evidence that
     the reaction coordinate omits important slow degrees of freedom.

## Decisions

Analysis software writes measurements and limitations only. It exits non-zero for
missing, malformed, mismatched, or mathematically invalid inputs—not because a
scientific metric crossed a project-invented threshold.

The Delta G promotion hold remains active until a method review documents:

- the exact estimand and claim scope;
- physical state definitions and coordinate corrections;
- connected overlap and correlation-aware analysis;
- time-dependent and independent-replica evidence;
- sensitivity analyses; and
- a claim whose uncertainty is reported rather than converted to a fake verdict.

Scale-up decisions use that documented evidence and scientific judgment. They are
not unlocked by a script-generated label.

The operational preregistration for independently initialized campaigns and
sequential evidence-driven sampling is in
[`../pmf/INDEPENDENT_REPLICA_PLAN.md`](../pmf/INDEPENDENT_REPLICA_PLAN.md).

## Primary and official sources

- GROMACS, [`gmx wham` documentation](https://manual.gromacs.org/2024.5/onlinehelp/gmx-wham.html): histogram overlap, IACT weighting, bootstrap methods, and explicit warnings about underestimated errors.
- Hub, de Groot & van der Spoel, [*J. Chem. Theory Comput.* 6, 3713-3720 (2010)](https://doi.org/10.1021/ct100494z): GROMACS WHAM implementation, autocorrelation, and bootstrap error analysis.
- Kästner, [*WIREs Comput. Mol. Sci.* 1, 932-942 (2011)](https://doi.org/10.1002/wcms.66): umbrella-sampling theory and window overlap.
- Woo & Roux, [*PNAS* 102, 6825-6830 (2005)](https://doi.org/10.1073/pnas.0409005102): PMF-based binding free energy with explicit restraint/state treatment.
- Deng & Roux, [*J. Phys. Chem. B* 113, 2234-2246 (2009)](https://doi.org/10.1021/jp807701h): standard binding free-energy definitions and corrections.
