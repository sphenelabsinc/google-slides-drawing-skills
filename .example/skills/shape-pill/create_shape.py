"""Create pill-shaped nodes via the shape-pill skill."""
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
    shape_id = next_id("pill")
    command = {
        "tool": "batch_draw",
        "presentation_id": config["presentation_id"],
        "slide_index": config["slide_index"],
        "operations": [
            {
                "type": "shape",
                "id": shape_id,
                "shape_type": "FLOW_CHART_ROUNDED_RECTANGLE",
                "x": 140,
                "y": 120,
                "w": 240,
                "h": 70,
                "fill_color": "#1A237E",
                "outline_color": "#FFFFFF",
                "outline_width": 1.5,
            }
        ],
    }

    print(f"Creating pill shape {shape_id}...")
    result = call_server(command)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
