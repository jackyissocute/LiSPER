# LiSPER computational validation strategy

Status: active method definition. Only calculations tied to the declared
estimands and provenance below can support the final table.

## Claims and estimands

### 1. Lithium affinity

For a declared peptide state and Li-binding site at temperature `T`, report the
1 M standard binding free energy

`DeltaG_bind_Li = R T ln(Kd_Li / C_standard)`, where `C_standard = 1 mol/L`.

More-negative `DeltaG_bind_Li` means lower `Kd` and stronger equilibrium
binding. A peptide is only "better than other proteins" relative to a declared
control panel measured with the same estimand and conditions.

### 2. Lithium-over-sodium selectivity

Use the paired definition

`DeltaDeltaG_Li-Na = DeltaG_bind_Li - DeltaG_bind_Na`.

Negative values favor Li. The equilibrium selectivity ratio is

`K_assoc_Li / K_assoc_Na = exp(-DeltaDeltaG_Li-Na / (R T))`.

For an alchemical Li-to-Na transformation, the thermodynamic cycle gives

`DeltaDeltaG_Li-Na = DeltaG_bulk_Li-to-Na - DeltaG_site_Li-to-Na`.

The bulk and site legs must use the same force field, water model, temperature,
electrostatics, lambda path, and analysis convention.

### 3. Capture kinetics is a separate claim

Equilibrium affinity does not establish rapid capture. If the intended product
claim includes capture speed or retention, preregister `k_on`, `k_off`, or
residence-time calculations/experiments separately. Capacity and binding
stoichiometry are also not determined by one-site Delta G.

## What each computational method can establish

| Method | Valid role | Cannot establish alone |
|---|---|---|
| Electrostatic maps / ordinary docking | Generate candidate sites or poses | Li/Na binding affinity or selectivity; ordinary docking scores omit the required explicit hydration, polarization, and peptide ensemble |
| Explicit-solvent competition MD | Discover sites; measure coordination, hydration, ion density, exchange, peptide response, and concentration-specific preferential interaction | A standard binding free energy from contact counts or residence time alone |
| Alchemical relative free energy, Li-to-Na | Primary Li/Na selectivity estimator through matched site and bulk legs | Absolute Li affinity unless an absolute thermodynamic cycle is also run |
| Double-decoupling absolute binding free energy | Primary 1 M affinity estimator when a bound state and restraints are well-defined | Diffuse, multi-site association without explicitly accounting for all relevant bound states |
| Umbrella/PMF or metadynamics | Binding/unbinding mechanism and an independent free-energy cross-check when the coordinate and restraint corrections are valid | A binding Delta G from PMF well depth alone |
| QM or QM/MM model-compound benchmark | Test whether the force field describes Li/Na-water, carboxylate, carbonyl, and amide competition | Peptide ensemble binding thermodynamics by itself |

Ordinary AutoDock Vina is therefore excluded from the quantitative evidence
chain. Its published scoring function is empirical and was designed for
protein-small-molecule pose/search problems, not a fully hydrated monatomic
ion competition problem.

## Validation ladder before peptide production

1. **Bulk-ion force-field check**
   - Compute `DeltaG_bulk_Li-to-Na` in explicit water with a net-neutral box.
   - Use independently seeded complete lambda campaigns.
   - Compare replica estimates, time blocks, adjacent-state support, Li/Na
     water RDFs, first-shell distances, coordination, and diffusion with
     experimental or high-level reference data.
   - Match reference conditions where possible. Experimental structural anchors
     include Li--O at 1.96 (0.02) Angstrom with about 4.8 (0.3) waters at
     1 molal LiCl, and Na--O at 2.384 (0.003) Angstrom with coordination
     5.5 (0.3); concentration and water-model differences must be reported,
     not hidden inside a binary gate.
2. **Functional-group check**
   - Test Li/Na competition for acetate and N-methylacetamide, representing
     carboxylate and peptide-amide donors.
   - Compare additive CHARMM/NBFIX against published condensed-phase and
     QM/QM-MM reference data. If the selectivity changes materially under a
     validated polarizable model, carry force-field-model uncertainty forward.
3. **Unbiased peptide competition pilots**
   - Place LiCl and NaCl together at the same activities/concentrations.
   - Run independent peptide conformations and velocity seeds.
   - Map three-dimensional ion density, coordination identities, hydration,
     site exchange, and peptide conformational states.
   - Use this only to define bound states and identify hidden slow variables.
4. **Primary selectivity calculation**
   - For every populated site, run Li-to-Na alchemical transformations in the
     site and bulk water.
   - Maintain the same chemical site with a documented restraint; include or
     cancel its free-energy contribution correctly.
   - Report each independent campaign, convergence diagnostics, and the paired
     `DeltaDeltaG`, not only a pooled mean.
5. **Absolute affinity and controls**
   - Run double-decoupling ABFE for Li and Na only after bound-state and
     force-field validation.
   - Include restraint, standard-volume, periodic-electrostatics, and charged
     species corrections.
   - Use at least a same-composition scrambled peptide, donor-removal mutant,
     and a justified positive reference. Do not compare unrelated proteins by
     raw docking score or total interaction energy.
6. **Independent path cross-check**
   - Use a corrected PMF/enhanced-sampling path for selected candidates to test
     the alchemical result and characterize the mechanism.

No fixed trajectory duration or single numerical gate certifies this ladder.
Sampling is extended where independent campaigns, time blocks, or thermodynamic
state support disagree.

## Current EPYC feasibility result

- GROMACS 2026.0 has native A/B-state free-energy support and BAR analysis.
- A net-charged first smoke input was rejected without `-maxwarn`; the proof was
  corrected by adding a non-alchemical chloride counterion.
- The corrected 11-state Li-to-Na proof produced DHDL data for every state and
  completed `gmx bar`. Its 50 ps numerical value is explicitly non-scientific.
- Three independently seeded 0.5 ns/state bulk campaigns completed all 33
  windows without fatal or LINCS evidence. Full-trajectory BAR estimates were
  103.06, 102.73, and 103.54 kJ/mol; estimates starting at 100, 200, 300, or
  400 ps remained in the 102.55--103.74 kJ/mol range. These values describe the
  finite-box, net-neutral `LiCl-to-NaCl` bulk leg, not an isolated-ion hydration
  free energy and not peptide selectivity.
- The 0.0-to-0.1 lambda pair has the largest GROMACS relative-entropy distance
  (`s_A` 4.12--4.32 kT), so the uniform 11-state path requires additional
  states near the Li endpoint before quantitative use. Agreement among three
  short replicas does not repair weak thermodynamic-state support.
- Three refined 14-state campaigns then completed all 42 windows without fatal
  or LINCS evidence. Full BAR estimates were 103.42, 103.98, and 102.98 kJ/mol;
  100--400 ps start-time analyses ranged from 102.60 to 104.62 kJ/mol. Adding
  lambda states at 0.025, 0.05, and 0.075 reduced the former endpoint-pair
  `s_A` to 0.32--0.37 kT. The largest remaining adjacent-state value is
  `s_A` 1.38--1.54 kT for lambda 0.1-to-0.2. This is evidence that refinement
  improved phase-space support, not a universal pass threshold.
- Endpoint RDF analysis over 100--500 ps gave Li--O peaks at 0.192--0.194 nm
  and coordination 4.08--4.10 at a declared 0.25 nm shell cutoff; Na--O peaks
  were 0.232--0.238 nm with coordination 5.80--5.84 at a declared 0.32 nm
  cutoff. Na is close to the cited experimental structural anchors. Li distance
  is close, but its coordination is below the 4.8 (0.3) value reported for
  1 molal LiCl; differing concentration and water model prevent a binary
  verdict, but the discrepancy requires model-sensitivity testing.
- Peptide production remains unauthorized. Next validation tests acetate and
  N-methylacetamide and compares additive and polarizable descriptions before
  any peptide-site leg.

## Primary methods and software sources

- GROMACS 2026.0, [free-energy implementation](https://manual.gromacs.org/2026.0/reference-manual/special/free-energy-implementation.html) and [`gmx bar`](https://manual.gromacs.org/2026.0/onlinehelp/gmx-bar.html).
- Mey et al., [best practices for alchemical free-energy calculations](https://doi.org/10.33011/livecoms.2.1.18378).
- Deng and Roux, [standard binding free energies from explicit-solvent simulations](https://doi.org/10.1021/jp807701h).
- Duboue-Dijon and Henin, [bound-state definitions and restraints](https://doi.org/10.1063/5.0046853).
- Rocklin et al., [finite-size corrections for charged binding calculations](https://doi.org/10.1063/1.4826261).
- Yu et al., [ion-selectivity thermodynamic cycles](https://doi.org/10.1073/pnas.1007150107).
- Song and Corry, [Li/Na competition in biological binding sites](https://doi.org/10.1039/C7SC05284G).
- Savelyev and MacKerell, [additive and Drude Li/Na competition parameters](https://doi.org/10.1021/acs.jpcb.5b00683).
- Nan and MacKerell, [polarizable group-I ion/polar-compound parameters](https://doi.org/10.1021/acs.jctc.3c01380).
- Mason et al., [neutron-scattering Li hydration structure](https://doi.org/10.1021/jp511508n).
- Galib et al., [XRD/EXAFS Na hydration structure](https://doi.org/10.1063/1.4975608).
- AutoDock Vina, [original scoring/search method](https://doi.org/10.1002/jcc.21334) and [official manual](https://vina.scripps.edu/manual/).
