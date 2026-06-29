#!/usr/bin/env bash
set -eo pipefail
source /root/miniconda3/etc/profile.d/conda.sh
conda activate lisper-gmx
cd "$(dirname "$0")"
gmx wham -it tpr-files.dat -if pullf-files.dat -o profile_v2.xvg -hist histo_v2.xvg -unit kJ -b 100 2>&1 | tee wham_v2.log
python3 - <<PY
from pathlib import Path
import re, math
log=Path("wham_v2.log").read_text(errors="ignore") if Path("wham_v2.log").exists() else ""
rows=[]
profile=Path("profile_v2.xvg")
if profile.exists():
    for line in profile.read_text(errors="ignore").splitlines():
        if not line or line.startswith(("#","@")): continue
        p=line.split()
        if len(p)>=2:
            try: rows.append((float(p[0]), float(p[1])))
            except ValueError: pass
finite=[r for r in rows if math.isfinite(r[1])]
empty=len(rows)-len(finite)
patterns=[r"(?i)empty",r"(?i)weak",r"(?i)only one",r"(?i)single.window",r"(?i)poor overlap",r"(?i)Warning"]
warning_hits=sum(len(re.findall(p, log)) for p in patterns)
pmf_min=min((y for _,y in finite), default=float("nan"))
pmf_max=max((y for _,y in finite), default=float("nan"))
with Path("wham_v2_qc_summary.tsv").open("w") as f:
    f.write("metric\tvalue\n")
    f.write(f"input_windows\t{len(Path(tpr-files.dat).read_text().splitlines())}\n")
    f.write(f"profile_points\t{len(rows)}\n")
    f.write(f"finite_points\t{len(finite)}\n")
    f.write(f"nonfinite_profile_points\t{empty}\n")
    f.write(f"warning_keyword_hits\t{warning_hits}\n")
    f.write(f"pmf_min_kj_mol\t{pmf_min:.6g}\n")
    f.write(f"pmf_max_kj_mol\t{pmf_max:.6g}\n")
    f.write(f"pmf_span_kj_mol\t{(pmf_max-pmf_min) if finite else float(nan):.6g}\n")
    f.write("status\tpreliminary_qc_review_required\n")
PY
