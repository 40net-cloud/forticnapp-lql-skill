#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "beautifulsoup4",
#     "markdownify",
# ]
# ///
"""Regenerate skills/forticnapp-lql/references/ from the online
FortiCNAPP LQL Reference Guide (docs.fortinet.com).

Usage:
    uv run scripts/generate_references.py [--version 26.2]

Dependencies (beautifulsoup4, markdownify, plus a curl on PATH) are declared
both in the PEP 723 block above and in the repo pyproject.toml, so `uv run`
resolves them automatically into an ephemeral environment.

The script fetches the guide's HTML pages, extracts the main content div,
converts it to markdown, cleans it (unescape, strip links, notes -> blockquotes),
compacts datasource tables to one-line bullets, splits the datasource metadata
page per provider, and stamps each output file with a provenance header.

SKILL.md is NOT regenerated — it is hand-maintained. After regenerating,
diff the references and update SKILL.md if syntax/policy rules changed.
"""

import argparse
import datetime
import os
import re
import subprocess
import sys
import tempfile

from bs4 import BeautifulSoup
from markdownify import markdownify as to_md

BASE = "https://docs.fortinet.com/document/forticnapp/latest/lql-reference"
PAGES = {
    "overview": f"{BASE}/598361/lql-overview",
    "query-types": f"{BASE}/842922/query-types",
    "lql-operators": f"{BASE}/754354/lql-operators",
    "lql-functions": f"{BASE}/486918/lql-functions",
    "example-queries": f"{BASE}/435177/example-queries",
    "datasource-metadata": f"{BASE}/771173/datasource-metadata",
}
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# Provider grouping for splitting the datasource-metadata page (## headings).
DATASOURCE_GROUPS = {
    "datasources-aws.md": ["## AWS Configuration Datasources",
                           "## CloudTrail Logging Datasources"],
    "datasources-azure.md": ["## Azure Configuration Datasources"],
    "datasources-gcp.md": ["## Google Cloud Configuration Datasources",
                           "## Google Cloud Audit Log Activity"],
    "datasources-oci.md": ["## OCI Configuration Datasources"],
    "datasources-agent-k8s.md": ["## Workload Security Datasources",
                                 "## Attack Path Analysis Datasources",
                                 "## Cloud Entitlement Datasources"],
}


def fetch(url):
    out = subprocess.run(["curl", "-sL", "-A", UA, url],
                         capture_output=True, check=True)
    return out.stdout.decode("utf-8", errors="replace")


def html_to_markdown(html):
    soup = BeautifulSoup(html, "html.parser")
    el = soup.select_one("div#content")
    if el is None:
        sys.exit("content div not found — docs.fortinet.com layout may have changed")
    return to_md(str(el), heading_style="ATX")


def clean(text):
    text = text.replace("\r", "")  # docs pages embed CRLF inside <pre> blocks
    text = text.replace("\\_", "_").replace("\\*", "*").replace("\\#", "#")
    # "Note" callout tables -> blockquotes
    text = re.sub(r"\|\s*\|\s*\|\n\|\s*---\s*\|\s*---\s*\|\n\|\s*Note\s*\|\s*(.*?)\s*\|",
                  r"> **Note:** \1", text)
    # links -> plain text
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def compact_tables(text):
    """Datasource/field tables -> one-line bullets (major token saving)."""
    out = []
    for ln in text.split("\n"):
        s = ln.strip()
        if re.match(r"^\|\s*Datasource\s*\|\s*Description\s*\|$", s):
            continue
        if re.match(r"^\| Column Name \| Data Type \| Description \|$", s):
            continue
        if re.match(r"^\|[\s|-]+\|$", s):
            continue
        m = re.match(r"^\|\s*([A-Z0-9_]+)\s*\|\s*(\w+)\s*\|\s*(.*?)\s*\|$", s)
        if m:  # 3-col field table row
            out.append(f"- `{m.group(1)}` ({m.group(2)}) — {m.group(3)}")
            continue
        m = re.match(r"^\|\s*([A-Z0-9_]+)\s*\|\s*(.*?)\s*\|$", s)
        if m:  # 2-col datasource table row
            out.append(f"- `{m.group(1)}` — {m.group(2)}")
            continue
        out.append(ln)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def provenance(urls, version):
    today = datetime.date.today().isoformat()
    lines = "\n".join("     " + u for u in urls)
    return (f"<!-- Generated from FortiCNAPP {version} LQL Reference Guide "
            f"(fetched {today}). Source:\n{lines} -->\n\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default="26.2",
                    help="Guide version stamped in provenance headers")
    args = ap.parse_args()

    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dst = os.path.join(repo, "skills", "forticnapp-lql", "references")
    os.makedirs(dst, exist_ok=True)

    md = {}
    for name, url in PAGES.items():
        print(f"fetching {name} ...")
        md[name] = clean(html_to_markdown(fetch(url)))

    def write(fname, content, urls):
        path = os.path.join(dst, fname)
        with open(path, "w") as fh:
            fh.write(provenance(urls, args.version) + content)
        print(f"  wrote {fname} ({len(content) // 4} tokens approx)")

    write("syntax.md",
          md["overview"] + "\n\n" + md["query-types"] + "\n\n" + md["lql-operators"],
          [PAGES["overview"], PAGES["query-types"], PAGES["lql-operators"]])
    write("functions.md", md["lql-functions"], [PAGES["lql-functions"]])
    write("examples.md", md["example-queries"], [PAGES["example-queries"]])

    sections = re.split(r"\n(?=## )", compact_tables(md["datasource-metadata"]))
    by_title = {s.split("\n", 1)[0].strip(): s for s in sections[1:]}
    for fname, titles in DATASOURCE_GROUPS.items():
        parts = []
        for t in titles:
            if t not in by_title:
                print(f"  WARNING: section {t!r} not found — guide structure changed?")
                continue
            parts.append(by_title.pop(t))
        write(fname, "# Datasource Metadata\n\n" + "\n\n".join(parts),
              [PAGES["datasource-metadata"]])
    for leftover in by_title:
        print(f"  WARNING: unassigned section {leftover!r} — add it to DATASOURCE_GROUPS")


if __name__ == "__main__":
    main()
