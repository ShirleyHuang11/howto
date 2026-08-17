#!/usr/bin/env python3
"""Validate journeys against the journey schema.

A journey (journeys/*.md, kind: journey) is a long-horizon task: a temporal DAG whose leaf
nodes are ordinary recipes. This checks the frontmatter, the fixed section order, per-milestone
structure, and — the load-bearing check — that **every recipe id a journey references resolves
to a real, validated recipe in this corpus**. Unresolved leaves are errors, so a journey can
never quietly decay into a listicle.

Usage: python3 scripts/validate_journeys.py [journeys/foo.md ...]   (default: all journeys/*.md)
Exits non-zero and prints one line per violation.
"""
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FIELDS = ["name", "kind", "domain", "locale", "horizon", "difficulty",
                   "risk", "actors", "status", "last_verified"]
ENUMS = {
    "difficulty": {"basic", "intermediate", "advanced"},
    "risk": {"low", "medium", "high"},
    "status": {"draft", "reviewed", "verified"},
}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HORIZON = re.compile(r"^[0-9]+(min|h|d|wk|mo|yr)(-[0-9]+(min|h|d|wk|mo|yr))?$")
DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
SECTIONS = ["Goal", "Outcome state", "Preconditions", "Milestones", "Dependency graph",
            "Decision points", "Failure modes & recovery", "Re-plan triggers",
            "Verification", "Variations", "Safety & privacy"]
RECIPE_ID = re.compile(r"`([a-z0-9-]+(?:/[a-z0-9-]+)+)`")
MILESTONE = re.compile(r"^### +M\d+\b.*$", re.M)


def corpus_ids():
    with open(os.path.join(ROOT, "domains.json")) as f:
        domains = json.load(f)
    ids = set()
    for domain in domains:
        d = os.path.join(ROOT, domain)
        if not os.path.isdir(d):
            continue
        for dirpath, _, names in os.walk(d):
            for n in names:
                if n.endswith(".md"):
                    ids.add("%s/%s" % (domain, n[:-3]))
    return ids


def parse(path):
    with open(path) as f:
        text = f.read()
    if not text.startswith("---\n"):
        return None, None, "missing frontmatter"
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, None, "unterminated frontmatter"
    return yaml.safe_load(text[4:end]), text[end + 5:], None


def split_sections(body):
    out, cur, buf = {}, None, []
    for line in body.splitlines():
        m = re.match(r"^## +(.+?)\s*$", line)
        if m:
            if cur is not None:
                out[cur] = "\n".join(buf)
            cur, buf = m.group(1), []
        else:
            buf.append(line)
    if cur is not None:
        out[cur] = "\n".join(buf)
    return out


def check(path, ids):
    errs = []
    meta, body, err = parse(path)
    if err:
        return [err], 0, 0
    for f in REQUIRED_FIELDS:
        if f not in meta:
            errs.append("missing field: %s" % f)
    if meta.get("kind") != "journey":
        errs.append("kind must be 'journey'")
    for f, allowed in ENUMS.items():
        if f in meta and meta[f] not in allowed:
            errs.append("%s %r not in %s" % (f, meta[f], sorted(allowed)))
    stem = os.path.splitext(os.path.basename(path))[0]
    if meta.get("name") and meta["name"] != stem:
        errs.append("name %r != filename %r" % (meta["name"], stem))
    if meta.get("name") and not KEBAB.match(str(meta["name"])):
        errs.append("name not kebab-case")
    if meta.get("horizon") and not HORIZON.match(str(meta["horizon"])):
        errs.append("horizon %r must look like 2wk-3mo, 6mo-2yr" % meta.get("horizon"))
    if meta.get("last_verified") and not DATE.match(str(meta["last_verified"])):
        errs.append("last_verified must be YYYY-MM-DD")
    if not isinstance(meta.get("actors"), list) or not meta.get("actors"):
        errs.append("actors must be a non-empty list")

    sec = split_sections(body)
    for s in SECTIONS:
        if s not in sec:
            errs.append("missing section: %s" % s)
    order = [s for s in sec if s in SECTIONS]
    expected = [s for s in SECTIONS if s in sec]
    if order != expected:
        errs.append("sections out of order: %s" % order)

    ms_body = sec.get("Milestones", "")
    n_ms = len(MILESTONE.findall(ms_body))
    if n_ms < 3:
        errs.append("a journey needs >=3 milestones (found %d)" % n_ms)
    chunks = re.split(r"(^### +M\d+\b.*$)", ms_body, flags=re.M)
    for i in range(1, len(chunks) - 1, 2):
        head, block = chunks[i], chunks[i + 1]
        label = head.strip().lstrip("# ").split("—")[0].strip()
        for field in ("Gate:", "Do:", "Verify:", "Re-plan if:"):
            if field not in block:
                errs.append("%s missing **%s**" % (label, field.rstrip(":")))

    refs = sorted(set(RECIPE_ID.findall(ms_body)))
    unresolved = [r for r in refs if r not in ids]
    for r in unresolved:
        errs.append("unresolved recipe reference: %s" % r)

    if "```mermaid" not in sec.get("Dependency graph", ""):
        errs.append("Dependency graph must contain a ```mermaid block")

    return errs, n_ms, len(refs)


def main():
    ids = corpus_ids()
    jdir = os.path.join(ROOT, "journeys")
    paths = sys.argv[1:] or sorted(
        os.path.join(jdir, f) for f in os.listdir(jdir)
        if f.endswith(".md") and f not in ("README.md", "TEMPLATE.md"))
    total_err = 0
    for p in paths:
        errs, n_ms, n_ref = check(p, ids)
        rel = os.path.relpath(p, ROOT)
        if errs:
            total_err += len(errs)
            for e in errs:
                print("FAIL %s: %s" % (rel, e))
        else:
            print("ok   %s: %d milestones, %d recipe refs, all resolve" % (rel, n_ms, n_ref))
    if total_err:
        print("\n%d violation(s)" % total_err)
        sys.exit(1)
    print("\n%d journey(s) valid; leaves resolve against %d recipes" % (len(paths), len(ids)))


if __name__ == "__main__":
    main()
