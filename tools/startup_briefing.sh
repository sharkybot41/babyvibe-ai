#!/bin/bash
# startup_briefing.sh — Run daily briefing, save to file, echo urgent items to stdout
# Usage: ./startup_briefing.sh [--urgent-only]

set -euo pipefail

BRIEFING_PY="/Users/sharky/.openclaw/workspace/tools/daily_briefing.py"
OUTDIR="/Users/sharky/.openclaw/workspace/data/briefings"
TODAY=$(date +%Y-%m-%d)
OUTFILE="$OUTDIR/$TODAY.md"
URGENT_ONLY=false

if [[ "${1:-}" == "--urgent-only" ]]; then
    URGENT_ONLY=true
fi

mkdir -p "$OUTDIR"

# Run the briefing script
if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found" >&2
    exit 1
fi

if [[ ! -f "$BRIEFING_PY" ]]; then
    echo "ERROR: $BRIEFING_PY not found" >&2
    exit 1
fi

OUTPUT=$(python3 "$BRIEFING_PY" 2>&1) || {
    echo "ERROR: Briefing script failed: $OUTPUT" >&2
    exit 1
}

# Save full briefing to file
cat > "$OUTFILE" <<EOF
# Daily Briefing — $TODAY

_Generated at $(date '+%H:%M:%S %Z')_

---

$OUTPUT
EOF

echo "[✓] Briefing saved to $OUTFILE"

# Extract urgent items (lines containing keywords) and output to stdout
if [[ "$URGENT_ONLY" == true ]]; then
    echo "$OUTPUT" | grep -iE '(urgent|alert|warning|important|critical|⚠️|🚨|action required|deadline|ASAP)' || true
else
    # Always echo urgent lines to stdout for piping
    URGENT=$(echo "$OUTPUT" | grep -iE '(urgent|alert|warning|important|critical|⚠️|🚨|action required|deadline|ASAP)' || true)
    if [[ -n "$URGENT" ]]; then
        echo "⚠️ URGENT ITEMS:"
        echo "$URGENT"
    fi
fi
