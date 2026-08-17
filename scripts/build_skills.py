#!/usr/bin/env python3
"""Build installable agent skills from packs.

For each pack (packs/*.md), emit a self-contained Claude Code skill at
packs/skills/<pack>/SKILL.md: a `name`/`description` frontmatter plus every recipe in the pack
inlined as goal + numbered steps (with the "Expect:" observation and ⚠ irreversible markers).
Drop the folder into an agent that reads skills (Claude Code: `.claude/skills/`), or use the
howto MCP server for the same content on demand.

Usage:
  python3 scripts/build_skills.py [pack-name ...]   (default: all packs)
"""
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import export  # noqa: E402  reuse the corpus parser

export.ROOT = ROOT


def load_pack(path):
    with open(path) as f:
        text = f.read()
    end = text.find("\n---\n", 4)
    return yaml.safe_load(text[4:end])


def recipe_index():
    idx = {}
    for r in export.collect(None):
        idx[r["id"]] = r
    return idx


def skill_for(pack, idx):
    name = pack["name"]
    lines = ["---",
             "name: howto-%s" % name,
             "description: %s Verified howto recipes for: %s."
             % (pack["tagline"], pack["title"]),
             "---", "",
             "# %s — howto skill" % pack["title"], "",
             pack["tagline"], "",
             "When the user needs any task below, follow its verified steps in order. Each step's "
             "**Expect** is the observation that confirms it worked; steps marked ⚠ are "
             "irreversible — confirm before doing them. For the full recipe (decision points, "
             "failure recovery, variations) use the howto MCP `get_howto(<id>)` or read the "
             "linked source.", ""]
    missing = []
    for rid in pack["recipes"]:
        r = idx.get(rid)
        if not r:
            missing.append(rid)
            continue
        m, sec = r["meta"], r["sections"]
        lines.append("## %s  \n`%s`" % (str(m.get("name", "")).replace("-", " "), rid))
        goal = " ".join(sec.get("Goal", "").split())
        if goal:
            lines.append("")
            lines.append("**Goal:** %s" % goal)
        lines.append("")
        for s in r["steps"]:
            line = "%d. %s%s" % (s["n"], "⚠ " if s["irreversible"] else "", s["action"])
            if s["expect"]:
                line += "  → *Expect:* %s" % s["expect"]
            lines.append(line)
        if sec.get("Verification"):
            lines.append("")
            lines.append("**Done when:** %s" % " ".join(sec["Verification"].split()))
        lines.append("")
    for j in pack.get("journeys", []):
        lines.append("## 🗺️ %s (journey)  \n`%s`" % (
            j.split("/")[-1].replace("-", " "), j))
        lines.append("")
        lines.append("A long-horizon plan spanning this whole area — read `%s.md` or ask the "
                     "howto MCP. Mind the gates and re-plan triggers." % j)
        lines.append("")
    return "\n".join(lines), missing


def main():
    pdir = os.path.join(ROOT, "packs")
    names = sys.argv[1:] or [f[:-3] for f in sorted(os.listdir(pdir))
                             if f.endswith(".md") and f != "README.md"]
    idx = recipe_index()
    for name in names:
        pack = load_pack(os.path.join(pdir, name + ".md"))
        text, missing = skill_for(pack, idx)
        out_dir = os.path.join(pdir, "skills", name)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "SKILL.md"), "w") as f:
            f.write(text + "\n")
        note = " (MISSING: %s)" % ", ".join(missing) if missing else ""
        print("wrote packs/skills/%s/SKILL.md%s" % (name, note))


if __name__ == "__main__":
    main()
