---
name: robot-manipulation-primitives
kind: pack
title: "Robot Manipulation Primitives"
tagline: "The grasp-and-place fundamentals a household robot composes into everything else."
recipes:
  - embodied/crack-an-egg
  - embodied/pour-a-glass-of-water
  - embodied/use-kitchen-tongs
  - embodied/fold-a-tshirt
  - embodied/hammer-a-nail
  - embodied/use-a-screwdriver
  - embodied/open-a-door
  - embodied/use-an-elevator
  - embodied/load-a-dishwasher
  - embodied/hand-an-object-to-a-person
---
# 🦾 Robot Manipulation Primitives

*The grasp-and-place fundamentals a household robot composes into everything else.*

## Why this pack

Each recipe carries the embodied frontmatter (objects, affordances, workspace, safety) that compiles into a simulator task. This is the skill-DAG's root layer — the primitives higher tasks depend on.

## What's inside

10 recipes:

- [crack an egg](../embodied/kitchen/crack-an-egg.md)
- [pour a glass of water](../embodied/kitchen/pour-a-glass-of-water.md)
- [use kitchen tongs](../embodied/kitchen/use-kitchen-tongs.md)
- [fold a tshirt](../embodied/household/fold-a-tshirt.md)
- [hammer a nail](../embodied/household/hammer-a-nail.md)
- [use a screwdriver](../embodied/household/use-a-screwdriver.md)
- [open a door](../embodied/mobility/open-a-door.md)
- [use an elevator](../embodied/mobility/use-an-elevator.md)
- [load a dishwasher](../embodied/kitchen/load-a-dishwasher.md)
- [hand an object to a person](../embodied/care/hand-an-object-to-a-person.md)

## Install as an agent skill

```bash
python3 scripts/build_skills.py robot-manipulation-primitives
```

That writes a self-contained `packs/skills/robot-manipulation-primitives/SKILL.md` (each recipe's steps inlined). Drop it into your agent — Claude Code reads skills from `.claude/skills/` — or point your agent at the [howto MCP server](../mcp/) and ask it to consult this pack.

