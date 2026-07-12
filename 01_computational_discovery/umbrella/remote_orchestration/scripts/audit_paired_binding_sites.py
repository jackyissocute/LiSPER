from pathlib import Path
import argparse
import csv
import math


def read_gro(path):
    lines = path.read_text().splitlines()
    atoms = []
    for line in lines[2:-1]:
        try:
            atoms.append(
                {
                    "resnr": int(line[:5]),
                    "resname": line[5:10].strip(),
                    "atomname": line[10:15].strip(),
                    "index": int(line[15:20]),
                    "xyz": tuple(float(line[start : start + 8]) for start in (20, 28, 36)),
                }
            )
        except ValueError:
            continue
    parts = [float(value) for value in lines[-1].split()]
    vectors = (
        ((parts[0], 0.0, 0.0), (0.0, parts[1], 0.0), (0.0, 0.0, parts[2]))
        if len(parts) == 3
        else ((parts[0], parts[3], parts[4]), (parts[5], parts[1], parts[6]), (parts[7], parts[8], parts[2]))
    )
    return atoms, vectors


def identity(atom):
    return f"{atom['resnr']}:{atom['resname']}:{atom['atomname']}"


def inverse(matrix):
    a, b, c = matrix
    det = a[0] * (b[1] * c[2] - b[2] * c[1]) - b[0] * (a[1] * c[2] - a[2] * c[1]) + c[0] * (a[1] * b[2] - a[2] * b[1])
    return (
        ((b[1] * c[2] - b[2] * c[1]) / det, (c[0] * b[2] - b[0] * c[2]) / det, (b[0] * c[1] - c[0] * b[1]) / det),
        ((c[1] * a[2] - a[1] * c[2]) / det, (a[0] * c[2] - c[0] * a[2]) / det, (c[0] * a[1] - a[0] * c[1]) / det),
        ((a[1] * b[2] - b[1] * a[2]) / det, (b[0] * a[2] - a[0] * b[2]) / det, (a[0] * b[1] - b[0] * a[1]) / det),
    )


def minimum_image_distance(a, b, vectors):
    matrix = tuple(tuple(vectors[column][row] for column in range(3)) for row in range(3))
    inv = inverse(matrix)
    delta = tuple(a[i] - b[i] for i in range(3))
    fractional = [sum(inv[row][i] * delta[i] for i in range(3)) for row in range(3)]
    fractional = [value - round(value) for value in fractional]
    cartesian = [sum(matrix[row][i] * fractional[i] for i in range(3)) for row in range(3)]
    return math.sqrt(sum(value * value for value in cartesian))


def condition_record(root, candidate, locked_ids):
    umbrella = root / "systems" / candidate / "gromacs" / "umbrella_sampling_binding_site_v2"
    metadata = next(csv.DictReader((umbrella / "umbrella_metadata.tsv").open(), delimiter="\t"))
    atoms, vectors = read_gro(umbrella / "representative_full_system.gro")
    by_index = {atom["index"]: atom for atom in atoms}
    by_identity = {identity(atom): atom for atom in atoms}
    missing = [item for item in locked_ids if item not in by_identity]
    if missing:
        raise RuntimeError(f"{candidate}: missing locked donors in {root.name}: {','.join(missing)}")
    donors = [by_identity[item] for item in locked_ids]
    center = tuple(sum(atom["xyz"][axis] for atom in donors) / len(donors) for axis in range(3))
    ions = [atom for atom in atoms if atom["resname"] == metadata["ion_resname"]]
    target = min(ions, key=lambda atom: minimum_image_distance(center, atom["xyz"], vectors))
    current_indices = [int(value) for value in metadata["binding_site_atoms"].split(",")]
    return {
        "current_indices": ",".join(map(str, current_indices)),
        "current_identities": ",".join(identity(by_index[index]) for index in current_indices),
        "locked_indices": ",".join(str(atom["index"]) for atom in donors),
        "target_index": str(target["index"]),
        "initial_distance_nm": f"{minimum_image_distance(center, target['xyz'], vectors):.4f}",
    }


def find_nacl_root(roots, candidate):
    for root in roots:
        if (root / "systems" / candidate).exists():
            return root
    raise FileNotFoundError(candidate)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--design", type=Path, required=True)
    parser.add_argument("--licl-root", type=Path, required=True)
    parser.add_argument("--nacl-root", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest-dir", type=Path, required=True)
    args = parser.parse_args()

    rows = []
    args.manifest_dir.mkdir(parents=True, exist_ok=True)
    for design in csv.DictReader(args.design.open(), delimiter="\t"):
        candidate = design["candidate"]
        locked_ids = design["donor_identities"].split(",")
        li = condition_record(args.licl_root, candidate, locked_ids)
        na = condition_record(find_nacl_root(args.nacl_root, candidate), candidate, locked_ids)
        li_current = set(li["current_identities"].split(","))
        na_current = set(na["current_identities"].split(","))
        overlap = sorted(li_current & na_current)
        classification = (
            "SITE_LOCKED"
            if li_current == na_current == set(locked_ids)
            else "SITE_MISMATCH_PARTIAL_OVERLAP_REVIEW"
            if overlap
            else "SITE_MISMATCH_RERUN_REQUIRED"
        )
        row = {
            "candidate": candidate,
            "classification": classification,
            "site_id": design["site_id"],
            "locked_identities": design["donor_identities"],
            "selection_rationale": design["rationale"],
            "li_current_identities": li["current_identities"],
            "na_current_identities": na["current_identities"],
            "current_overlap": ",".join(overlap),
            "li_locked_indices": li["locked_indices"],
            "na_locked_indices": na["locked_indices"],
            "li_target_index": li["target_index"],
            "na_target_index": na["target_index"],
            "li_initial_distance_nm": li["initial_distance_nm"],
            "na_initial_distance_nm": na["initial_distance_nm"],
        }
        rows.append(row)
        manifest = args.manifest_dir / f"{candidate}.tsv"
        with manifest.open("w", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
                    "candidate",
                    "site_id",
                    "donor_identities",
                    "selection_rationale",
                    "starting_state_status",
                ],
                delimiter="\t",
            )
            writer.writeheader()
            writer.writerow(
                {
                    "candidate": candidate,
                    "site_id": design["site_id"],
                    "donor_identities": design["donor_identities"],
                    "selection_rationale": design["rationale"],
                    "starting_state_status": "PROPOSED_REQUIRES_RECONSTRUCTION",
                }
            )
    with args.output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0], delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
