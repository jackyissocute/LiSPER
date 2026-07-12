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
    n = 0
    for line in gro.read_text(errors="ignore").splitlines()[2:]:
        if len(line) >= 10 and line[5:10].strip() == name:
            n += 1
    return n


def ensure_nacl_topol(gmx_dir: Path, cand: str, gro: Path):
    top = gmx_dir / "topol.top"
    if top.exists():
        return top
    licl = ROOT / "LiSPER_8cand_LiCl" / "systems" / cand / "gromacs"
    if not (licl / "toppar" / "PROA.itp").exists():
        return None
    toppar = gmx_dir / "toppar"
    toppar.mkdir(exist_ok=True)
    for f in ["forcefield.itp", "PROA.itp", "TIP3.itp", "CLA.itp"]:
        src = licl / "toppar" / f
        if src.exists():
            (toppar / f).write_bytes(src.read_bytes())
    sod = ROOT / "LiSPER_8cand_NaCl_prod_worker/systems/LiLC-1/gromacs/toppar/SOD.itp"
    if sod.exists():
        (toppar / "SOD.itp").write_bytes(sod.read_bytes())
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
