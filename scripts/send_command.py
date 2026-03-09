#!/usr/bin/env python3
"""Send a JSON command to the slides server (127.0.0.1:8765) and print the response.

Usage:
  echo '{"tool":"read_slide","presentation_id":"...","slide_index":0}' | python scripts/send_command.py
  python scripts/send_command.py '{"tool":"read_slide",...}'
"""
import json
import socket
import sys

HOST = "127.0.0.1"
PORT = 8765
BUFFER_SIZE = 131072


def send_command(command: dict) -> dict:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(json.dumps(command).encode("utf-8"))
        response = sock.recv(BUFFER_SIZE)
    return json.loads(response.decode("utf-8"))


if __name__ == "__main__":
    raw = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    cmd = json.loads(raw)
    result = send_command(cmd)
    print(json.dumps(result, indent=2))
