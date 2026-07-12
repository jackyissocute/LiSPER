#!/usr/bin/env python3
"""Paired PMF QC gate evaluator (protocol thresholds from LISPER_UMBRELLA_QC_PROTOCOL.md).

Inputs are already-computed WHAM products for one candidate pair:
  --li-profile / --na-profile          xvg free-energy profiles (kJ/mol)
  --li-bootstrap / --na-bootstrap      optional xydy bootstrap std profiles
  --li-histo / --na-histo              optional histogram xvgs (overlap warnings)
  --li-half-a --li-half-b ...          optional early/late half profiles
  --bound-min --bound-max              shared bound region (nm)
  --ref-min --ref-max                  shared reference plateau (nm)

Prints PASS/FAIL/REPAIR and writes a TSV summary. Does not invent regions.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path


def read_xvg(path: Path):
    rows = []
    for line in path.read_text(errors="replace").splitlines():
        if not line or line[0] in "#@":
            continue
        parts = line.split()
        try:
            rows.append(tuple(float(x) for x in parts[:3]))
        except ValueError:
            continue
    return rows


def series_xy(rows):
    return [(r[0], r[1]) for r in rows]


def interpolate(xy, x):
    if not xy:
        raise ValueError("empty profile")
    if x <= xy[0][0]:
        return xy[0][1]
    if x >= xy[-1][0]:
        return xy[-1][1]
    for (x0, y0), (x1, y1) in zip(xy, xy[1:]):
        if x0 <= x <= x1:
            if x1 == x0:
                return y0
            t = (x - x0) / (x1 - x0)
            return y0 + t * (y1 - y0)
    return xy[-1][1]


def mean_region(xy, lo, hi):
    vals = [y for x, y in xy if lo <= x <= hi]
    if not vals:
        # fallback to endpoints
        return 0.5 * (interpolate(xy, lo) + interpolate(xy, hi))
    return sum(vals) / len(vals)


def delta_g(xy, bound_lo, bound_hi, ref_lo, ref_hi):
    return mean_region(xy, ref_lo, ref_hi) - mean_region(xy, bound_lo, bound_hi)


def plateau_flatness(xy, ref_lo, ref_hi):
    ys = [y for x, y in xy if ref_lo <= x <= ref_hi]
    if len(ys) < 2:
        y0, y1 = interpolate(xy, ref_lo), interpolate(xy, ref_hi)
        return abs(y1 - y0)
    return max(ys) - min(ys)


def bootstrap_unc(xy_dy, lo, hi):
    """Conservative combined uncertainty: rms of mean std in bound and ref regions."""
    if not xy_dy or len(xy_dy[0]) < 3:
        return None
    bound = [r[2] for r in xy_dy if lo[0] <= r[0] <= lo[1]]
    ref = [r[2] for r in xy_dy if hi[0] <= r[0] <= hi[1]]
    if not bound or not ref:
        return None
    b = sum(bound) / len(bound)
    r = sum(ref) / len(ref)
    return math.sqrt(b * b + r * r)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--candidate", required=True)
    p.add_argument("--li-profile", type=Path, required=True)
    p.add_argument("--na-profile", type=Path, required=True)
    p.add_argument("--li-bootstrap", type=Path)
    p.add_argument("--na-bootstrap", type=Path)
    p.add_argument("--li-half-early", type=Path)
    p.add_argument("--li-half-late", type=Path)
    p.add_argument("--na-half-early", type=Path)
    p.add_argument("--na-half-late", type=Path)
    p.add_argument("--bound-min", type=float, required=True)
    p.add_argument("--bound-max", type=float, required=True)
    p.add_argument("--ref-min", type=float, required=True)
    p.add_argument("--ref-max", type=float, required=True)
    p.add_argument("--flat-max", type=float, default=1.0)
    p.add_argument("--half-max", type=float, default=1.0)
    p.add_argument("--unc-max", type=float, default=1.0)
    p.add_argument("--unc-frac-of-ddg", type=float, default=0.25)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--wham-warning-files", type=Path, nargs="*", default=[])
    args = p.parse_args()

    li = series_xy(read_xvg(args.li_profile))
    na = series_xy(read_xvg(args.na_profile))
    dg_li = delta_g(li, args.bound_min, args.bound_max, args.ref_min, args.ref_max)
    dg_na = delta_g(na, args.bound_min, args.bound_max, args.ref_min, args.ref_max)
    ddg = dg_li - dg_na

    gates = []

    flat_li = plateau_flatness(li, args.ref_min, args.ref_max)
    flat_na = plateau_flatness(na, args.ref_min, args.ref_max)
    gates.append(("plateau_flat_li", flat_li <= args.flat_max, f"{flat_li:.3f}"))
    gates.append(("plateau_flat_na", flat_na <= args.flat_max, f"{flat_na:.3f}"))

    if args.li_half_early and args.li_half_late:
        e = delta_g(series_xy(read_xvg(args.li_half_early)), args.bound_min, args.bound_max, args.ref_min, args.ref_max)
        late = delta_g(series_xy(read_xvg(args.li_half_late)), args.bound_min, args.bound_max, args.ref_min, args.ref_max)
        gates.append(("half_agree_li", abs(e - late) <= args.half_max, f"{abs(e-late):.3f}"))
    if args.na_half_early and args.na_half_late:
        e = delta_g(series_xy(read_xvg(args.na_half_early)), args.bound_min, args.bound_max, args.ref_min, args.ref_max)
        late = delta_g(series_xy(read_xvg(args.na_half_late)), args.bound_min, args.bound_max, args.ref_min, args.ref_max)
        gates.append(("half_agree_na", abs(e - late) <= args.half_max, f"{abs(e-late):.3f}"))

    unc_li = unc_na = None
    if args.li_bootstrap:
        unc_li = bootstrap_unc(read_xvg(args.li_bootstrap), (args.bound_min, args.bound_max), (args.ref_min, args.ref_max))
    if args.na_bootstrap:
        unc_na = bootstrap_unc(read_xvg(args.na_bootstrap), (args.bound_min, args.bound_max), (args.ref_min, args.ref_max))
    if unc_li is not None:
        gates.append(("bootstrap_unc_li", unc_li <= args.unc_max, f"{unc_li:.3f}"))
    if unc_na is not None:
        gates.append(("bootstrap_unc_na", unc_na <= args.unc_max, f"{unc_na:.3f}"))
    if unc_li is not None and unc_na is not None and abs(ddg) > 1e-9:
        comb = math.sqrt(unc_li**2 + unc_na**2)
        gates.append(
            (
                "bootstrap_unc_vs_ddg",
                comb <= args.unc_frac_of_ddg * abs(ddg),
                f"{comb:.3f}/{abs(ddg):.3f}",
            )
        )

    interior_warn = False
    for path in args.wham_warning_files:
        text = path.read_text(errors="replace")
        for line in text.splitlines():
            low = line.lower()
            if "warning" in low and ("empty" in low or "only one" in low or "single" in low):
                interior_warn = True
    gates.append(("no_interior_wham_warnings", not interior_warn, "warned" if interior_warn else "clean"))

    failed = [name for name, ok, _ in gates if not ok]
    status = "PASS" if not failed else "REPAIR"
    row = {
        "candidate": args.candidate,
        "status": status,
        "delta_g_li_kjmol": f"{dg_li:.3f}",
        "delta_g_na_kjmol": f"{dg_na:.3f}",
        "delta_delta_g_kjmol": f"{ddg:.3f}",
        "bound_min_nm": f"{args.bound_min:.4f}",
        "bound_max_nm": f"{args.bound_max:.4f}",
        "ref_min_nm": f"{args.ref_min:.4f}",
        "ref_max_nm": f"{args.ref_max:.4f}",
        "failed_gates": ",".join(failed),
    }
    for name, ok, detail in gates:
        row[f"gate_{name}"] = "PASS" if ok else "FAIL"
        row[f"gate_{name}_detail"] = detail

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row.keys()), delimiter="\t")
        writer.writeheader()
        writer.writerow(row)

    print(f"{args.candidate}\t{status}\tΔG_Li={dg_li:.3f}\tΔG_Na={dg_na:.3f}\tΔΔG={ddg:.3f}")
    if failed:
        print("failed_gates:", ",".join(failed))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
