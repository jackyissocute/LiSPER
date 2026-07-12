#!/usr/bin/env python3
"""Estimate locked-site umbrella wall time on an N-thread CPU host.

Uses the 2026-07-11 benchmark: ~4.615 ns/day per 1-thread window mdrun.
Default protocol: 1.0 ns pull + per window (0.5 ns eq + 2.0 ns prod).
"""
from __future__ import annotations

import argparse
import math


def windows_for_extension(initial_nm: float, analysis_ext_nm: float, spacing_nm: float, guards: int) -> int:
    total_ext = analysis_ext_nm + guards * spacing_nm
    return int(round(total_ext / spacing_nm)) + 1


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--threads", type=int, default=100)
    p.add_argument("--reserve-threads", type=int, default=4, help="SSH/WHAM/OS reserve")
    p.add_argument("--ns-per-day", type=float, default=4.615)
    p.add_argument("--pull-ns", type=float, default=1.0)
    p.add_argument("--window-eq-ns", type=float, default=0.5)
    p.add_argument("--window-ns", type=float, default=2.0)
    p.add_argument("--spacing-nm", type=float, default=0.075)
    p.add_argument("--analysis-ext-nm", type=float, default=2.0)
    p.add_argument("--guards", type=int, default=3)
    p.add_argument("--initial-nm", type=float, default=0.45, help="Typical bound start distance")
    p.add_argument("--pairs", type=int, default=1, help="Candidate pairs (Li+Na = 1 pair)")
    p.add_argument("--candidates", type=int, default=1)
    args = p.parse_args()

    usable = max(1, args.threads - args.reserve_threads)
    nwin = windows_for_extension(args.initial_nm, args.analysis_ext_nm, args.spacing_nm, args.guards)
    per_window_ns = args.window_eq_ns + args.window_ns
    # Pull is serial per condition before windows fan out
    pull_days = args.pull_ns / args.ns_per_day
    # Windows: one thread each; schedule across usable cores
    window_ns_total = nwin * per_window_ns
    # With W concurrent windows, throughput = W * ns_per_day
    conditions = args.candidates * 2  # Li + Na
    # Schedule all conditions' windows into one pool after their pulls finish.
    # Conservative: assume pulls run first (serial per condition, parallel across conditions).
    pull_waves = math.ceil(conditions / usable)
    pull_wall_days = pull_waves * pull_days
    total_window_jobs = conditions * nwin
    window_wall_days = (total_window_jobs * per_window_ns) / (usable * args.ns_per_day)
    total_days = pull_wall_days + window_wall_days

    print(f"threads_total\t{args.threads}")
    print(f"threads_usable\t{usable}")
    print(f"candidates\t{args.candidates}")
    print(f"conditions\t{conditions}")
    print(f"windows_per_condition\t{nwin}")
    print(f"ns_per_window\t{per_window_ns}")
    print(f"total_window_jobs\t{total_window_jobs}")
    print(f"pull_wall_days\t{pull_wall_days:.2f}")
    print(f"window_wall_days\t{window_wall_days:.2f}")
    print(f"estimated_total_days\t{total_days:.2f}")
    print(f"recommended_LISPER_GLOBAL_MDRUN_LIMIT\t{usable}")
    print(f"recommended_LISPER_JOBS_per_driver\t{min(usable, nwin)}")
    print()
    print("note\tEstimate ignores WHAM/QC time and overlap-repair windows.")
    print("note\tDo not launch until VALIDATED_BOUND + readiness checker PASS.")


if __name__ == "__main__":
    main()
