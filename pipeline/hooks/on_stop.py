#!/usr/bin/env python3
"""Cursor stop hook: run the strict content gate at the end of every agent turn."""
import subprocess, datetime
from pathlib import Path

result = subprocess.run(
    ["python", "pipeline/validate/validate.py", "--strict"],
    capture_output=True, text=True
)
status = "PASS" if result.returncode == 0 else "FAIL"
Path(".cursor").mkdir(exist_ok=True)
with open(".cursor/validation.log", "a") as f:
    f.write(f"\n{datetime.datetime.now().isoformat()} [{status}] session stop (--strict)\n")
    f.write(result.stdout + "\n")
