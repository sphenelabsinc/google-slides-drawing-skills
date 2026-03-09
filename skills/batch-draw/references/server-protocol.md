# Server Protocol Reference

## Connection Details

- **Host:** `127.0.0.1`
- **Port:** `8765`
- **Protocol:** TCP socket
- **Encoding:** UTF-8 JSON
- **Buffer:** 131072 bytes (128 KB)

## Starting the Server

```bash
python run_server.py
```

The server must be running before sending commands. It holds a persistent Google Slides API connection via OAuth2.

## config.json

```json
{ "presentation_id": "1c-z-5s1Ofu0MPb2bad..." }
```

Load with: `json.load(open("config.json"))["presentation_id"]`

## Request Format

Send a single JSON object (one command per connection):

```json
{
  "tool": "batch_draw",
  "presentation_id": "...",
  "slide_index": 0,
  "operations": [...]
}
```

## Response Format

Success:
```json
{ "status": "ok", "requests_sent": 12 }
```

Error:
```json
{ "status": "error", "message": "HttpError 400 ..." }
```

Always check `response["status"] == "ok"` before proceeding.

## Supported Tools

| tool | Required fields |
|---|---|
| `batch_draw` | `presentation_id`, `slide_index`, `operations` |
| `read_slide` | `presentation_id`, `slide_index` |
| `duplicate_slide` | `presentation_id`, `slide_index` |
| `clear_slide` | `presentation_id`, `slide_index` |

## Error Handling

Common errors:
- `"slide_index is out of bounds"` — slide doesn't exist at that index
- `"HttpError 400"` — invalid API request (check operation field names and values)
- `"unknown operation type"` — unsupported `type` field in operations array
- `"unknown tool"` — tool name not recognized

If the server is not running: `ConnectionRefusedError: [Errno 61] Connection refused`
