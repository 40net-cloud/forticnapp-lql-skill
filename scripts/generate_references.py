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
    uv run scripts/generate_references.py --print-remote-version

With no --version, the guide version is detected from the docs site and
stamped into the provenance headers. --print-remote-version just prints that
detected version and exits (used by the refresh GitHub Actions workflow to
decide whether a regeneration is needed).

Dependencies (beautifulsoup4, markdownify, plus a curl on PATH) are declared
both in the PEP 723 block above and in the repo pyproject.toml, so `uv run`
resolves them automatically into an ephemeral environment.

The script fetches the guide's HTML pages, extracts the main content div,
converts it to markdown, cleans it (unescape, strip links, notes -> blockquotes),
compacts datasource tables to one-line bullets, splits the datasource metadata
page per provider, and stamps each output file with a provenance header.

The guide version the skill is based on is the single source of truth in
skills/forticnapp-lql/guide-version.json — this script rewrites it on every
run, and the refresh workflow reads it to decide whether to regenerate.

SKILL.md is NOT regenerated — it is hand-maintained. After regenerating,
diff the references and update SKILL.md if syntax/policy rules changed.
"""

import argparse
import datetime
import json
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

# Patterns tried in order. The site layout has changed before (the old
# "Version: 26.2.0" version-picker text disappeared), so keep several.
VERSION_RES = [
    re.compile(r"<title>[^<]*FortiCNAPP\s+([0-9]+(?:\.[0-9]+){1,2})\b"),
    re.compile(r'data-version="([0-9]+(?:\.[0-9]+){1,2})"'),
    re.compile(r"Version:\s*([0-9]+(?:\.[0-9]+){1,2})"),
]

# Selectors for the page's main content, tried in order.
CONTENT_SELECTORS = ["article.reader__page div.prose", "div.prose", "div#content"]

# Provider grouping for splitting the datasource-metadata page (## headings).
# Keys are file stem prefixes; a group larger than MAX_CHUNK_CHARS is further
# split on its "### " service headings into alphabetical chunks
# (e.g. datasources-aws-config-a-c.md), so no single file is expensive to load.
DATASOURCE_GROUPS = {
    "datasources-aws-config": ["## AWS Configuration Datasources"],
    "datasources-aws-cloudtrail": ["## CloudTrail Logging Datasources"],
    "datasources-azure": ["## Azure Configuration Datasources"],
    "datasources-gcp-config": ["## Google Cloud Configuration Datasources"],
    "datasources-gcp-audit": ["## Google Cloud Audit Log Activity"],
    "datasources-oci": ["## OCI Configuration Datasources"],
    "datasources-workload": ["## Workload Security Datasources"],
    "datasources-attackpath": ["## Attack Path Analysis Datasources"],
    "datasources-entitlements": ["## Cloud Entitlement Datasources"],
}
MAX_CHUNK_CHARS = 24000  # ~6K tokens


def fetch(url):
    out = subprocess.run(["curl", "-sL", "-A", UA, url],
                         capture_output=True, check=True)
    return out.stdout.decode("utf-8", errors="replace")


def detect_remote_version(html=None):
    """Read the guide version from the docs-site page (title / data-version).

    Returns e.g. "26.2" (a trailing ".0" patch component is dropped so the
    value matches the two-part version stamped in existing provenance headers).
    """
    if html is None:
        html = fetch(PAGES["overview"])
    m = next((m for r in VERSION_RES if (m := r.search(html))), None)
    if not m:
        sys.exit("could not detect guide version — docs.fortinet.com layout may have changed")
    return re.sub(r"\.0$", "", m.group(1))


def html_to_markdown(html):
    soup = BeautifulSoup(html, "html.parser")
    # Current layout: <article class="reader__page"><div class="prose ...">.
    # "div#content" was the previous layout; keep it as a fallback.
    el = next((e for sel in CONTENT_SELECTORS if (e := soup.select_one(sel))), None)
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


def fix_functions_errata(text):
    """Correct known upstream errors in the LQL functions page.

    The FortiCNAPP guide describes IP_CONTAINS twice. The detailed entry is
    right ("return true if arg0 contains arg1"), but the summary-table row has
    the arguments inverted ("returns true if A is a subset of ... B"). A model
    that greps functions.md hits the table row first and gets the argument
    order backwards, so rewrite that one row to agree with the detailed entry.
    See https://github.com/40net-cloud/forticnapp-lql-skill/issues/1.
    """
    pat = re.compile(
        r"^\| IP_CONTAINS \| Interprets two arguments A and B as sets of IP "
        r"addresses and returns true if A is a subset of, or equal to, B\. \|$",
        re.MULTILINE,
    )
    fixed = (
        "| IP_CONTAINS | Interprets `arg0` and `arg1` as sets of IP addresses "
        "and returns true if `arg0` contains `arg1` (i.e. `arg1` is a subset "
        "of, or equal to, `arg0`). See the detailed entry below. |"
    )
    text, n = pat.subn(fixed, text)
    if n == 0:
        print("  WARNING: IP_CONTAINS summary-table errata pattern not found — "
              "guide may have fixed it upstream; drop fix_functions_errata if so")
    return text


def chunk_section(text, limit=MAX_CHUNK_CHARS):
    """Split a "## " section on "### " headings into chunks of <= limit chars.

    Returns [(label, text)]; label is "" for a single chunk, else "a-c" style
    first/last letters of the first/last service in the chunk. The section
    preamble (e.g. the common-fields list) is repeated at the top of every chunk.
    """
    if len(text) <= limit:
        return [("", text)]
    parts = re.split(r"\n(?=### )", text)
    pre, units = parts[0], parts[1:]
    if not units:
        return [("", text)]
    chunks, cur = [], []
    size = len(pre)
    for u in units:
        if cur and size + len(u) > limit:
            chunks.append(cur)
            cur, size = [], len(pre)
        cur.append(u)
        size += len(u) + 1
    chunks.append(cur)

    def letter(unit):
        ch = unit[4:5].lower()
        return ch if ch.isalnum() else "x"

    out, used = [], set()
    for c in chunks:
        a, b = letter(c[0]), letter(c[-1])
        label = a if a == b else f"{a}-{b}"
        while label in used:  # same range twice: disambiguate
            label += "x"
        used.add(label)
        out.append((label, pre + "\n" + "\n".join(c)))
    return out


def provenance(urls, version):
    today = datetime.date.today().isoformat()
    lines = "\n".join("     " + u for u in urls)
    return (f"<!-- Generated from FortiCNAPP {version} LQL Reference Guide "
            f"(fetched {today}). Source:\n{lines} -->\n\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=None,
                    help="Guide version stamped in provenance headers "
                         "(default: detect from docs.fortinet.com)")
    ap.add_argument("--print-remote-version", action="store_true",
                    help="Print the guide version detected on docs.fortinet.com and exit")
    args = ap.parse_args()

    if args.print_remote_version:
        print(detect_remote_version())
        return

    version = args.version or detect_remote_version()
    print(f"guide version: {version}")

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
            fh.write(provenance(urls, version) + content)
        print(f"  wrote {fname} ({len(content) // 4} tokens approx)")

    write("syntax.md", md["overview"], [PAGES["overview"]])
    write("query-types.md", md["query-types"], [PAGES["query-types"]])
    write("operators.md", md["lql-operators"], [PAGES["lql-operators"]])
    write("functions.md", fix_functions_errata(md["lql-functions"]),
          [PAGES["lql-functions"]])
    write("examples.md", md["example-queries"], [PAGES["example-queries"]])

    sections = re.split(r"\n(?=## )", compact_tables(md["datasource-metadata"]))
    by_title = {s.split("\n", 1)[0].strip(): s for s in sections[1:]}
    # Drop previously generated datasource files so renamed/re-chunked ones don't linger.
    for old in os.listdir(dst):
        if old.startswith("datasources-") and old.endswith(".md"):
            os.remove(os.path.join(dst, old))
    index = []
    for stem, titles in DATASOURCE_GROUPS.items():
        parts = []
        for t in titles:
            if t not in by_title:
                print(f"  WARNING: section {t!r} not found — guide structure changed?")
                continue
            parts.append(by_title.pop(t))
        for part in parts:
            for label, body in chunk_section(part):
                fname = f"{stem}-{label}.md" if label else f"{stem}.md"
                if fname in {i[0] for i in index}:  # two sections in one stem
                    fname = fname.replace(".md", "-2.md")
                write(fname, "# Datasource Metadata\n\n" + body, [PAGES["datasource-metadata"]])
                services = re.findall(r"^### (.+)$", body, re.MULTILINE)
                names = re.findall(r"^- `([A-Z0-9_a-z]+)` — ", body, re.MULTILINE)
                heading = part.split("\n", 1)[0].lstrip("# ").strip()
                rng = ("(no sub-sections)" if not services else services[0] if len(services) == 1
                       else f"{services[0]} … {services[-1]}")
                index.append((fname, heading, rng))
    with open(os.path.join(dst, "datasources-index.md"), "w") as fh:
        fh.write("# Datasource files\n\nGrep these files for a service name; "
                 "each file lists its services alphabetically.\n\n")
        for fname, heading, rng in index:
            fh.write(f"- `{fname}` — {heading}: {rng}\n")
    print("  wrote datasources-index.md")
    for leftover in by_title:
        print(f"  WARNING: unassigned section {leftover!r} — add it to DATASOURCE_GROUPS")

    version_file = os.path.join(os.path.dirname(dst), "guide-version.json")
    with open(version_file, "w") as fh:
        json.dump({
            "version": version,
            "fetched": datetime.date.today().isoformat(),
            "source": BASE,
        }, fh, indent=2)
        fh.write("\n")
    print(f"  wrote guide-version.json ({version})")


if __name__ == "__main__":
    main()
