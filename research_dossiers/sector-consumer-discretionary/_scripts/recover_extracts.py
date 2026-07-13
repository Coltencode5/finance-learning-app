#!/usr/bin/env python3
"""Recover the longest '# Extract' assistant message from each subagent transcript."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(
    r"c:\Users\cfroo\OneDrive\finance-learning-app\research_dossiers\sector-consumer-discretionary\01_EXTRACTS"
)
OUT.mkdir(parents=True, exist_ok=True)

BASE = Path(
    r"C:\Users\cfroo\.cursor\projects\c-Users-cfroo-OneDrive-finance-learning-app\agent-transcripts\3352db41-1b79-4aac-9fea-567cec0cc123\subagents"
)


def all_texts(path: Path) -> list[str]:
    texts = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = obj.get("message") or {}
            content = msg.get("content", [])
            if isinstance(content, str):
                texts.append(content)
            elif isinstance(content, list):
                for c in content:
                    if isinstance(c, dict) and c.get("type") == "text":
                        texts.append(c.get("text", ""))
                    elif isinstance(c, str):
                        texts.append(c)
            for key in ("text", "response", "content"):
                if key in obj and isinstance(obj[key], str):
                    texts.append(obj[key])
    return texts


def best_extract(texts: list[str]) -> str:
    cands = [t for t in texts if "# Extract" in t]
    if not cands:
        cands = [t for t in texts if "**Argument:**" in t]
    if not cands:
        return ""
    return max(cands, key=len)


def clean(body: str) -> str:
    if "# Extract" in body:
        body = body[body.index("# Extract") :]
    for stop in [
        "\nAsk mode",
        "\n**Blocked:**",
        "\nCan't write",
        "\nI can’t write",
        "\nI can't write",
        "\nSwitch to **Agent",
    ]:
        if stop in body:
            body = body[: body.index(stop)]
    return body.strip() + "\n"


def write(name: str, body: str) -> None:
    body = clean(body)
    (OUT / name).write_text(body, encoding="utf-8")
    print(name, len(body))


def main():
    es = best_extract(all_texts(BASE / "67ec1958-fb82-4724-9477-cdcc5b761ffb.jsonl"))
    write("everything_store.md", es)

    rr = best_extract(all_texts(BASE / "be29f0b6-20ef-4790-a7c8-d70e47454761.jsonl"))
    write("resurrecting_retail.md", rr)

    both = best_extract(all_texts(BASE / "35136bf2-51c0-41fd-9489-a1e7d98899f4.jsonl"))
    if "===== FILE: trading_up.md =====" in both:
        rest = both.split("===== FILE: trading_up.md =====", 1)[1]
        if "===== FILE: different.md =====" in rest:
            tu, diff = rest.split("===== FILE: different.md =====", 1)
        else:
            tu, diff = rest, ""
        write("trading_up.md", tu if "# Extract" in tu else "# Extract — Trading Up\n" + tu)
        write("different.md", diff if "# Extract" in diff else "# Extract — Different\n" + diff)
    else:
        parts = both.split("# Extract — Different")
        if len(parts) == 2:
            write("trading_up.md", parts[0])
            write("different.md", "# Extract — Different" + parts[1])
        else:
            write("trading_up.md", both)
            write(
                "different.md",
                "# Extract — Different\n\nFLAG: recovery failed to split; see trading_up.md parent transcript.\n",
            )


if __name__ == "__main__":
    main()
