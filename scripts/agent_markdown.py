#!/usr/bin/env python3
"""Copy source markdown into the built site; generate llms.txt and llms-full.txt.

Makes the site agent-ready: every rendered page at <site_url>/<path>/ has
its raw markdown source served at <site_url>/<path>.md, /llms.txt
(https://llmstxt.org/) indexes them for AI agents, and /llms-full.txt
holds the full markdown content of every page in one file.

Run from the repo root after `zensical build`:
    python3 scripts/agent_markdown.py
"""
import os
import re
import shutil

DOCS, SITE = "docs", "site"

with open("zensical.toml", encoding="utf-8") as f:
    toml_text = f.read()


def toml_key(key, default=""):
    m = re.search(rf'^{key}\s*=\s*"([^"]*)"', toml_text, re.M)
    return m.group(1) if m else default


site_url = toml_key("site_url").rstrip("/")
assert site_url, "site_url not found in zensical.toml"
name = toml_key("site_name", site_url)
desc = toml_key("site_description")

entries = []
for root, _, files in os.walk(DOCS):
    for fn in sorted(files):
        if not fn.endswith(".md"):
            continue
        src = os.path.join(root, fn)
        rel = os.path.relpath(src, DOCS)
        dst = os.path.join(SITE, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        title = rel
        with open(src, encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r"#\s+(.+)", line)
                if m:
                    title = m.group(1).strip()
                    break
        entries.append((rel, title))

lines = [
    f"# {name}",
    "",
    f"> {desc}",
    "",
    "Raw markdown source for every page on this site. Each `<path>.md`",
    f"below is the source of the rendered page at {site_url}/<path>/.",
    "",
    "## Pages",
    "",
]
for rel, title in sorted(entries, key=lambda e: e[0]):
    lines.append(f"- [{title}]({site_url}/{rel})")
lines.append("")
lines.append(f"Full content of every page in one file: {site_url}/llms-full.txt")
with open(os.path.join(SITE, "llms.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

full = [f"# {name}", "", f"> {desc}", "",
        "Full markdown content of every page on this site.", ""]
for rel, title in sorted(entries, key=lambda e: e[0]):
    with open(os.path.join(DOCS, rel), encoding="utf-8") as fh:
        content = fh.read().rstrip()
    full += ["-" * 72, "", f"## {title}", f"URL: {site_url}/{rel}", "", content, ""]
with open(os.path.join(SITE, "llms-full.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(full) + "\n")
print(f"agent_markdown: copied {len(entries)} markdown files, wrote llms.txt and llms-full.txt")
