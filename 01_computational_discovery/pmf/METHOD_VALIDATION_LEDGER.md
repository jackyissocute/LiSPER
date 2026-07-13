# LiSPER umbrella / PMF method-validation ledger

Status: active method review; no final Delta G or Delta Delta G is authorized.

This ledger separates three kinds of evidence:

1. **software semantics** — what GROMACS implements;
2. **statistical-mechanical method** — what the peer-reviewed derivation supports; and
3. **LiSPER design choice** — a system-specific parameter that must be measured or tested here.

A citation can support the first two. It cannot prove that a trajectory length,
window spacing, site definition, or reaction coordinate is adequate for LiSPER.

## Current evidence ledger

| Item | Current implementation | Evidence class and source | Live LiSPER evidence | Status / next action |
|---|---|---|---|---|
| Representative clustering | GROMOS, peptide RMSD, 0.20 nm cutoff | Algorithm: [Daura et al. 1999](https://doi.org/10.1002/(SICI)1521-3773(19990115)38:1/2%3C236::AID-ANIE236%3E3.0.CO;2-M) and [`gmx cluster`](https://manual.gromacs.org/2026.0/onlinehelp/gmx-cluster.html). Cutoff: LiSPER choice. | LiLC-1 top peptide clusters contain 4.15% (Li) and 1.95% (Na) of frames. | Cutoff/basin sensitivity and independently initialized basins required. |
| Pull coordinate | 3-D distance between the center of mass of five donor atoms and one tagged ion | GROMACS semantics: [pull code](https://manual.gromacs.org/2026.0/reference-manual/special/pulling.html). Site/group definition: LiSPER chemical hypothesis. | Analysis of 500--2200 ps from every window found off-site rebinding. Li windows 0, 4, and 5 and Na windows 2 and 4 spent more than 25% of frames within 0.30 nm of peptide oxygens outside the declared five-donor site. In Na window 4, that fraction was 100%, while contact with the declared donors was 0.6%. The Na trajectory is force-field-invalid but independently demonstrates that the coordinate does not geometrically prevent site exchange. | Current coordinate is rejected for a same-site dissociation claim. Compare restrained radial/path-coordinate designs and include the restraint-release contribution in the estimator. |
| Umbrella spacing / spring | 0.075 nm / 1000 kJ mol^-1 nm^-2 | LiSPER pilot choices; no universal GROMACS values. | At 2.22 ns, all adjacent histograms share support. Descriptive overlap coefficients: Li minimum 0.305, Na minimum 0.325. | Preserve full overlap matrix; target gaps rather than impose a universal threshold. Na result is diagnostic only because its force field was invalid. |
| Equilibration / production | 0.5 ns equilibration; initially 2 ns, continued toward 4 ns | LiSPER sampling budgets, not confidence levels. Sampling assessment: [Grossfield et al. 2018](https://doi.org/10.33011/livecoms.1.1.5067). | Disjoint 0.5 ns PMF blocks still differ in shape. Maximum GROMACS IACT is about 151 ps (Li) and 111 ps (Na). | Use relaxation, effective sampling, time dependence, and independent campaigns to allocate additional sampling. Do not certify 4/6/8 ns by duration alone. |
| WHAM | `gmx wham -ac`, IACT output, trajectory bootstrap | [`gmx wham`](https://manual.gromacs.org/2026.0/onlinehelp/gmx-wham.html); [Hub et al. 2010](https://doi.org/10.1021/ct100494z). | WHAM converges numerically and overlap is connected. Bootstrap remains conditional on sampled phase space. | Report histograms, IACT, time blocks, bootstrap, replicas, and limitations; no binary software verdict. |
| Standard binding free energy | Not yet implemented | A 1-D PMF needs explicit restraint/volume/standard-state treatment: [Doudou et al. 2009](https://doi.org/10.1021/ct8002354), [Gumbart et al. 2013](https://doi.org/10.1021/ct3008099), and [Woo & Roux 2005](https://doi.org/10.1073/pnas.0409005102). | Current summarizer reports only a bound/reference log-probability contrast. | Derive the exact estimator before promotion. Never use PMF well depth or arithmetic mean as Delta G. |
| Ion force field | CHARMM-GUI / additive CHARMM ion parameters | Na-carboxylate NBFIX: [Venable et al. 2013](https://doi.org/10.1021/jp401512z). Monovalent-ion competition parameters: [Savelyev & MacKerell 2015](https://doi.org/10.1021/acs.jpcb.5b00683). | Historical Na force fields for seven candidates omitted `SOD-OC` and `CLA-SOD`; only LiDA-1 contained both terms. LiLC-1's file is now corrected, but its old TPRs and trajectories predate that correction. A corrected LiLC-1 proof TPR has both terms and zero warnings. | Rebuild the seven affected Na paths from corrected, pinned topologies. Preserve historical trajectories as diagnostic only; they are unusable for claims. |
| Paired comparison | Separate LiCl and NaCl systems | A valid difference requires the same estimand and controlled thermodynamic conditions. | Boxes contain 42 salt pairs plus two counterions. Salt-pair concentrations are about 0.159 M (Li) and 0.148 M (Na); boxes and clustered peptide basins differ. | Decide whether the claim is standard-state binding or finite-concentration selectivity; then match/correct concentration, box, state, and sampling design. |

## What peer review can reasonably require

There is no universal numerical `PASS` threshold for umbrella sampling. A
defensible report instead needs all of the following, with unresolved evidence
left visible:

- an exact thermodynamic estimand and sign convention;
- force-field provenance and identical controlled conditions for the paired comparison;
- a reaction coordinate and restraints consistent with that estimand;
- connected window overlap and documented histogram support;
- equilibration and autocorrelation analysis for the sampled observables;
- cumulative and disjoint time dependence;
- independently initialized complete umbrella campaigns and between-campaign variation;
- sensitivity to binning, analysis start, physical state boundaries, box/concentration,
  and reasonable protocol choices; and
- uncertainty propagated through the final estimator, with claims limited to what
  the uncertainty and replica evidence support.

## Approval boundary

Method-validation calculations may use the EPYC node. The remaining seven
candidates and the final 124-thread production campaign remain frozen until this
ledger contains a reviewed estimand, corrected topology manifests, a completed
LiLC-1 pilot analysis, and an explicit human authorization record.

## Corrected workflow proposed for review

This is a validation sequence, not a collection of fixed magic numbers:

1. **Define the estimand first.** The proposed publication target is the 1 M
   standard binding free energy of one tagged ion for a declared chemical site,
   followed by a paired difference with a documented sign convention. A
   finite-concentration selectivity is a different estimand and must not be
   mixed with it.
2. **Make Li and Na thermodynamic conditions comparable.** Rebuild the Na path
   with the corrected `SOD-OC` and `CLA-SOD` NBFIX terms; pin and hash every
   topology and MDP; match box construction, salt chemical condition,
   protonation, temperature, and analysis definition.
3. **Represent structural uncertainty rather than select one convenient
   cluster.** Cluster independently equilibrated trajectories using peptide
   conformation together with ion-site coordination descriptors. Use several
   populated basins as independently initialized campaigns. The clustering
   cutoff is documented and sensitivity-tested, not treated as a truth gate.
4. **Validate the reaction coordinate before production.** Compare a radial or
   path coordinate plus explicit restraints that keep the tagged ion associated
   with the declared site during the bound-to-bulk path. Demonstrate on short
   pilots that hidden coordination, hydration, peptide conformation, and
   off-site contacts are sampled or controlled. Derive the restraint-release,
   radial-Jacobian, and standard-volume terms before choosing the design.
5. **Use pulling only to seed windows.** A slow pull supplies starting
   configurations; its nonequilibrium work is not the reported free energy.
   Initial window centers cover the complete bound-to-bulk path. Spacing and
   spring constants are adjusted from measured neighboring distributions so
   gaps receive more windows and redundant regions receive fewer.
6. **Equilibrate and produce adaptively.** Each window is equilibrated until
   the biased coordinate and preregistered orthogonal observables lose their
   initialization dependence. Production is accumulated in batches. Sampling
   is extended in windows with long autocorrelation, metastable state changes,
   poor neighboring support, or replica disagreement; 4, 6, or 8 ns is never a
   confidence guarantee by itself.
7. **Reconstruct and convert the PMF correctly.** Use autocorrelation-aware
   WHAM or an equivalently validated estimator, preserve the overlap matrix,
   and integrate the Boltzmann-weighted PMF with the coordinate Jacobian and all
   restraint/standard-state corrections. PMF well depth is not Delta G.
8. **Make the evidence peer-reviewable.** Report cumulative and disjoint time
   behavior, effective sample information, independent-campaign estimates,
   between-campaign dispersion, state-definition and analysis sensitivities,
   and the full propagated uncertainty. No single invented cutoff produces a
   `PASS`; the claim is narrowed or sampling is added wherever the evidence is
   unresolved.

Formal eight-candidate production requires a written protocol containing the
equations and corrections, a successful LiLC-1 proof under that protocol, and
the user's explicit approval. Until then, EPYC time may be used for bounded
method tests and analysis, but not for generating promotable Delta G rows.
