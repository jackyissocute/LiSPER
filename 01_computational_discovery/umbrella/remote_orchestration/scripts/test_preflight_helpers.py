#!/usr/bin/env python3
"""Minimal self-checks for preflight helpers (no GROMACS required)."""
from __future__ import annotations

import math
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def test_estimate_runs():
    script = ROOT / "estimate_umbrella_campaign.py"
    out = subprocess.check_output([sys.executable, str(script), "--threads", "100", "--candidates", "1"], text=True)
    assert "recommended_LISPER_GLOBAL_MDRUN_LIMIT\t96" in out
    assert "windows_per_condition\t" in out


def test_validate_bound_geometry():
    # Tiny fake gro: two donors + one LI near centroid
    gro = tempfile.NamedTemporaryFile("w", suffix=".gro", delete=False)
    # 3 atoms, cubic 5 nm box
    gro.write("bound check\n3\n")
    gro.write(f"{1:5d}{'ASP':<5}{'OD1':>5}{1:5d}{1.000:8.3f}{1.000:8.3f}{1.000:8.3f}\n")
    gro.write(f"{1:5d}{'ASP':<5}{'OD2':>5}{2:5d}{1.200:8.3f}{1.000:8.3f}{1.000:8.3f}\n")
    gro.write(f"{2:5d}{'LIT':<5}{'LIT':>5}{3:5d}{1.100:8.3f}{1.050:8.3f}{1.000:8.3f}\n")
    gro.write(f"{5.0:10.5f}{5.0:10.5f}{5.0:10.5f}\n")
    gro.close()
    man = tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False)
    man.write("candidate\tsite_id\tdonor_identities\tselection_rationale\tstarting_state_status\n")
    man.write("Toy\tsite\t1:ASP:OD1,1:ASP:OD2\treason\tPROPOSED_REQUIRES_RECONSTRUCTION\n")
    man.close()
    script = ROOT / "validate_bound_start.py"
    subprocess.check_call(
        [
            sys.executable,
            str(script),
            "--gro",
            gro.name,
            "--manifest",
            man.name,
            "--ion-resname",
            "LIT",
            "--max-bound-nm",
            "0.55",
            "--promote",
        ]
    )
    text = Path(man.name).read_text()
    assert "VALIDATED_BOUND" in text


def test_qc_math_smoke():
    # Synthetic flat profiles → estimate ready + ΔΔG computable
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        li = tmp / "li.xvg"
        na = tmp / "na.xvg"
        # bound ~0.4, ref ~2.0; Li barrier 10, Na barrier 5 → ddg = 5
        lines_li = ["# li\n"] + [f"{x:.3f} { (0.0 if x < 1.0 else 10.0):.3f}\n" for x in [i * 0.1 for i in range(5, 26)]]
        lines_na = ["# na\n"] + [f"{x:.3f} { (0.0 if x < 1.0 else 5.0):.3f}\n" for x in [i * 0.1 for i in range(5, 26)]]
        li.write_text("".join(lines_li))
        na.write_text("".join(lines_na))
        bootstrap = tmp / "bootstrap.xvg"
        bootstrap.write_text("".join(f"{x:.3f} 0.0 0.2\n" for x in [i * 0.1 for i in range(5, 26)]))
        warnings = tmp / "wham.log"
        warnings.write_text("clean\n")
        histo = tmp / "histo.xvg"
        histo.write_text("".join(f"{x:.3f} 1.0 1.0 1.0\n" for x in [i * 0.1 for i in range(5, 26)]))
        regions = tmp / "regions.tsv"
        regions.write_text(
            "candidate\tstatus\tbound_min_nm\tbound_max_nm\tref_min_nm\tref_max_nm\n"
            "Toy\tLOCKED_PRE_PMF\t0.4\t0.6\t1.8\t2.2\n"
        )
        out = tmp / "qc.tsv"
        script = Path(__file__).resolve().parents[2] / "pmf/remote_orchestration/scripts/evaluate_paired_pmf_qc.py"
        # fix path: this test lives under umbrella/.../scripts; pmf script is sibling stage
        script = ROOT.parents[2] / "pmf" / "remote_orchestration" / "scripts" / "evaluate_paired_pmf_qc.py"
        subprocess.check_call(
            [
                sys.executable,
                str(script),
                "--candidate",
                "Toy",
                "--li-profile",
                str(li),
                "--na-profile",
                str(na),
                "--li-bootstrap",
                str(bootstrap),
                "--na-bootstrap",
                str(bootstrap),
                "--li-half-early",
                str(li),
                "--li-half-late",
                str(li),
                "--na-half-early",
                str(na),
                "--na-half-late",
                str(na),
                "--li-burnin",
                str(li),
                str(li),
                "--na-burnin",
                str(na),
                str(na),
                "--li-histo",
                str(histo),
                "--na-histo",
                str(histo),
                "--wham-warning-files",
                str(warnings),
                "--regions",
                str(regions),
                "--out",
                str(out),
            ]
        )
        body = out.read_text()
        assert "ESTIMATE_READY" in body
        assert "delta_delta_g_kjmol" in body
        missing = subprocess.run(
            [sys.executable, str(script), "--candidate", "Toy", "--li-profile", str(li), "--na-profile", str(na)],
            text=True,
            capture_output=True,
        )
        assert missing.returncode != 0


def test_wham_prepare_fails_closed_then_writes_inputs():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        umbrella = root / "umbrella"
        window = umbrella / "window_000_0.40nm"
        window.mkdir(parents=True)
        (window / "umbrella.log").write_text("unfinished\n")
        script = ROOT.parents[2] / "pmf" / "remote_orchestration" / "scripts" / "run_wham_qc.py"
        cmd = [sys.executable, str(script), "--umbrella-dir", str(umbrella), "--out", str(root / "out"), "--prepare-only"]
        assert subprocess.run(cmd, capture_output=True).returncode != 0
        (window / "umbrella.log").write_text("Finished mdrun\n")
        (window / "umbrella.tpr").write_text("tpr\n")
        (window / "umbrella_pullf.xvg").write_text("@ title\n500 0\n2500 0\n")
        subprocess.check_call(cmd)
        assert (root / "out/tpr-files.dat").exists()
        assert "burnin_25\t1000.000\t2500.000" in (root / "out/analysis_times.tsv").read_text()


def test_region_lock_uses_shared_non_guard_range():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        header = "candidate_id\tsite_lock_id\twindow_spacing_nm\twindow_eq_ns\twindow_ns\tguard_windows\tinitial_distance_nm\teffective_analysis_extension_nm\n"
        li, na, out = root / "li.tsv", root / "na.tsv", root / "regions.tsv"
        li.write_text(header + "Toy\tsite\t0.075\t0.500\t2.000\t3\t0.4400\t1.950\n")
        na.write_text(header + "Toy\tsite\t0.075\t0.500\t2.000\t3\t0.4200\t1.950\n")
        script = ROOT.parents[2] / "pmf" / "remote_orchestration" / "scripts" / "lock_paired_regions.py"
        subprocess.check_call([sys.executable, str(script), "--li-metadata", str(li), "--na-metadata", str(na), "--out", str(out)])
        text = out.read_text()
        assert "LOCKED_PRE_PMF" in text
        assert "0.4400\t0.5500\t2.0700\t2.3700" in text


if __name__ == "__main__":
    test_estimate_runs()
    test_validate_bound_geometry()
    test_qc_math_smoke()
    test_wham_prepare_fails_closed_then_writes_inputs()
    test_region_lock_uses_shared_non_guard_range()
    # also keep existing driver unit checks
    subprocess.check_call([sys.executable, str(ROOT / "test_umbrella_design.py")])
    print("preflight_selfcheck_ok")
