import importlib.util
import os
from pathlib import Path
import tempfile


def load_driver(root):
    os.environ.pop("LISPER_GLOBAL_MDRUN_LIMIT", None)
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
        assert driver.GLOBAL_MDRUN_LIMIT == 126
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


def test_mdrun_usage_counts_real_process_threads():
    with tempfile.TemporaryDirectory() as tmp:
        driver = load_driver(Path(tmp))
        proc = Path(tmp) / "proc"
        for pid, comm, cmdline, threads in [
            ("1", "gmx", b"gmx\0mdrun\0-ntomp\07\0", 7),
            ("2", "gmx_mpi", b"gmx_mpi\0mdrun\0-ntomp\01\0", 1),
            ("3", "bash", b"bash\0driver.sh\0", 1),
        ]:
            path = proc / pid
            path.mkdir(parents=True)
            (path / "comm").write_text(comm + "\n")
            (path / "cmdline").write_bytes(cmdline)
            (path / "status").write_text(f"Name:\t{comm}\nThreads:\t{threads}\n")
        assert driver.active_mdrun_usage(proc) == (2, 8)


def test_active_mdrun_cwds_excludes_wrappers():
    with tempfile.TemporaryDirectory() as tmp:
        driver = load_driver(Path(tmp))
        proc = Path(tmp) / "proc"
        work = Path(tmp) / "window"
        work.mkdir()
        for pid, comm, cmdline in [
            ("1", "gmx", b"gmx\0mdrun\0"),
            ("2", "bash", b"bash\0-lc\0gmx mdrun\0"),
        ]:
            path = proc / pid
            path.mkdir(parents=True)
            (path / "comm").write_text(comm + "\n")
            (path / "cmdline").write_bytes(cmdline)
            (path / "cwd").symlink_to(work, target_is_directory=True)
        assert driver.active_mdrun_cwds(proc) == {work.resolve()}


def test_mdrun_finished_requires_target_step():
    with tempfile.TemporaryDirectory() as tmp:
        driver = load_driver(Path(tmp))
        mdp = Path(tmp) / "run.mdp"
        log = Path(tmp) / "run.log"
        mdp.write_text("nsteps = 1000000\n")
        log.write_text("Step           Time\n83360 166.72000\nFinished mdrun\n")
        assert not driver.mdrun_finished(log, mdp)
        log.write_text("Step           Time\n1000000 2000.00000\nFinished mdrun\n")
        assert driver.mdrun_finished(log, mdp)


if __name__ == "__main__":
    test_fresh_campaign_gets_three_pbc_safe_guards()
    test_existing_campaign_keeps_original_window_set()
    test_minimum_image_distance_uses_box()
    test_mdrun_usage_counts_real_process_threads()
    test_active_mdrun_cwds_excludes_wrappers()
    test_mdrun_finished_requires_target_step()
