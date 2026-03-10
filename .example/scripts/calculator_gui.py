#!/usr/bin/env python3
"""Floating calculator that draws formula plots or digit art via the available skills."""

import ast
import json
import logging
import math
import socket
import threading
import uuid
from pathlib import Path
import tkinter as tk
from tkinter import ttk

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config.json"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8765
SLIDE_WIDTH = 720
SLIDE_HEIGHT = 540
PLOT_MARGIN = 48
DIGIT_WIDTH = 70
DIGIT_HEIGHT = 130
DIGIT_SPACING = 12
DIGIT_THICKNESS = 16
DOT_SIZE = 22
DASH_WIDTH = 50
DASH_HEIGHT = 14
SAMPLES_DEFAULT = 180
GUI_OPACITY = 0.92

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
LOGGER = logging.getLogger(__name__)
GUI_OPACITY = 1

SAFE_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "sqrt": math.sqrt,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "pow": pow,
    "abs": abs,
    "max": max,
    "min": min,
    "round": round,
    "floor": math.floor,
    "ceil": math.ceil,
}
SAFE_CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}

SEGMENT_MAP = {
    "0": {"a", "b", "c", "d", "e", "f"},
    "1": {"b", "c"},
    "2": {"a", "b", "g", "e", "d"},
    "3": {"a", "b", "g", "c", "d"},
    "4": {"f", "g", "b", "c"},
    "5": {"a", "f", "g", "c", "d"},
    "6": {"a", "f", "g", "c", "d", "e"},
    "7": {"a", "b", "c"},
    "8": {"a", "b", "c", "d", "e", "f", "g"},
    "9": {"a", "b", "c", "d", "f", "g"},
}


def unique_id(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:6]}"


def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))


def line_op(x, y, w, h, label):
    return {
        "type": "line",
        "id": unique_id(label),
        "x": x,
        "y": y,
        "w": w,
        "h": h,
        "category": "STRAIGHT",
        "line_color": "#37474F",
        "line_weight": 1,
    }


def rect_op(x, y, w, h, label):
    return {
        "type": "shape",
        "id": unique_id(label),
        "x": x,
        "y": y,
        "w": max(w, 2),
        "h": max(h, 2),
        "shape_type": "RECTANGLE",
        "fill_color": {"hex": "#FF7043", "alpha": 0.94},
        "outline_color": "#BF360C",
        "outline_width": 1,
    }


def draw_decimal_point(x, y, idx):
    return {
        "type": "shape",
        "id": unique_id(f"calc_dot_{idx}"),
        "x": x,
        "y": y,
        "w": DOT_SIZE,
        "h": DOT_SIZE,
        "shape_type": "ELLIPSE",
        "fill_color": {"hex": "#FF5722", "alpha": 0.95},
        "outline_color": None,
    }


def draw_dash(x, y, idx):
    return rect_op(x, y, DASH_WIDTH, DASH_HEIGHT, f"calc_dash_{idx}")


def char_width(ch):
    if ch == ".":
        return DOT_SIZE
    if ch == "-":
        return DASH_WIDTH
    return DIGIT_WIDTH


def format_number(value):
    rounded = round(value, 6)
    if isinstance(rounded, float) and rounded.is_integer():
        return str(int(rounded))
    text = f"{rounded:.6f}".rstrip("0").rstrip(".")
    return text or "0"


def draw_digit(char, x_start, y_start):
    segments = SEGMENT_MAP.get(char)
    if not segments:
        return []
    horizontal_length = DIGIT_WIDTH - 2 * DIGIT_THICKNESS
    vertical_length = (DIGIT_HEIGHT - 3 * DIGIT_THICKNESS) / 2
    ops = []
    for seg in segments:
        if seg in {"a", "d", "g"}:
            y_positions = {
                "a": 0,
                "g": DIGIT_THICKNESS + vertical_length,
                "d": DIGIT_HEIGHT - DIGIT_THICKNESS,
            }
            y_offset = y_positions[seg]
            ops.append(rect_op(x_start + DIGIT_THICKNESS, y_start + y_offset, horizontal_length, DIGIT_THICKNESS, f"calc_digit_{char}_{seg}"))
        else:
            if seg == "b":
                x_offset = DIGIT_WIDTH - DIGIT_THICKNESS
                y_offset = DIGIT_THICKNESS
            elif seg == "c":
                x_offset = DIGIT_WIDTH - DIGIT_THICKNESS
                y_offset = DIGIT_THICKNESS * 2 + vertical_length
            elif seg == "e":
                x_offset = 0
                y_offset = DIGIT_THICKNESS * 2 + vertical_length
            else:  # f
                x_offset = 0
                y_offset = DIGIT_THICKNESS
            ops.append(rect_op(x_start + x_offset, y_start + y_offset, DIGIT_THICKNESS, vertical_length, f"calc_digit_{char}_{seg}"))
    return ops


class ExpressionError(Exception):
    pass


class ExpressionInspector(ast.NodeVisitor):
    ALLOWED_NODES = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.BoolOp,
        ast.Compare,
        ast.IfExp,
        ast.Call,
        ast.Constant,
        ast.Name,
        ast.Load,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Pow,
        ast.Mod,
        ast.UAdd,
        ast.USub,
        ast.And,
        ast.Or,
        ast.Not,
        ast.Eq,
        ast.NotEq,
        ast.Lt,
        ast.Gt,
        ast.LtE,
        ast.GtE,
    )

    def __init__(self):
        self.names = set()

    def generic_visit(self, node):
        if not isinstance(node, self.ALLOWED_NODES):
            raise ExpressionError(f"Unsupported expression node: {type(node).__name__}")
        super().generic_visit(node)

    def visit_Name(self, node):
        self.names.add(node.id)
        super().generic_visit(node)


class ExpressionEvaluator(ast.NodeVisitor):
    def __init__(self, variables=None):
        self.variables = variables or {}

    def visit(self, node):
        method = f"visit_{type(node).__name__}"
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def visit_Expression(self, node):
        return self.visit(node.body)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_type = type(node.op)
        if op_type is ast.Add:
            return left + right
        if op_type is ast.Sub:
            return left - right
        if op_type is ast.Mult:
            return left * right
        if op_type is ast.Div:
            return left / right
        if op_type is ast.Pow:
            return left ** right
        if op_type is ast.Mod:
            return left % right
        raise ExpressionError(f"Unsupported binary operator: {op_type.__name__}")

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        op_type = type(node.op)
        if op_type is ast.UAdd:
            return +operand
        if op_type is ast.USub:
            return -operand
        if op_type is ast.Not:
            return not operand
        raise ExpressionError(f"Unsupported unary operator: {op_type.__name__}")

    def visit_BoolOp(self, node):
        if isinstance(node.op, ast.And):
            return all(self.visit(value) for value in node.values)
        if isinstance(node.op, ast.Or):
            return any(self.visit(value) for value in node.values)
        raise ExpressionError("Unsupported boolean operator")

    def visit_Compare(self, node):
        left = self.visit(node.left)
        for operator, comparator in zip(node.ops, node.comparators):
            right = self.visit(comparator)
            if isinstance(operator, ast.Lt) and not (left < right):
                return False
            if isinstance(operator, ast.Gt) and not (left > right):
                return False
            if isinstance(operator, ast.LtE) and not (left <= right):
                return False
            if isinstance(operator, ast.GtE) and not (left >= right):
                return False
            if isinstance(operator, ast.Eq) and not (left == right):
                return False
            if isinstance(operator, ast.NotEq) and not (left != right):
                return False
            left = right
        return True

    def visit_IfExp(self, node):
        condition = self.visit(node.test)
        return self.visit(node.body) if condition else self.visit(node.orelse)

    def visit_Call(self, node):
        if not isinstance(node.func, ast.Name):
            raise ExpressionError("Only simple function names are allowed")
        func = node.func.id
        target = SAFE_FUNCTIONS.get(func)
        if not target:
            raise ExpressionError(f"Unknown function: {func}")
        args = [self.visit(arg) for arg in node.args]
        return target(*args)

    def visit_Name(self, node):
        name = node.id
        if name in self.variables:
            return self.variables[name]
        if name in SAFE_FUNCTIONS:
            return SAFE_FUNCTIONS[name]
        if name in SAFE_CONSTANTS:
            return SAFE_CONSTANTS[name]
        raise ExpressionError(f"Unknown variable or symbol: {name}")

    def visit_Constant(self, node):
        value = node.value
        if isinstance(value, (int, float, bool)):
            return value
        raise ExpressionError(f"Unsupported constant type: {type(value).__name__}")


class ParsedExpression:
    def __init__(self, text):
        cleaned = text.strip()
        if not cleaned:
            raise ExpressionError("Expression cannot be empty")
        self.text = cleaned
        self.tree = ast.parse(cleaned, mode="eval")
        inspector = ExpressionInspector()
        inspector.visit(self.tree)
        self.names = inspector.names

    def evaluate(self, variables=None):
        evaluator = ExpressionEvaluator(variables)
        return evaluator.visit(self.tree)

    @property
    def uses_variable(self):
        return "x" in self.names


class PlotBuilder:
    def __init__(self):
        self.plot_left = PLOT_MARGIN
        self.plot_top = PLOT_MARGIN
        self.plot_right = SLIDE_WIDTH - PLOT_MARGIN
        self.plot_bottom = SLIDE_HEIGHT - PLOT_MARGIN
        self.plot_width = self.plot_right - self.plot_left
        self.plot_height = self.plot_bottom - self.plot_top

    def map_x(self, x, x_min, x_max):
        return self.plot_left + (x - x_min) / (x_max - x_min) * self.plot_width

    def map_y(self, y, y_min, y_max):
        if y_max == y_min:
            return (self.plot_top + self.plot_bottom) / 2
        ratio = (y - y_min) / (y_max - y_min)
        return self.plot_bottom - ratio * self.plot_height

    def build_plot_operations(self, parsed_expr, x_min, x_max, samples):
        dx = (x_max - x_min) / max(samples - 1, 1)
        points = []
        values = []
        for index in range(samples):
            x = x_min + dx * index
            try:
                y = parsed_expr.evaluate({"x": x})
            except Exception:
                points.append(None)
                continue
            if isinstance(y, (int, float)) and math.isfinite(y):
                points.append((x, y))
                values.append(y)
            else:
                points.append(None)
        if values:
            y_min, y_max = min(values), max(values)
            if math.isclose(y_min, y_max):
                y_min -= 1.0
                y_max += 1.0
        else:
            y_min, y_max = -1.0, 1.0
        operations = []
        operations.append({
            "type": "shape",
            "id": unique_id("calc_plot_bg"),
            "x": self.plot_left,
            "y": self.plot_top,
            "w": self.plot_width,
            "h": self.plot_height,
            "shape_type": "RECTANGLE",
            "fill_color": {"hex": "#0D47A1", "alpha": 0.08},
            "outline_color": None,
            "outline_width": 0,
        })
        nodes = []
        for idx in range(len(points) - 1):
            a = points[idx]
            b = points[idx + 1]
            if a is None or b is None:
                continue
            x1, y1 = a
            x2, y2 = b
            px1 = self.map_x(x1, x_min, x_max)
            py1 = self.map_y(y1, y_min, y_max)
            px2 = self.map_x(x2, x_min, x_max)
            py2 = self.map_y(y2, y_min, y_max)
            nodes.append((px1, py1, px2, py2))
        axis_y = self.map_y(0.0, y_min, y_max)
        axis_x = self.map_x(0.0, x_min, x_max)
        axis_y = clamp(axis_y, self.plot_top, self.plot_bottom)
        axis_x = clamp(axis_x, self.plot_left, self.plot_right)
        operations.append(line_op(self.plot_left, axis_y, self.plot_width, 0.5, "calc_plot_haxis"))
        operations.append(line_op(axis_x, self.plot_top, 0.5, self.plot_height, "calc_plot_vaxis"))
        for (px1, py1, px2, py2) in nodes:
            x = min(px1, px2)
            y = min(py1, py2)
            w = max(abs(px2 - px1), 1)
            h = max(abs(py2 - py1), 1)
            operations.append({
                "type": "line",
                "id": unique_id("calc_plot_line"),
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "category": "STRAIGHT",
                "line_color": "#1565C0",
                "line_weight": 2,
            })
        operations.append({
            "type": "text",
            "id": unique_id("calc_formula"),
            "x": self.plot_left,
            "y": max(8, self.plot_top - 34),
            "w": self.plot_width,
            "h": 28,
            "text": f"y = {parsed_expr.text.strip()}",
            "text_style": {
                "font_family": "Roboto",
                "font_size": 16,
                "bold": True,
                "foreground_color": "#0D47A1",
                "alignment": "CENTER",
            },
        })
        return operations

    def build_number_operations(self, value):
        text = format_number(value)
        ops = []
        widths = [char_width(ch) for ch in text]
        total_width = sum(widths) + DIGIT_SPACING * (len(widths) - 1)
        anchor_x = (SLIDE_WIDTH - total_width) / 2
        anchor_y = SLIDE_HEIGHT - PLOT_MARGIN - DIGIT_HEIGHT - 8
        current_x = anchor_x
        for idx, ch in enumerate(text):
            width = widths[idx]
            if ch.isdigit():
                ops.extend(draw_digit(ch, current_x, anchor_y))
            elif ch == ".":
                ops.append(draw_decimal_point(current_x + width / 2 - DOT_SIZE / 2, anchor_y + DIGIT_HEIGHT - DOT_SIZE, idx))
            elif ch == "-":
                ops.append(draw_dash(current_x, anchor_y + DIGIT_HEIGHT / 2 - DASH_HEIGHT / 2, idx))
            current_x += width + DIGIT_SPACING
        ops.append({
            "type": "text",
            "id": unique_id("calc_formula"),
            "x": anchor_x,
            "y": anchor_y - 32,
            "w": total_width,
            "h": 24,
            "text": f"value = {text}",
            "text_style": {
                "font_family": "Roboto",
                "font_size": 16,
                "bold": True,
                "foreground_color": "#1E88E5",
                "alignment": "CENTER",
            },
        })
        return ops


def load_config():
    if not CONFIG_PATH.exists():
        return None
    try:
        with CONFIG_PATH.open() as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        raise ExpressionError(f"config.json is invalid: {exc}")
    return {
        "presentation_id": data["presentation_id"],
        "slide_index": data["slide_index"],
        "host": data.get("host", DEFAULT_HOST),
        "port": data.get("port", DEFAULT_PORT),
    }


class SlideClient:
    def __init__(self, presentation_id, slide_index, host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.presentation_id = presentation_id
        self.slide_index = slide_index
        self.host = host
        self.port = port

    def send(self, payload):
        payload.update({
            "presentation_id": self.presentation_id,
            "slide_index": self.slide_index,
        })
        message = json.dumps(payload)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(message.encode("utf-8"))
            data = b""
            while True:
                chunk = sock.recv(65536)
                if not chunk:
                    break
                data += chunk
        if not data:
            raise ConnectionError("empty response from skill server")
        return json.loads(data.decode("utf-8"))

    def read_slide(self):
        return self.send({"tool": "read_slide"})

    def delete_objects(self, object_ids):
        return self.send({"tool": "delete_objects", "object_ids": object_ids})

    def batch_draw(self, operations):
        return self.send({"tool": "batch_draw", "operations": operations})


class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Formula Drawer")
        self.root.geometry("320x220")
        self.root.attributes("-alpha", GUI_OPACITY)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#1c2331")
        LOGGER.info("Calculator GUI window initialized with opacity %.2f", GUI_OPACITY)
        self.config = None
        self.client = None
        self.plot_builder = PlotBuilder()
        self.build_widgets()
        self.load_client()

    def set_message(self, text):
        self.root.after(0, lambda: self.message_var.set(text))

    def run_worker(self, target, *args):
        worker = threading.Thread(target=target, args=args)
        worker.daemon = True
        worker.start()

    def build_widgets(self):
        frame = ttk.Frame(self.root, padding=8)
        frame.pack(fill="both", expand=True)
        header = ttk.Label(frame, text="Calculator (floating)", foreground="#ECEFF1")
        header.pack(anchor="w")
        self.formula_var = tk.StringVar(value="0.5+2/3.1415926*(sin(x)+sin(3*x)/3+sin(5*x)/5)")
        ttk.Entry(frame, textvariable=self.formula_var).pack(fill="x", pady=(6, 0))
        range_frame = ttk.Frame(frame)
        range_frame.pack(fill="x", pady=(6, 0))
        ttk.Label(range_frame, text="x start").grid(row=0, column=0)
        self.x_start_var = tk.StringVar(value="-6")
        self.x_end_var = tk.StringVar(value="6")
        self.sample_var = tk.StringVar(value=str(SAMPLES_DEFAULT))
        ttk.Entry(range_frame, width=8, textvariable=self.x_start_var).grid(row=0, column=1)
        ttk.Label(range_frame, text="x end").grid(row=0, column=2)
        ttk.Entry(range_frame, width=8, textvariable=self.x_end_var).grid(row=0, column=3)
        ttk.Label(range_frame, text="samples").grid(row=1, column=0, pady=(4, 0))
        ttk.Entry(range_frame, width=6, textvariable=self.sample_var).grid(row=1, column=1, pady=(4, 0))
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill="x", pady=6)
        ttk.Button(button_frame, text="Plot / Draw", command=self.handle_plot).pack(side="left")
        ttk.Button(button_frame, text="Clear calc", command=self.clear_slide).pack(side="left", padx=6)
        ttk.Button(button_frame, text="Close", command=self.root.quit).pack(side="right")
        self.message_var = tk.StringVar(value="Ready to evaluate")
        ttk.Label(frame, textvariable=self.message_var, foreground="#AED581").pack(anchor="w")
        self.footer = ttk.Label(frame, text="Slide config: awaiting config.json", foreground="#90A4AE")
        self.footer.pack(anchor="w", pady=(6, 0))

    def load_client(self):
        LOGGER.info("load_client: loading configuration from %s", CONFIG_PATH)
        try:
            cfg = load_config()
        except ExpressionError as exc:
            LOGGER.error("load_client: config.json invalid: %s", exc)
            self.footer.configure(text=f"config.json error: {exc}")
            return
        if not cfg:
            LOGGER.warning("load_client: config.json missing")
            self.footer.configure(text="config.json missing; copy config.example.json and fill values")
            return
        self.config = cfg
        self.footer.configure(text=f"Slide {cfg['presentation_id']}#{cfg['slide_index']} @ {cfg['host']}:{cfg['port']}")
        LOGGER.info(
            "load_client: connecting to server %s:%d for slide %s#%s",
            cfg["host"],
            cfg["port"],
            cfg["presentation_id"],
            cfg["slide_index"],
        )
        try:
            self.client = SlideClient(cfg["presentation_id"], cfg["slide_index"], cfg["host"], cfg["port"])
            self.client.read_slide()
            LOGGER.info("load_client: skill server handshake succeeded")
        except Exception as exc:
            LOGGER.exception("load_client: skill server unreachable")
            self.footer.configure(text=f"skill server unreachable: {exc}")
            self.client = None

    def handle_plot(self):
        expression = self.formula_var.get()
        try:
            parsed = ParsedExpression(expression)
        except ExpressionError as exc:
            self.message_var.set(f"Invalid formula: {exc}")
            return
        x_start = parse_float(self.x_start_var.get(), -6)
        x_end = parse_float(self.x_end_var.get(), 6)
        if x_end == x_start:
            x_end += 1
        samples = parse_int(self.sample_var.get(), SAMPLES_DEFAULT)
        operations = []
        if parsed.uses_variable:
            operations = self.plot_builder.build_plot_operations(parsed, x_start, x_end, samples)
            operation_kind = "plot"
        else:
            result = parsed.evaluate()
            operations = self.plot_builder.build_number_operations(result)
            operation_kind = "value"
        LOGGER.info(
            "handle_plot: built %s operations -> %d",
            operation_kind,
            len(operations),
        )
        if self.client:
            self.set_message("Drawing to slide...")
            self.run_worker(self._draw_worker, operations)
        else:
            LOGGER.warning("No skill server available; emitting operations to stdout")
            print(json.dumps(operations, indent=2))

    def delete_prior_objects(self, elements):
        ids = [el["objectId"] for el in elements if el["objectId"].startswith("calc_")]
        if ids and self.client:
            self.client.delete_objects(ids)

    def clear_slide(self):
        if not self.client:
            self.set_message("No skill server to clear")
            return
        LOGGER.info("Clear action triggered")
        self.set_message("Clearing calculator content...")
        self.run_worker(self._clear_worker)

    def _draw_worker(self, operations):
        LOGGER.info("Draw worker starting")
        try:
            slide = self.client.read_slide()
            self.delete_prior_objects(slide.get("elements", []))
            self.client.batch_draw(operations)
            self.set_message("Slide updated")
            LOGGER.info("Draw worker finished")
        except Exception as exc:
            self.set_message(f"Failed to draw: {exc}")
            LOGGER.exception("Draw worker failed")

    def _clear_worker(self):
        LOGGER.info("Clear worker starting")
        try:
            slide = self.client.read_slide()
            self.delete_prior_objects(slide.get("elements", []))
            self.set_message("Cleared previous calculator art")
            LOGGER.info("Clear worker finished")
        except Exception as exc:
            self.set_message(f"Cleanup failed: {exc}")
            LOGGER.exception("Clear worker failed")


def parse_float(text, fallback):
    try:
        return float(text)
    except ValueError:
        return fallback


def parse_int(text, fallback):
    try:
        value = int(text)
        return max(12, min(value, 500))
    except ValueError:
        return fallback


def main():
    gui = CalculatorGUI()
    gui.root.mainloop()


if __name__ == "__main__":
    main()
