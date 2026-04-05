# Sharky Knowledge Base

> Living reference doc. Last updated: 2026-04-05.

---

## 1. Vapi API Reference

**Base URL:** `https://api.vapi.ai`
**Auth:** `Authorization: Bearer <API_KEY>` (key in `.secrets/credentials.env`)
**Sharky's Number:** +1 (319) 719-9951
**Local CLI:** `tools/vapi.sh`

### Key Endpoints

#### POST /call — Create Call (including outbound phone)

Makes outbound calls. Use `assistant`/`assistantId`, `squad`/`squadId`, or `workflow`/`workflowId`.

```bash
curl -X POST https://api.vapi.ai/call \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "assistantId": "<id>",
    "customer": { "number": "+18318898775" },
    "phoneNumberId": "<vapi-number-id>",
    "name": "Optional call name"
  }'
```

**Key params:**
| Field | Description |
|-------|-------------|
| `assistantId` / `assistant` | Use existing ID or inline transient assistant config |
| `squadId` / `squad` | Multi-assistant squad |
| `workflowId` / `workflow` | Workflow to execute |
| `customer` | `{ "number": "+1..." }` for single call |
| `customers` | Array for batch calls |
| `phoneNumberId` | Existing Vapi number to call from |
| `phoneNumber` | Transient number config |
| `name` | Optional label (≤40 chars) |
| `schedulePlan` | Schedule for delayed/recurring calls |
| `transport` | Transport config |
| `maxDurationSeconds` | Max call length |
| `server` | `{ url, headers }` for webhook callbacks |

#### GET /call — List Calls

```bash
curl https://api.vapi.ai/call \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

Returns array of call objects. Supports query filters.

#### GET /call/:id — Get Call Details

```bash
curl https://api.vapi.ai/call/<call-id> \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

Returns full call object including transcript, recording, artifacts, status, timestamps, cost.

#### DELETE /call/:id — End Call

```bash
curl -X DELETE https://api.vapi.ai/call/<call-id> \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

#### POST /assistant — Create Assistant

```bash
curl -X POST https://api.vapi.ai/assistant \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sharky Voice",
    "model": {
      "provider": "openai",
      "model": "gpt-4o",
      "messages": [{ "role": "system", "content": "You are Sharky..." }]
    },
    "voice": {
      "provider": "11labs",
      "voiceId": "<voice-id>"
    },
    "firstMessage": "Hey, Sharky here. What do you need?",
    "transcriber": { "provider": "deepgram", "model": "nova-2" }
  }'
```

#### PATCH /assistant/:id — Update Assistant

```bash
curl -X PATCH https://api.vapi.ai/assistant/<id> \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "firstMessage": "Updated greeting" }'
```

#### GET /assistant — List Assistants
#### GET /assistant/:id — Get Assistant
#### DELETE /assistant/:id — Delete Assistant

#### GET /phone-number — List Phone Numbers

```bash
curl https://api.vapi.ai/phone-number \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

#### POST /phone-number — Buy Number
#### PATCH /phone-number/:id — Update Number (attach assistant, set hooks)
#### DELETE /phone-number/:id — Release Number

### Webhook Event Types

All webhooks are `POST` to your Server URL with shape:
```json
{ "message": { "type": "<event-type>", "call": { ... }, ... } }
```

**Events requiring a response (within 7.5s):**

| Event | Description |
|-------|-------------|
| `assistant-request` | Return assistant ID or transient config for inbound calls |
| `tool-calls` | Function tool triggered, return results |
| `transfer-destination-request` | Assistant wants to transfer but destination unknown |
| `knowledge-base-request` | Dynamic knowledge base lookup |

**Informational events (no response needed):**

| Event | Description |
|-------|-------------|
| `conversation-update` | Real-time transcript/update |
| `call.start` | Call started |
| `call.end` | Call ended (includes transcript, recording, cost) |
| `speech.start` | Speech detected |
| `speech.end` | Speech ended |
| `status-update` | Call status changed |
| `transfer-update` | Transfer occurred |

**Assistant Hooks** (configured on assistant, not server URL):
- `call.end` — Trigger on call completion
- `customer.speech.timeout` — Customer silence (configurable delay)
- `assistant.transcriber.endpointedSpeechLowConfidence` — Low-confidence transcripts

**Phone Number Hooks:**
- `call.ringing` — Trigger on ring, supports `transfer` and `say` actions

### Call Object Key Fields

```
id, orgId, type, status, startedAt, endedAt, cost,
assistantId, phoneNumberId,
customer: { number, sipUri },
transcript, recording, messages,
artifact, analysis
```

---

## 2. OpenClaw Skills Reference

### gog (Google Workspace CLI)

**Binary:** `gogcli`
**Setup:** OAuth — `gogcli auth login` (already done for sharkybot41@gmail.com)
**What:** Gmail, Calendar, Drive, Contacts, Sheets, Docs from the CLI.

| Command | Example |
|---------|---------|
| Gmail list | `gogcli gmail list --max 10 --query "is:unread"` |
| Gmail read | `gogcli gmail read <msg-id>` |
| Gmail send | `gogcli gmail send --to "x@y.com" --subject "Hi" --body "text"` |
| Calendar list | `gogcli calendar list --from today --days 3` |
| Drive search | `gogcli drive search "filename"` |

### memo (Apple Notes)

**Binary:** `memo`
**Setup:** No auth needed (macOS native)
**What:** Create, view, edit, delete, search Apple Notes.

| Command | Example |
|---------|---------|
| List | `memo list` |
| Search | `memo search "query"` |
| Create | `memo add "Title" --body "content"` |
| Read | `memo read <id>` |

### remindctl (Apple Reminders)

**Binary:** `remindctl`
**Setup:** No auth needed
**What:** List, add, edit, complete, delete reminders with list/date support.

| Command | Example |
|---------|---------|
| List | `remindctl list --list "Today"` |
| Add | `remindctl add "Buy milk" --due "tomorrow 9am"` |
| Complete | `remindctl complete <id>` |

### summarize (URL/Content Summarization)

**Binary:** `summarize`
**What:** Summarize or extract transcripts from URLs, podcasts, videos (YouTube).

| Command | Example |
|---------|---------|
| Summarize URL | `summarize https://example.com/article` |
| YouTube transcript | `summarize https://youtube.com/watch?v=XXX` |

### xurl (X/Twitter API)

**Binary:** `xurl`
**Setup:** API keys in config
**What:** Post tweets, reply, search, read, DMs, upload media.

| Command | Example |
|---------|---------|
| Post tweet | `xurl tweet "Hello world"` |
| Search | `xurl search "query" --limit 10` |
| Timeline | `xurl timeline` |

### peekaboo (macOS UI Automation)

**Binary:** `peekaboo`
**Setup:** Accessibility permissions granted
**What:** Capture screens, click, type, inspect UI elements on macOS.

| Command | Example |
|---------|---------|
| Screenshot | `peekaboo screenshot` |
| Click | `peekaboo click --x 100 --y 200` |
| Get element | `peekaboo get --role button --name "Save"` |

### weather

**Skill:** Uses wttr.in or Open-Meteo
**What:** Current weather and forecasts.

| Command | Example |
|---------|---------|
| Current | `curl wttr.in/?format=3` |
| Forecast | `curl wttr.in/?format=4` |

### github (gh CLI)

**Binary:** `gh`
**Setup:** `gh auth login` (done for sharkybot41)
**What:** Issues, PRs, CI, code review, API queries.

| Command | Example |
|---------|---------|
| PR list | `gh pr list` |
| Create issue | `gh issue create --title "Bug" --body "desc"` |
| CI status | `gh run list` |

### oracle (Prompt Bundling)

**Binary:** `oracle`
**What:** Bundle prompts + files, send to LLM engines with session support.

| Command | Example |
|---------|---------|
| Query | `oracle "explain this code" --files src/main.py` |
| Session | `oracle --session <id> "follow up"` |

---

## 3. Sharky Architecture

### System Overview

```
┌─────────────────────────────────────────────────┐
│                    Darius                        │
│         (Human, +18318898775, LA timezone)       │
└──────────┬──────────┬──────────┬────────────────┘
           │          │          │
     iMessage    Telegram    Discord
           │          │          │
           ▼          ▼          ▼
┌─────────────────────────────────────────────────┐
│              COMMUNICATION CHANNELS              │
│  BlueBubbles │ Telegram Bot │ Discord Bot        │
│  (Zrok tunnel)                                      │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│              OpenClaw (Orchestrator)             │
│  - Session management                            │
│  - Heartbeat scheduling                          │
│  - Cron jobs                                     │
│  - Subagent spawning                             │
│  - Skill routing                                 │
│  - Memory (MEMORY.md + memory/*.md)              │
│  v2026.4.2 · Darwin 25.3.0 · ARM64              │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│              GLM-5.1 (Brain)                     │
│  Model: zai/glm-5.1                             │
│  Reasoning: off (toggle /reasoning)              │
│  Thinking: low                                   │
└──────────────────────┬──────────────────────────┘
                       │
              ┌────────┼────────┐
              ▼        ▼        ▼
         ┌────────┐ ┌────────┐ ┌────────────┐
         │ Skills │ │ Tools  │ │  Channels   │
         │ (CLI)  │ │ (exec) │ │ (outbound)  │
         └────────┘ └────────┘ └────────────┘
```

### Communication Flow

```
Inbound Message:
  Darius → iMessage → BlueBubbles → OpenClaw → GLM-5.1 → Response → BlueBubbles → iMessage → Darius

Outbound Action:
  GLM-5.1 → OpenClaw → Skill CLI (exec) → Result → Response

Proactive (Heartbeat):
  OpenClaw timer → Heartbeat prompt → GLM-5.1 → Check email/calendar/etc → Message Darius if needed

Proactive (Cron):
  OpenClaw cron → Subagent → Task → Channel delivery
```

### Data Storage

| Path | Contents |
|------|----------|
| `~/.openclaw/workspace/` | Main workspace, all files below |
| `~/.openclaw/workspace/SOUL.md` | Identity & personality |
| `~/.openclaw/workspace/USER.md` | Darius's profile |
| `~/.openclaw/workspace/TOOLS.md` | Tool/account notes |
| `~/.openclaw/workspace/AGENTS.md` | Behavioral rules |
| `~/.openclaw/workspace/MEMORY.md` | Long-term curated memory |
| `~/.openclaw/workspace/memory/YYYY-MM-DD.md` | Daily session logs |
| `~/.openclaw/workspace/memory/heartbeat-state.json` | Last check timestamps |
| `~/.openclaw/workspace/docs/` | Documentation |
| `~/.openclaw/workspace/tools/` | Custom scripts (vapi.sh, sharkyctl.sh) |
| `~/.secrets/credentials.env` | API keys (Vapi, etc.) |
| `~/.openclaw/openclaw.json` | OpenClaw config (channels, crons, etc.) |

### Scheduling

**Heartbeat:** Periodic poll (every ~30 min). Sharky reads `HEARTBEAT.md` and checks:
- Email (urgent unread)
- Calendar (upcoming events)
- Social mentions
- Weather (if relevant)
- Memory maintenance (periodic)

**Cron:** Exact-time scheduled tasks via OpenClaw cron system.
- Better for precise timing, isolated tasks, one-shot reminders
- Different model/thinking level configurable per cron

### Infrastructure

- **Mac mini (2024)** — Apple Silicon, 16GB RAM, 228GB SSD
- **macOS** — Darwin 25.3.0
- **OpenClaw 2026.4.2** — Orchestrator
- **Railway** — Cloud deployment
- **Google Cloud** — Free trial active
- **Firebase** — BlueBubbles project (Blaze plan)
- **Zrok** — Tunnel for BlueBubbles (`sharky2.share.zrok.io`)
- **Vapi** — Voice/phone (+1 319 719 9951)

### Accounts

| Service | Account | Auth Method |
|---------|---------|-------------|
| Google | sharkybot41@gmail.com | OAuth (gogcli) |
| GitHub | sharkybot41 | gh CLI (authenticated) |
| Vapi | API key | Bearer token |
| Telegram | @sharkybot | Bot token |
| Discord | Sharky | Bot token |
| BlueBubbles | iMessage | Zrok tunnel |

---

*This is a living document. Update as systems evolve.*
