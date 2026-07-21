#!/usr/bin/env python3
"""Validate every recipe against the howto schema.

Checks frontmatter fields (mirroring schema/recipe.schema.json), filename/directory
consistency with domains.json, and required body sections. Exits non-zero and prints
one line per violation if any recipe fails.

Usage: python3 scripts/validate.py [paths...]   (default: all registered domains)
"""
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FIELDS = ["name", "domain", "locale", "interface", "difficulty",
                   "est_time", "risk", "prerequisites", "status", "last_verified"]
ENUMS = {
    "interface": {"physical", "web", "mobile-app", "phone-call", "mixed"},
    "difficulty": {"basic", "intermediate", "advanced"},
    "risk": {"low", "medium", "high"},
    "status": {"draft", "reviewed", "verified"},
}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
EST_TIME = re.compile(r"^[0-9]+(min|h|d)(-[0-9]+(min|h|d))?$")
DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
EMBODIED_FIELDS = ["subdomain", "objects", "affordances", "workspace", "safety"]
MEDIA_ROLES = {"action-demo", "expected-observation", "diagram", "warning", "overview"}
REQUIRED_SECTIONS = ["Goal", "Preconditions", "Steps", "Failure modes & recovery", "Verification"]


def load_domains():
    with open(os.path.join(ROOT, "domains.json")) as f:
        return json.load(f)


def parse_recipe(path):
    with open(path) as f:
        text = f.read()
    if not text.startswith("---\n"):
        return None, None, "missing frontmatter (file must start with ---)"
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, None, "unterminated frontmatter"
    try:
        meta = yaml.safe_load(text[4:end])
    except yaml.YAMLError as e:
        return None, None, "frontmatter YAML error: %s" % e
    return meta, text[end + 5:], None


def check_recipe(path, domains):
    errors = []
    rel = os.path.relpath(path, ROOT)
    meta, body, err = parse_recipe(path)
    if err:
        return [err]
    if not isinstance(meta, dict):
        return ["frontmatter is not a mapping"]

    for field in REQUIRED_FIELDS:
        if field not in meta:
            errors.append("missing field: %s" % field)
    for field, allowed in ENUMS.items():
        if field in meta and meta[field] not in allowed:
            errors.append("%s: %r not in %s" % (field, meta[field], sorted(allowed)))

    name = meta.get("name", "")
    if name and not KEBAB.match(str(name)):
        errors.append("name is not kebab-case: %r" % name)
    stem = os.path.splitext(os.path.basename(path))[0]
    if name and name != stem:
        errors.append("name %r != filename %r" % (name, stem))

    parts = rel.split(os.sep)
    file_domain = parts[0]
    domain = meta.get("domain")
    if domain and domain != file_domain:
        errors.append("domain %r != directory %r" % (domain, file_domain))
    if domain and domain not in domains:
        errors.append("domain %r not registered in domains.json" % domain)

    spec = domains.get(file_domain, {})
    subdomains = spec.get("subdomains")
    if subdomains:
        if len(parts) < 3:
            errors.append("domain %r requires a subdomain directory" % file_domain)
        else:
            file_sub = parts[1]
            if file_sub not in subdomains:
                errors.append("subdomain dir %r not registered in domains.json" % file_sub)
            if meta.get("subdomain") != file_sub:
                errors.append("subdomain %r != directory %r" % (meta.get("subdomain"), file_sub))

    if "est_time" in meta and not EST_TIME.match(str(meta["est_time"])):
        errors.append("est_time %r must look like 10min, 1h, 2h-4h" % meta["est_time"])
    lv = meta.get("last_verified")
    if lv is not None and not DATE.match(str(lv)):
        errors.append("last_verified %r must be YYYY-MM-DD" % lv)

    locale = meta.get("locale")
    if locale is not None:
        if not isinstance(locale, list) or not locale:
            errors.append("locale must be a non-empty list")
        else:
            for loc in locale:
                if not re.match(r"^[a-z0-9-]+$", str(loc)):
                    errors.append("locale entry not kebab-case: %r" % loc)
    prereqs = meta.get("prerequisites")
    if prereqs is not None and not isinstance(prereqs, list):
        errors.append("prerequisites must be a list")

    media = meta.get("media")
    if media is not None:
        if not isinstance(media, list):
            errors.append("media must be a list")
        else:
            n_steps = len(re.findall(r"^\d+\.\s", body, re.M))
            for i, m in enumerate(media):
                if not isinstance(m, dict):
                    errors.append("media[%d] must be a mapping" % i)
                    continue
                for field in ("path", "role", "alt"):
                    if field not in m:
                        errors.append("media[%d] missing field: %s" % (i, field))
                role = m.get("role")
                if role is not None and role not in MEDIA_ROLES:
                    errors.append("media[%d].role %r not in %s" % (i, role, sorted(MEDIA_ROLES)))
                mpath = m.get("path")
                if mpath:
                    if not str(mpath).startswith("assets/"):
                        errors.append("media[%d].path must start with assets/" % i)
                    elif not os.path.isfile(os.path.join(os.path.dirname(path), str(mpath))):
                        errors.append("media[%d].path not found: %s" % (i, mpath))
                step_ref = m.get("step")
                if step_ref is not None:
                    if not isinstance(step_ref, int) or step_ref < 1:
                        errors.append("media[%d].step must be a positive integer" % i)
                    elif n_steps and step_ref > n_steps:
                        errors.append("media[%d].step %d exceeds step count %d" % (i, step_ref, n_steps))

    if domain == "embodied":
        for field in EMBODIED_FIELDS:
            if field not in meta:
                errors.append("embodied recipe missing field: %s" % field)
        hp = (meta.get("safety") or {}).get("human_proximity") if isinstance(meta.get("safety"), dict) else None
        if hp is not None and hp not in {"continue", "slow", "pause"}:
            errors.append("safety.human_proximity %r not in continue|slow|pause" % hp)

    headings = set(re.findall(r"^## +(.+?)\s*$", body, re.M))
    for section in REQUIRED_SECTIONS:
        if section not in headings:
            errors.append("missing section: ## %s" % section)

    steps = re.search(r"^## +Steps\s*$(.*?)(?=^## |\Z)", body, re.M | re.S)
    if steps and "*Expect:*" not in steps.group(1) and "*Expect*" not in steps.group(1):
        errors.append("Steps section has no *Expect:* observations")

    return errors


def collect(paths, domains):
    files = []
    if paths:
        for p in paths:
            if os.path.isdir(p):
                for dirpath, _, names in os.walk(p):
                    files += [os.path.join(dirpath, n) for n in names if n.endswith(".md")]
            else:
                files.append(p)
    else:
        for domain in domains:
            d = os.path.join(ROOT, domain)
            if os.path.isdir(d):
                for dirpath, _, names in os.walk(d):
                    files += [os.path.join(dirpath, n) for n in names if n.endswith(".md")]
    return sorted(files)


def main():
    domains = load_domains()
    files = collect(sys.argv[1:], domains)
    if not files:
        print("no recipes found")
        return 0
    failed = 0
    for path in files:
        errors = check_recipe(path, domains)
        rel = os.path.relpath(path, ROOT)
        if errors:
            failed += 1
            for e in errors:
                print("FAIL %s: %s" % (rel, e))
        else:
            print("ok   %s" % rel)
    print("%d/%d recipes valid" % (len(files) - failed, len(files)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
