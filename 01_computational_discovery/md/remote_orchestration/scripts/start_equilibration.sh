#!/usr/bin/env bash
set -euo pipefail

REMOTE_ROOT="${LISPER_REMOTE_ROOT:-/root/LiSPER_remote}"
LISPER_WORKDIR="${LISPER_WORKDIR:-${REMOTE_ROOT}/LiSPER_8cand_LiCl}"

cd "${REMOTE_ROOT}"
exec env LISPER_WORKDIR="${LISPER_WORKDIR}" \
  python3 "${REMOTE_ROOT}/run_lisper_equilibrate.py" \
  > "${LISPER_WORKDIR}/remote_runs/equilibration_batch.nohup.log" 2>&1
