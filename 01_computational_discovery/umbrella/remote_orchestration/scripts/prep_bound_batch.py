#!/usr/bin/env python3
"""Place, minimize, and geometry-screen locked-site starts for non-pilot candidates.

Skip umbrella launch. Record the manifest only when both ions are within the
declared distance screen. This does not validate binding or PMF reliability.
LiLC-1 is excluded (already screened / running).
"""
from __future__ import annotations

import csv
import subprocess
from pathlib import Path

ROOT = Path("/data/LiSPER_remote")
SCRIPTS = ROOT / "scripts"
GMX = "export PATH=/opt/gromacs/2026.0/bin:/usr/local/bin:$PATH"
CANDS = [
    "LiD3-Core",
    "LiD3-Flex",
    "LiND-Hybrid",
    "LiDS-1",
    "LiDA-1",
    "LiN3-Core",
    "LiA3-Ref",
]
ION_MAP = {
    "LiCl": ("LiSPER_8cand_LiCl", "LIT"),
    "NaCl": ("LiSPER_8cand_NaCl_prod_worker", "SOD"),
}
MIN_MDP = """integrator = steep
nsteps = 500
emtol = 1000.0
emstep = 0.01
nstlist = 10
cutoff-scheme = Verlet
rlist = 1.2
rcoulomb = 1.2
rvdw = 1.2
pbc = xyz
"""


def run(cmd, cwd=None):
    return subprocess.run(cmd, shell=True, cwd=cwd, text=True, capture_output=True)


def count_res(gro: Path, name: str) -> int:
    """Count molecules (unique resnr) with this residue name — not atoms."""
    seen = set()
    for line in gro.read_text(errors="ignore").splitlines()[2:]:
        if len(line) < 10:
            continue
        if line[5:10].strip() != name:
            continue
        try:
            resnr = int(line[:5])
        except ValueError:
            continue
        seen.add(resnr)
    return len(seen)


def sync_topol_counts(top: Path, gro: Path) -> Path:
    """Rewrite [ molecules ] ion/water counts to match gro (fixes CHARMM-GUI drift)."""
    text = top.read_text(errors="replace")
    if "[ molecules ]" not in text:
        return top
    head, _, rest = text.partition("[ molecules ]")
    lines = rest.splitlines()
    out = [head + "[ molecules ]"]
    # keep header comment lines until first compound
    i = 0
    while i < len(lines) and (not lines[i].strip() or lines[i].strip().startswith(";")):
        out.append(lines[i])
        i += 1
    compounds = []
    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip() or line.strip().startswith(";"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            compounds.append(parts[0])
    counts = {name: count_res(gro, name) for name in compounds}
    # PROA stays 1 even if naming differs
    for name in compounds:
        n = 1 if name == "PROA" else counts.get(name, 0)
        out.append(f"{name} {n}")
    synced = top.with_name(top.stem + "_boundprep.top")
    # includes are relative to gmx_dir; write beside original
    synced.write_text("\n".join(out) + "\n")
    return synced


SOD_ATOMTYPE_LINE = (
    "     SOD    11    22.9898      1.000     A    2.51367073323e-01    1.962296e-01 "
)
# CHARMM36 NBFIX converted by CHARMM-GUI and cross-checked against an independently
# generated NaCl topology. SOD-OC: Venable et al., DOI 10.1021/jp401512z;
# CLA-SOD: Savelyev & MacKerell, DOI 10.1021/acs.jpcb.5b00683.
SOD_NBFIX_LINES = (
    "    CLA     SOD     1  3.32394311738e-01  3.51037600000e-01 ",
    "    SOD      OC     1  2.87760285959e-01  3.13883680000e-01 ",
)


def ensure_sod_parameters(forcefield: Path) -> None:
    """Add the CHARMM-GUI SOD atom type and Na-Cl/Na-carboxylate NBFIX terms."""
    if not forcefield.exists():
        return
    text = forcefield.read_text(errors="replace")
    lines = text.splitlines()
    if not any(ln.split()[:1] == ["SOD"] for ln in lines):
        for i, ln in enumerate(lines):
            if ln.split()[:1] == ["LIT"]:
                lines.insert(i + 1, SOD_ATOMTYPE_LINE)
                break
        else:
            raise RuntimeError(f"Cannot locate atomtypes insertion point in {forcefield}")

    pairs = {frozenset(ln.split()[:2]) for ln in lines if len(ln.split()) >= 5}
    missing = [ln for ln in SOD_NBFIX_LINES if frozenset(ln.split()[:2]) not in pairs]
    if missing:
        start = next((i for i, ln in enumerate(lines) if "nonbond_params" in ln), None)
        if start is None:
            lines.extend(["", "[ nonbond_params ]", "; i j func sigma epsilon", *missing])
        else:
            end = next((i for i in range(start + 1, len(lines)) if lines[i].strip().startswith("[")), len(lines))
            lines[end:end] = missing
    forcefield.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""))


def ensure_nacl_topol(gmx_dir: Path, cand: str, gro: Path):
    top = gmx_dir / "topol.top"
    licl = ROOT / "LiSPER_8cand_LiCl" / "systems" / cand / "gromacs"
    toppar = gmx_dir / "toppar"
    toppar.mkdir(exist_ok=True)
    sod_itp = ROOT / "LiSPER_8cand_NaCl_prod_worker/systems/LiLC-1/gromacs/toppar/SOD.itp"
    if (licl / "toppar" / "PROA.itp").exists():
        for f in ["forcefield.itp", "PROA.itp", "TIP3.itp", "CLA.itp"]:
            src = licl / "toppar" / f
            if src.exists() and (f == "forcefield.itp" or not (toppar / f).exists()):
                (toppar / f).write_bytes(src.read_bytes())
    if sod_itp.exists():
        (toppar / "SOD.itp").write_bytes(sod_itp.read_bytes())
    ensure_sod_parameters(toppar / "forcefield.itp")
    n_sod = count_res(gro, "SOD")
    n_cla = count_res(gro, "CLA")
    n_tip = count_res(gro, "TIP3")
    if n_sod == 0:
        return top if top.exists() else None
    top.write_text(
        f";; auto {cand} NaCl\n"
        '#include "toppar/forcefield.itp"\n'
        '#include "toppar/PROA.itp"\n'
        '#include "toppar/SOD.itp"\n'
        '#include "toppar/CLA.itp"\n'
        '#include "toppar/TIP3.itp"\n\n'
        f"[ system ]\n{cand} NaCl\n\n[ molecules ]\n"
        f"PROA 1\nSOD {n_sod}\nCLA {n_cla}\nTIP3 {n_tip}\n"
    )
    return top


def resolve_gro_src(gmx_dir: Path, cand: str, ion: str) -> Path | None:
    """Prefer real NaCl prod; else eq; else LiCl→SOD identity swap for locked-site prep."""
    seed_marker = gmx_dir / "run_prod_20ns" / "SEEDED_FROM_LICL.txt"
    prod = gmx_dir / "run_prod_20ns" / "step5_production_20ns.gro"
    eq = gmx_dir / "run_eq" / "step4.1_equilibration.gro"
    for path in (prod, eq):
        if not path.exists():
            continue
        if path == prod and seed_marker.exists():
            continue  # regenerate seed below
        try:
            nat = int(path.read_text(errors="ignore").splitlines()[1])
        except (IndexError, ValueError):
            continue
        if nat > 1000:
            return path
    if ion != "NaCl":
        return None
    licl = (
        ROOT
        / "LiSPER_8cand_LiCl"
        / "systems"
        / cand
        / "gromacs"
        / "run_prod_20ns"
        / "step5_production_20ns.gro"
    )
    if not licl.exists():
        return None
    out = gmx_dir / "run_prod_20ns" / "step5_production_20ns.gro"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = licl.read_text(errors="replace").splitlines()
    nat = int(lines[1])
    atoms = []
    for line in lines[2 : 2 + nat]:
        if len(line) >= 15 and line[5:10].strip() == "LIT":
            line = line[:5] + f"{'SOD':<5}" + f"{'SOD':>5}" + line[15:]
        atoms.append(line)
    note = f"{lines[0]} | seeded_from_LiCl_LIT_to_SOD_for_bound_prep"
    out.write_text(note + "\n" + f"{nat:5d}\n" + "\n".join(atoms) + "\n" + lines[2 + nat] + "\n")
    seed_marker.write_text(
        "NaCl prod gro missing on host; LIT→SOD copy of LiCl prod for locked-site place only.\n"
        f"source={licl}\n"
    )
    return out


def placed_ion_index(place_stdout: str) -> int | None:
    for line in place_stdout.splitlines():
        if line.startswith("ion_index\t"):
            return int(line.split("\t", 1)[1])
    return None


def write_ion_posres(ndx_path: Path, itp_path: Path, ion_index: int) -> None:
    ndx_path.write_text(f"[ placed_ion ]\n{ion_index}\n")
    itp_path.write_text(
        "; position restraints on placed ion during bound min\n"
        "[ position_restraints ]\n"
        ";  i funct       fcx        fcy        fcz\n"
        "   1    1       4000       4000       4000\n"
    )


def prep_one(cand: str, ion: str) -> str:
    work, ion_res = ION_MAP[ion]
    gmx_dir = ROOT / work / "systems" / cand / "gromacs"
    man = ROOT / "paired_binding_sites" / f"{cand}.tsv"
    if not man.exists():
        return f"{cand}/{ion}\tBLOCKED\tno_manifest"
    gro_src = resolve_gro_src(gmx_dir, cand, ion)
    if gro_src is None:
        return f"{cand}/{ion}\tBLOCKED\tmissing_prod_gro"
    umb = gmx_dir / "umbrella_sampling"
    umb.mkdir(exist_ok=True)
    out_log = ROOT / "logs" / "bound_prep" / f"{cand}_{ion}.log"
    out_log.parent.mkdir(parents=True, exist_ok=True)

    placed = umb / "representative_full_system.placed.gro"
    p = run(
        f"python3 {SCRIPTS}/place_ion_at_locked_site.py --gro {gro_src} --manifest {man} "
        f"--ion-resname {ion_res} --out {placed}"
    )
    if p.returncode != 0:
        out_log.write_text(p.stdout + p.stderr)
        return f"{cand}/{ion}\tFAIL_PLACE\t{(p.stderr or p.stdout).strip()[:160]}"

    top = gmx_dir / "topol.top"
    if ion == "NaCl":
        top = ensure_nacl_topol(gmx_dir, cand, placed) or top
    if not Path(top).exists():
        return f"{cand}/{ion}\tBLOCKED\tmissing_topol"
    top = sync_topol_counts(Path(top), placed)

    bdir = umb / "bound_place_min"
    bdir.mkdir(exist_ok=True)
    ion_idx = placed_ion_index(p.stdout)
    mdp = MIN_MDP
    gp_extra = ""
    if ion_idx:
        write_ion_posres(bdir / "ion.ndx", bdir / "posre_ion.itp", ion_idx)
        mdp = MIN_MDP + (
            f"\n; freeze placed ion index {ion_idx} during EM\n"
            "freezegrps = placed_ion\n"
            "freezedim = Y Y Y\n"
        )
        gp_extra = f" -n {bdir / 'ion.ndx'}"

    (bdir / "min.mdp").write_text(mdp)
    gp = run(
        f"{GMX} && gmx grompp -f min.mdp -c {placed} -p {top} -o min.tpr{gp_extra}",
        cwd=bdir,
    )
    if gp.returncode != 0:
        (bdir / "grompp.log").write_text(gp.stdout + gp.stderr)
        out_log.write_text(gp.stdout + gp.stderr)
        return f"{cand}/{ion}\tFAIL_GROMPP\tsee_log"

    md = run(
        f"{GMX} && OMP_NUM_THREADS=4 gmx mdrun -deffnm min -ntmpi 1 -ntomp 4",
        cwd=bdir,
    )
    if md.returncode != 0 or not (bdir / "min.gro").exists():
        out_log.write_text(md.stdout + md.stderr)
        return f"{cand}/{ion}\tFAIL_MIN\tsee_log"

    final = umb / "representative_full_system.gro"
    final.write_bytes((bdir / "min.gro").read_bytes())

    v = run(
        f"python3 {SCRIPTS}/validate_bound_start.py --gro {final} --manifest {man} "
        f"--ion-resname {ion_res}"
    )
    out_log.write_text(
        f"gro_src\t{gro_src}\nion_index\t{ion_idx}\n" + v.stdout + v.stderr
    )
    if v.returncode != 0:
        # re-place on min output if EM drifted a different ion into "nearest"
        placed2 = umb / "representative_full_system.replaced.gro"
        p2 = run(
            f"python3 {SCRIPTS}/place_ion_at_locked_site.py --gro {final} --manifest {man} "
            f"--ion-resname {ion_res} --out {placed2}"
        )
        if p2.returncode == 0:
            final.write_bytes(placed2.read_bytes())
            v = run(
                f"python3 {SCRIPTS}/validate_bound_start.py --gro {final} --manifest {man} "
                f"--ion-resname {ion_res}"
            )
            out_log.write_text(out_log.read_text() + "\n## replace_after_min\n" + p2.stdout + v.stdout)
            if v.returncode == 0:
                return f"{cand}/{ion}\tBOUND_DISTANCE_SCREENED\tdistance_ok_after_replace"
        return f"{cand}/{ion}\tGEOMETRY_SCREEN_FAILED\t{(v.stdout or v.stderr).strip()[:160]}"
    return f"{cand}/{ion}\tBOUND_DISTANCE_SCREENED\tdistance_ok"


def promote_if_both(cand: str) -> str:
    man = ROOT / "paired_binding_sites" / f"{cand}.tsv"
    gro = (
        ROOT
        / "LiSPER_8cand_LiCl"
        / "systems"
        / cand
        / "gromacs"
        / "umbrella_sampling"
        / "representative_full_system.gro"
    )
    gro_na = (
        ROOT
        / "LiSPER_8cand_NaCl_prod_worker"
        / "systems"
        / cand
        / "gromacs"
        / "umbrella_sampling"
        / "representative_full_system.gro"
    )
    if not gro.exists() or not gro_na.exists():
        return f"{cand}/BOTH\tHOLD\twait_both_ions"
    v_li = run(
        f"python3 {SCRIPTS}/validate_bound_start.py --gro {gro} --manifest {man} "
        f"--ion-resname LIT"
    )
    v_na = run(
        f"python3 {SCRIPTS}/validate_bound_start.py --gro {gro_na} --manifest {man} "
        f"--ion-resname SOD"
    )
    if v_li.returncode == 0 and v_na.returncode == 0:
        v_p = run(
            f"python3 {SCRIPTS}/validate_bound_start.py --gro {gro} --manifest {man} "
            f"--ion-resname LIT --record"
        )
        return f"{cand}/BOTH\tPROMOTE\trc={v_p.returncode}\t{(v_p.stdout or '').strip()[:80]}"
    return f"{cand}/BOTH\tHOLD\tli={v_li.returncode},na={v_na.returncode}"


def main():
    import sys

    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    cands = only or CANDS
    ions = ("NaCl",) if only else ("LiCl", "NaCl")
    rows = []
    for cand in cands:
        ion_ok = {}
        for ion in ions:
            print(f"## {cand} {ion}", flush=True)
            try:
                row = prep_one(cand, ion)
            except Exception as exc:  # noqa: BLE001
                row = f"{cand}/{ion}\tERROR\t{exc}"
            print(row, flush=True)
            rows.append(row)
            ion_ok[ion] = row.split("\t")[1] == "BOUND_DISTANCE_SCREENED"
        # if only NaCl retry, still check both sides for promote
        row = promote_if_both(cand)
        print(row, flush=True)
        rows.append(row)
    summary = ROOT / "logs" / "bound_prep" / "summary.tsv"
    summary.parent.mkdir(parents=True, exist_ok=True)
    prev = summary.read_text() if summary.exists() else "record\n"
    summary.write_text(prev.rstrip() + "\n# retry\n" + "\n".join(rows) + "\n")
    print("SUMMARY", summary, flush=True)


if __name__ == "__main__":
    main()
