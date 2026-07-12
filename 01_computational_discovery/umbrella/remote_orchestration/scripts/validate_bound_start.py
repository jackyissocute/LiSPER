#!/usr/bin/env python3
"""Validate a full-system .gro against the locked donor site; optionally promote manifest.

Bound criterion (practical, predeclared):
  nearest target ion to locked-donor centroid <= --max-bound-nm (default 0.55 nm)

Does NOT invent geometry. If distance fails, exit 2 and leave manifest unchanged.
Promotion writes:
  - validation log beside the gro
  - starting_state_status=VALIDATED_BOUND in paired_site_manifests/<cand>.tsv
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
import time
from pathlib import Path


def read_gro(path: Path):
    lines = path.read_text(errors="replace").splitlines()
    natoms = int(lines[1].strip())
    atoms = []
    for line in lines[2 : 2 + natoms]:
        atoms.append(
            {
                "resnr": int(line[:5]),
                "resname": line[5:10].strip(),
                "atomname": line[10:15].strip(),
                "index": int(line[15:20]),
                "xyz": (float(line[20:28]), float(line[28:36]), float(line[36:44])),
            }
        )
    parts = [float(value) for value in lines[2 + natoms].split()]
    if len(parts) == 3:
        vectors = ((parts[0], 0.0, 0.0), (0.0, parts[1], 0.0), (0.0, 0.0, parts[2]))
    else:
        vectors = (
            (parts[0], parts[3], parts[4]),
            (parts[5], parts[1], parts[6]),
            (parts[7], parts[8], parts[2]),
        )
    return atoms, vectors


def inverse(matrix):
    a, b, c = matrix
    det = (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - b[0] * (a[1] * c[2] - a[2] * c[1])
        + c[0] * (a[1] * b[2] - a[2] * b[1])
    )
    return (
        (
            (b[1] * c[2] - b[2] * c[1]) / det,
            (c[0] * b[2] - b[0] * c[2]) / det,
            (b[0] * c[1] - c[0] * b[1]) / det,
        ),
        (
            (c[1] * a[2] - a[1] * c[2]) / det,
            (a[0] * c[2] - c[0] * a[2]) / det,
            (c[0] * a[1] - a[0] * c[1]) / det,
        ),
        (
            (a[1] * b[2] - b[1] * a[2]) / det,
            (b[0] * a[2] - a[0] * b[2]) / det,
            (a[0] * b[1] - b[0] * a[1]) / det,
        ),
    )


def minimum_image_distance(a, b, vectors):
    matrix = tuple(tuple(vectors[column][row] for column in range(3)) for row in range(3))
    inv = inverse(matrix)
    delta = tuple(a[i] - b[i] for i in range(3))
    fractional = [sum(inv[row][i] * delta[i] for i in range(3)) for row in range(3)]
    fractional = [value - round(value) for value in fractional]
    cartesian = [sum(matrix[row][i] * fractional[i] for i in range(3)) for row in range(3)]
    return math.sqrt(sum(value * value for value in cartesian))


def identity(atom):
    return f"{atom['resnr']}:{atom['resname']}:{atom['atomname']}"


def load_manifest(path: Path) -> dict:
    return next(csv.DictReader(path.open(), delimiter="\t"))


def write_manifest(path: Path, record: dict):
    fields = [
        "candidate",
        "site_id",
        "donor_identities",
        "selection_rationale",
        "starting_state_status",
    ]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerow({key: record[key] for key in fields})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gro", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--ion-resname", required=True, choices=("LIT", "SOD"))
    parser.add_argument("--max-bound-nm", type=float, default=0.55)
    parser.add_argument("--promote", action="store_true", help="Flip manifest to VALIDATED_BOUND on PASS")
    parser.add_argument("--log", type=Path, help="Validation log path")
    args = parser.parse_args()

    # CHARMM-GUI LiCl uses LIT; NaCl uses SOD. Do not remap for .gro lookup.
    ion = args.ion_resname
    if ion in {"LI", "NA"}:
        raise SystemExit(f"Use CHARMM residue name LIT or SOD, not {ion}")

    record = load_manifest(args.manifest)
    locked_ids = record["donor_identities"].split(",")
    atoms, vectors = read_gro(args.gro)
    by_id = {identity(atom): atom for atom in atoms}
    missing = [item for item in locked_ids if item not in by_id]
    if missing:
        print(f"FAIL missing locked donors: {','.join(missing)}", file=sys.stderr)
        return 2

    donors = [by_id[item] for item in locked_ids]
    center = tuple(sum(atom["xyz"][axis] for atom in donors) / len(donors) for axis in range(3))
    ions = [atom for atom in atoms if atom["resname"] == ion]
    if not ions:
        print(f"FAIL no {ion} ions in {args.gro}", file=sys.stderr)
        return 2

    target = min(ions, key=lambda atom: minimum_image_distance(center, atom["xyz"], vectors))
    dist = minimum_image_distance(center, target["xyz"], vectors)
    passed = dist <= args.max_bound_nm
    stamp = time.strftime("%Y-%m-%dT%H:%M:%S")
    lines = [
        f"timestamp\t{stamp}",
        f"gro\t{args.gro}",
        f"manifest\t{args.manifest}",
        f"candidate\t{record['candidate']}",
        f"site_id\t{record['site_id']}",
        f"locked_donors\t{record['donor_identities']}",
        f"ion_resname\t{ion}",
        f"target_ion_index\t{target['index']}",
        f"distance_nm\t{dist:.4f}",
        f"max_bound_nm\t{args.max_bound_nm:.4f}",
        f"result\t{'PASS' if passed else 'FAIL'}",
    ]
    text = "\n".join(lines) + "\n"
    log_path = args.log or args.gro.with_suffix(".bound_validation.log")
    log_path.write_text(text)
    print(text, end="")

    if not passed:
        print(
            f"FAIL distance {dist:.4f} nm > {args.max_bound_nm:.4f} nm — reconstruct before promote",
            file=sys.stderr,
        )
        return 2

    if args.promote:
        if record.get("starting_state_status") != "VALIDATED_BOUND":
            record["starting_state_status"] = "VALIDATED_BOUND"
            write_manifest(args.manifest, record)
            print(f"promoted\t{args.manifest}\tVALIDATED_BOUND")
        else:
            print(f"already\t{args.manifest}\tVALIDATED_BOUND")
    return 0


if __name__ == "__main__":
    sys.exit(main())
