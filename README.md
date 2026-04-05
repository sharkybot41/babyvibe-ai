# 🦈 Sharky — Autonomous AI Agent

> *"I don't sleep so Darius can."*

Sharky is a 24/7 autonomous AI agent running on a Mac mini, powered by [OpenClaw](https://openclaw.ai). It serves as the first and only employee of a one-man business.

## What Sharky Does
- 📱 Manages communications (iMessage, Telegram, Discord, voice calls)
- 🔧 Builds tools and automations
- 📊 Monitors systems and flags issues
- 🧠 Learns and evolves every session
- 🚀 Ships code while the boss sleeps

## Communication Channels
| Channel | Endpoint | Status |
|---------|----------|--------|
| Voice | +1 (319) 719-9951 | ✅ Active |
| iMessage | BlueBubbles | ✅ Active |
| Telegram | @sharkybot | ✅ Active |
| Discord | Sharky Bot | ✅ Active |

## Tech Stack
- **Runtime**: OpenClaw 2026.4.2 on macOS (Apple Silicon)
- **Model**: GLM-5.1 (202k context)
- **Voice**: Vapi (Deepgram + OpenAI)
- **Tools**: Python, Node.js, Go, ffmpeg, gh CLI, and 60+ specialized CLIs

## Project Structure
```
├── AGENTS.md          # Agent behavior rules
├── SOUL.md            # Personality and identity
├── USER.md            # About the human
├── TOOLS.md           # Tool documentation
├── MEMORY.md          # Long-term memory
├── IDENTITY.md        # Core identity
├── HEARTBEAT.md       # Periodic check config
├── memory/            # Daily logs
├── tools/             # Custom CLI tools
│   ├── vapi.sh        # Vapi phone management
│   └── sharkyctl.sh   # Sharky control center
└── .secrets/          # API credentials (gitignored)
```

## Philosophy
- Move fast, iterate
- Never ask questions you can answer yourself
- Ship PRs, not live code
- Build something cool every night

---

*Sharky has been running since April 5, 2026.*
