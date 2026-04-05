const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3456;
const LOG_DIR = process.env.LOG_DIR || path.join(__dirname, '..', '..', 'data', 'call_logs');

// Ensure log directory exists
try {
  fs.mkdirSync(LOG_DIR, { recursive: true });
} catch (err) {
  console.error(`Failed to create log directory ${LOG_DIR}:`, err.message);
  process.exit(1);
}

// --- Helpers ---

function parseBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    const limit = 10 * 1024 * 1024; // 10MB
    req.on('data', (chunk) => {
      size += chunk.length;
      if (size > limit) {
        reject(new Error('Payload too large'));
        req.destroy();
        return;
      }
      chunks.push(chunk);
    });
    req.on('end', () => {
      const raw = Buffer.concat(chunks).toString('utf8');
      try {
        resolve({ raw, parsed: JSON.parse(raw) });
      } catch {
        resolve({ raw, parsed: null });
      }
    });
    req.on('error', reject);
  });
}

function sendJson(res, status, data) {
  const body = JSON.stringify(data);
  res.writeHead(status, {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(body),
  });
  res.end(body);
}

function formatCallLog(payload) {
  const now = new Date().toISOString();
  // Vapi sends various event shapes; extract what we can
  const callId = payload.call?.id || payload.id || payload.callId || 'unknown';
  const type = payload.type || payload.event || 'unknown';
  const analysis = payload.analysis || {};
  const callObj = payload.call || payload;
  const endedReason = callObj.endedReason || payload.endedReason || null;
  const duration = callObj.durationSeconds ?? payload.durationSeconds ?? payload.duration ?? null;
  const cost = callObj.cost ?? payload.cost ?? null;
  const transcript = analysis.transcript || payload.transcript || '';
  const summary = analysis.summary || payload.summary || '';
  const phoneCallProvider = callObj.phoneCallProvider || null;
  const customer = callObj.customer || payload.customer || null;

  return {
    timestamp: now,
    callId,
    type,
    endedReason,
    duration,
    cost,
    transcript,
    summary,
    phoneCallProvider,
    customer,
  };
}

function writeCallLog(logEntry) {
  const filename = `${logEntry.callId}_${logEntry.type}_${Date.now()}.json`;
  const filepath = path.join(LOG_DIR, filename);
  fs.writeFileSync(filepath, JSON.stringify(logEntry, null, 2));
  return filename;
}

function getRecentCalls(limit = 50) {
  try {
    const files = fs.readdirSync(LOG_DIR)
      .filter(f => f.endsWith('.json'))
      .sort()
      .reverse()
      .slice(0, limit);
    return files.map(f => {
      try {
        return JSON.parse(fs.readFileSync(path.join(LOG_DIR, f), 'utf8'));
      } catch {
        return { error: `Failed to read ${f}`, filename: f };
      }
    });
  } catch (err) {
    return { error: err.message };
  }
}

// --- Router ---

const server = http.createServer(async (req, res) => {
  const { method, url } = req;
  const pathname = url.split('?')[0];

  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (method === 'OPTIONS') {
    res.writeHead(204);
    return res.end();
  }

  try {
    // POST /vapi-webhook
    if (method === 'POST' && pathname === '/vapi-webhook') {
      const { raw, parsed } = await parseBody(req);
      if (!parsed) {
        return sendJson(res, 400, { error: 'Invalid JSON' });
      }
      const logEntry = formatCallLog(parsed);
      const filename = writeCallLog(logEntry);
      console.log(`[${logEntry.timestamp}] Logged ${logEntry.type} for call ${logEntry.callId} → ${filename}`);
      return sendJson(res, 200, { ok: true, logged: filename });
    }

    // GET /health
    if (method === 'GET' && pathname === '/health') {
      return sendJson(res, 200, { status: 'ok', uptime: process.uptime(), logDir: LOG_DIR });
    }

    // GET /calls
    if (method === 'GET' && pathname === '/calls') {
      const params = new URLSearchParams(url.split('?')[1] || '');
      const limit = Math.min(parseInt(params.get('limit') || '50', 10), 200);
      const calls = getRecentCalls(limit);
      return sendJson(res, 200, { count: Array.isArray(calls) ? calls.length : 0, calls });
    }

    // 404
    sendJson(res, 404, { error: 'Not found', endpoints: ['POST /vapi-webhook', 'GET /health', 'GET /calls'] });
  } catch (err) {
    console.error('Request error:', err);
    sendJson(res, 500, { error: 'Internal server error' });
  }
});

server.listen(PORT, () => {
  console.log(`🦈 Vapi webhook server listening on http://localhost:${PORT}`);
  console.log(`   POST /vapi-webhook  — receive call events`);
  console.log(`   GET  /health        — server status`);
  console.log(`   GET  /calls         — recent call logs`);
  console.log(`   Log directory: ${LOG_DIR}`);
});

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`Port ${PORT} already in use. Set PORT env var to use a different port.`);
    process.exit(1);
  }
  throw err;
});
