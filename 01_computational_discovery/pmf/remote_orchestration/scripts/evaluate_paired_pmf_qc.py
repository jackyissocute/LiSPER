#!/usr/bin/env python3
"""Compute paired Li/Na PMF estimates and report diagnostics without invented cutoffs."""
from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

R_KJ_MOL_K = 0.00831446261815324


def read_xvg(path: Path):
    rows = []
    for line in path.read_text(errors="replace").splitlines():
        if not line or line[0] in "#@":
            continue
        try:
            rows.append(tuple(float(value) for value in line.split()))
        except ValueError:
            continue
    return rows


def corrected_profile(path: Path, temperature: float):
    """Remove the 4*pi*r^2 distance-coordinate entropy from a radial PMF."""
    rt = R_KJ_MOL_K * temperature
    profile = []
    for row in read_xvg(path):
        if len(row) >= 2 and row[0] > 0:
            profile.append((row[0], row[1] + rt * math.log(4 * math.pi * row[0] ** 2)))
    if not profile:
        raise RuntimeError(f"No usable PMF points: {path}")
    return profile


def interpolate(xy, x):
    if x <= xy[0][0]:
        return xy[0][1]
    if x >= xy[-1][0]:
        return xy[-1][1]
    for (x0, y0), (x1, y1) in zip(xy, xy[1:]):
        if x0 <= x <= x1:
            fraction = (x - x0) / (x1 - x0) if x1 != x0 else 0
            return y0 + fraction * (y1 - y0)
    return xy[-1][1]


def mean_region(xy, lo, hi):
    values = [y for x, y in xy if lo <= x <= hi]
    return sum(values) / len(values) if values else 0.5 * (interpolate(xy, lo) + interpolate(xy, hi))


def binding_delta_g(xy, bound_lo, bound_hi, ref_lo, ref_hi):
    """Endpoint-referenced PMF binding difference; negative means bound is favored."""
    return mean_region(xy, bound_lo, bound_hi) - mean_region(xy, ref_lo, ref_hi)


def region_span(xy, lo, hi):
    values = [y for x, y in xy if lo <= x <= hi]
    if len(values) < 2:
        values = [interpolate(xy, lo), interpolate(xy, hi)]
    return max(values) - min(values)


def bootstrap_unc(path, bound, reference):
    if path is None:
        return None
    rows = read_xvg(path)
    if not rows or len(rows[0]) < 3:
        return None
    bound_std = [row[2] for row in rows if bound[0] <= row[0] <= bound[1]]
    ref_std = [row[2] for row in rows if reference[0] <= row[0] <= reference[1]]
    if not bound_std or not ref_std:
        return None
    b = sum(bound_std) / len(bound_std)
    r = sum(ref_std) / len(ref_std)
    return math.sqrt(b * b + r * r)


def histogram_coverage(path, lo, hi):
    if path is None:
        return None, None
    supports = [
        sum(math.isfinite(value) and value > 0 for value in row[1:])
        for row in read_xvg(path)
        if lo <= row[0] <= hi
    ]
    return (min(supports), sum(value < 2 for value in supports)) if supports else (0, 1)


def optional_delta(path, regions, temperature):
    if path is None:
        return None
    return binding_delta_g(corrected_profile(path, temperature), *regions)


def fmt(value):
    return "missing" if value is None else f"{value:.3f}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--li-profile", type=Path, required=True)
    parser.add_argument("--na-profile", type=Path, required=True)
    parser.add_argument("--li-bootstrap", type=Path)
    parser.add_argument("--na-bootstrap", type=Path)
    parser.add_argument("--li-half-early", type=Path)
    parser.add_argument("--li-half-late", type=Path)
    parser.add_argument("--na-half-early", type=Path)
    parser.add_argument("--na-half-late", type=Path)
    parser.add_argument("--li-burnin", type=Path, nargs="*", default=[])
    parser.add_argument("--na-burnin", type=Path, nargs="*", default=[])
    parser.add_argument("--li-histo", type=Path)
    parser.add_argument("--na-histo", type=Path)
    parser.add_argument("--regions", type=Path, required=True)
    parser.add_argument("--temperature", type=float, default=298.15)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--wham-warning-files", type=Path, nargs="*", default=[])
    args = parser.parse_args()

    region_row = next(csv.DictReader(args.regions.open(), delimiter="\t"))
    if region_row.get("candidate") != args.candidate:
        parser.error("region candidate does not match")
    bound = (float(region_row["bound_min_nm"]), float(region_row["bound_max_nm"]))
    reference = (float(region_row["ref_min_nm"]), float(region_row["ref_max_nm"]))
    regions = (*bound, *reference)

    li = corrected_profile(args.li_profile, args.temperature)
    na = corrected_profile(args.na_profile, args.temperature)
    dg_li = binding_delta_g(li, *regions)
    dg_na = binding_delta_g(na, *regions)
    ddg = dg_li - dg_na

    diagnostics = {
        "endpoint_span_li_kjmol": fmt(region_span(li, *reference)),
        "endpoint_span_na_kjmol": fmt(region_span(na, *reference)),
    }
    warnings = []
    for ion, early_path, late_path, full_dg, burnins, histo in (
        ("li", args.li_half_early, args.li_half_late, dg_li, args.li_burnin, args.li_histo),
        ("na", args.na_half_early, args.na_half_late, dg_na, args.na_burnin, args.na_histo),
    ):
        early = optional_delta(early_path, regions, args.temperature)
        late = optional_delta(late_path, regions, args.temperature)
        diagnostics[f"half_difference_{ion}_kjmol"] = fmt(
            None if early is None or late is None else abs(early - late)
        )
        burnin_values = [optional_delta(path, regions, args.temperature) for path in burnins]
        diagnostics[f"burnin_max_shift_{ion}_kjmol"] = fmt(
            max((abs(full_dg - value) for value in burnin_values if value is not None), default=None)
        )
        min_support, weak_bins = histogram_coverage(histo, bound[0], reference[1])
        diagnostics[f"histogram_min_support_{ion}"] = "missing" if min_support is None else str(min_support)
        diagnostics[f"histogram_weak_bins_{ion}"] = "missing" if weak_bins is None else str(weak_bins)
        if weak_bins:
            warnings.append(f"weak_histogram_bins_{ion}:{weak_bins}")

    unc_li = bootstrap_unc(args.li_bootstrap, bound, reference)
    unc_na = bootstrap_unc(args.na_bootstrap, bound, reference)
    diagnostics["bootstrap_unc_li_kjmol"] = fmt(unc_li)
    diagnostics["bootstrap_unc_na_kjmol"] = fmt(unc_na)
    diagnostics["bootstrap_unc_ddg_kjmol"] = fmt(
        None if unc_li is None or unc_na is None else math.sqrt(unc_li**2 + unc_na**2)
    )
    for path in args.wham_warning_files:
        text = path.read_text(errors="replace").lower()
        if "fatal error" in text or "not converged" in text or "did not converge" in text:
            warnings.append(f"wham_warning:{path.name}")

    row = {
        "candidate": args.candidate,
        "status": "ESTIMATE_WITH_WARNINGS" if warnings else "ESTIMATE_READY",
        "estimand": "radially_corrected_endpoint_referenced_pmf_binding_difference",
        "standard_state": "no",
        "sign_convention": "negative_delta_delta_g_means_Li_preference",
        "temperature_k": f"{args.temperature:.2f}",
        "delta_g_li_kjmol": f"{dg_li:.3f}",
        "delta_g_na_kjmol": f"{dg_na:.3f}",
        "delta_delta_g_kjmol": f"{ddg:.3f}",
        "bound_min_nm": f"{bound[0]:.4f}",
        "bound_max_nm": f"{bound[1]:.4f}",
        "ref_min_nm": f"{reference[0]:.4f}",
        "ref_max_nm": f"{reference[1]:.4f}",
        "diagnostic_warnings": ",".join(warnings),
        **diagnostics,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=row, delimiter="\t")
        writer.writeheader()
        writer.writerow(row)
    print(
        f"{args.candidate}\t{row['status']}\t"
        f"DeltaG_Li={dg_li:.3f}\tDeltaG_Na={dg_na:.3f}\tDeltaDeltaG={ddg:.3f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
