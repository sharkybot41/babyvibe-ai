#!/usr/bin/env python3
"""Vapi AI phone/call management CLI."""

import argparse
import json
import subprocess
import sys

API_KEY = "07f9b790-22a5-4819-9a11-659d9f6c0d77"
BASE_URL = "https://api.vapi.ai"
ASSISTANT_ID = "8e9a507f-5063-4182-bf9c-da0447d84b2e"
PHONE_NUMBER_ID = "b9eddda9-174e-4b10-8738-35e0ba302288"
PHONE_NUMBER = "+13197199951"
DARIUS_NUMBER = "+18318898775"


def curl(method, path, data=None):
    """Make an HTTP request via curl. Returns parsed JSON or raw text."""
    url = f"{BASE_URL}{path}"
    cmd = ["curl", "-s", "-X", method, url,
           "-H", f"Authorization: Bearer {API_KEY}",
           "-H", "Content-Type: application/json"]
    if data:
        cmd += ["-d", json.dumps(data)]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        print(f"curl error: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return result.stdout


def cmd_call(args):
    """Initiate an outbound call to the given number."""
    number = args.number
    resp = curl("POST", "/call", {
        "assistantId": ASSISTANT_ID,
        "phoneNumberId": PHONE_NUMBER_ID,
        "customer": {"number": number},
    })
    call_id = resp.get("id", "unknown")
    status = resp.get("status", "unknown")
    print(f"Call initiated: {call_id} → {number} [{status}]")


def cmd_calls(_args):
    """List recent calls (last 10)."""
    resp = curl("GET", "/call?limit=10")
    if isinstance(resp, list):
        for c in resp[:10]:
            cid = c.get("id", "?")[:8]
            num = c.get("customer", {}).get("number", "?")
            status = c.get("status", "?")
            ended = c.get("endedReason", "")
            ts = c.get("createdAt", "")[:19]
            print(f"  {ts}  {cid}…  {num}  {status}  {ended}")
    else:
        print(json.dumps(resp, indent=2))


def cmd_call_log(args):
    """Get details of a specific call."""
    resp = curl("GET", f"/call/{args.call_id}")
    print(json.dumps(resp, indent=2))


def cmd_test_call(_args):
    """Test call to Darius."""
    print(f"Calling Darius ({DARIUS_NUMBER})…")
    resp = curl("POST", "/call", {
        "assistantId": ASSISTANT_ID,
        "phoneNumberId": PHONE_NUMBER_ID,
        "customer": {"number": DARIUS_NUMBER},
    })
    call_id = resp.get("id", "unknown")
    status = resp.get("status", "unknown")
    print(f"Test call initiated: {call_id} [{status}]")


def cmd_status(_args):
    """Show phone number and assistant status."""
    phone = curl("GET", f"/phone-number/{PHONE_NUMBER_ID}")
    assistant = curl("GET", f"/assistant/{ASSISTANT_ID}")
    print(f"Phone: {phone.get('number', '?')}  (ID: {PHONE_NUMBER_ID})")
    print(f"Assistant: {assistant.get('name', '?')}  (ID: {ASSISTANT_ID})")


def main():
    parser = argparse.ArgumentParser(description="Vapi call management")
    sub = parser.add_subparsers(dest="command", required=True)

    p_call = sub.add_parser("call", help="Initiate outbound call")
    p_call.add_argument("number", help="Phone number to call")
    p_call.set_defaults(func=cmd_call)

    sub.add_parser("calls", help="List recent calls").set_defaults(func=cmd_calls)

    p_log = sub.add_parser("call-log", help="Get call details")
    p_log.add_argument("call_id", help="Call ID")
    p_log.set_defaults(func=cmd_call_log)

    sub.add_parser("test-call", help="Test call to Darius").set_defaults(func=cmd_test_call)
    sub.add_parser("status", help="Show phone/assistant status").set_defaults(func=cmd_status)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
