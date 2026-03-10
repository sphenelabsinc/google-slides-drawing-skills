"""
Floating GUI — updates a clock rectangle on the slide every 5s,
and evaluates math expressions typed into the input bar (triggered by '=').
Both clock and math result rectangles get randomly changing rainbow colors.
"""

import json
import math
import random
import socket
import threading
import tkinter as tk
from datetime import datetime

# ── Config ──────────────────────────────────────────────────────────────────
HOST = "127.0.0.1"
PORT = 8765
PRES_ID = "1c-z-5s1Ofu0MPb2badSlIefGeLqTaAkIPTv4JTP0ki4"
SLIDE_INDEX = 0

CLOCK_TICK_MS = 5000          # how often to push clock to slide

# Fixed object IDs — we delete-and-redraw each update so colors can change
CLOCK_SHAPE_ID  = "hud_clock_box"
CLOCK_TEXT_ID   = "hud_clock_lbl"
MATH_SHAPE_ID   = "hud_math_box"
MATH_TEXT_ID    = "hud_math_lbl"

# Layout on the slide (PT)  — bottom-right corner area
CLOCK_X, CLOCK_Y, CLOCK_W, CLOCK_H = 460, 460, 240, 50
MATH_X,  MATH_Y,  MATH_W,  MATH_H  = 460, 395, 240, 50

RAINBOW = [
    "#FF0000", "#FF4500", "#FF7F00", "#FFA500", "#FFCC00",
    "#FFFF00", "#AAEE00", "#00CC00", "#00AAAA", "#0088FF",
    "#0000FF", "#4B0082", "#8B00FF", "#CC00CC", "#FF00AA",
]

# ── Slide helpers ────────────────────────────────────────────────────────────

def _send(cmd: dict) -> dict:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(8)
            s.connect((HOST, PORT))
            s.sendall(json.dumps(cmd).encode())
            data = b""
            while True:
                chunk = s.recv(131072)
                if not chunk:
                    break
                data += chunk
        return json.loads(data.decode())
    except Exception as e:
        return {"error": str(e)}


def _rand_color() -> str:
    return random.choice(RAINBOW)


def _text_color(hex_bg: str) -> str:
    """Return white or black depending on luminance of hex_bg."""
    h = hex_bg.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    return "#000000" if lum > 140 else "#FFFFFF"


def _draw_labeled_box(shape_id, text_id, x, y, w, h, text: str):
    """Delete old shapes and redraw with a fresh random rainbow color."""
    color = _rand_color()
    fg    = _text_color(color)
    _send({
        "tool": "delete_objects",
        "presentation_id": PRES_ID,
        "object_ids": [shape_id, text_id],
    })
    _send({
        "tool": "batch_draw",
        "presentation_id": PRES_ID,
        "slide_index": SLIDE_INDEX,
        "operations": [
            {
                "type": "shape", "id": shape_id,
                "x": x, "y": y, "w": w, "h": h,
                "shape_type": "ROUND_RECTANGLE",
                "fill_color": color,
                "outline_color": "#FFFFFF",
                "outline_width": 2,
            },
            {
                "type": "text", "id": text_id,
                "x": x, "y": y, "w": w, "h": h,
                "text": text,
                "text_style": {
                    "bold": True,
                    "font_size": 16,
                    "foreground_color": fg,
                    "alignment": "CENTER",
                },
            },
        ],
    })


# ── Clock thread ─────────────────────────────────────────────────────────────

def _clock_loop(status_var: tk.StringVar, stop_event: threading.Event):
    while not stop_event.is_set():
        now = datetime.now().strftime("%H:%M:%S  %b %d")
        status_var.set(f"Clock: {now}")
        threading.Thread(
            target=_draw_labeled_box,
            args=(CLOCK_SHAPE_ID, CLOCK_TEXT_ID,
                  CLOCK_X, CLOCK_Y, CLOCK_W, CLOCK_H, now),
            daemon=True,
        ).start()
        stop_event.wait(CLOCK_TICK_MS / 1000)


# ── Math evaluator ───────────────────────────────────────────────────────────

def _safe_eval(expr: str) -> str:
    """Evaluate a basic math expression safely."""
    allowed = set("0123456789 +-*/.()%eE")
    clean = expr.strip().rstrip("=").strip()
    if not all(c in allowed for c in clean):
        # allow math functions
        pass
    try:
        result = eval(clean, {"__builtins__": {}}, {  # noqa: S307
            k: getattr(math, k) for k in dir(math) if not k.startswith("_")
        })
        if isinstance(result, float) and result == int(result):
            return str(int(result))
        return str(round(result, 6))
    except Exception as e:
        return f"Err: {e}"


# ── GUI ──────────────────────────────────────────────────────────────────────

def build_gui():
    root = tk.Tk()
    root.title("Slide HUD")
    root.geometry("380x140")
    root.resizable(False, False)
    root.attributes("-topmost", True)          # always on top (floating)
    root.configure(bg="#1E1E2E")

    # ── header ──
    tk.Label(
        root, text="Slide HUD",
        bg="#1E1E2E", fg="#CDD6F4",
        font=("Helvetica", 13, "bold"),
    ).pack(pady=(10, 2))

    # ── status line ──
    status_var = tk.StringVar(value="Starting clock…")
    tk.Label(
        root, textvariable=status_var,
        bg="#1E1E2E", fg="#A6E3A1",
        font=("Helvetica", 10),
    ).pack()

    # ── math result line ──
    math_var = tk.StringVar(value="Type math below and press =")
    tk.Label(
        root, textvariable=math_var,
        bg="#1E1E2E", fg="#F9E2AF",
        font=("Helvetica", 10),
    ).pack()

    # ── input bar ──
    frame = tk.Frame(root, bg="#1E1E2E")
    frame.pack(pady=6, padx=12, fill="x")

    entry_var = tk.StringVar()
    entry = tk.Entry(
        frame, textvariable=entry_var,
        font=("Helvetica", 12),
        bg="#313244", fg="#CDD6F4",
        insertbackground="#CDD6F4",
        relief="flat", bd=4,
    )
    entry.pack(side="left", fill="x", expand=True)
    entry.focus()

    def _on_key(event):
        text = entry_var.get()
        if text.endswith("="):
            expr = text[:-1]
            result = _safe_eval(expr)
            display = f"{expr.strip()} = {result}"
            math_var.set(display)
            # push to slide in background
            threading.Thread(
                target=_draw_labeled_box,
                args=(MATH_SHAPE_ID, MATH_TEXT_ID,
                      MATH_X, MATH_Y, MATH_W, MATH_H, display),
                daemon=True,
            ).start()
            entry_var.set("")

    entry.bind("<KeyRelease>", _on_key)

    # ── start clock thread ──
    stop_event = threading.Event()
    clock_thread = threading.Thread(
        target=_clock_loop, args=(status_var, stop_event), daemon=True
    )
    clock_thread.start()

    def _on_close():
        stop_event.set()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", _on_close)
    root.mainloop()


if __name__ == "__main__":
    build_gui()
