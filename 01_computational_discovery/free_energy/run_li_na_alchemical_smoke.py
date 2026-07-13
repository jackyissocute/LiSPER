#!/usr/bin/env python3
"""Prove native GROMACS Li->Na alchemical plumbing in bulk water.

This is an engine/input smoke test, not a hydration, binding, or selectivity
result.  Method semantics:
https://manual.gromacs.org/2026.0/reference-manual/special/free-energy-implementation.html
https://manual.gromacs.org/2026.0/onlinehelp/gmx-bar.html
"""

from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from pathlib import Path
import argparse
import os
import shutil
import subprocess


LAMBDAS = (0.0, 0.025, 0.05, 0.075, 0.1, 0.2, 0.3, 0.4,
           0.5, 0.6, 0.7, 0.8, 0.9, 1.0)


def run(command: list[str], cwd: Path, stdout: Path) -> None:
    env = os.environ | {"GMX_MAXBACKUP": "-1", "OMP_NUM_THREADS": "1"}
    with stdout.open("w") as handle:
        subprocess.run(command, cwd=cwd, env=env, stdout=handle,
                       stderr=subprocess.STDOUT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gmx", default="/opt/gromacs/2026.0/bin/gmx")
    parser.add_argument("--forcefield", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--steps", type=int, default=25_000,
                        help="Smoke-test steps per lambda (default: 50 ps)")
    parser.add_argument("--seed-base", type=int, default=-1,
                        help="Deterministic base seed; -1 lets grompp record generated seeds")
    args = parser.parse_args()
    if args.steps <= 0:
        raise SystemExit("--steps must be positive")

    out = args.out.resolve()
    if out.exists():
        raise SystemExit(f"Refusing to overwrite existing proof: {out}")
    out.mkdir(parents=True)
    shutil.copy2(args.forcefield, out / "forcefield.itp")
    ff = (out / "forcefield.itp").read_text()
    if not all(token in ff for token in ("LIT", "SOD", "CLA")):
        raise SystemExit("Force field must contain LIT, SOD, and CLA atom types")

    (out / "ion.gro").write_text(
        "Li-to-Na alchemical smoke test\n2\n"
        "    1ION    ION    1   1.500   1.500   1.500\n"
        "    2CLR     CL    2   0.500   0.500   0.500\n"
        "   3.00000   3.00000   3.00000\n"
    )
    (out / "topol.top").write_text(
        '#include "forcefield.itp"\n\n'
        "[ moleculetype ]\nTAG 1\n\n"
        "[ atoms ]\n"
        "; nr type resnr residue atom cgnr charge mass typeB chargeB massB\n"
        "1 LIT 1 ION ION 1 1.0 6.9410 SOD 1.0 22.9898\n\n"
        "[ moleculetype ]\nCLR 1\n\n"
        "[ atoms ]\n1 CLA 1 CLR CL 1 -1.0 35.4500\n\n"
        "[ moleculetype ]\nSOL 2\n\n"
        "[ atoms ]\n"
        "1 OT 1 SOL OW 1 -0.834 15.9994\n"
        "2 HT 1 SOL HW1 2 0.417 1.0080\n"
        "3 HT 1 SOL HW2 3 0.417 1.0080\n\n"
        "[ settles ]\n1 1 0.09572 0.15139\n\n"
        "[ exclusions ]\n1 2 3\n2 1 3\n3 1 2\n\n"
        "[ system ]\nLi-to-Na bulk-water smoke test\n\n"
        "[ molecules ]\nTAG 1\nCLR 1\nSOL 0\n"
    )
    run([args.gmx, "solvate", "-cp", "ion.gro", "-cs", "spc216.gro",
         "-o", "solvated.gro", "-p", "topol.top"], out, out / "solvate.log")

    common = f"""
cutoff-scheme = Verlet
nstlist = 20
rlist = 1.0
coulombtype = PME
rcoulomb = 1.0
vdwtype = Cut-off
rvdw = 1.0
pbc = xyz
free-energy = yes
fep-lambdas = {' '.join(map(str, LAMBDAS))}
init-lambda-state = 0
calc-lambda-neighbors = -1
sc-alpha = 0
"""
    (out / "min.mdp").write_text(
        "integrator = steep\nnsteps = 5000\nemtol = 1000\n" + common
    )
    run([args.gmx, "grompp", "-f", "min.mdp", "-c", "solvated.gro",
         "-p", "topol.top", "-o", "min.tpr"], out, out / "min.grompp.log")
    run([args.gmx, "mdrun", "-deffnm", "min", "-ntmpi", "1", "-ntomp", "1"],
        out, out / "min.mdrun.log")

    production = f"""
integrator = md
dt = 0.002
nsteps = {args.steps}
continuation = no
gen-vel = yes
gen-temp = 298.15
gen-seed = -1
tcoupl = v-rescale
tc-grps = System
tau-t = 1.0
ref-t = 298.15
pcoupl = no
nstenergy = 100
nstlog = 500
nstxout-compressed = 500
nstdhdl = 100
dhdl-derivatives = yes
dhdl-print-energy = total
separate-dhdl-file = yes
constraints = h-bonds
{common}
"""
    jobs: list[tuple[Path, list[str], Path]] = []
    for state in range(len(LAMBDAS)):
        window = out / f"lambda_{state:02d}"
        window.mkdir()
        seed = -1 if args.seed_base < 0 else args.seed_base + state
        mdp = production.replace("init-lambda-state = 0", f"init-lambda-state = {state}")
        mdp = mdp.replace("gen-seed = -1", f"gen-seed = {seed}")
        (window / "run.mdp").write_text(mdp)
        run([args.gmx, "grompp", "-f", "run.mdp", "-c", "../min.gro",
             "-p", "../topol.top", "-o", "run.tpr"], window,
            window / "grompp.log")
        jobs.append((window, [args.gmx, "mdrun", "-deffnm", "run",
                              "-ntmpi", "1", "-ntomp", "1"],
                     window / "mdrun.log"))
    with ThreadPoolExecutor(max_workers=len(LAMBDAS)) as pool:
        list(pool.map(lambda job: run(job[1], job[0], job[2]), jobs))

    # With -deffnm run, GROMACS 2026 names the separate DHDL file run.xvg.
    dhdl = [str(Path(f"lambda_{state:02d}") / "run.xvg") for state in range(len(LAMBDAS))]
    run([args.gmx, "bar", "-f", *dhdl, "-o", "bar.xvg", "-oi", "barint.xvg"],
        out, out / "bar.log")
    for file in [out / "forcefield.itp", out / "topol.top", out / "min.mdp",
                 *[out / f"lambda_{i:02d}" / "run.mdp" for i in range(len(LAMBDAS))]]:
        with (out / "SHA256SUMS").open("a") as manifest:
            manifest.write(f"{sha256(file.read_bytes()).hexdigest()}  {file.relative_to(out)}\n")
    print(f"smoke_test_complete\t{out}")
    print("interpretation\tGROMACS plumbing only; numerical free energy is not scientific")


if __name__ == "__main__":
    main()
