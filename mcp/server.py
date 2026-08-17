#!/usr/bin/env python3
"""howto MCP server — give an agent the verified steps for everyday tasks.

Exposes the howto corpus over the Model Context Protocol so any MCP client (Claude Code,
Claude Desktop, Cursor, …) can, at inference time:
  - list_domains()            what kinds of tasks exist, with counts
  - search_howto(query, ...)  find the right recipe for a task
  - get_howto(id)             pull the full step-by-step, with expected observations,
                              irreversible-step warnings, failure recovery, and the
                              done-when check

The point: an agent stops guessing (and stops confidently skipping the step that matters) —
it reads the recipe first. Recipes are parsed with the repo's own parser (../scripts/export.py)
so what the agent sees can never drift from what the validator enforces.

Run (stdio):  python3 mcp/server.py
Requires:     pip install -r mcp/requirements.txt   (mcp, pyyaml)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(REPO, "scripts"))
import export  # noqa: E402  the repo's own recipe parser

try:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as _Server
except ImportError:
    try:  # mcp 2.x renamed the high-level server class
        from mcp.server import MCPServer as _Server
    except ImportError:
        sys.exit("Missing dependency. Run: pip install -r mcp/requirements.txt")

export.ROOT = REPO
mcp = _Server("howto")  # both classes accept a name and expose .tool() and .run()

# Load the corpus once at startup.
_RECIPES = export.collect(None)
_BY_ID = {r["id"]: r for r in _RECIPES}


def _domain_counts():
    counts = {}
    for r in _RECIPES:
        counts[r["meta"]["domain"]] = counts.get(r["meta"]["domain"], 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: -kv[1]))


def _score(r, terms):
    title = str(r["meta"].get("name", "")).replace("-", " ").lower()
    goal = r["sections"].get("Goal", "").lower()
    dom = (r["meta"].get("domain", "") + " " + str(r["meta"].get("subdomain") or "")).lower()
    steps = " ".join(s["action"] for s in r["steps"]).lower()
    s = 0
    for t in terms:
        if t in title:
            s += 5
        elif t in goal or t in dom:
            s += 3
        elif t in steps:
            s += 1
        else:
            return 0
    return s


@mcp.tool()
def list_domains() -> str:
    """List the task domains in the howto corpus with a recipe count for each.

    Use this first to see what kinds of everyday tasks have verified recipes."""
    counts = _domain_counts()
    lines = ["howto corpus: %d recipes across %d domains" % (len(_RECIPES), len(counts)), ""]
    for dom, n in counts.items():
        lines.append("  %-14s %4d" % (dom, n))
    return "\n".join(lines)


@mcp.tool()
def search_howto(query: str, domain: str = "", limit: int = 8) -> str:
    """Search the corpus for recipes matching a task description.

    Args:
        query: what you want to do, e.g. "change a flat tire" or "help someone choking".
        domain: optional filter to one domain (see list_domains).
        limit: max results (default 8).
    Returns a ranked list of "id — goal" lines; feed an id to get_howto for the full steps."""
    terms = [t for t in query.lower().split() if t]
    rows = _RECIPES
    if domain:
        rows = [r for r in rows if r["meta"].get("domain") == domain]
    scored = [(sc, r) for r in rows for sc in (_score(r, terms),) if sc > 0]
    scored.sort(key=lambda x: (-x[0], x[1]["id"]))
    if not scored:
        return "No recipes matched %r%s." % (query, " in domain " + domain if domain else "")
    out = ["%d match(es) for %r:" % (len(scored), query), ""]
    for _, r in scored[: max(1, limit)]:
        goal = " ".join(r["sections"].get("Goal", "").split())
        out.append("  %s\n      %s" % (r["id"], goal[:160]))
    return "\n".join(out)


@mcp.tool()
def get_howto(id: str) -> str:
    """Return the full recipe for a given id (e.g. "transit/ride-a-subway").

    The result includes each step with its expected observation, ⚠ markers on irreversible
    steps, decision points, failure recovery, and the checkable "done when" verification.
    Always read this before performing an unfamiliar real-world or irreversible task."""
    r = _BY_ID.get(id)
    if not r:
        return ("No recipe with id %r. Use search_howto to find one, or list_domains to browse."
                % id)
    m, sec = r["meta"], r["sections"]
    lines = ["# How to %s" % str(m.get("name", "")).replace("-", " "),
             "id: %s | domain: %s | difficulty: %s | est: %s | risk: %s"
             % (r["id"], m.get("domain"), m.get("difficulty"), m.get("est_time"), m.get("risk"))]
    if m.get("prerequisites"):
        lines.append("prerequisites: %s" % ", ".join(map(str, m["prerequisites"])))
    lines += ["", "## Goal", sec.get("Goal", "").strip()]
    if sec.get("Preconditions"):
        lines += ["", "## Preconditions", sec["Preconditions"].strip()]
    lines += ["", "## Steps"]
    for s in r["steps"]:
        line = "%d. %s%s" % (s["n"], "⚠ " if s["irreversible"] else "", s["action"])
        if s["expect"]:
            line += "  -> Expect: %s" % s["expect"]
        lines.append(line)
    for name in ("Decision points", "Failure modes & recovery", "Verification",
                 "Variations", "Safety & privacy"):
        if sec.get(name):
            lines += ["", "## %s" % name, sec[name].strip()]
    if m.get("domain") == "embodied":
        lines += ["", "## Robot scene",
                  "objects: %s" % m.get("objects"),
                  "affordances: %s" % m.get("affordances"),
                  "workspace: %s | safety: %s" % (m.get("workspace"), m.get("safety"))]
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
