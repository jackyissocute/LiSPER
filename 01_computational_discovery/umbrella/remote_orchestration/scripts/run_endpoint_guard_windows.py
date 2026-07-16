from pathlib import Path
import csv
import re
import shutil

import run_lisper_umbrella_sampling as driver

def window_number(path):
    return int(re.match(r"window_(\d+)_", path.name).group(1))


def main():
    metadata = next(csv.DictReader((driver.UMB_DIR / "umbrella_metadata.tsv").open(), delimiter="\t"))
    initial_distance = float(metadata["initial_distance_nm"])
    base_index = int(driver.WINDOW_EXTENSION_NM / driver.WINDOW_SPACING_NM)
    windows = {window_number(path): path for path in driver.UMB_DIR.glob("window_*")}
    previous = windows.get(base_index)
    if previous is None or not driver.mdrun_finished(previous / "umbrella.log", previous / "umbrella.mdp"):
        raise RuntimeError("The final base window must complete before endpoint guards start")

    first_guard = base_index + 1
    rows = []
    for offset in range(3):
        index = first_guard + offset
        center = initial_distance + index * driver.WINDOW_SPACING_NM
        window = driver.UMB_DIR / f"window_{index:03d}_{center:.2f}nm"
        window.mkdir(exist_ok=True)
        start = window / "start.gro"
        if not start.exists():
            shutil.copy2(previous / "umbrella.gro", start)
        eq_mdp = window / "umbrella_eq.mdp"
        mdp = window / "umbrella.mdp"
        eq_mdp.write_text(driver.base_mdp(int(driver.WINDOW_EQ_NS * 500000), "no", 0.0, center))
        mdp.write_text(driver.base_mdp(int(driver.WINDOW_NS * 500000), "yes", 0.0, center))
        status = "complete"
        if not driver.mdrun_finished(window / "umbrella_eq.log", eq_mdp):
            status = driver.grompp_mdrun(window, eq_mdp, start, "umbrella_eq")
        if status == "complete" and not driver.mdrun_finished(window / "umbrella.log", mdp):
            status = driver.grompp_mdrun(
                window, mdp, window / "umbrella_eq.gro", "umbrella", cpt=window / "umbrella_eq.cpt"
            )
        rows.append({"window_id": f"{index:03d}", "center_nm": f"{center:.4f}", "role": "guard", "status": status})
        if status != "complete":
            break
        previous = window

    with (driver.UMB_DIR / "endpoint_guard_manifest.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0], delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    if rows[-1]["status"] != "complete":
        raise RuntimeError(f"Guard window {rows[-1]['window_id']} ended as {rows[-1]['status']}")


if __name__ == "__main__":
    main()
