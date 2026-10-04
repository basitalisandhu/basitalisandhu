#!/usr/bin/env python3
"""Refresh the "Latest releases" block in the profile README.

Fetches the latest release of each portfolio repository from the public GitHub
API and rewrites the text between the RELEASES:START and RELEASES:END markers.

Rules this script follows:

* Standard library only (urllib honours HTTPS_PROXY / HTTP_PROXY from the env).
* It never fails the job. Every error path prints a warning and exits 0.
* HTTP 404 (no release yet, or the repo is not public yet) renders as
  "no public release yet".
* Rate limits, other HTTP errors and network failures keep the row that is
  already in the README for that repo, so a bad day at the API never wipes
  good data.
* Output is deterministic (no timestamps), so the auto-commit step only
  commits when a release actually changed.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

OWNER = "basitalisandhu"
REPOS = [
    "llm-agent-control-plane",
    "ai-agent-incidents",
    "agentic-semgrep-rules",
    "agent-threat-model",
    "agent-security-skills",
    "masoon",
]
START = "<!-- RELEASES:START -->"
END = "<!-- RELEASES:END -->"
README = Path(__file__).resolve().parent.parent / "README.md"
TIMEOUT_SECONDS = 15
API = "https://api.github.com"

HEADER = [
    "| Project | Latest release | Published |",
    "|---|---|---|",
]
ROW_RE = re.compile(r"^\| \[(?P<repo>[^\]]+)\]\(")


def warn(message: str) -> None:
    """Print a GitHub Actions warning annotation (plain text elsewhere)."""
    print(f"::warning::{message}" if os.environ.get("GITHUB_ACTIONS") else f"warning: {message}")


def fetch_latest(repo: str) -> tuple[str, dict | str | None]:
    """Return ("ok", release_json) | ("none", None) | ("error", reason)."""
    url = f"{API}/repos/{OWNER}/{repo}/releases/latest"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{OWNER}-profile-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return "ok", json.load(response)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return "none", None
        remaining = err.headers.get("x-ratelimit-remaining")
        if err.code in (403, 429) and remaining == "0":
            return "error", f"rate limited (HTTP {err.code})"
        return "error", f"HTTP {err.code} {err.reason}"
    except (urllib.error.URLError, OSError, ValueError) as err:
        return "error", f"{type(err).__name__}: {err}"


def cell(text: str) -> str:
    """Make a value safe inside a Markdown table cell."""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def parse_rows(block: str) -> dict[str, str]:
    """Map repo name -> existing table row, so failed fetches keep old data."""
    rows: dict[str, str] = {}
    for line in block.splitlines():
        match = ROW_RE.match(line.strip())
        if match:
            rows[match.group("repo")] = line.strip()
    return rows


def render_row(repo: str, status: str, data: dict | None) -> str:
    repo_link = f"[{repo}](https://github.com/{OWNER}/{repo})"
    if status == "ok" and isinstance(data, dict):
        tag = cell(data.get("tag_name") or data.get("name") or "release")
        href = data.get("html_url") or f"https://github.com/{OWNER}/{repo}/releases/latest"
        published = cell((data.get("published_at") or "")[:10])
        return f"| {repo_link} | [{tag}]({href}) | {published} |"
    return f"| {repo_link} | no public release yet | |"


def build_block(previous: dict[str, str]) -> str:
    rows = []
    for repo in REPOS:
        status, data = fetch_latest(repo)
        if status == "error":
            reason = data
            if repo in previous:
                warn(f"{repo}: {reason}; keeping previous row")
                rows.append(previous[repo])
            else:
                warn(f"{repo}: {reason}; no previous row, showing placeholder")
                rows.append(render_row(repo, "none", None))
            continue
        rows.append(render_row(repo, status, data if isinstance(data, dict) else None))
    return "\n" + "\n".join(HEADER + rows) + "\n"


def main() -> int:
    try:
        text = README.read_text(encoding="utf-8")
    except OSError as err:
        warn(f"cannot read {README}: {err}")
        return 0

    if START not in text or END not in text or text.index(START) > text.index(END):
        warn("release markers not found or out of order; nothing to do")
        return 0

    before, rest = text.split(START, 1)
    old_block, after = rest.split(END, 1)

    new_block = build_block(parse_rows(old_block))
    new_text = f"{before}{START}{new_block}{END}{after}"

    if new_text == text:
        print("README already up to date")
        return 0

    try:
        README.write_text(new_text, encoding="utf-8")
    except OSError as err:
        warn(f"cannot write {README}: {err}")
        return 0
    print("README updated")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as err:  # noqa: BLE001 - last line of defence, never fail the job
        warn(f"update_readme.py hit an unexpected error: {err}")
        sys.exit(0)
