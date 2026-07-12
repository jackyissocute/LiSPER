#!/usr/bin/env python3
"""Place+min+validate locked-site bound starts for non-pilot candidates.

Skip umbrella launch. Promote manifest to VALIDATED_BOUND only when BOTH ions PASS.
LiLC-1 is excluded (already validated / running).
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


def ensure_sod_atomtype(forcefield: Path) -> None:
    """LiCl-derived forcefield.itp often lacks SOD; grompp then fails on SOD.itp."""
    if not forcefield.exists():
        return
    text = forcefield.read_text(errors="replace")
    if any(ln.split()[:1] == ["SOD"] for ln in text.splitlines()):
        return
    lines = text.splitlines()
    out: list[str] = []
    in_atomtypes = False
    inserted = False
    for ln in lines:
        if ln.strip().startswith("["):
            if "atomtypes" in ln:
                in_atomtypes = True
            elif in_atomtypes and not inserted:
                out.append(SOD_ATOMTYPE_LINE)
                inserted = True
                in_atomtypes = False
            else:
                in_atomtypes = False
        if in_atomtypes and ln.split()[:1] == ["LIT"] and not inserted:
            out.append(ln)
            out.append(SOD_ATOMTYPE_LINE)
            inserted = True
            continue
        out.append(ln)
    if not inserted:
        out.append(SOD_ATOMTYPE_LINE)
    forcefield.write_text("\n".join(out) + ("\n" if text.endswith("\n") else ""))


def ensure_nacl_topol(gmx_dir: Path, cand: str, gro: Path):
    top = gmx_dir / "topol.top"
    toppar = gmx_dir / "toppar"
    sod_itp = ROOT / "LiSPER_8cand_NaCl_prod_worker/systems/LiLC-1/gromacs/toppar/SOD.itp"
    if top.exists():
        # Prior auto-builds copied LiCl forcefield (LIT only) + SOD.itp → grompp Atomtype SOD missing.
        ensure_sod_atomtype(toppar / "forcefield.itp")
        if sod_itp.exists() and not (toppar / "SOD.itp").exists():
            toppar.mkdir(exist_ok=True)
            (toppar / "SOD.itp").write_bytes(sod_itp.read_bytes())
        return top
    licl = ROOT / "LiSPER_8cand_LiCl" / "systems" / cand / "gromacs"
    if not (licl / "toppar" / "PROA.itp").exists():
        return None
    toppar.mkdir(exist_ok=True)
    for f in ["forcefield.itp", "PROA.itp", "TIP3.itp", "CLA.itp"]:
        src = licl / "toppar" / f
        if src.exists():
            (toppar / f).write_bytes(src.read_bytes())
    if sod_itp.exists():
        (toppar / "SOD.itp").write_bytes(sod_itp.read_bytes())
    ensure_sod_atomtype(toppar / "forcefield.itp")
    n_sod = count_res(gro, "SOD")
    n_cla = count_res(gro, "CLA")
    n_tip = count_res(gro, "TIP3")
    if n_sod == 0:
        return None
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


def prep_one(cand: str, ion: str) -> str:
    work, ion_res = ION_MAP[ion]
    gmx_dir = ROOT / work / "systems" / cand / "gromacs"
    man = ROOT / "paired_binding_sites" / f"{cand}.tsv"
    if not man.exists():
        return f"{cand}/{ion}\tBLOCKED\tno_manifest"
    gro_src = gmx_dir / "run_prod_20ns" / "step5_production_20ns.gro"
    if not gro_src.exists():
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
        top = ensure_nacl_topol(gmx_dir, cand, gro_src) or top
    if not Path(top).exists():
        return f"{cand}/{ion}\tBLOCKED\tmissing_topol"
    top = sync_topol_counts(Path(top), placed)

    bdir = umb / "bound_place_min"
    bdir.mkdir(exist_ok=True)
    (bdir / "min.mdp").write_text(MIN_MDP)
    gp = run(
        f"{GMX} && gmx grompp -f min.mdp -c {placed} -p {top} -o min.tpr -maxwarn 2",
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
    out_log.write_text(v.stdout + v.stderr)
    if v.returncode != 0:
        return f"{cand}/{ion}\tFAIL_VALIDATE\t{(v.stdout or v.stderr).strip()[:160]}"
    return f"{cand}/{ion}\tPASS_ION\tdistance_ok"


def main():
    rows = []
    for cand in CANDS:
        ion_ok = {}
        for ion in ("LiCl", "NaCl"):
            print(f"## {cand} {ion}", flush=True)
            try:
                row = prep_one(cand, ion)
            except Exception as exc:  # noqa: BLE001
                row = f"{cand}/{ion}\tERROR\t{exc}"
            print(row, flush=True)
            rows.append(row)
            ion_ok[ion] = row.split("\t")[1] == "PASS_ION"
        if ion_ok.get("LiCl") and ion_ok.get("NaCl"):
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
            v = run(
                f"python3 {SCRIPTS}/validate_bound_start.py --gro {gro} --manifest {man} "
                f"--ion-resname LIT --promote"
            )
            row = f"{cand}/BOTH\tPROMOTE\trc={v.returncode}\t{(v.stdout or '').strip()[:80]}"
        else:
            row = f"{cand}/BOTH\tHOLD\twait_both_ions"
        print(row, flush=True)
        rows.append(row)
    summary = ROOT / "logs" / "bound_prep" / "summary.tsv"
    summary.parent.mkdir(parents=True, exist_ok=True)
    summary.write_text("record\n" + "\n".join(rows) + "\n")
    print("SUMMARY", summary, flush=True)


if __name__ == "__main__":
    main()
