# Delta G promotion hold

Status: active.

Do not promote any Delta G or Delta Delta G as final while this file exists.

Release requires a documented method review for each candidate-condition pair:

1. `SITE_LOCKED` paired binding-site identity from the machine-readable manifest.
2. Manifest `starting_state_status=GEOMETRY_SCREENED_BOUND_START` with logged geometry for both ions; this is not evidence of binding reliability.
3. Explicit physical state definitions and a thermodynamically defined estimator.
4. Connected histogram overlap and autocorrelation-aware WHAM evidence.
5. Time-dependent, independent-replica, and analysis-sensitivity evidence.
6. Correct restraint, coordinate-measure/Jacobian, state-volume, and standard-state treatment for any absolute binding-free-energy claim.

No script-generated binary verdict releases this hold.

## Compute policy

Authorized compute: locked-site, geometry-screened umbrella on `lisper-epyc`, pilot **LiLC-1** first. Scale remaining candidates only after the pilot method review supports that decision; no automatic QC label unlocks scale-up.
