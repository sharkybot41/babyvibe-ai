#!/bin/bash
# Sharky Vapi CLI Tool
set -e

API_KEY="07f9b790-22a5-4819-9a11-659d9f6c0d77"
BASE="https://api.vapi.ai"
ASSISTANT_ID="8e9a507f-5063-4182-bf9c-da0447d84b2e"
PHONE_ID="b9eddda9-174e-4b10-8738-35e0ba302288"

case "${1:-help}" in
  call)
    TO="${2:?Usage: vapi.sh call +number}"
    curl -s -X POST "$BASE/call/phone" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d "{\"assistantId\":\"$ASSISTANT_ID\",\"phoneNumberId\":\"$PHONE_ID\",\"customer\":{\"number\":\"$TO\"}}"
    ;;
  calls)
    LIMIT="${2:-10}"
    curl -s "$BASE/call?limit=$LIMIT" -H "Authorization: Bearer $API_KEY" | python3 -m json.tool
    ;;
  assistants)
    curl -s "$BASE/assistant" -H "Authorization: Bearer $API_KEY" | python3 -m json.tool
    ;;
  phone)
    curl -s "$BASE/phone-number" -H "Authorization: Bearer $API_KEY" | python3 -m json.tool
    ;;
  help|*)
    echo "🦈 Sharky Vapi CLI"
    echo "  call +number  - Make outbound call"
    echo "  calls [limit] - List recent calls"
    echo "  assistants    - List assistants"
    echo "  phone         - List phone numbers"
    ;;
esac
