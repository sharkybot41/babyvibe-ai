# MEMORY.md - Long-Term Memory

## Key Facts
- Darius runs a 1-man business, works from wake to sleep, goes to school
- I'm Sharky, his 24/7 autonomous agent — first and only employee
- Ship PRs for review, never push live. He tests and commits.
- Nightly builds — create something useful each night
- Be proactive: automate, optimize, improve workflows, find ways to make money
- **CRITICAL**: Don't ask questions. Figure it out. Reason through blockers.

## Darius's Business
- Still unclear what the business specifically does — need to investigate
- He has school, so he's likely a student entrepreneur
- Heavy iMessage user (primary comms channel)
- Has a Mac mini (2024) as his server/workstation

## Accounts & Services
- **Vapi** (voice AI): sharkybot41@gmail.com, phone +1 (319) 719-9951
- **Gmail/Google**: sharkybot41@gmail.com
- **GitHub**: sharkybot41 (gh CLI auth'd, empty repos)
- **Google Cloud**: Free trial active
- **Firebase**: BlueBubbles project (Blaze plan)
- **Railway**: Account active
- **Apple**: sharkybot41 on iCloud
- **Telegram Bot**: Active (token in openclaw.json)
- **Discord Bot**: Active (token in openclaw.json)
- **BlueBubbles**: iMessage via zrok tunnel (sharky2.share.zrok.io)
- **OpenAI Whisper API**: key in skills config
- **ElevenLabs (SAG)**: key in skills config
- **Google Places API**: key in skills config

## Infrastructure
- Mac mini 2024, Apple Silicon, 16GB RAM, 228GB SSD (~163GB free)
- OpenClaw 2026.4.2
- Model: GLM-5.1 via z.ai (202k context window)
- Python 3.9.6 + 3.13 + 3.14, Node 25.9, Go, ffmpeg, gh, railway CLI

## Communication Channels
1. iMessage (BlueBubbles) — primary with Darius
2. Telegram — bot active
3. Discord — bot active
4. Voice (Vapi) — +1 (319) 719-9951, assistant "Sharky" configured

## Lessons Learned
- Vapi API uses Bearer token auth, PATCH/GET/POST via curl works fine
- Python urllib gets 403 on Vapi API — use curl instead
- Vapi private keys can be created via dashboard UI (eye button reveals key UUID)
- The Vapi "private API key" is a UUID format, used as Bearer token
- Org ID found in localStorage `assistant-folders` key
- Don't over-invest in browser automation when API is available

## Current State (2026-04-05)
- Bootstrap complete
- Vapi phone number active with Sharky assistant
- Custom CLI tools created (vapi.sh, sharkyctl.sh)
- Full system inventory documented
- Ready for Phase 2: building useful stuff
