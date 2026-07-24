import importlib.util
import math
from pathlib import Path
import tempfile


path = Path(__file__).with_name("evaluate_paired_pmf_qc.py")
spec = importlib.util.spec_from_file_location("pmf_estimator", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


with tempfile.TemporaryDirectory() as tmp:
    profile = Path(tmp) / "profile.xvg"
    rt = module.R_KJ_MOL_K * 298.15
    profile.write_text("\n".join(f"{r} {-rt * math.log(4 * math.pi * r * r)}" for r in (0.5, 1.0, 2.0)))
    corrected = module.corrected_profile(profile, 298.15)
    assert max(abs(y) for _, y in corrected) < 1e-12
    assert module.binding_delta_g([(0.5, -5.0), (2.0, 0.0)], 0.4, 0.6, 1.9, 2.1) == -5.0
    iact = Path(tmp) / "iact.xvg"
    iact.write_text("0.5 3\n1.0 1\n1.5 2\n")
    assert module.iact_stats(iact) == (1.0, 2.0, 3.0)
