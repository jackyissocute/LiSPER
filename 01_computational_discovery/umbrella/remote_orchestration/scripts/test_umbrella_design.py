import importlib.util
import os
from pathlib import Path
import tempfile


def load_driver(root):
    os.environ.pop("LISPER_TOPOLOGY", None)
    os.environ.update(
        LISPER_WORKDIR=str(root),
        LISPER_ION_RESNAME="SOD",
        LISPER_CANDIDATE="LiD3-Flex",
        LISPER_UMB_SUBDIR="umbrella_sampling_binding_site_v2",
    )
    path = Path(__file__).with_name("run_lisper_umbrella_sampling.py")
    spec = importlib.util.spec_from_file_location("umbrella_driver_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fresh_campaign_gets_three_pbc_safe_guards():
    with tempfile.TemporaryDirectory() as tmp:
        driver = load_driver(Path(tmp))
        analysis, total, safe_max = driver.pbc_safe_extensions(0.1083, 9.5727)
        assert driver.GUARD_WINDOWS == 3
        assert abs(analysis - 1.95) < 1e-9
        assert abs(total - 2.175) < 1e-9
        assert 0.1083 + total < safe_max
        try:
            driver.load_site_lock()
        except RuntimeError as error:
            assert "require a paired binding-site manifest" in str(error)
        else:
            raise AssertionError("fresh campaign accepted without a paired site manifest")


def test_existing_campaign_keeps_original_window_set():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        marker = root / "systems/LiD3-Flex/gromacs/umbrella_sampling_binding_site_v2/pull/pull_config.tsv"
        marker.parent.mkdir(parents=True)
        marker.write_text("existing\n")
        driver = load_driver(root)
        analysis, total, _ = driver.pbc_safe_extensions(0.1083, 9.5727)
        assert driver.GUARD_WINDOWS == 0
        assert analysis == total
        assert driver.load_site_lock() is None


def test_minimum_image_distance_uses_box():
    with tempfile.TemporaryDirectory() as tmp:
        driver = load_driver(Path(tmp))
        box = ((2.0, 0.0, 0.0), (0.0, 2.0, 0.0), (0.0, 0.0, 2.0))
        assert abs(driver.minimum_image_distance((0.1, 0.0, 0.0), (1.9, 0.0, 0.0), box) - 0.2) < 1e-9


def test_topology_must_be_explicit_and_hashed():
    with tempfile.TemporaryDirectory() as tmp:
        driver = load_driver(Path(tmp))
        try:
            driver.resolve_topology()
        except RuntimeError as error:
            assert "LISPER_TOPOLOGY" in str(error)
        else:
            raise AssertionError("driver accepted an unpinned topology")
        topology = Path(tmp) / "reviewed.top"
        topology.write_text("reviewed topology\n")
        os.environ["LISPER_TOPOLOGY"] = str(topology)
        resolved, digest = driver.resolve_topology()
        assert resolved == topology.resolve()
        assert len(digest) == 64


if __name__ == "__main__":
    test_fresh_campaign_gets_three_pbc_safe_guards()
    test_existing_campaign_keeps_original_window_set()
    test_minimum_image_distance_uses_box()
    test_topology_must_be_explicit_and_hashed()
