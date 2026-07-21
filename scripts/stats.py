#!/usr/bin/env python3
"""Per-domain coverage dashboard (proposal section 5.1 reports per-domain, not aggregate).

Usage: python3 scripts/stats.py
"""
import json
import os
from collections import defaultdict

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def frontmatter(path):
    with open(path) as f:
        text = f.read()
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}


def main():
    with open(os.path.join(ROOT, "domains.json")) as f:
        domains = json.load(f)

    rows = []
    totals = defaultdict(int)
    for domain in sorted(domains):
        d = os.path.join(ROOT, domain)
        counts = defaultdict(int)
        locales = set()
        for dirpath, _, names in os.walk(d) if os.path.isdir(d) else []:
            for n in names:
                if not n.endswith(".md"):
                    continue
                meta = frontmatter(os.path.join(dirpath, n))
                counts["recipes"] += 1
                counts[meta.get("status", "draft")] += 1
                for loc in meta.get("locale") or []:
                    if loc != "generic":
                        locales.add(loc)
        rows.append((domain, domains[domain].get("track", "-"), counts, sorted(locales)))
        for k, v in counts.items():
            totals[k] += v

    fmt = "%-15s %-13s %7s %7s %9s %9s  %s"
    print(fmt % ("domain", "track", "recipes", "draft", "reviewed", "verified", "locale variants"))
    for domain, track, c, locs in rows:
        print(fmt % (domain, track, c["recipes"], c["draft"], c["reviewed"], c["verified"],
                     ",".join(locs) if locs else "-"))
    print(fmt % ("TOTAL", "", totals["recipes"], totals["draft"], totals["reviewed"], totals["verified"], ""))


if __name__ == "__main__":
    main()
