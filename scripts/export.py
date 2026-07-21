#!/usr/bin/env python3
"""Export recipes into training products (proposal section 6).

Formats:
  json  full structured recipes: frontmatter + parsed sections + parsed steps
  sft   instruction-tuning pairs (JSONL): "how do I X" -> structured plan
  eval  task specs (JSONL): goal + preconditions + verification -> checkable task

Usage:
  python3 scripts/export.py --format json [paths...] > recipes.json
  python3 scripts/export.py --format sft  > sft.jsonl
  python3 scripts/export.py --format eval > eval.jsonl
"""
import argparse
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTION_RE = re.compile(r"^## +(.+?)\s*$", re.M)
STEP_RE = re.compile(r"^(\d+)\.\s+(.*?)(?=^\d+\.\s|\Z)", re.M | re.S)
EXPECT_RE = re.compile(r"→ \*Expect:?\*:?\s*(.*?)\s*$", re.S)


def parse_sections(body):
    sections = {}
    matches = list(SECTION_RE.finditer(body))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        sections[m.group(1)] = body[m.end():end].strip()
    return sections


def parse_steps(steps_text):
    steps = []
    for m in STEP_RE.finditer(steps_text):
        raw = m.group(2).strip()
        expect = None
        em = EXPECT_RE.search(raw)
        if em:
            expect = re.sub(r"\s+", " ", em.group(1)).strip()
            raw = raw[:em.start()].strip()
        action = re.sub(r"\s+", " ", raw)
        steps.append({
            "n": int(m.group(1)),
            "action": action,
            "expect": expect,
            "irreversible": "*Irreversible:*" in raw or "⚠️" in raw,
        })
    return steps


def load_recipe(path):
    with open(path) as f:
        text = f.read()
    end = text.find("\n---\n", 4)
    if not text.startswith("---\n") or end == -1:
        return None
    meta = yaml.safe_load(text[4:end])
    sections = parse_sections(text[end + 5:])
    return {
        "id": "%s/%s" % (meta.get("domain"), meta.get("name")),
        "dir": os.path.relpath(os.path.dirname(path), ROOT),
        "meta": meta,
        "sections": sections,
        "steps": parse_steps(sections.get("Steps", "")),
    }


def collect(paths):
    with open(os.path.join(ROOT, "domains.json")) as f:
        domains = json.load(f)
    files = []
    roots = paths or [os.path.join(ROOT, d) for d in sorted(domains)]
    for p in roots:
        if os.path.isdir(p):
            for dirpath, _, names in os.walk(p):
                files += [os.path.join(dirpath, n) for n in names if n.endswith(".md")]
        elif os.path.isfile(p):
            files.append(p)
    return [r for r in (load_recipe(f) for f in sorted(files)) if r]


def to_sft(recipe):
    meta, sections = recipe["meta"], recipe["sections"]
    task = meta["name"].replace("-", " ")
    prompt = "How do I %s? Give a concrete step-by-step plan, including what to expect after each step, what can go wrong, and how I know I'm done." % task
    lines = ["Goal: %s" % sections.get("Goal", "").strip(), "", "Plan:"]
    for s in recipe["steps"]:
        line = "%d. %s" % (s["n"], s["action"])
        if s["expect"]:
            line += " (expect: %s)" % s["expect"]
        lines.append(line)
    if sections.get("Failure modes & recovery"):
        lines += ["", "If something goes wrong:", sections["Failure modes & recovery"]]
    if sections.get("Verification"):
        lines += ["", "You are done when: %s" % sections["Verification"].strip()]
    out = {"id": recipe["id"], "prompt": prompt, "response": "\n".join(lines),
           "domain": meta["domain"], "risk": meta.get("risk"), "status": meta.get("status")}
    if meta.get("media"):
        out["media"] = [{"path": "%s/%s" % (recipe["dir"], m.get("path")),
                         "step": m.get("step"), "role": m.get("role"), "alt": m.get("alt")}
                        for m in meta["media"]]
    return out


def to_eval(recipe):
    meta, sections = recipe["meta"], recipe["sections"]
    spec = {
        "task_id": recipe["id"],
        "goal": sections.get("Goal", "").strip(),
        "preconditions": sections.get("Preconditions", "").strip(),
        "success_criteria": sections.get("Verification", "").strip(),
        "interface": meta.get("interface"),
        "risk": meta.get("risk"),
        "n_steps": len(recipe["steps"]),
        "irreversible_steps": [s["n"] for s in recipe["steps"] if s["irreversible"]],
        "status": meta.get("status"),
    }
    if meta.get("media"):
        spec["media"] = [{"path": "%s/%s" % (recipe["dir"], m.get("path")),
                          "step": m.get("step"), "role": m.get("role"), "alt": m.get("alt")}
                         for m in meta["media"]]
    if meta.get("domain") == "embodied":
        spec["sim"] = {
            "workspace": meta.get("workspace"),
            "objects": meta.get("objects"),
            "affordances": meta.get("affordances"),
            "safety": meta.get("safety"),
        }
    return spec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--format", choices=["json", "sft", "eval"], default="json")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()
    recipes = collect(args.paths)
    if args.format == "json":
        json.dump(recipes, sys.stdout, indent=2, ensure_ascii=False, default=str)
        print()
    else:
        conv = to_sft if args.format == "sft" else to_eval
        for r in recipes:
            print(json.dumps(conv(r), ensure_ascii=False, default=str))
    print("exported %d recipes as %s" % (len(recipes), args.format), file=sys.stderr)


if __name__ == "__main__":
    main()
