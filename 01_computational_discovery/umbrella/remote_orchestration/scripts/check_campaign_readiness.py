#!/usr/bin/env python3
"""Inventory whether each candidate×ion is ready for locked-site umbrella.

Exit 0 only if every requested system is READY (or --pilot passes for LiLC-1).
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

CANDIDATES = [
    "LiD3-Core",
    "LiD3-Flex",
    "LiND-Hybrid",
    "LiLC-1",
    "LiDS-1",
    "LiDA-1",
    "LiN3-Core",
    "LiA3-Ref",
]
IONS = ("li_cl", "na_cl")
ION_RESNAME = {"li_cl": "LI", "na_cl": "SOD"}


def md_root(repo: Path, ion: str) -> Path:
    return repo / "01_computational_discovery" / "md" / ion / "remote_results" / "systems"


def gromacs_dir(repo: Path, ion: str, candidate: str) -> Path:
    return md_root(repo, ion) / candidate / "gromacs"


def first_existing(paths):
    for path in paths:
        if path.exists() and path.stat().st_size > 0:
            return path
    return None


def assess(repo: Path, ion: str, candidate: str) -> dict:
    gmx = gromacs_dir(repo, ion, candidate)
    prod = gmx / "run_prod_20ns"
    cluster = gmx / "cluster_20ns"
    umb = gmx / "umbrella_sampling"

    rep = first_existing(
        [
            cluster / "representative_top_cluster.pdb",
            gmx.parent / "cluster_20ns" / "representative_top_cluster.pdb",
        ]
    )
    xtc = first_existing([prod / "step5_production_20ns.xtc"])
    tpr = first_existing([prod / "step5_production_20ns.tpr"])
    gro_final = first_existing([prod / "step5_production_20ns.gro"])
    full_rep = first_existing([umb / "representative_full_system.gro"])
    topol = first_existing(
        [
            gmx / "topol_cleaned_for_prod.top",
            gmx / "topol_clean_attempt2.top",
            gmx / "topol_clean_attempt1.top",
            gmx / "topol.top",
            gmx / "run_min" / "topol_cleaned.top",
        ]
    )
    manifest = (
        repo
        / "01_computational_discovery"
        / "umbrella"
        / "paired_site_manifests"
        / f"{candidate}.tsv"
    )
    status = "PROPOSED_REQUIRES_RECONSTRUCTION"
    if manifest.exists():
        row = next(csv.DictReader(manifest.open(), delimiter="\t"))
        status = row.get("starting_state_status", status)

    # READY for locked umbrella launch:
    # - topology
    # - geometry-screened bound-start manifest
    # - full-system start gro OR (rep pdb + prod xtc + tpr for extract)
    has_extract_path = bool(rep and xtc and tpr and topol)
    has_screened_gro = bool(full_rep and topol and status == "GEOMETRY_SCREENED_BOUND_START")
    if has_screened_gro:
        ready = "READY"
    elif status != "GEOMETRY_SCREENED_BOUND_START":
        ready = "BLOCKED_SITE_LOCK"
    elif has_extract_path:
        ready = "READY_NEEDS_EXTRACT"
    elif topol and rep and gro_final and not xtc:
        ready = "MISSING_XTC"
    elif not topol:
        ready = "MISSING_TOPOL"
    else:
        ready = "MISSING_OTHER"

    return {
        "candidate": candidate,
        "ion": ion,
        "ion_resname": ION_RESNAME[ion],
        "ready": ready,
        "manifest_status": status,
        "rep_pdb": "Y" if rep else "N",
        "prod_xtc": "Y" if xtc else "N",
        "prod_tpr": "Y" if tpr else "N",
        "prod_gro": "Y" if gro_final else "N",
        "full_rep_gro": "Y" if full_rep else "N",
        "topol": "Y" if topol else "N",
        "rep_path": str(rep) if rep else "",
        "topol_path": str(topol) if topol else "",
        "full_rep_path": str(full_rep) if full_rep else "",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path(__file__).resolve().parents[4],
    )
    parser.add_argument("--pilot", action="store_true", help="Only require LiLC-1 both ions")
    parser.add_argument("--out", type=Path, help="Write TSV report")
    args = parser.parse_args()

    wanted = ["LiLC-1"] if args.pilot else CANDIDATES
    rows = [assess(args.repo, ion, cand) for cand in wanted for ion in IONS]

    fieldnames = list(rows[0].keys())
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)

    ready_ok = {"READY", "READY_NEEDS_EXTRACT"}
    width = max(len(r["ready"]) for r in rows)
    print(f"{'candidate':12} {'ion':6} {'ready':{width}} manifest rep xtc tpr gro full topol")
    for row in rows:
        print(
            f"{row['candidate']:12} {row['ion']:6} {row['ready']:{width}} "
            f"{row['manifest_status'][:22]:22} "
            f"{row['rep_pdb']}   {row['prod_xtc']}   {row['prod_tpr']}   "
            f"{row['prod_gro']}   {row['full_rep_gro']}    {row['topol']}"
        )

    n_ok = sum(1 for row in rows if row["ready"] in ready_ok)
    print(f"\n{n_ok}/{len(rows)} launch-ready")
    blockers = sorted({row["ready"] for row in rows if row["ready"] not in ready_ok})
    if blockers:
        print("blockers:", ", ".join(blockers))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
