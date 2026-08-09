#!/usr/bin/env python3
"""Curate final PMF evidence, verify it, and render selectivity figures."""
from __future__ import annotations

import csv
import hashlib
import math
import shutil
import statistics
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "01_computational_discovery/umbrella/analysis_archive_20260725"
SOURCE = ARCHIVE / "paired_pmf"
RAW = ROOT / "01_computational_discovery/data/raw"
PROCESSED = ROOT / "01_computational_discovery/data/processed"
R_KJ_MOL_K = 0.00831446261815324
TEMPERATURE_K = 298.15
IONS = ("LiCl", "NaCl")
PROFILE_FILES = (
    "profile_full.xvg",
    "profile_burnin_12p5.xvg",
    "profile_burnin_25.xvg",
    "profile_half_early.xvg",
    "profile_half_late.xvg",
    "bootstrap_std.xvg",
    "histo_full.xvg",
    "iact_full.xvg",
    "analysis_times.tsv",
    "tpr-files.dat",
    "pullf-files.dat",
    "wham_full.log",
)
LI_COLOR = "#0072B2"
NA_COLOR = "#D55E00"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_xvg(path: Path) -> np.ndarray:
    rows = []
    for line in path.read_text(errors="replace").splitlines():
        if not line or line[0] in "#@":
            continue
        try:
            rows.append([float(value) for value in line.split()])
        except ValueError:
            continue
    if not rows:
        raise AssertionError(f"No numeric rows in {path}")
    return np.asarray(rows, dtype=float)


def corrected_profile(path: Path) -> np.ndarray:
    rows = read_xvg(path)
    assert rows.shape[1] >= 2 and np.all(rows[:, 0] > 0)
    correction = R_KJ_MOL_K * TEMPERATURE_K * np.log(4 * np.pi * rows[:, 0] ** 2)
    return np.column_stack((rows[:, 0], rows[:, 1] + correction))


def mean_region(profile: np.ndarray, lo: float, hi: float) -> float:
    values = profile[(profile[:, 0] >= lo) & (profile[:, 0] <= hi), 1]
    if values.size:
        return float(values.mean())
    return float(np.interp([lo, hi], profile[:, 0], profile[:, 1]).mean())


def binding_delta_g(profile: np.ndarray, bounds: tuple[float, float, float, float]) -> float:
    bound_lo, bound_hi, ref_lo, ref_hi = bounds
    return mean_region(profile, bound_lo, bound_hi) - mean_region(profile, ref_lo, ref_hi)


def region_span(profile: np.ndarray, lo: float, hi: float) -> float:
    values = profile[(profile[:, 0] >= lo) & (profile[:, 0] <= hi), 1]
    if values.size < 2:
        values = np.interp([lo, hi], profile[:, 0], profile[:, 1])
    return float(values.max() - values.min())


def bootstrap_uncertainty(path: Path, bounds: tuple[float, float, float, float]) -> float:
    rows = read_xvg(path)
    assert rows.shape[1] >= 3
    bound_lo, bound_hi, ref_lo, ref_hi = bounds
    bound = rows[(rows[:, 0] >= bound_lo) & (rows[:, 0] <= bound_hi), 2]
    reference = rows[(rows[:, 0] >= ref_lo) & (rows[:, 0] <= ref_hi), 2]
    assert bound.size and reference.size
    return math.hypot(float(bound.mean()), float(reference.mean()))


def assert_close(actual: float, expected: str, label: str, tolerance: float = 0.0015) -> None:
    if not math.isclose(actual, float(expected), abs_tol=tolerance):
        raise AssertionError(f"{label}: recomputed {actual:.6f}, reported {expected}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def curate(candidates: list[str]) -> None:
    selected: list[tuple[Path, Path, str]] = [
        (SOURCE / "delta_g_summary.tsv", RAW / "pmf/summary/delta_g_summary.tsv", "condition_summary"),
        (SOURCE / "selectivity_summary.tsv", RAW / "pmf/summary/selectivity_summary.tsv", "selectivity_summary"),
        (ARCHIVE / "manifest/archive_verification.tsv", RAW / "manifests/archive_verification.tsv", "archive_verification"),
        (ARCHIVE / "manifest/bulk_data_coverage.tsv", RAW / "manifests/bulk_data_coverage.tsv", "bulk_data_coverage"),
    ]
    for candidate in candidates:
        candidate_source = SOURCE / candidate
        selected.extend((
            (
                candidate_source / f"{candidate}_paired_qc.tsv",
                RAW / f"pmf/{candidate}/paired_qc.tsv",
                "paired_qc",
            ),
            (
                candidate_source / "paired_regions.tsv",
                RAW / f"pmf/{candidate}/paired_regions.tsv",
                "paired_regions",
            ),
        ))
        for ion in IONS:
            for name in PROFILE_FILES:
                selected.append(
                    (
                        candidate_source / ion / name,
                        RAW / f"pmf/{candidate}/{ion}/{name}",
                        "wham_log" if name.endswith(".log") else "pmf_evidence",
                    )
                )
    for stage in ("bound_prep", "drivers"):
        for source in sorted((ARCHIVE / f"workflow/remote_logs/{stage}").glob("*.log")):
            selected.append((source, RAW / f"logs/{stage}/{source.name}", "workflow_log"))

    manifest = []
    for source, destination, role in selected:
        if not source.is_file():
            raise FileNotFoundError(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        source_hash = sha256(source)
        if sha256(destination) != source_hash:
            raise AssertionError(f"Copy hash mismatch: {destination}")
        manifest.append(
            {
                "curated_path": destination.relative_to(ROOT).as_posix(),
                "source_path": source.relative_to(ROOT).as_posix(),
                "bytes": destination.stat().st_size,
                "sha256": source_hash,
                "role": role,
            }
        )

    manifest_path = RAW / "source_manifest.tsv"
    with manifest_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=manifest[0], delimiter="\t")
        writer.writeheader()
        writer.writerows(sorted(manifest, key=lambda row: row["curated_path"]))


def validate() -> tuple[list[dict[str, object]], dict[tuple[str, str], np.ndarray]]:
    delta_rows = read_tsv(SOURCE / "delta_g_summary.tsv")
    selectivity_rows = read_tsv(SOURCE / "selectivity_summary.tsv")
    candidates = [row["candidate"] for row in selectivity_rows]
    assert len(candidates) == len(set(candidates)) == 8
    assert len(delta_rows) == 16
    condition_rows = {(row["candidate"], row["condition"]): row for row in delta_rows}
    assert set(condition_rows) == {(candidate, ion) for candidate in candidates for ion in IONS}

    results: list[dict[str, object]] = []
    centered_profiles: dict[tuple[str, str], np.ndarray] = {}
    for summary in selectivity_rows:
        candidate = summary["candidate"]
        qc_rows = read_tsv(SOURCE / candidate / f"{candidate}_paired_qc.tsv")
        assert len(qc_rows) == 1
        qc = qc_rows[0]
        regions = read_tsv(SOURCE / candidate / "paired_regions.tsv")
        assert len(regions) == 1 and regions[0]["candidate"] == candidate
        bounds = tuple(float(regions[0][name]) for name in ("bound_min_nm", "bound_max_nm", "ref_min_nm", "ref_max_nm"))
        assert all(math.isclose(bounds[index], float(summary[name]), abs_tol=5e-5) for index, name in enumerate(("bound_min_nm", "bound_max_nm", "ref_min_nm", "ref_max_nm")))

        ion_results = {}
        for ion, qc_suffix in (("LiCl", "li"), ("NaCl", "na")):
            folder = SOURCE / candidate / ion
            profile = corrected_profile(folder / "profile_full.xvg")
            raw_profile = read_xvg(folder / "profile_full.xvg")
            bootstrap = read_xvg(folder / "bootstrap_std.xvg")
            histogram = read_xvg(folder / "histo_full.xvg")
            iact = read_xvg(folder / "iact_full.xvg")
            assert profile.shape == (200, 2)
            assert bootstrap.shape == (200, 3)
            assert histogram.shape[0] == 200 and histogram.shape[1] >= 3
            assert iact.shape[1] >= 2 and np.all(np.isfinite(iact[:, 1]))
            assert np.all(np.diff(profile[:, 0]) > 0)
            assert np.allclose(raw_profile[:, 0], bootstrap[:, 0], atol=5e-8)
            assert np.all(np.isfinite(profile)) and np.all(np.isfinite(bootstrap)) and np.all(histogram[:, 1:] >= 0)
            analysis_times = read_tsv(folder / "analysis_times.tsv")
            assert [row["variant"] for row in analysis_times] == ["full", "burnin_12p5", "burnin_25", "half_early", "half_late"]
            assert float(analysis_times[0]["begin_ps"]) == 0 and float(analysis_times[0]["end_ps"]) == 2000
            assert "Converged in" in (folder / "wham_full.log").read_text(errors="replace")

            dg = binding_delta_g(profile, bounds)
            uncertainty = bootstrap_uncertainty(folder / "bootstrap_std.xvg", bounds)
            condition = condition_rows[(candidate, ion)]
            assert_close(dg, condition["delta_g_kjmol"], f"{candidate} {ion} delta G")
            assert_close(uncertainty, condition["bootstrap_unc_kjmol"], f"{candidate} {ion} uncertainty")
            assert_close(region_span(profile, bounds[2], bounds[3]), qc[f"endpoint_span_{qc_suffix}_kjmol"], f"{candidate} {ion} endpoint span")

            early = binding_delta_g(corrected_profile(folder / "profile_half_early.xvg"), bounds)
            late = binding_delta_g(corrected_profile(folder / "profile_half_late.xvg"), bounds)
            assert_close(abs(early - late), qc[f"half_difference_{qc_suffix}_kjmol"], f"{candidate} {ion} half difference")
            burnin_shift = max(
                abs(dg - binding_delta_g(corrected_profile(folder / name), bounds))
                for name in ("profile_burnin_12p5.xvg", "profile_burnin_25.xvg")
            )
            assert_close(burnin_shift, qc[f"burnin_max_shift_{qc_suffix}_kjmol"], f"{candidate} {ion} burn-in shift")

            supports = [
                int(np.count_nonzero(np.isfinite(row[1:]) & (row[1:] > 0)))
                for row in histogram[(histogram[:, 0] >= bounds[0]) & (histogram[:, 0] <= bounds[3])]
            ]
            assert supports
            assert min(supports) == int(qc[f"histogram_min_support_{qc_suffix}"])
            assert sum(value < 2 for value in supports) == int(qc[f"histogram_weak_bins_{qc_suffix}"])
            assert_close(float(iact[:, 1].min()), qc[f"iact_min_{qc_suffix}_ps"], f"{candidate} {ion} IACT min")
            assert_close(float(np.median(iact[:, 1])), qc[f"iact_median_{qc_suffix}_ps"], f"{candidate} {ion} IACT median")
            assert_close(float(iact[:, 1].max()), qc[f"iact_max_{qc_suffix}_ps"], f"{candidate} {ion} IACT max")

            reference_mean = mean_region(profile, bounds[2], bounds[3])
            centered_profiles[(candidate, ion)] = np.column_stack((profile[:, 0], profile[:, 1] - reference_mean))
            ion_results[ion] = (dg, uncertainty)

        ddg = ion_results["LiCl"][0] - ion_results["NaCl"][0]
        ddg_unc = math.hypot(ion_results["LiCl"][1], ion_results["NaCl"][1])
        assert_close(ddg, summary["delta_delta_g_kjmol"], f"{candidate} delta delta G")
        assert_close(ddg_unc, summary["bootstrap_unc_ddg_kjmol"], f"{candidate} delta delta G uncertainty")
        assert_close(ddg, qc["delta_delta_g_kjmol"], f"{candidate} paired QC delta delta G")
        results.append(
            {
                "candidate": candidate,
                "dg_li": ion_results["LiCl"][0],
                "unc_li": ion_results["LiCl"][1],
                "dg_na": ion_results["NaCl"][0],
                "unc_na": ion_results["NaCl"][1],
                "ddg": ddg,
                "unc_ddg": ddg_unc,
                "bounds": bounds,
            }
        )
    return results, centered_profiles


def save_figure(fig: plt.Figure, stem: str) -> None:
    PROCESSED.mkdir(parents=True, exist_ok=True)
    fig.savefig(PROCESSED / f"{stem}.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(PROCESSED / f"{stem}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_selectivity(results: list[dict[str, object]]) -> None:
    ordered = sorted(results, key=lambda row: float(row["ddg"]))
    y = np.arange(len(ordered))
    fig, (ax_ddg, ax_dg) = plt.subplots(1, 2, figsize=(12.0, 5.8), sharey=True)
    ddg = np.array([row["ddg"] for row in ordered], dtype=float)
    ddg_unc = np.array([row["unc_ddg"] for row in ordered], dtype=float)
    ax_ddg.errorbar(ddg, y, xerr=ddg_unc, fmt="o", color=LI_COLOR, ecolor="#4D4D4D", capsize=3, markersize=6)
    ax_ddg.axvline(0, color="#333333", linewidth=1)
    ax_ddg.set_yticks(y, [str(row["candidate"]) for row in ordered])
    ax_ddg.invert_yaxis()
    ax_ddg.set_xlabel("ΔΔG = ΔG(Li) − ΔG(Na) (kJ mol⁻¹)")
    ax_ddg.set_title("Selectivity (± propagated bootstrap SD)", fontsize=11)

    li = np.array([row["dg_li"] for row in ordered], dtype=float)
    na = np.array([row["dg_na"] for row in ordered], dtype=float)
    li_unc = np.array([row["unc_li"] for row in ordered], dtype=float)
    na_unc = np.array([row["unc_na"] for row in ordered], dtype=float)
    ax_dg.errorbar(li, y - 0.10, xerr=li_unc, fmt="o", color=LI_COLOR, ecolor=LI_COLOR, capsize=3, label="LiCl")
    ax_dg.errorbar(na, y + 0.10, xerr=na_unc, fmt="s", color=NA_COLOR, ecolor=NA_COLOR, capsize=3, label="NaCl")
    ax_dg.axvline(0, color="#333333", linewidth=1)
    ax_dg.set_xlabel("Endpoint-referenced ΔG (kJ mol⁻¹)")
    ax_dg.set_title("Ion-specific binding estimates (± bootstrap SD)", fontsize=11)
    ax_dg.legend(frameon=False, loc="center left", bbox_to_anchor=(1.01, 0.5))

    for axis in (ax_ddg, ax_dg):
        axis.grid(axis="x", color="#D9D9D9", linewidth=0.7)
        axis.set_axisbelow(True)
        axis.spines[["top", "right"]].set_visible(False)
    fig.subplots_adjust(left=0.12, right=0.82, bottom=0.15, top=0.88, wspace=0.08)
    save_figure(fig, "selectivity_overview")


def plot_profiles(results: list[dict[str, object]], profiles: dict[tuple[str, str], np.ndarray]) -> None:
    ordered = sorted(results, key=lambda row: float(row["ddg"]))
    fig, axes = plt.subplots(4, 2, figsize=(9.0, 11.2), sharex=False, sharey=True, constrained_layout=True)
    fig.suptitle("Radially corrected PMF profiles", fontsize=14, fontweight="bold")
    display_ranges = []
    for row in ordered:
        bound_lo, _, _, ref_hi = row["bounds"]
        display_ranges.append((max(0.20, bound_lo - 0.15), ref_hi + 0.05))
    visible_values = []
    for row, (lo, hi) in zip(ordered, display_ranges):
        for ion in IONS:
            profile = profiles[(str(row["candidate"]), ion)]
            visible_values.extend(profile[(profile[:, 0] >= lo) & (profile[:, 0] <= hi), 1])
    y_min, y_max = float(np.min(visible_values)), float(np.max(visible_values))
    margin = 0.05 * max(1.0, y_max - y_min)

    for axis, row, (lo, hi) in zip(axes.flat, ordered, display_ranges):
        candidate = str(row["candidate"])
        bound_lo, bound_hi, ref_lo, ref_hi = row["bounds"]
        axis.axvspan(bound_lo, bound_hi, color="#B3DDF2", alpha=0.55, linewidth=0)
        axis.axvspan(ref_lo, ref_hi, color="#D9D9D9", alpha=0.7, linewidth=0)
        for ion, color, label in (("LiCl", LI_COLOR, "LiCl"), ("NaCl", NA_COLOR, "NaCl")):
            profile = profiles[(candidate, ion)]
            mask = (profile[:, 0] >= lo) & (profile[:, 0] <= hi)
            axis.plot(profile[mask, 0], profile[mask, 1], color=color, linewidth=1.7, label=label)
        axis.axhline(0, color="#666666", linewidth=0.7)
        axis.set_xlim(lo, hi)
        axis.set_ylim(y_min - margin, y_max + margin)
        axis.set_title(candidate, fontsize=10, fontweight="bold")
        axis.grid(color="#E5E5E5", linewidth=0.5)
        axis.set_axisbelow(True)
        axis.spines[["top", "right"]].set_visible(False)
    for axis in axes[-1, :]:
        axis.set_xlabel("Ion–peptide distance (nm)")
    for axis in axes[:, 0]:
        axis.set_ylabel("PMF − reference mean (kJ mol⁻¹)")
    handles = [
        plt.Line2D([0], [0], color=LI_COLOR, linewidth=2, label="LiCl"),
        plt.Line2D([0], [0], color=NA_COLOR, linewidth=2, label="NaCl"),
        Patch(color="#B3DDF2", alpha=0.55, label="Bound region"),
        Patch(color="#D9D9D9", alpha=0.7, label="Reference region"),
    ]
    fig.legend(handles=handles, loc="outside lower center", ncol=4, frameon=False)
    save_figure(fig, "pmf_profiles")


def main() -> None:
    results, profiles = validate()
    curate([str(row["candidate"]) for row in results])
    plot_selectivity(results)
    plot_profiles(results, profiles)
    print(f"validated_candidates={len(results)} curated_files={sum(1 for _ in (RAW / 'source_manifest.tsv').open()) - 1}")


if __name__ == "__main__":
    main()
