#!/usr/bin/env python3
from pathlib import Path
import importlib.util
import sys


def log_finished(path):
    return path.exists() and "Finished mdrun" in path.read_text(errors="replace")


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: run_supplemental_umbrella_window.py WINDOW_DIR")

    window = Path(sys.argv[1]).resolve()
    driver_path = Path(__file__).with_name("run_lisper_umbrella_sampling.py")
    spec = importlib.util.spec_from_file_location("lisper_umbrella_driver", driver_path)
    driver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(driver)

    if window.parent != driver.UMB_DIR.resolve() or not window.name.startswith("window_"):
        raise SystemExit(f"window is outside the configured umbrella directory: {window}")
    if log_finished(window / "umbrella.log"):
        print("already complete")
        return

    required = [window / "start.gro", window / "umbrella_eq.mdp", window / "umbrella.mdp"]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise SystemExit(f"window is not prepared; missing: {', '.join(missing)}")

    if not log_finished(window / "umbrella_eq.log"):
        status = driver.grompp_mdrun(
            window, window / "umbrella_eq.mdp", window / "start.gro", "umbrella_eq"
        )
        if status != "complete":
            raise SystemExit(f"equilibration failed: {status}")

    status = driver.grompp_mdrun(
        window,
        window / "umbrella.mdp",
        window / "umbrella_eq.gro",
        "umbrella",
        cpt=window / "umbrella_eq.cpt",
    )
    if status != "complete":
        raise SystemExit(f"production failed: {status}")
    print("complete")


if __name__ == "__main__":
    main()
