#!/usr/bin/env python3
"""OBSOLETE (2026-07-12): do not relaunch.

Legacy dynamic-nearest binding-site v2 resumes cannot yield publishable paired ΔΔG
(0/8 SITE_LOCKED). See pmf/LEGACY_DATA_EVALUATION.md and DELTA_G_PROMOTION_HOLD.md.

Next path: VALIDATED_BOUND locked-site umbrella (pilot LiLC-1).
Prior implementation remains in git history before this stub.
"""
from __future__ import annotations

import sys

sys.stderr.write(
    "ERROR: resume_incomplete_windows_quickpod.py is obsolete. "
    "Legacy mismatched-site campaigns are stopped. "
    "Use locked-site VALIDATED_BOUND umbrella instead.\n"
)
raise SystemExit(2)
