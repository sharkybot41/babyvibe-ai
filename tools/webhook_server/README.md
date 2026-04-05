# Vapi Webhook Server

Receives Vapi call events via webhook and logs them as JSON files.

## Quick Start

```bash
node server.js
```

Listens on **port 3456** by default. Override with `PORT` env var:

```bash
PORT=8080 node server.js
```

No `npm install` needed — uses only built-in Node.js modules.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/vapi-webhook` | Receive Vapi call events |
| `GET` | `/health` | Server status and uptime |
| `GET` | `/calls?limit=50` | Recent call logs (max 200) |

## Log Format

Each call event is saved as a JSON file in `data/call_logs/`:

```json
{
  "timestamp": "2026-04-05T08:00:00.000Z",
  "callId": "abc-123",
  "type": "end-of-call-report",
  "endedReason": "customer-ended-call",
  "duration": 120,
  "cost": 0.36,
  "transcript": "...",
  "summary": "...",
  "phoneCallProvider": "vapi",
  "customer": { "number": "+1..." }
}
```

## Configure Vapi

In your Vapi dashboard (or via API), set the **Server URL** to point to this webhook:

1. **With a public tunnel** (e.g. ngrok, zrok, cloudflare tunnel):
   ```
   https://your-tunnel-domain/vapi-webhook
   ```

2. **Using zrok** (already available on this machine):
   ```bash
   zrok reserve public 3456
   # Use the reserved URL as your Vapi server URL
   ```

3. **In Vapi Dashboard** → Your Assistant → **Server URL** → paste the URL

Vapi will POST call events (start, end-of-call-report, etc.) to this endpoint.

## Custom Log Directory

Override the log directory with `LOG_DIR`:

```bash
LOG_DIR=/tmp/call_logs node server.js
```

Default: `../../data/call_logs/` (resolves to `workspace/data/call_logs/`).

## Run as Background Service

```bash
nohup node server.js > webhook.log 2>&1 &
```
