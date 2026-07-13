# Delta G promotion hold

Status: active.

Do not promote any Delta G or Delta Delta G as final while this file exists.

Release requires, for each candidate-condition pair:

1. `SITE_LOCKED` paired binding-site identity from the machine-readable manifest.
2. Manifest `starting_state_status=VALIDATED_BOUND` with logged site check for both ions.
3. A shared physical-region and estimator manifest.
4. Region-aware WHAM QC from the central evaluator.

## Compute policy

Authorized compute: locked-site `VALIDATED_BOUND` umbrella on `lisper-epyc`, pilot **LiLC-1** first, then scale remaining candidates after paired QC PASS.
