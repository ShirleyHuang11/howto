---
name: kitchen-starter
kind: pack
title: "Kitchen Starter"
tagline: "Cook anything — the ten fundamentals every other recipe builds on."
recipes:
  - daily/boil-water
  - daily/cook-rice
  - daily/fry-an-egg
  - daily/cook-pasta
  - daily/make-a-stir-fry
  - daily/roast-vegetables
  - daily/make-a-salad
  - daily/store-leftovers
  - daily/read-food-labels
  - daily/sharpen-a-kitchen-knife
---
# 🍳 Kitchen Starter

*Cook anything — the ten fundamentals every other recipe builds on.*

## Why this pack

The base skills a household robot or a first-time cook needs before any specific dish: heat, rice, eggs, pasta, a stir-fry, a salad, safe storage, and a sharp knife.

## What's inside

10 recipes:

- [boil water](../daily/food/boil-water.md)
- [cook rice](../daily/food/cook-rice.md)
- [fry an egg](../daily/food/fry-an-egg.md)
- [cook pasta](../daily/food/cook-pasta.md)
- [make a stir fry](../daily/food/make-a-stir-fry.md)
- [roast vegetables](../daily/food/roast-vegetables.md)
- [make a salad](../daily/food/make-a-salad.md)
- [store leftovers](../daily/food/store-leftovers.md)
- [read food labels](../daily/food/read-food-labels.md)
- [sharpen a kitchen knife](../daily/food/sharpen-a-kitchen-knife.md)

## Install as an agent skill

```bash
python3 scripts/build_skills.py kitchen-starter
```

That writes a self-contained `packs/skills/kitchen-starter/SKILL.md` (each recipe's steps inlined). Drop it into your agent — Claude Code reads skills from `.claude/skills/` — or point your agent at the [howto MCP server](../mcp/) and ask it to consult this pack.

