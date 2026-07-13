#!/usr/bin/env python3
"""Summarize paired WHAM evidence without inventing a binary reliability gate.

The reported state contrast is a log probability ratio integrated over declared
coordinate regions. It is not a standard binding free energy. Only invalid or
missing inputs cause a non-zero exit; scientific diagnostics are never converted
to binary scientific thresholds here.
"""
from __future__ import annotations

import argparse
import csv
import math
import statistics
from pathlib import Path

R_KJ_MOL_K = 0.008314462618


def read_xvg(path: Path) -> list[tuple[float, ...]]:
    rows = []
    for line in path.read_text(errors="replace").splitlines():
        if not line or line[0] in "#@&":
            continue
        try:
            rows.append(tuple(float(value) for value in line.split()))
        except ValueError:
            continue
    if not rows:
        raise ValueError(f"no numeric data in {path}")
    return rows


def read_xvg_sets(path: Path) -> list[list[tuple[float, float]]]:
    sets: list[list[tuple[float, float]]] = []
    current: list[tuple[float, float]] = []
    for line in path.read_text(errors="replace").splitlines():
        if line.startswith("&"):
            if current:
                sets.append(current)
                current = []
            continue
        if not line or line[0] in "#@":
            continue
        try:
            x, y = map(float, line.split()[:2])
            current.append((x, y))
        except ValueError:
            continue
    if current:
        sets.append(current)
    if not sets:
        raise ValueError(f"no profile sets in {path}")
    return sets


def interpolate(xy: list[tuple[float, float]], x: float) -> float:
    if not xy or x < xy[0][0] or x > xy[-1][0]:
        raise ValueError(f"region boundary {x} lies outside profile")
    for (x0, y0), (x1, y1) in zip(xy, xy[1:]):
        if x0 <= x <= x1:
            if x1 == x0:
                return y0
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return xy[-1][1]


def region_points(xy: list[tuple[float, float]], lo: float, hi: float) -> list[tuple[float, float]]:
    if not lo < hi:
        raise ValueError("region minimum must be below maximum")
    points = [(lo, interpolate(xy, lo))]
    points.extend((x, y) for x, y in xy if lo < x < hi)
    points.append((hi, interpolate(xy, hi)))
    return points


def log_integral_probability(xy: list[tuple[float, float]], lo: float, hi: float, beta: float) -> float:
    points = region_points(xy, lo, hi)
    shift = min(y for _, y in points)
    area = sum(
        0.5 * (x1 - x0) * (math.exp(-beta * (y0 - shift)) + math.exp(-beta * (y1 - shift)))
        for (x0, y0), (x1, y1) in zip(points, points[1:])
    )
    if area <= 0:
        raise ValueError("non-positive integrated probability")
    return math.log(area) - beta * shift


def state_contrast(
    xy: list[tuple[float, float]], bound: tuple[float, float], reference: tuple[float, float], temperature: float
) -> float:
    beta = 1.0 / (R_KJ_MOL_K * temperature)
    log_bound = log_integral_probability(xy, *bound, beta)
    log_reference = log_integral_probability(xy, *reference, beta)
    return -(log_bound - log_reference) / beta


def histogram_diagnostics(rows: list[tuple[float, ...]], lo: float, hi: float) -> tuple[int, int, int]:
    selected = [row for row in rows if lo <= row[0] <= hi]
    if not selected:
        raise ValueError("histogram does not cover declared regions")
    supports = [sum(math.isfinite(value) and value > 0 for value in row[1:]) for row in selected]
    window_count = max(len(row) - 1 for row in selected)
    zero_adjacent = sum(
        not any(row[left + 1] > 0 and row[left + 2] > 0 for row in selected if len(row) > left + 2)
        for left in range(max(0, window_count - 1))
    )
    return min(supports), sum(support == 0 for support in supports), zero_adjacent


def iact_summary(path: Path) -> tuple[int, float, float]:
    values: list[float] = []
    for line in path.read_text(errors="replace").splitlines():
        # gmx wham -oiact writes window-indexed estimates as comment records:
        # "#  WIN tau(gr1) ...", then "#  0  12.34 ...".
        if not line.startswith("#"):
            continue
        fields = line[1:].split()
        if not fields or not fields[0].isdigit():
            continue
        try:
            values.extend(value for value in map(float, fields[1:]) if math.isfinite(value))
        except ValueError:
            continue
    if not values:
        raise ValueError(f"no IACT estimates in {path}")
    return len(values), statistics.median(values), max(values)


def variants(paths: list[Path], bound, reference, temperature) -> str:
    return ";".join(
        f"{path.stem}={state_contrast([(r[0], r[1]) for r in read_xvg(path)], bound, reference, temperature):.6f}"
        for path in paths
    )


def bootstrap_summary(path: Path, bound, reference, temperature) -> tuple[int, float | None]:
    values = [state_contrast(profile, bound, reference, temperature) for profile in read_xvg_sets(path)]
    return len(values), statistics.stdev(values) if len(values) > 1 else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--li-profile", type=Path, required=True)
    parser.add_argument("--na-profile", type=Path, required=True)
    parser.add_argument("--li-bootstrap-profiles", type=Path, required=True)
    parser.add_argument("--na-bootstrap-profiles", type=Path, required=True)
    parser.add_argument("--li-time-profiles", type=Path, nargs="+", required=True)
    parser.add_argument("--na-time-profiles", type=Path, nargs="+", required=True)
    parser.add_argument("--li-histo", type=Path, required=True)
    parser.add_argument("--na-histo", type=Path, required=True)
    parser.add_argument("--li-iact", type=Path, required=True)
    parser.add_argument("--na-iact", type=Path, required=True)
    parser.add_argument("--regions", type=Path, required=True)
    parser.add_argument("--bootstrap-method", required=True)
    parser.add_argument("--independent-replicates-per-window", type=int, default=1)
    parser.add_argument("--temperature", type=float, default=298.15)
    parser.add_argument("--wham-log-files", type=Path, nargs="+", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    region = next(csv.DictReader(args.regions.open(), delimiter="\t"))
    if region.get("candidate") != args.candidate:
        parser.error("region record must match candidate")
    bound = float(region["bound_min_nm"]), float(region["bound_max_nm"])
    reference = float(region["ref_min_nm"]), float(region["ref_max_nm"])
    if not bound[0] < bound[1] < reference[0] < reference[1]:
        parser.error("declared regions are not ordered and disjoint")

    li_xy = [(row[0], row[1]) for row in read_xvg(args.li_profile)]
    na_xy = [(row[0], row[1]) for row in read_xvg(args.na_profile)]
    li_contrast = state_contrast(li_xy, bound, reference, args.temperature)
    na_contrast = state_contrast(na_xy, bound, reference, args.temperature)
    li_boot_n, li_boot_sd = bootstrap_summary(args.li_bootstrap_profiles, bound, reference, args.temperature)
    na_boot_n, na_boot_sd = bootstrap_summary(args.na_bootstrap_profiles, bound, reference, args.temperature)
    li_support, li_empty, li_disconnected = histogram_diagnostics(read_xvg(args.li_histo), bound[0], reference[1])
    na_support, na_empty, na_disconnected = histogram_diagnostics(read_xvg(args.na_histo), bound[0], reference[1])
    li_iact_n, li_iact_median, li_iact_max = iact_summary(args.li_iact)
    na_iact_n, na_iact_median, na_iact_max = iact_summary(args.na_iact)
    fatal = any(
        term in path.read_text(errors="replace").lower()
        for path in args.wham_log_files
        for term in ("fatal error", "did not converge", "not converged")
    )
    combined_sd = math.hypot(li_boot_sd, na_boot_sd) if li_boot_sd is not None and na_boot_sd is not None else None

    row = {
        "candidate": args.candidate,
        "analysis_type": "EVIDENCE_SUMMARY_NO_BINARY_VERDICT",
        "region_record_status": region.get("status", "UNSPECIFIED"),
        "estimand": "BOUND_MINUS_REFERENCE_LOG_PROBABILITY_CONTRAST",
        "claim_scope": "DIAGNOSTIC_RELATIVE_STATE_CONTRAST_ONLY",
        "absolute_binding_free_energy_supported": "NO",
        "temperature_k": f"{args.temperature:.2f}",
        "independent_replicates_per_window": args.independent_replicates_per_window,
        "between_replica_variation_available": "YES" if args.independent_replicates_per_window > 1 else "NO",
        "li_state_contrast_kjmol": f"{li_contrast:.6f}",
        "na_state_contrast_kjmol": f"{na_contrast:.6f}",
        "paired_contrast_li_minus_na_kjmol": f"{li_contrast - na_contrast:.6f}",
        "bootstrap_method": args.bootstrap_method,
        "li_bootstrap_profiles": li_boot_n,
        "na_bootstrap_profiles": na_boot_n,
        "li_bootstrap_contrast_sd_kjmol": "" if li_boot_sd is None else f"{li_boot_sd:.6f}",
        "na_bootstrap_contrast_sd_kjmol": "" if na_boot_sd is None else f"{na_boot_sd:.6f}",
        "paired_independent_bootstrap_sd_kjmol": "" if combined_sd is None else f"{combined_sd:.6f}",
        "li_min_histogram_support": li_support,
        "na_min_histogram_support": na_support,
        "li_empty_histogram_bins": li_empty,
        "na_empty_histogram_bins": na_empty,
        "li_zero_overlap_adjacent_pairs": li_disconnected,
        "na_zero_overlap_adjacent_pairs": na_disconnected,
        "li_iact_values": li_iact_n,
        "na_iact_values": na_iact_n,
        "li_iact_median_ps": f"{li_iact_median:.6f}",
        "na_iact_median_ps": f"{na_iact_median:.6f}",
        "li_iact_max_ps": f"{li_iact_max:.6f}",
        "na_iact_max_ps": f"{na_iact_max:.6f}",
        "li_time_profile_contrasts": variants(args.li_time_profiles, bound, reference, args.temperature),
        "na_time_profile_contrasts": variants(args.na_time_profiles, bound, reference, args.temperature),
        "wham_fatal_or_nonconverged": "YES" if fatal else "NO",
        "limitations": "no_automatic_reliability_thresholds;not_standard_state_binding_free_energy;bootstrap_can_underestimate_unsampled_slow_modes",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=row, delimiter="\t")
        writer.writeheader()
        writer.writerow(row)
    print(f"{args.candidate}\tevidence_summary\tpaired_contrast={li_contrast - na_contrast:.6f} kJ/mol\tno binary verdict assigned")


if __name__ == "__main__":
    main()
