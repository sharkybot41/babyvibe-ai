#!/bin/bash
# check_voicemail.sh — Check Vapi for new calls since last check, log transcripts
# Tracks last check timestamp and only surfaces new calls.

set -euo pipefail

VAPI_KEY="07f9b790-22a5-4819-9a11-659d9f6c0d77"
VAPI_URL="https://api.vapi.ai/call?limit=5"
DATA_DIR="/Users/sharky/.openclaw/workspace/data/call_logs"
TS_FILE="/Users/sharky/.openclaw/workspace/data/.last_voicemail_check"

mkdir -p "$DATA_DIR"

# Get last check timestamp (ISO 8601) or epoch zero
if [[ -f "$TS_FILE" ]]; then
    LAST_CHECK=$(cat "$TS_FILE")
else
    LAST_CHECK="1970-01-01T00:00:00.000Z"
fi

# Fetch recent calls from Vapi
RESPONSE=$(curl -sS -f \
    -H "Authorization: Bearer $VAPI_KEY" \
    -H "Content-Type: application/json" \
    "$VAPI_URL") || {
    echo "ERROR: Failed to fetch calls from Vapi API" >&2
    exit 1
}

# Update last check timestamp
date -u +%Y-%m-%dT%H:%M:%S.000Z > "$TS_FILE"

# Parse calls with python (most reliable JSON parsing on macOS)
python3 <<'PYEOF' "$RESPONSE" "$LAST_CHECK" "$DATA_DIR"
import json, sys, os
from datetime import datetime, timezone

response = json.loads(sys.argv[1])
last_check = datetime.fromisoformat(sys.argv[2].replace("Z", "+00:00"))
data_dir = sys.argv[3]

new_calls = []
for call in response:
    # Vapi calls have a 'createdAt' field
    created = call.get("createdAt", "")
    if not created:
        continue
    created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
    if created_dt > last_check:
        new_calls.append(call)

if not new_calls:
    print("No new calls since last check.")
    sys.exit(0)

print(f"Found {len(new_calls)} new call(s) since {last_check.isoformat()}:\n")

for call in new_calls:
    call_id = call.get("id", "unknown")
    created = call.get("createdAt", "unknown")
    status = call.get("status", "unknown")
    phone = call.get("customer", {}).get("number", "unknown")
    duration = call.get("duration", 0)
    transcript = call.get("transcript", "") or call.get("artifacts", {}).get("transcript", "")

    print(f"📞 {phone} | {status} | {duration}s | {created}")

    # Save transcript to file
    date_str = created[:10] if created else "unknown"
    safe_phone = phone.replace("+", "").replace(" ", "-")
    log_file = os.path.join(data_dir, f"{date_str}_{safe_phone}_{call_id[:8]}.md")

    with open(log_file, "w") as f:
        f.write(f"# Call Log — {created}\n\n")
        f.write(f"- **From:** {phone}\n")
        f.write(f"- **Status:** {status}\n")
        f.write(f"- **Duration:** {duration}s\n")
        f.write(f"- **Call ID:** {call_id}\n\n")
        if transcript:
            f.write(f"## Transcript\n\n{transcript}\n")
        else:
            f.write("## Transcript\n\n_No transcript available._\n")

    print(f"  → Saved to {os.path.basename(log_file)}")
PYEOF
