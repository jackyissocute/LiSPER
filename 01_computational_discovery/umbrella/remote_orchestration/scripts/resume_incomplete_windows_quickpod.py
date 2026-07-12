#!/usr/bin/env python3
"""Resume incomplete binding-site v2 umbrella windows on QuickPod with authentic gmx.

Uses only local QuickPod paths under /data/LiSPER_remote (no GCP mount paths).
Each job: gmx mdrun -ntmpi 1 -ntomp 1. Cap concurrent jobs for 126-thread host.
Deletes compressed xtc after Finished mdrun to protect 100 GB disk.
"""
from __future__ import annotations

import fcntl
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(os.environ.get("LISPER_REMOTE_ROOT", "/data/LiSPER_remote"))
LIMIT = int(os.environ.get("LISPER_GLOBAL_MDRUN_LIMIT", "120"))
LOCK = Path(os.environ.get("LISPER_GLOBAL_MDRUN_LOCK", "/tmp/lisper_gmx_mdrun.lock"))
GMX = os.environ.get(
    "LISPER_GMX",
    "export PATH=/opt/gromacs/2026.0/bin:/usr/local/bin:$HOME/.local/bin:$PATH",
)
QUEUE = ROOT / "quickpod_resume_queue.tsv"
LOGDIR = ROOT / "logs" / "quickpod_resume"
SUBDIR = "umbrella_sampling_binding_site_v2"


def finished(log: Path) -> bool:
    return log.exists() and "Finished mdrun" in log.read_text(errors="replace")


def count_mdrun() -> int:
    count = 0
    for proc in Path("/proc").glob("[0-9]*"):
        try:
            cmdline = (proc / "cmdline").read_bytes().replace(b"\0", b" ").decode(errors="replace")
        except OSError:
            continue
        if "gmx" in cmdline and "mdrun" in cmdline and "pgrep" not in cmdline:
            count += 1
    return count


def wait_for_slot(timeout=7200):
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    deadline = time.time() + timeout
    while True:
        with LOCK.open("a+") as handle:
            fcntl.flock(handle, fcntl.LOCK_EX)
            n = count_mdrun()
            fcntl.flock(handle, fcntl.LOCK_UN)
        if n < LIMIT:
            return
        if time.time() > deadline:
            raise TimeoutError(f"mdrun slot timeout at {n}/{LIMIT}")
        time.sleep(3)


def run_mdrun(cwd: Path, deffnm: str, cpt: Path | None) -> int:
    # -noappend: critical files were migrated without prior xtc/pullx/pullf/edr parts
    # that checkpoint append expects. Authentic gmx still continues from .cpt.
    resume = f" -cpi {cpt.name} -noappend" if cpt and cpt.exists() else ""
    cmd = f"{GMX} && OMP_NUM_THREADS=1 gmx mdrun -deffnm {deffnm}{resume} -ntmpi 1 -ntomp 1"
    wait_for_slot()
    proc = subprocess.run(
        ["bash", "-lc", cmd],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    (cwd / f"{deffnm}.mdrun.stdout.log").write_text(proc.stdout)
    return proc.returncode


def grompp(cwd: Path, mdp: Path, gro: Path, deffnm: str, ndx: Path, tops: list[Path]) -> bool:
    tpr = cwd / f"{deffnm}.tpr"
    log = cwd / f"{deffnm}.grompp.log"
    chunks = []
    for top in tops:
        proc = subprocess.run(
            [
                "bash",
                "-lc",
                f"{GMX} && gmx grompp -f {mdp} -c {gro} -p {top} -n {ndx} -o {tpr} -maxwarn 1",
            ],
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        chunks.append(f"### {top}\n{proc.stdout}")
        if proc.returncode == 0:
            log.write_text("\n\n".join(chunks))
            return True
    log.write_text("\n\n".join(chunks))
    return False


def topology_candidates(gromacs_dir: Path) -> list[Path]:
    out = []
    for name in [
        "topol_cleaned_for_prod.top",
        "topol_clean_attempt2.top",
        "topol_clean_attempt1.top",
        "topol.top",
    ]:
        path = gromacs_dir / name
        if path.exists():
            out.append(path)
    cleaned = gromacs_dir / "run_min" / "topol_cleaned.top"
    if cleaned.exists():
        out.append(cleaned)
    return out


def cleanup_xtc(window: Path):
    for path in window.glob("*.xtc"):
        try:
            path.unlink()
        except OSError:
            pass


def build_queue() -> list[dict]:
    rows = []
    for umb in ROOT.rglob(SUBDIR):
        if umb.name != SUBDIR:
            continue
        if "autodl_shutdown_archive" in str(umb):
            continue
        gromacs_dir = umb.parent
        ndx = umb / "umbrella_index.ndx"
        for window in sorted(umb.glob("window_*")):
            if window.parent != umb:
                continue
            if finished(window / "umbrella.log"):
                continue
            tops = topology_candidates(gromacs_dir)
            row = {
                "path": window,
                "ndx": ndx,
                "tops": tops,
                "gromacs_dir": gromacs_dir,
            }
            if (window / "umbrella.tpr").exists():
                row["mode"] = "prod_resume" if (window / "umbrella.cpt").exists() else "prod_run"
            elif finished(window / "umbrella_eq.log") and (window / "umbrella_eq.gro").exists():
                row["mode"] = "prod_grompp"
            elif (window / "umbrella_eq.tpr").exists():
                row["mode"] = "eq_resume" if (window / "umbrella_eq.cpt").exists() else "eq_run"
            elif (window / "start.gro").exists() and (window / "umbrella_eq.mdp").exists():
                row["mode"] = "eq_grompp"
            else:
                continue
            rows.append(row)
    return rows


def process(row: dict) -> str:
    window: Path = row["path"]
    ndx: Path = row["ndx"]
    tops: list[Path] = row["tops"]
    mode = row["mode"]
    if not tops:
        return f"FAIL\t{window}\tno_topology"
    if not ndx.exists():
        return f"FAIL\t{window}\tno_index"

    if mode in {"eq_grompp", "eq_run", "eq_resume"}:
        if mode == "eq_grompp":
            ok = grompp(window, window / "umbrella_eq.mdp", window / "start.gro", "umbrella_eq", ndx, tops)
            if not ok:
                return f"FAIL\t{window}\teq_grompp"
        cpt = window / "umbrella_eq.cpt" if (window / "umbrella_eq.cpt").exists() else None
        code = run_mdrun(window, "umbrella_eq", cpt)
        if code != 0 or not finished(window / "umbrella_eq.log"):
            return f"FAIL\t{window}\teq_mdrun"
        cleanup_xtc(window)
        mode = "prod_grompp"

    if mode in {"prod_grompp", "prod_run", "prod_resume"}:
        if mode == "prod_grompp" or not (window / "umbrella.tpr").exists():
            gro = window / "umbrella_eq.gro"
            if not gro.exists():
                return f"FAIL\t{window}\tno_eq_gro"
            ok = grompp(window, window / "umbrella.mdp", gro, "umbrella", ndx, tops)
            if not ok:
                return f"FAIL\t{window}\tprod_grompp"
        cpt = window / "umbrella.cpt" if (window / "umbrella.cpt").exists() else None
        code = run_mdrun(window, "umbrella", cpt)
        if code != 0 or not finished(window / "umbrella.log"):
            return f"FAIL\t{window}\tprod_mdrun"
        cleanup_xtc(window)
        return f"OK\t{window}\tcomplete"

    return f"FAIL\t{window}\tbad_mode_{mode}"


def main():
    LOGDIR.mkdir(parents=True, exist_ok=True)
    rows = build_queue()
    with QUEUE.open("w") as handle:
        handle.write("path\tmode\n")
        for row in rows:
            handle.write(f"{row['path']}\t{row['mode']}\n")
    print(f"queue={len(rows)} limit={LIMIT} root={ROOT}", flush=True)
    workers = min(LIMIT, max(1, len(rows)))
    results = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(process, row) for row in rows]
        for fut in as_completed(futures):
            line = fut.result()
            results.append(line)
            print(line, flush=True)
    out = LOGDIR / f"resume_results_{time.strftime('%Y%m%dT%H%M%SZ')}.tsv"
    out.write_text("\n".join(results) + ("\n" if results else ""))
    ok = sum(1 for line in results if line.startswith("OK\t"))
    print(f"done ok={ok} fail={len(results) - ok} results={out}", flush=True)


if __name__ == "__main__":
    main()
