#!/usr/bin/env python3
"""Record explicit paired analysis regions and rationale; do not derive them heuristically."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def metadata(path: Path) -> dict[str, str]:
    return next(csv.DictReader(path.open(), delimiter="\t"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--li-metadata", type=Path, required=True)
    parser.add_argument("--na-metadata", type=Path, required=True)
    parser.add_argument("--bound-min", type=float, required=True)
    parser.add_argument("--bound-max", type=float, required=True)
    parser.add_argument("--ref-min", type=float, required=True)
    parser.add_argument("--ref-max", type=float, required=True)
    parser.add_argument("--bound-rationale", required=True)
    parser.add_argument("--reference-rationale", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    li, na = metadata(args.li_metadata), metadata(args.na_metadata)
    if li["candidate_id"] != na["candidate_id"] or li["site_lock_id"] != na["site_lock_id"]:
        raise RuntimeError("paired metadata candidate/site-lock mismatch")
    for key in ("window_spacing_nm", "window_eq_ns", "window_ns", "guard_windows"):
        if li[key] != na[key]:
            raise RuntimeError(f"paired protocol mismatch: {key}")
    if not args.bound_min < args.bound_max < args.ref_min < args.ref_max:
        raise RuntimeError("declared regions must be ordered and disjoint")
    starts = [float(row["initial_distance_nm"]) for row in (li, na)]
    ends = [start + float(row["effective_analysis_extension_nm"]) for start, row in zip(starts, (li, na))]
    if args.bound_min < max(starts) or args.ref_max > min(ends):
        raise RuntimeError("declared regions exceed shared paired coordinate coverage")
    row = {
        "candidate": li["candidate_id"],
        "site_lock_id": li["site_lock_id"],
        "status": "DECLARED_DIAGNOSTIC_REGIONS",
        "bound_min_nm": f"{args.bound_min:.4f}",
        "bound_max_nm": f"{args.bound_max:.4f}",
        "ref_min_nm": f"{args.ref_min:.4f}",
        "ref_max_nm": f"{args.ref_max:.4f}",
        "bound_rationale": args.bound_rationale,
        "reference_rationale": args.reference_rationale,
        "claim_scope": "diagnostic_relative_state_contrast_not_absolute_binding_free_energy",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=row, delimiter="\t")
        writer.writeheader()
        writer.writerow(row)


if __name__ == "__main__":
    main()
