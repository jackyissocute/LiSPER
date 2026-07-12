#!/bin/bash
# Pull cloud/automation pushes into local Mac clones when the tree is clean.
set -u
export PATH="/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$PATH"
export GIT_TERMINAL_PROMPT=0

LOG_DIR="${HOME}/Library/Logs"
mkdir -p "$LOG_DIR"
LOG="${LOG_DIR}/lisper-git-sync.log"
ts() { date '+%Y-%m-%d %H:%M:%S'; }

sync_repo() {
  local dir="$1"
  local name
  name="$(basename "$dir")"
  if [[ ! -d "$dir/.git" ]]; then
    echo "$(ts) SKIP ${name}: not a git repo" >>"$LOG"
    return 0
  fi
  cd "$dir" || return 0

  # Tracked changes only — untracked files (e.g. new local notes) must not block sync.
  if [[ -n "$(git status --porcelain -uno 2>/dev/null)" ]]; then
    echo "$(ts) SKIP ${name}: dirty tracked files" >>"$LOG"
    return 0
  fi

  if ! git fetch origin >/dev/null 2>&1; then
    echo "$(ts) FAIL ${name}: fetch" >>"$LOG"
    return 0
  fi

  local branch behind
  branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)"
  behind="$(git rev-list --count "HEAD..origin/${branch}" 2>/dev/null || echo 0)"
  if [[ "$behind" == "0" ]]; then
    echo "$(ts) OK   ${name}: already up to date (${branch})" >>"$LOG"
    return 0
  fi

  if git pull --rebase --autostash origin "$branch" >>"$LOG" 2>&1; then
    echo "$(ts) PULL ${name}: +${behind} commit(s) on ${branch}" >>"$LOG"
  else
    echo "$(ts) FAIL ${name}: pull --rebase" >>"$LOG"
    git rebase --abort >/dev/null 2>&1 || true
  fi
}

echo "$(ts) ---- sync start ----" >>"$LOG"
sync_repo "${HOME}/Documents/GitHub/LiSPER"
sync_repo "${HOME}/Documents/GitHub/LiSPER-Dashboard"
echo "$(ts) ---- sync end ----" >>"$LOG"
