#!/bin/bash
export PATH=/opt/gromacs/2026.0/bin:/usr/local/bin:$PATH
export LISPER_REMOTE_ROOT=/data/LiSPER_remote
export LISPER_GLOBAL_MDRUN_LIMIT=120
LOG=/data/LiSPER_remote/logs/quickpod_resume/watchdog.log
mkdir -p "$(dirname "$LOG")"
cd /data/LiSPER_remote
while true; do
  n=$(pgrep -af "gmx mdrun" | grep -v pgrep | wc -l)
  l=$(pgrep -af resume_incomplete_windows_quickpod.py | grep -v pgrep | wc -l)
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) mdrun=$n launcher=$l" >> "$LOG"
  if [ "$l" -eq 0 ]; then
    left=$(/usr/bin/python3 -c "from importlib.util import spec_from_file_location, module_from_spec; s=spec_from_file_location('r','/data/LiSPER_remote/scripts/resume_incomplete_windows_quickpod.py'); m=module_from_spec(s); s.loader.exec_module(m); print(len(m.build_queue()))")
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) queue_left=$left" >> "$LOG"
    if [ "$left" -gt 0 ] && [ "$n" -lt 110 ]; then
      echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) launching resume" >> "$LOG"
      nohup /usr/bin/python3 /data/LiSPER_remote/scripts/resume_incomplete_windows_quickpod.py \
        >> /data/LiSPER_remote/logs/quickpod_resume/launcher_loop.stdout 2>&1 &
    fi
    if [ "$left" -eq 0 ] && [ "$n" -eq 0 ]; then
      echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ALL_COMPLETE" >> "$LOG"
      break
    fi
  fi
  find /data/LiSPER_remote/LiSPER_8cand_LiCl /data/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker /data/LiSPER_remote/LiSPER_8cand_NaCl_overflow_workerA \
    -path "*umbrella_sampling_binding_site_v2*" -name "*.xtc" 2>/dev/null | while read -r f; do
      d=$(dirname "$f")
      if grep -q "Finished mdrun" "$d/umbrella.log" 2>/dev/null; then rm -f "$f"; fi
    done
  sleep 120
done
