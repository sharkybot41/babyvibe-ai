#!/bin/bash
# Sharky Control Center - Main CLI for all Sharky operations
set -e

WORKSPACE="/Users/sharky/.openclaw/workspace"
MEMORY="$WORKSPACE/memory"

case "${1:-status}" in
  status)
    echo "🦈 Sharky Status Report"
    echo "========================"
    echo "Phone: +1 (319) 719-9951 (Vapi - Active)"
    echo "Email: sharkybot41@gmail.com"
    echo "GitHub: sharkybot41"
    echo "Uptime: $(uptime | sed 's/.*up //' | sed 's/,.*//')"
    echo "Disk: $(df -h / | tail -1 | awk '{print $4 " free"}')"
    ;;
  log)
    MSG="${2:?Usage: sharkyctl log 'message'}"
    TIMESTAMP=$(date '+%H:%M')
    echo "- [$TIMESTAMP] $MSG" >> "$MEMORY/$(date '+%Y-%m-%d').md"
    echo "📝 Logged: $MSG"
    ;;
  memory)
    cat "$MEMORY/$(date '+%Y-%m-%d').md" 2>/dev/null || echo "No memory for today"
    ;;
  git-push)
    cd "$WORKSPACE" && git add -A && git commit -m "${2:-sharky auto-commit}" 2>/dev/null
    ;;
  help|*)
    echo "🦈 Sharky Control Center"
    echo "  status     - Show system status"
    echo "  log 'msg'  - Log a memory entry"
    echo "  memory     - Show today's memory log"
    echo "  git-push   - Commit workspace changes"
    ;;
esac
