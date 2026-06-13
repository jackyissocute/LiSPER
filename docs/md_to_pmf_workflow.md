# MD to PMF Workflow

LiSPER peptides are short, Gly/Ser/Pro-rich, and intentionally flexible. For these systems, umbrella sampling should not start directly from a single ESMFold structure or a random MD frame.

## Correct Order

1. ESMFold structure prediction
2. CHARMM-GUI system setup
3. Energy minimization
4. Equilibration
5. 20 ns production MD
6. Structural clustering
7. Representative structure selection
8. Umbrella sampling
9. PMF calculation
10. Delta G for Li+ and Na+
11. Delta Delta G selectivity comparison

## Why Clustering Is Required

During production MD, each peptide samples an ensemble of conformations. A 20 ns trajectory may contain thousands of useful saved frames. For IDP-like peptides, those frames may represent multiple recurrent shapes rather than one stable fold.

Structural clustering asks which conformations occur most often. A representative structure from the most populated cluster is more statistically meaningful than a random frame.

## Current Remote Implementation

The remote production/clustering runner:

- starts from completed step4.1 equilibration
- creates a 20 ns production MDP from CHARMM-GUI `step5_production.mdp`
- saves compressed trajectory frames every 10 ps
- clusters the production trajectory with `gmx cluster`
- uses the peptide group `SOLU` for RMSD clustering
- writes the top-cluster representative to `cluster_20ns/representative_top_cluster.pdb`
- writes top-cluster population metrics to `production_clustering_summary.tsv`

Current default clustering cutoff:

- 0.20 nm peptide RMSD

The cutoff may be tuned after inspecting cluster populations. Very low top-cluster population is not a failure; for LiSPER it is evidence of strong conformational disorder and should be recorded as part of the selectivity interpretation.

## PMF Entry Point

Umbrella sampling should start from representative structures, not raw ESMFold predictions. For the first pass, use the representative structure of the largest cluster for each peptide and ion condition.

After Li+ and Na+ PMFs are computed:

Delta Delta G = Delta G(Li+) - Delta G(Na+)

More negative Delta Delta G indicates stronger Li+ preference.
