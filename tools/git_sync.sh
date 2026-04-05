#!/bin/bash
# git_sync.sh — Stage, commit, and push workspace changes to GitHub
# Safe: exits cleanly if nothing to commit.

set -euo pipefail

cd /Users/sharky/.openclaw/workspace

# Stage all changes
git add -A

# Check if there's anything to commit
if git diff --cached --quiet; then
    echo "[✓] Nothing to commit — workspace is clean."
    exit 0
fi

# Commit and push
MSG="auto-sync: $(date '+%Y-%m-%d %H:%M:%S %Z')"
git commit -m "$MSG"
git push

echo "[✓] Pushed: $MSG"
