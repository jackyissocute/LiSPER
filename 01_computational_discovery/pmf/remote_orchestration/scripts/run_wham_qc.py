#!/usr/bin/env python3
"""Generate reproducible full, burn-in, half, histogram, and bootstrap WHAM products."""
from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path


def data_times(path: Path) -> tuple[float, float]:
    times = [float(line.split()[0]) for line in path.read_text(errors="replace").splitlines() if line and line[0] not in "#@"]
    if len(times) < 2:
        raise RuntimeError(f"Insufficient pull-force data: {path}")
    return times[0], times[-1]


def prepare(umbrella: Path, out: Path) -> tuple[float, float]:
    windows = sorted(umbrella.glob("window_*"))
    if not windows:
        raise RuntimeError(f"No windows under {umbrella}")
    missing = [
        window.name
        for window in windows
        if not (window / "umbrella.log").exists()
        or "Finished mdrun" not in (window / "umbrella.log").read_text(errors="replace")
    ]
    if missing:
        raise RuntimeError(f"Production incomplete for {len(missing)}/{len(windows)} windows: {','.join(missing[:5])}")
    tprs = [window / "umbrella.tpr" for window in windows]
    pullfs = [window / "umbrella_pullf.xvg" for window in windows]
    absent = [str(path) for path in tprs + pullfs if not path.exists()]
    if absent:
        raise RuntimeError(f"Missing WHAM inputs: {absent[0]}")
    ranges = {data_times(path) for path in pullfs}
    if len(ranges) != 1:
        raise RuntimeError(f"Window time ranges differ: {sorted(ranges)}")
    out.mkdir(parents=True, exist_ok=True)
    (out / "tpr-files.dat").write_text("\n".join(map(str, tprs)) + "\n")
    (out / "pullf-files.dat").write_text("\n".join(map(str, pullfs)) + "\n")
    start, end = ranges.pop()
    (out / "analysis_times.tsv").write_text(
        "variant\tbegin_ps\tend_ps\n"
        f"full\t{start:.3f}\t{end:.3f}\n"
        f"burnin_12p5\t{start + 0.125 * (end-start):.3f}\t{end:.3f}\n"
        f"burnin_25\t{start + 0.25 * (end-start):.3f}\t{end:.3f}\n"
        f"half_early\t{start:.3f}\t{start + 0.5 * (end-start):.3f}\n"
        f"half_late\t{start + 0.5 * (end-start):.3f}\t{end:.3f}\n"
    )
    return start, end


def run_wham(gmx: str, out: Path, name: str, begin: float, end: float, bootstrap: bool = False) -> None:
    cmd = [
        gmx, "wham", "-it", "tpr-files.dat", "-if", "pullf-files.dat", "-o", f"profile_{name}.xvg",
        "-hist", f"histo_{name}.xvg", "-unit", "kJ", "-b", str(begin), "-e", str(end), "-bins", "200",
        "-ac", "-oiact", f"iact_{name}.xvg", "-v",
    ]
    if bootstrap:
        cmd += ["-nBootstrap", "200", "-bs-method", "traj", "-bs-seed", "20260713", "-bsres", "bootstrap_std.xvg", "-bsprof", "bootstrap_profiles.xvg"]
    env = os.environ.copy()
    env.setdefault("OMP_NUM_THREADS", "1")
    result = subprocess.run(cmd, cwd=out, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (out / f"wham_{name}.log").write_text(result.stdout)
    autocorr = out / "hist_autocorr.xvg"
    if autocorr.exists():
        autocorr.replace(out / f"autocorr_{name}.xvg")
    if result.returncode:
        raise RuntimeError(f"WHAM {name} failed; see {out / f'wham_{name}.log'}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--umbrella-dir", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--gmx", default="gmx")
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    start, end = prepare(args.umbrella_dir.resolve(), args.out.resolve())
    if args.prepare_only:
        return
    span = end - start
    for name, begin, finish, bootstrap in (
        ("full", start, end, True),
        ("burnin_12p5", start + 0.125 * span, end, False),
        ("burnin_25", start + 0.25 * span, end, False),
        ("half_early", start, start + 0.5 * span, False),
        ("half_late", start + 0.5 * span, end, False),
    ):
        run_wham(args.gmx, args.out.resolve(), name, begin, finish, bootstrap)


if __name__ == "__main__":
    main()
