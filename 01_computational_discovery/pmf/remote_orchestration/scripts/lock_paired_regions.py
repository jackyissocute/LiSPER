#!/usr/bin/env python3
"""Lock shared bound/reference regions from paired metadata before PMF inspection."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def metadata(path: Path) -> dict:
    return next(csv.DictReader(path.open(), delimiter="\t"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--li-metadata", type=Path, required=True)
    parser.add_argument("--na-metadata", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--bound-cutoff", type=float, default=0.55)
    parser.add_argument("--reference-width", type=float, default=0.30)
    args = parser.parse_args()
    li, na = metadata(args.li_metadata), metadata(args.na_metadata)
    if li["candidate_id"] != na["candidate_id"] or li["site_lock_id"] != na["site_lock_id"]:
        raise RuntimeError("Paired metadata candidate/site lock mismatch")
    for key in ("window_spacing_nm", "window_eq_ns", "window_ns", "guard_windows"):
        if li[key] != na[key]:
            raise RuntimeError(f"Paired protocol mismatch: {key}")
    starts = [float(row["initial_distance_nm"]) for row in (li, na)]
    ends = [start + float(row["effective_analysis_extension_nm"]) for start, row in zip(starts, (li, na))]
    bound_min, bound_max = max(starts), args.bound_cutoff
    ref_max = min(ends)
    ref_min = ref_max - args.reference_width
    if not bound_min < bound_max < ref_min < ref_max:
        raise RuntimeError("Derived regions are invalid")
    row = {
        "candidate": li["candidate_id"],
        "site_lock_id": li["site_lock_id"],
        "rule": "shared_start_to_bound_cutoff__final_shared_non_guard_reference",
        "status": "LOCKED_PRE_PMF",
        "bound_min_nm": f"{bound_min:.4f}",
        "bound_max_nm": f"{bound_max:.4f}",
        "ref_min_nm": f"{ref_min:.4f}",
        "ref_max_nm": f"{ref_max:.4f}",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=row, delimiter="\t")
        writer.writeheader()
        writer.writerow(row)


if __name__ == "__main__":
    main()
