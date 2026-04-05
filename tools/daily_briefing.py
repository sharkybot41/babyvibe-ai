#!/usr/bin/env python3
"""Daily morning briefing for Darius — run with `python3 daily_briefing.py`"""

import json
import subprocess
import urllib.request
import urllib.error
import os
import random
from datetime import datetime
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────
VAPI_API_KEY = os.environ.get("VAPI_API_KEY", "07f9b790-22a5-4819-9a11-659d9f6c0d77")
VAPI_BASE = "https://api.vapi.ai"
LOCATION = "Los Angeles"
WEATHER_URL = "https://wttr.in/Los+Angeles?format=j1"

QUOTES = [
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
    "The only way to do great work is to love what you do. — Steve Jobs",
    "Ship it. Ship it now. Perfect is the enemy of shipped.",
    "You don't have to be great to start, but you have to start to be great.",
    "Action is the foundational key to all success. — Picasso",
    "Every morning brings new potential, but if you dwell on the misfortunes of the day before, you tend to overlook tremendous opportunities. — Harvey Mackay",
    "Move fast and break things. Unless you're Darius. Then ship PRs.",
]

DIVIDER = "═" * 50

# ── Helpers ─────────────────────────────────────────────────────────────────

def run(cmd, timeout=15):
    """Run a shell command, return stdout or None on failure."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def fetch_json(url, headers=None, timeout=10):
    """GET a URL and return parsed JSON or None."""
    try:
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None


def header(title):
    return f"\n  {title}\n  {'─' * (len(title))}"


# ── Sections ────────────────────────────────────────────────────────────────

def get_vapi_calls():
    """Check Vapi for recent calls (last 24h)."""
    data = fetch_json(
        f"{VAPI_BASE}/call",
        headers={"Authorization": f"Bearer {VAPI_API_KEY}"},
    )
    if not data or not isinstance(data, list):
        return "  ⚠ Could not fetch Vapi calls"

    lines = []
    for call in data[:10]:
        cid = call.get("id", "?")[:8]
        status = call.get("status", "unknown")
        ended = call.get("endedAt", "")
        started = call.get("startedAt", "")
        phone = call.get("customer", {}).get("number", "unknown")
        cost = call.get("cost", "?")
        line = f"  • {cid}… | {status} | {phone} | cost: ${cost}"
        if ended:
            line += f" | ended: {ended[:16]}"
        lines.append(line)

    if not lines:
        return "  No recent calls."
    total = len(data)
    return "\n".join(lines) + f"\n  ({total} total calls fetched)"


def get_weather():
    """Fetch weather via wttr.in JSON."""
    data = fetch_json(WEATHER_URL)
    if not data:
        # Fallback to plain text
        txt = run("curl -s 'wttr.in/Los+Angeles?format=3'")
        return f"  {txt}" if txt else "  ⚠ Could not fetch weather"

    try:
        cur = data["current_condition"][0]
        area = data.get("nearest_area", [{}])[0].get("areaName", [{}])[0].get("value", LOCATION)
        temp_f = cur.get("temp_F", "?")
        feels = cur.get("FeelsLikeF", "?")
        desc = cur.get("weatherDesc", [{}])[0].get("value", "?")
        humidity = cur.get("humidity", "?")
        wind = cur.get("windspeedMiles", "?")
        vis = cur.get("visibility", "?")

        lines = [
            f"  📍 {area}",
            f"  🌡  {temp_f}°F (feels {feels}°F) — {desc}",
            f"  💧 Humidity: {humidity}% | 💨 Wind: {wind} mph | 👁 Visibility: {vis} mi",
        ]

        # Forecast
        for day in data.get("weather", [])[:3]:
            date = day.get("date", "?")
            hi = day.get("maxtempF", "?")
            lo = day.get("mintempF", "?")
            desc_d = day.get("hourly", [{}])[4].get("weatherDesc", [{}])[0].get("value", "?") if day.get("hourly") else "?"
            lines.append(f"  📅 {date}: {lo}°–{hi}°F, {desc_d}")

        return "\n".join(lines)
    except (KeyError, IndexError):
        return "  ⚠ Weather data format unexpected"


def get_github_notifications():
    """Check GitHub notifications via gh CLI."""
    out = run("gh api notifications --paginate 2>/dev/null | head -c 20000")
    if not out:
        return "  No unread notifications (or gh not authenticated)."

    try:
        notifs = json.loads(out)
    except json.JSONDecodeError:
        return f"  ⚠ Could not parse GitHub output"

    if not notifs:
        return "  ✅ No unread notifications!"

    lines = []
    by_repo = {}
    for n in notifs:
        repo = n.get("repository", {}).get("full_name", "?")
        reason = n.get("reason", "?")
        subject = n.get("subject", {}).get("title", "?")
        stype = n.get("subject", {}).get("type", "?")
        url = n.get("subject", {}).get("url", "")
        by_repo.setdefault(repo, []).append(f"  • [{stype}] {subject} ({reason})")

    for repo, items in list(by_repo.items())[:5]:
        lines.append(f"  📦 {repo}")
        lines.extend(items[:5])

    total = len(notifs)
    if total > 20:
        lines.append(f"  … and {total - 20} more")
    lines.append(f"  ({total} total unread)")
    return "\n".join(lines)


def get_system_status():
    """Disk, uptime, memory."""
    lines = []

    # Uptime
    uptime = run("uptime -p") or run("uptime")
    if uptime:
        lines.append(f"  ⏱  Uptime: {uptime}")

    # Disk
    disk = run("df -h / | tail -1")
    if disk:
        parts = disk.split()
        if len(parts) >= 5:
            lines.append(f"  💾 Disk: {parts[1]} total, {parts[2]} used, {parts[3]} avail ({parts[4]})")

    # Memory
    mem = run("vm_stat | head -10")
    if mem:
        # Parse page count for a quick summary
        lines.append(f"  🧠 Memory (vm_stat):\n    " + "\n    ".join(mem.split("\n")[:6]))

    # Load
    load = run("sysctl -n vm.loadavg")
    if load:
        lines.append(f"  ⚡ Load: {load.strip()}")

    return "\n".join(lines) if lines else "  ⚠ Could not fetch system info"


def get_calendar_events():
    """Try gogcli for upcoming calendar events."""
    out = run("gogcli calendar list --max 10 --days 2 2>/dev/null")
    if out:
        lines = ["  " + line for line in out.split("\n") if line.strip()]
        return "\n".join(lines) if lines else "  No upcoming events."
    return "  📅 Calendar not available (gogcli not configured)"


def get_quote():
    return f"  💬 {random.choice(QUOTES)}"


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    now = datetime.now().strftime("%A, %B %d, %Y — %I:%M %p")
    sections = [
        ("🌤  WEATHER", get_weather),
        ("📞 VAPI — RECENT CALLS", get_vapi_calls),
        ("🐙 GITHUB NOTIFICATIONS", get_github_notifications),
        ("🖥  SYSTEM STATUS", get_system_status),
        ("📅 CALENDAR", get_calendar_events),
        ("💭 DAILY WISDOM", get_quote),
    ]

    print(f"\n{DIVIDER}")
    print(f"  🦈 SHARKY'S MORNING BRIEFING")
    print(f"  {now}")
    print(DIVIDER)

    for title, fn in sections:
        print(header(title))
        try:
            print(fn())
        except Exception as e:
            print(f"  ⚠ Error: {e}")

    print(f"\n{DIVIDER}")
    print(f"  Have a great day, Darius! 🦈")
    print(f"{DIVIDER}\n")


if __name__ == "__main__":
    main()
