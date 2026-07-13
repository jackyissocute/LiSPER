#!/usr/bin/env python3
"""Minimal self-checks for preflight helpers (no GROMACS required)."""
from __future__ import annotations

import math
import os
import subprocess
import sys
import tempfile
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def test_sod_parameters_include_required_nbfix():
    script = ROOT / "prep_bound_batch.py"
    spec = importlib.util.spec_from_file_location("prep_bound_batch", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory() as tmp:
        forcefield = Path(tmp) / "forcefield.itp"
        forcefield.write_text(
            "[ atomtypes ]\n"
            "LIT 3 6.941 1.0 A 0.23 0.01\n"
            "OC 8 15.999 -0.76 A 0.30 0.50\n"
            "CLA 17 35.45 -1.0 A 0.40 0.62\n\n"
            "[ nonbond_params ]\n"
            "; i j func sigma epsilon\n"
            "CLA LIT 1 0.32 0.07\n"
        )
        module.ensure_sod_parameters(forcefield)
        module.ensure_sod_parameters(forcefield)
        text = forcefield.read_text()
        assert text.count("SOD    11") == 1
        assert text.count("CLA     SOD") == 1
        assert text.count("SOD      OC") == 1


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
            "--record",
        ]
    )
    text = Path(man.name).read_text()
    assert "GEOMETRY_SCREENED_BOUND_START" in text


def test_evidence_summary_math_smoke():
    # Synthetic profiles exercise the diagnostic estimator without a PASS gate.
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        li = tmp / "li.xvg"
        na = tmp / "na.xvg"
        # bound ~0.4, ref ~2.0; Li barrier 10, Na barrier 5 → ddg = 5
        lines_li = ["# li\n"] + [f"{x:.3f} { (0.0 if x < 1.0 else 10.0):.3f}\n" for x in [i * 0.1 for i in range(5, 26)]]
        lines_na = ["# na\n"] + [f"{x:.3f} { (0.0 if x < 1.0 else 5.0):.3f}\n" for x in [i * 0.1 for i in range(5, 26)]]
        li.write_text("".join(lines_li))
        na.write_text("".join(lines_na))
        bootstrap_li = tmp / "bootstrap_li.xvg"
        bootstrap_na = tmp / "bootstrap_na.xvg"
        bootstrap_li.write_text("".join(lines_li) + "&\n" + "".join(lines_li))
        bootstrap_na.write_text("".join(lines_na) + "&\n" + "".join(lines_na))
        warnings = tmp / "wham.log"
        warnings.write_text("clean\n")
        histo = tmp / "histo.xvg"
        histo.write_text("".join(f"{x:.3f} 1.0 1.0 1.0\n" for x in [i * 0.1 for i in range(5, 26)]))
        iact = tmp / "iact.xvg"
        iact.write_text("#  WIN   tau(gr1)\n#   0    2.0\n#   1    3.0\n#   2    4.0\n")
        regions = tmp / "regions.tsv"
        regions.write_text(
            "candidate\tstatus\tbound_min_nm\tbound_max_nm\tref_min_nm\tref_max_nm\n"
            "Toy\tDECLARED_DIAGNOSTIC_REGIONS\t0.5\t0.7\t1.8\t2.2\n"
        )
        out = tmp / "evidence.tsv"
        script = ROOT.parents[2] / "pmf" / "remote_orchestration" / "scripts" / "summarize_paired_pmf_evidence.py"
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
                "--li-bootstrap-profiles",
                str(bootstrap_li),
                "--na-bootstrap-profiles",
                str(bootstrap_na),
                "--li-time-profiles",
                str(li),
                str(li),
                "--na-time-profiles",
                str(na),
                str(na),
                "--li-histo",
                str(histo),
                "--na-histo",
                str(histo),
                "--li-iact",
                str(iact),
                "--na-iact",
                str(iact),
                "--bootstrap-method",
                "traj_with_gmx_iact",
                "--wham-log-files",
                str(warnings),
                "--regions",
                str(regions),
                "--out",
                str(out),
            ]
        )
        body = out.read_text()
        assert "\tPASS\t" not in body and "\tREPAIR\t" not in body
        assert "EVIDENCE_SUMMARY_NO_BINARY_VERDICT" in body
        assert "paired_contrast_li_minus_na_kjmol" in body
        assert "absolute_binding_free_energy_supported" in body
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


def test_analysis_plan_requires_explicit_regions():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        header = "candidate_id\tsite_lock_id\twindow_spacing_nm\twindow_eq_ns\twindow_ns\tguard_windows\tinitial_distance_nm\teffective_analysis_extension_nm\n"
        li, na, out = root / "li.tsv", root / "na.tsv", root / "regions.tsv"
        li.write_text(header + "Toy\tsite\t0.075\t0.500\t2.000\t3\t0.4400\t1.950\n")
        na.write_text(header + "Toy\tsite\t0.075\t0.500\t2.000\t3\t0.4200\t1.950\n")
        script = ROOT.parents[2] / "pmf" / "remote_orchestration" / "scripts" / "record_paired_analysis_plan.py"
        subprocess.check_call(
            [
                sys.executable,
                str(script),
                "--li-metadata",
                str(li),
                "--na-metadata",
                str(na),
                "--bound-min",
                "0.44",
                "--bound-max",
                "0.55",
                "--ref-min",
                "2.07",
                "--ref-max",
                "2.37",
                "--bound-rationale",
                "declared physical state definition",
                "--reference-rationale",
                "declared noninteracting-state evidence",
                "--out",
                str(out),
            ]
        )
        text = out.read_text()
        assert "DECLARED_DIAGNOSTIC_REGIONS" in text
        assert "0.4400\t0.5500\t2.0700\t2.3700" in text


def test_nonpilot_requires_documented_method_review():
    with tempfile.TemporaryDirectory() as tmp:
        script = ROOT / "run_lisper_umbrella_sampling.py"
        code = (
            "import importlib.util; "
            f"s=importlib.util.spec_from_file_location('driver',{str(script)!r}); "
            "m=importlib.util.module_from_spec(s); s.loader.exec_module(m); "
            "m.assert_scale_up_authorized()"
        )
        env = os.environ.copy()
        env.update(LISPER_WORKDIR=tmp, LISPER_ION_RESNAME="LIT", LISPER_CANDIDATE="Other")
        result = subprocess.run([sys.executable, "-c", code], env=env, text=True, capture_output=True)
        assert result.returncode != 0
        assert "Method review blocks non-pilot candidate" in result.stderr


if __name__ == "__main__":
    test_sod_parameters_include_required_nbfix()
    test_estimate_runs()
    test_validate_bound_geometry()
    test_evidence_summary_math_smoke()
    test_wham_prepare_fails_closed_then_writes_inputs()
    test_analysis_plan_requires_explicit_regions()
    test_nonpilot_requires_documented_method_review()
    # also keep existing driver unit checks
    subprocess.check_call([sys.executable, str(ROOT / "test_umbrella_design.py")])
    print("preflight_selfcheck_ok")
