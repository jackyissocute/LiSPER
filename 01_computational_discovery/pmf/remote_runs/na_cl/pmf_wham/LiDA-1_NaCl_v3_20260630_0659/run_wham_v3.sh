#!/usr/bin/env bash
set -eo pipefail
source /root/miniconda3/etc/profile.d/conda.sh
conda activate lisper-gmx
cd "$(dirname "$0")"
gmx wham -it tpr-files.dat -if pullf-files.dat -o profile_v3.xvg -hist histo_v3.xvg -unit kJ -b 100 2>&1 | tee wham_v3.log
gmx wham -it tpr-files.dat -if pullf-files.dat -o profile_v3_b250.xvg -hist histo_v3_b250.xvg -unit kJ -b 250 2>&1 | tee wham_v3_b250.log
gmx wham -it tpr-files.dat -if pullf-files.dat -o profile_v3_b500.xvg -hist histo_v3_b500.xvg -unit kJ -b 500 2>&1 | tee wham_v3_b500.log
mkdir -p bootstrap_100_b100
gmx wham -it tpr-files.dat -if pullf-files.dat -o bootstrap_100_b100/profile_kjmol.xvg -hist bootstrap_100_b100/histo.xvg -unit kJ -b 100 -nBootstrap 100 -bsres bootstrap_100_b100/bootstrap_profiles.xvg -bsprof bootstrap_100_b100/bootstrap_profile_std.xvg 2>&1 | tee bootstrap_100_b100/wham.stdout.log
python3 - <<"PY"
from pathlib import Path
import math,re

def read_profile(path):
    rows=[]
    p=Path(path)
    if not p.exists(): return rows
    for line in p.read_text(errors="ignore").splitlines():
        if not line or line.startswith(("#","@")): continue
        parts=line.split()
        if len(parts)>=2:
            try: rows.append((float(parts[0]), float(parts[1])))
            except ValueError: pass
    return rows
log="\n".join(Path(p).read_text(errors="ignore") for p in ["wham_v3.log","wham_v3_b250.log","wham_v3_b500.log","bootstrap_100_b100/wham.stdout.log"] if Path(p).exists())
warn_patterns=[r"(?i)empty",r"(?i)weak",r"(?i)only one",r"(?i)single.window",r"(?i)poor overlap",r"(?i)Warning"]
warning_hits=sum(len(re.findall(p, log)) for p in warn_patterns)
profiles={"b100":"profile_v3.xvg","b250":"profile_v3_b250.xvg","b500":"profile_v3_b500.xvg","bootstrap":"bootstrap_100_b100/profile_kjmol.xvg"}
summary=[]
spans=[]
for label,path in profiles.items():
    rows=read_profile(path)
    finite=[r for r in rows if math.isfinite(r[1])]
    vals=[y for _,y in finite]
    span=(max(vals)-min(vals)) if vals else float("nan")
    if math.isfinite(span): spans.append(span)
    summary.append((label,len(rows),len(finite),len(rows)-len(finite),min(vals) if vals else float("nan"),max(vals) if vals else float("nan"),span))
span_shift=(max(spans)-min(spans)) if spans else float("nan")
with Path("wham_v3_qc_summary.tsv").open("w") as f:
    f.write("metric\tvalue\n")
    f.write(f"input_windows\t{sum(1 for _ in Path(tpr-files.dat).open())}\n")
    f.write(f"warning_keyword_hits\t{warning_hits}\n")
    f.write(f"time_slice_span_shift_kj_mol\t{span_shift:.6g}\n")
    for label,n,fin,nonfin,mi,ma,span in summary:
        f.write(f"{label}_profile_points\t{n}\n")
        f.write(f"{label}_finite_points\t{fin}\n")
        f.write(f"{label}_nonfinite_points\t{nonfin}\n")
        f.write(f"{label}_pmf_min_kj_mol\t{mi:.6g}\n")
        f.write(f"{label}_pmf_max_kj_mol\t{ma:.6g}\n")
        f.write(f"{label}_pmf_span_kj_mol\t{span:.6g}\n")
    status="preliminary_qc_review_required"
    if warning_hits==0 and span_shift==span_shift and span_shift < 1.0:
        status="qc_numeric_screen_pass_manual_region_review_required"
    f.write(f"status\t{status}\n")
PY
