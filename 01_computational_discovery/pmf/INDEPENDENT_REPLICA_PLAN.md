# Independent-replica and method-correction plan

Status: preregistration draft; Delta G promotion remains frozen.

This plan does not promise that a fixed trajectory length or replica count will
produce convergence. It defines how additional evidence will be generated and
how unresolved sampling will remain visible.

## 1. Resolve the estimand before scale-up

1. Record the exact GROMACS pull coordinate, restrained groups, force constants,
   periodic-boundary handling, and coordinate range.
2. Define bound and reference states from ion coordination, hydration, peptide
   conformation, and distance evidence—not from a convenient PMF segment.
3. For the existing one-dimensional coordinate, report only the
   Boltzmann-integrated bound/reference probability contrast as a diagnostic.
4. Before any absolute binding claim, derive and validate the required
   coordinate-measure/Jacobian, restraint-release, state-volume, finite-size, and
   standard-state corrections. If the present setup cannot support them, change
   the claim rather than manufacture a correction.

## 2. Diagnose the current LiLC-1 replica

After the running continuation finishes:

- run capped `gmx wham -ac` and preserve every window's IACT estimate;
- produce the overlap matrix/graph, identify empty required regions and
  disconnected adjacent windows, and add targeted windows if the sampled path is
  disconnected;
- calculate replica-specific cumulative and disjoint-block state contrasts;
- inspect coordination number, hydration, peptide conformation, and ion position
  across the coordinate to determine whether the proposed reference is actually
  bulk-like/unbound;
- repeat the analysis across binning, start times, and physically plausible state
  boundaries; and
- retain every disagreement instead of collapsing it into a binary verdict.

## 3. Generate genuinely independent replicas

The independent unit is a complete umbrella campaign, not an early/late segment
of one campaign.

1. Start with two new LiCl and two new NaCl pilot campaigns, giving three
   independently generated campaigns per ion including the current one. Three is
   an initial design for estimating visible between-campaign variation, not a
   convergence guarantee or promotion threshold.
2. Generate each campaign from an independently equilibrated peptide/ion/solvent
   state and a recorded independent velocity seed. Do not copy production
   checkpoints between replicas.
3. Apply the same predeclared coordinate, window locations, force constants,
   equilibration procedure, production schedule, and state definitions to both
   ions and all replicas.
4. Analyze each campaign separately first. Report the individual estimates,
   within-campaign correlation-aware uncertainty, structural states sampled, and
   between-campaign spread before any pooled estimate.
5. Pool only after confirming that replicas target the same thermodynamic states
   and that pooling does not conceal distinct metastable populations.

## 4. Sequential sampling decisions

Additional sampling is targeted to the evidence:

- disconnected overlap -> add/reposition windows or increase sampling locally;
- long IACT or drifting block estimates -> extend affected windows/replicas;
- replica-specific metastable states or unresolved between-replica disagreement
  -> add independently initialized replicas and examine omitted coordinates;
- no demonstrably bulk-like reference or strong boundary/box sensitivity ->
  redesign the coordinate/state/box before interpreting Delta G; and
- stable-looking results with only one sampled basin -> remain explicitly
  inconclusive rather than calling them converged.

Every decision and its evidence is recorded before viewing the final paired
selectivity ranking. The protocol may be corrected when the estimand is wrong,
but thresholds or state boundaries are never tuned to obtain a desired ranking.
