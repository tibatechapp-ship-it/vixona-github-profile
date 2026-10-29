#!/usr/bin/env python3
"""Update the 'Last Updated' table in the profile README from GitHub API push times.

Reads the marker block:
  <!-- LAST-UPDATED:START --> ... <!-- LAST-UPDATED:END -->
and rewrites the table rows with each repo's latest push (UTC), preserving markers.

Uses GITHUB_TOKEN env var if present (higher rate limit); anonymous otherwise.
"""
import json
import os
import pathlib
import sys
import urllib.request

ORG = "tibatechapp-ship-it"
REPOS = ["Rasan", "lifelink-app", "pharma-sdl", "nexhub", "nexus-core", "chess-cli", "raqib"]
README = pathlib.Path(__file__).resolve().parent.parent / "README.md"
START = "<!-- LAST-UPDATED:START -->"
END = "<!-- LAST-UPDATED:END -->"

API = "https://api.github.com"


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def repo_push_row(repo: str) -> str:
    try:
        data = fetch(f"{API}/repos/{ORG}/{repo}")
        pushed = str(data.get("pushed_at", ""))[:10] or "غير معروف"
    except Exception as e:  # noqa: BLE001 — الصفحة لا تتعطل بسبب مستودع واحد
        print(f"warn: {repo}: {e}", file=sys.stderr)
        pushed = "غير معروف"
    return f"| {repo} | {pushed} | main |"


def main() -> None:
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit("marker block missing in README.md")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)

    rows = "\n".join(
        ["| المشروع | آخر دفعة (UTC) | فرع نشط |", "|---|---|---|"]
        + [repo_push_row(r) for r in REPOS]
    )
    README.write_text(head + START + "\n" + rows + "\n" + END + tail, encoding="utf-8")
    print("README Last Updated table refreshed")


if __name__ == "__main__":
    main()
