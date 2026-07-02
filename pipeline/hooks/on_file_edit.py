#!/usr/bin/env python3
"""Cursor afterFileEdit hook: re-validate whenever content/ or schemas/ change."""
import json, subprocess, sys, datetime
from pathlib import Path

payload = json.loads(sys.stdin.read() or "{}")
file_path = payload.get("file_path", "")

if not (file_path.startswith("content/") or file_path.startswith("schemas/")):
    sys.exit(0)

result = subprocess.run(
    ["python", "pipeline/validate/validate.py"],
    capture_output=True, text=True
)
status = "PASS" if result.returncode == 0 else "FAIL"
log_line = f"{datetime.datetime.now().isoformat()} [{status}] after edit: {file_path}\n"
Path(".cursor").mkdir(exist_ok=True)
with open(".cursor/validation.log", "a") as f:
    f.write(log_line)
    if status == "FAIL":
        f.write(result.stdout + "\n")

sys.exit(0)
