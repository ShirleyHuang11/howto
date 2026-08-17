---
name: first-aid-emergencies
kind: pack
title: "First-Aid & Emergencies"
tagline: "When seconds count — the recipes you hope you never need."
recipes:
  - healthcare/call-emergency-services
  - healthcare/do-hands-only-cpr
  - healthcare/help-someone-who-is-choking
  - healthcare/help-a-choking-infant
  - healthcare/stop-severe-bleeding
  - healthcare/recognize-a-heart-attack
  - healthcare/recognize-stroke-signs
  - healthcare/use-an-epipen
  - healthcare/put-someone-in-the-recovery-position
  - healthcare/treat-a-burn
---
# 🚑 First-Aid & Emergencies

*When seconds count — the recipes you hope you never need.*

## Why this pack

The highest-stakes recipes in the corpus, each with red-flag thresholds and a clear "call emergency services" trigger. An agent (or a person) reaching for these needs the verified steps immediately, not a paragraph of hedging.

## What's inside

10 recipes:

- [call emergency services](../healthcare/call-emergency-services.md)
- [do hands only cpr](../healthcare/do-hands-only-cpr.md)
- [help someone who is choking](../healthcare/help-someone-who-is-choking.md)
- [help a choking infant](../healthcare/help-a-choking-infant.md)
- [stop severe bleeding](../healthcare/stop-severe-bleeding.md)
- [recognize a heart attack](../healthcare/recognize-a-heart-attack.md)
- [recognize stroke signs](../healthcare/recognize-stroke-signs.md)
- [use an epipen](../healthcare/use-an-epipen.md)
- [put someone in the recovery position](../healthcare/put-someone-in-the-recovery-position.md)
- [treat a burn](../healthcare/treat-a-burn.md)

## Install as an agent skill

```bash
python3 scripts/build_skills.py first-aid-emergencies
```

That writes a self-contained `packs/skills/first-aid-emergencies/SKILL.md` (each recipe's steps inlined). Drop it into your agent — Claude Code reads skills from `.claude/skills/` — or point your agent at the [howto MCP server](../mcp/) and ask it to consult this pack.

