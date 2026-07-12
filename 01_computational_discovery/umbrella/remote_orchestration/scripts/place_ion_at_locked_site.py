#!/usr/bin/env python3
"""Move nearest target ion to locked-site centroid in a .gro (no Jacky/xtc needed).

Writes a new gro. Follow with short gmx grompp/mdrun minimize on remote.
"""
from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def read_gro(path: Path):
    lines = path.read_text(errors="replace").splitlines()
    title = lines[0]
    natoms = int(lines[1])
    atoms = lines[2 : 2 + natoms]
    box = lines[2 + natoms]
    return title, atoms, box


def write_gro(path: Path, title, atoms, box):
    path.write_text(title + "\n" + f"{len(atoms):5d}\n" + "\n".join(atoms) + "\n" + box + "\n")


def parse_atom(line):
    return {
        "resnr": int(line[:5]),
        "resname": line[5:10].strip(),
        "atomname": line[10:15].strip(),
        "index": int(line[15:20]),
        "xyz": [float(line[20:28]), float(line[28:36]), float(line[36:44])],
        "raw": line,
    }


def format_atom(atom):
    x, y, z = atom["xyz"]
    return f"{atom['resnr']:5d}{atom['resname']:<5}{atom['atomname']:>5}{atom['index']:5d}{x:8.3f}{y:8.3f}{z:8.3f}"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--gro", type=Path, required=True)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--ion-resname", required=True)
    p.add_argument("--target-distance-nm", type=float, default=0.35)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()

    record = next(csv.DictReader(args.manifest.open(), delimiter="\t"))
    locked = record["donor_identities"].split(",")
    title, atom_lines, box = read_gro(args.gro)
    atoms = [parse_atom(line) for line in atom_lines]
    by_id = {f"{a['resnr']}:{a['resname']}:{a['atomname']}": a for a in atoms}
    missing = [x for x in locked if x not in by_id]
    if missing:
        raise SystemExit(f"missing donors: {missing}")
    donors = [by_id[x] for x in locked]
    center = [sum(a["xyz"][i] for a in donors) / len(donors) for i in range(3)]
    ions = [a for a in atoms if a["resname"] == args.ion_resname]
    if not ions:
        raise SystemExit(f"no {args.ion_resname}")

    def dist(a, b):
        return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))

    target = min(ions, key=lambda a: dist(a["xyz"], center))
    old = dist(target["xyz"], center)
    # Move ion along vector to sit at target-distance from centroid
    vec = [target["xyz"][i] - center[i] for i in range(3)]
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    scale = args.target_distance_nm / norm
    target["xyz"] = [center[i] + vec[i] * scale for i in range(3)]
    # rewrite that atom line
    for i, a in enumerate(atoms):
        if a["index"] == target["index"]:
            atoms[i] = target
            break
    out_lines = [format_atom(a) for a in atoms]
    write_gro(args.out, title + " placed_ion", out_lines, box)
    new = dist(target["xyz"], center)
    print(f"ion_index\t{target['index']}")
    print(f"old_distance_nm\t{old:.4f}")
    print(f"new_distance_nm\t{new:.4f}")
    print(f"out\t{args.out}")


if __name__ == "__main__":
    main()
