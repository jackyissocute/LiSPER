# Delta G promotion hold

Status: active from 2026-07-12 P0 corrective mandate.

Do not promote any Delta G or Delta Delta G as final while this file exists.

Release requires, for each candidate-condition pair:

1. `SITE_LOCKED` paired binding-site identity from the machine-readable manifest.
2. Manifest `starting_state_status=VALIDATED_BOUND` with logged site check for both ions.
3. A shared physical-region and estimator manifest.
4. Region-aware WHAM QC from the central evaluator.

## Compute policy (2026-07-12)

Legacy dynamic-nearest-site umbrella (`umbrella_sampling_binding_site_v2` and its WHAM products) is **stopped**, not finished for ranking. Those campaigns are diagnostic only (`0/8` same-site pairs). See `LEGACY_DATA_EVALUATION.md`.

Do not relaunch `resume_incomplete_windows_quickpod.py` / `watchdog_resume.sh` for mismatched-site windows.

Next authorized compute: reconstruct/validate bound starts → mark `VALIDATED_BOUND` → locked-site umbrella pilot (**LiLC-1** first).
