# google-sheets-draw

A local socket server that lets AI agents (Claude, Codex, etc.) draw on Google Slides presentations by sending JSON commands. The server translates those commands into Google Slides API `batchUpdate` calls using a library of skill definitions.

**AI agents: read [`AGENT.md`](./AGENT.md) first** — it explains how to start working with the server and how to compose drawings.

---

## Folder Structure

```
google-sheets-draw/
├── AGENT.md                  ← AI agent onboarding guide (start here if you're an LLM)
├── README.md                 ← this file — human setup instructions
├── config.json               ← presentation_id and slide_index
├── run_server.py             ← start the socket server
├── socket_client_example.py  ← full example: smiley face with connectors and text
│
├── server/
│   ├── server.py             ← socket server; dispatches commands to handlers
│   ├── batch_planner.py      ← builds batchUpdate requests from operation dicts
│   ├── slide_reader.py       ← reads slide elements (type, text, x/y/w/h)
│   └── slides_api.py         ← thin wrapper around googleapiclient
│
├── scripts/
│   ├── send_command.py       ← TCP client utility — pipe JSON in, get response out
│   └── tmp-*.py              ← user job scripts (gitignored)
│
└── skills/                   ← reference docs for composing drawing operations
    ├── read-slide/           ← inspect slide state before drawing
    ├── batch-draw/           ← execute a batch of operations (the executor)
    ├── draw-shapes/          ← rectangles, ellipses, flowchart symbols, callouts
    ├── draw-lines/           ← lines, arrows, connectors
    ├── draw-text/            ← text boxes, labels, banners
    ├── draw-table/           ← tables with cell styling and merges
    ├── colors/               ← color specification reference
    ├── clear-slide/          ← delete all elements on a slide
    └── duplicate-slide/      ← copy a slide
```

---

## Prerequisites

1. Python 3.10+
2. Dependencies in `requirements.txt` (`google-auth`, `google-auth-oauthlib`, `google-api-python-client`, etc.)
3. A Google Cloud project with the **Google Slides API** and **Google Drive API** enabled

---

## Credential Setup

1. Open [Google Cloud Console](https://console.cloud.google.com) and select or create a project.
2. Configure the **OAuth consent screen**: choose *External*, fill in required fields, and add your Gmail as a *Test user*.
3. Enable **Google Slides API** and **Google Drive API** in the same project.
4. Create an **OAuth 2.0 Client ID** credential (choose "Desktop app"). Download `credentials.json` and place it in the project root.
5. `token.json` is created automatically after the first login and reused on subsequent runs.

Both `credentials.json` and `token.json` are gitignored.

---

## Installation

```bash
python3 -m pip install -r requirements.txt
```

---

## Verifying the Setup

```bash
python3 test.py
```

This will:
1. Prompt browser-based authentication and save `token.json`
2. List presentation files in your Drive
3. Draw a rectangle on the configured slide to confirm write access

---

## Running the Server

```bash
python3 run_server.py
```

The server listens on `127.0.0.1:8765`. Keep it running while you work. It handles authentication automatically on startup.

If `token.json` already exists you can also run `python3 server/server.py` directly.

---

## Available Server Tools

| Tool | Description |
|---|---|
| `read_slide` | Returns all elements with IDs, types, text, and position |
| `batch_draw` | Execute a list of drawing operations in a single API call |
| `delete_objects` | Delete specific elements by object ID |
| `duplicate_slide` | Copy a slide |
| `clear_slide` | Delete every element on a slide |

---

## Quick Test

```bash
# Read the current slide
python3 scripts/send_command.py '{
  "tool": "read_slide",
  "presentation_id": "YOUR_PRESENTATION_ID",
  "slide_index": 0
}'

# Or use config.json values directly from a script
python3 socket_client_example.py
```

---

## For AI Agents

See [`AGENT.md`](./AGENT.md) for:
- How to check if the server is running
- The full workflow (read → plan → delete → draw)
- Coordinate system and unit conversion (EMU → PT)
- Key API facts and common pitfalls
- How to write and run a job script (`scripts/tmp-*.py`)
