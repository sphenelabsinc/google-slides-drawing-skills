# AGENT.md — AI Agent Guide for google-sheets-draw

This file is for AI agents (Claude, Codex, etc.) entering this repository. Read it before doing anything else.

---

## What This Repo Does

This repo lets an AI agent draw on a Google Slides presentation by sending JSON commands to a local socket server. The server translates those commands into Google Slides API `batchUpdate` calls.

You compose operations using **skills** (reference docs in `skills/`), then execute them through the server via `scripts/send_command.py`.

---

## First Thing: Is the Server Running?

Before you can draw anything, the local server must be running. Check:

```bash
python3 scripts/send_command.py '{"tool":"read_slide","presentation_id":"YOUR_ID","slide_index":0}'
```

If you get a connection error, **stop and ask the user to start the server**:

```
The skill server isn't running. Please start it with:
    python3 run_server.py
Then come back and I'll continue.
```

Do not attempt to start the server yourself — it requires browser-based OAuth on first run.

---

## Presentation ID & Slide Index

The target presentation ID and slide index are in `config.json`:

```json
{
  "presentation_id": "...",
  "slide_index": 0
}
```

Always read this file before sending commands. Use these values in every command you send.

---

## Workflow: Always Follow This Order

```
1. read_slide       → inspect current state, get element IDs and positions
2. Plan             → decide what to add, move, or delete; avoid ID collisions
3. delete_objects   → remove old elements if replacing (optional)
4. batch_draw       → send all new operations in one call
```

Never skip step 1. Element IDs in the slide are permanent — reusing an existing ID will cause an error.

---

## Sending Commands

All communication goes through `scripts/send_command.py`:

```bash
python3 scripts/send_command.py 'JSON_PAYLOAD'
```

Or pipe from a file:

```bash
python3 scripts/send_command.py < my_payload.json
```

For complex drawings, write a Python script that builds the payload and sends it via the TCP socket directly (see `socket_client_example.py` for the pattern). Name these scripts `scripts/tmp-*.py` — they are gitignored and won't be committed.

---

## Available Server Tools

| Tool | Description |
|---|---|
| `read_slide` | Returns all elements on a slide with object IDs, types, text, and position (x, y, w, h in EMUs — divide by 12700 to get PT) |
| `batch_draw` | Execute a list of drawing operations in a single API call |
| `delete_objects` | Delete specific elements by object ID |
| `duplicate_slide` | Copy a slide (useful for versioning before destructive changes) |
| `clear_slide` | Delete every element on a slide |

---

## Coordinate System

- Slide standard size: **720 × 540 PT**
- This canvas can extend well beyond that — check existing element positions with `read_slide` first
- Coordinates from `read_slide` are in **EMUs** — convert to PT by dividing by **12700**
- All drawing operations use **PT** (points)
- Top-left is (0, 0); x increases right, y increases down

---

## Folder Structure

```
google-sheets-draw/
├── AGENT.md                  ← you are here
├── README.md                 ← setup & credential instructions for humans
├── config.json               ← presentation_id and slide_index
├── run_server.py             ← start the socket server (run this first)
├── socket_client_example.py  ← full example: smiley face diagram
│
├── server/
│   ├── server.py             ← socket server, dispatches commands to handlers
│   ├── batch_planner.py      ← builds batchUpdate requests from operation dicts
│   ├── slide_reader.py       ← reads slide elements (type, text, position)
│   └── slides_api.py         ← thin wrapper around googleapiclient
│
├── scripts/
│   ├── send_command.py       ← TCP client — use this to send all commands
│   └── tmp-*.py              ← your job scripts (gitignored — safe to create)
│
└── skills/                   ← reference docs for composing operations
    ├── read-slide/SKILL.md   ← how to inspect a slide
    ├── batch-draw/SKILL.md   ← how to execute a batch of operations
    ├── draw-shapes/SKILL.md  ← rectangles, ellipses, flowchart symbols, callouts
    ├── draw-lines/SKILL.md   ← lines, arrows, connectors between shapes
    ├── draw-text/SKILL.md    ← text boxes, labels, banners
    ├── draw-table/SKILL.md   ← tables with rows, columns, cell styling
    ├── colors/SKILL.md       ← color specification (hex, rgb, alpha)
    ├── clear-slide/SKILL.md  ← delete all elements on a slide
    └── duplicate-slide/SKILL.md ← copy a slide
```

---

## Skill Pattern: Composer + Executor

Skills are split into two roles:

- **Composer skills** (`draw-shapes`, `draw-lines`, `draw-text`, `draw-table`, `colors`) — describe how to build operation dicts
- **Executor skill** (`batch-draw`) — describes how to send them to the server

Read the relevant composer skills to build your `operations` list, then use `batch-draw` to send everything in one call.

---

## Key API Facts (Do Not Guess These)

- `createLine` uses `category` field: valid values are `STRAIGHT`, `BENT`, `CURVED`. **"ELBOW" does not exist.**
- `updateLineProperties` is a **separate request** from `createLine` — never nest them.
- `startArrow` / `endArrow` are **direct enum strings** (e.g. `"FILL_ARROW"`), not objects.
- `SolidFill.alpha` goes at the `solidFill` level, not inside `color`.
- Paragraph alignment uses `"START"` (not `"LEFT"`) and `"END"` (not `"RIGHT"`).
- Object IDs: **5–50 chars**, must start with `[a-zA-Z0-9_]`, must be unique across the whole presentation.

---

## Example: Read the Slide

```bash
python3 scripts/send_command.py '{
  "tool": "read_slide",
  "presentation_id": "1abc...",
  "slide_index": 0
}'
```

Response includes `elements[]` with `objectId`, `type`, `text`, `x`, `y`, `w`, `h` (in EMUs).

---

## Example: Draw a Labeled Rectangle

```bash
python3 scripts/send_command.py '{
  "tool": "batch_draw",
  "presentation_id": "1abc...",
  "slide_index": 0,
  "operations": [
    {
      "type": "shape", "id": "box1",
      "x": 100, "y": 100, "w": 200, "h": 60,
      "shape_type": "RECTANGLE",
      "fill_color": "#1A237E", "outline_color": "#FFFFFF", "outline_width": 1
    },
    {
      "type": "text", "id": "lbl1",
      "x": 100, "y": 100, "w": 200, "h": 60,
      "text": "Hello World",
      "text_style": { "bold": true, "font_size": 14, "foreground_color": "#FFFFFF", "alignment": "CENTER" }
    }
  ]
}'
```

---

## Example: Delete Specific Elements

```bash
python3 scripts/send_command.py '{
  "tool": "delete_objects",
  "presentation_id": "1abc...",
  "object_ids": ["element_id_1", "element_id_2"]
}'
```

---

## Writing a Job Script

For complex multi-step drawings, write a Python script at `scripts/tmp-yourjob.py`:

```python
import json, socket

HOST, PORT = "127.0.0.1", 8765

def send(cmd):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(cmd).encode())
        data = b""
        while True:
            chunk = s.recv(131072)
            if not chunk:
                break
            data += chunk
    return json.loads(data.decode())

ops = [
    # ... build your operations list here
]

result = send({
    "tool": "batch_draw",
    "presentation_id": "YOUR_PRESENTATION_ID",
    "slide_index": 0,
    "operations": ops,
})
print(result)
```

Run with `python3 scripts/tmp-yourjob.py`. The `tmp-` prefix keeps it out of git.
