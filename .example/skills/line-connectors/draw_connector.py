"""Draw connector between two ellipses to demonstrate line connector payloads."""
import json
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from scripts.send_command import send_command


def load_config() -> dict:
    config_path = REPO_ROOT / "config.json"
    with config_path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def call_server(command: dict) -> dict:
    try:
        return send_command(command)
    except (ConnectionRefusedError, OSError) as exc:
        print("The skill server isn't running. Please start it with:")
        print("    python3 run_server.py")
        raise SystemExit(1) from exc


def next_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}"


def main() -> None:
    config = load_config()
    start_id = next_id("connector_src")
    end_id = next_id("connector_tgt")
    line_id = next_id("connector")

    operations = [
        {
            "type": "shape",
            "id": start_id,
            "shape_type": "ELLIPSE",
            "x": 100,
            "y": 320,
            "w": 120,
            "h": 60,
            "fill_color": "#90CAF9",
        },
        {
            "type": "shape",
            "id": end_id,
            "shape_type": "ELLIPSE",
            "x": 360,
            "y": 320,
            "w": 120,
            "h": 60,
            "fill_color": "#F48FB1",
        },
        {
            "type": "line",
            "id": line_id,
            "category": "STRAIGHT",
            "x": 180,
            "y": 340,
            "w": 200,
            "h": 30,
            "start_connection": {
                "connected_object_id": start_id,
                "connection_site_index": 1,
            },
            "end_connection": {
                "connected_object_id": end_id,
                "connection_site_index": 5,
            },
            "line_color": "#000000",
            "line_weight": 2,
            "end_arrow": "FILL_ARROW",
        },
    ]

    command = {
        "tool": "batch_draw",
        "presentation_id": config["presentation_id"],
        "slide_index": config["slide_index"],
        "operations": operations,
    }

    print(f"Drawing connector {line_id} between {start_id} and {end_id}...")
    result = call_server(command)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
