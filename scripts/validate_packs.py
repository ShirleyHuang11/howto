#!/usr/bin/env python3
"""Validate packs against the pack schema.

A pack (packs/*.md, kind: pack) is a curated cross-domain kit — a manifest of recipe ids (and
optionally journey ids) plus a short rationale. Like journeys, the load-bearing check is that
**every referenced id resolves to a real recipe or journey**, so a pack can never advertise a
recipe that doesn't exist.

Usage: python3 scripts/validate_packs.py [packs/foo.md ...]   (default: all packs/*.md)
Exits non-zero and prints one line per violation.
"""
import json
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ["name", "kind", "title", "tagline", "recipes"]


def corpus_ids():
    with open(os.path.join(ROOT, "domains.json")) as f:
        domains = json.load(f)
    ids = set()
    for domain in domains:
        d = os.path.join(ROOT, domain)
        if not os.path.isdir(d):
            continue
        for dp, _, ns in os.walk(d):
            for n in ns:
                if n.endswith(".md"):
                    ids.add("%s/%s" % (domain, n[:-3]))
    return ids


def journey_ids():
    jdir = os.path.join(ROOT, "journeys")
    if not os.path.isdir(jdir):
        return set()
    return {"journeys/%s" % n[:-3] for n in os.listdir(jdir)
            if n.endswith(".md") and n not in ("README.md", "TEMPLATE.md")}


def check(path, ids, jids):
    errs = []
    with open(path) as f:
        text = f.read()
    if not text.startswith("---\n"):
        return ["missing frontmatter"], 0, 0
    end = text.find("\n---\n", 4)
    meta = yaml.safe_load(text[4:end]) if end != -1 else None
    if not isinstance(meta, dict):
        return ["bad frontmatter"], 0, 0
    for k in REQUIRED:
        if k not in meta:
            errs.append("missing field: %s" % k)
    if meta.get("kind") != "pack":
        errs.append("kind must be 'pack'")
    stem = os.path.splitext(os.path.basename(path))[0]
    if meta.get("name") and meta["name"] != stem:
        errs.append("name %r != filename %r" % (meta["name"], stem))
    recs = meta.get("recipes") or []
    if not isinstance(recs, list) or not recs:
        errs.append("recipes must be a non-empty list")
        recs = []
    for r in recs:
        if r not in ids:
            errs.append("unresolved recipe: %s" % r)
    jrs = meta.get("journeys") or []
    for j in jrs:
        if j not in jids:
            errs.append("unresolved journey: %s" % j)
    return errs, len(recs), len(jrs)


def main():
    ids, jids = corpus_ids(), journey_ids()
    pdir = os.path.join(ROOT, "packs")
    paths = sys.argv[1:] or sorted(
        os.path.join(pdir, f) for f in os.listdir(pdir)
        if f.endswith(".md") and f != "README.md")
    total_err = 0
    for p in paths:
        errs, nr, nj = check(p, ids, jids)
        rel = os.path.relpath(p, ROOT)
        if errs:
            total_err += len(errs)
            for e in errs:
                print("FAIL %s: %s" % (rel, e))
        else:
            print("ok   %s: %d recipes, %d journeys, all resolve" % (rel, nr, nj))
    if total_err:
        print("\n%d violation(s)" % total_err)
        sys.exit(1)
    print("\n%d pack(s) valid" % len(paths))


if __name__ == "__main__":
    main()
