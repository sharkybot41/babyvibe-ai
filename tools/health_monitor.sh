#!/usr/bash
# Sharky Health Monitor - checks system vitals and alerts if issues
set -e

ALERTS=""
WARNINGS=""

# Disk space check
DISK_PCT=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ "$DISK_PCT" -gt 90 ]; then
  ALERTS="$ALERTS\n🔴 DISK CRITICAL: ${DISK_PCT}% used"
elif [ "$DISK_PCT" -gt 80 ]; then
  WARNINGS="$WARNINGS\n🟡 DISK WARNING: ${DISK_PCT}% used"
else
  echo "✅ Disk: ${DISK_PCT}% used ($(df -h / | tail -1 | awk '{print $4}') free)"
fi

