# 🎒 Packs — grab a whole kit

A **pack** is a curated, cross-domain kit for one real situation — the "don't get scammed" kit,
the "new apartment" kit, the "robot manipulation primitives" kit. It bundles the handful of
recipes (and sometimes a [journey](../journeys/)) you actually need, so you — or your agent —
don't have to assemble them from a 2,100-recipe index.

Every pack's leaves are **machine-checked to resolve** to real recipes by
[`scripts/validate_packs.py`](../scripts/validate_packs.py).

## The kits

| Pack | For | Size |
|---|---|---|
| [🛡️ Scam & Fraud Defense](scam-and-fraud-defense.md) | spot it, stop it, recover from it | 12 + 1 journey |
| [🚑 First-Aid & Emergencies](first-aid-emergencies.md) | when seconds count | 10 |
| [📦 Move Into a New Place](move-into-a-new-place.md) | the first week in a new home | 10 + 1 journey |
| [🍳 Kitchen Starter](kitchen-starter.md) | cook anything | 10 |
| [🦾 Robot Manipulation Primitives](robot-manipulation-primitives.md) | the household-robot base layer | 10 |
| [🔐 Digital Security Basics](digital-security-basics.md) | lock down your online life | 10 |
| [🚗 New Car Owner](new-car-owner.md) | keep it running, handle the bad days | 10 |
| [💰 Money Starter](money-starter.md) | budget, bank, build credit | 10 + 1 journey |

## Install a pack as an agent skill

Turn any pack into a self-contained skill your agent can load — every recipe's steps inlined,
with the *Expect* observations and ⚠ irreversible markers:

```bash
python3 scripts/build_skills.py scam-and-fraud-defense
# → packs/skills/scam-and-fraud-defense/SKILL.md
```

Drop the generated folder into a tool that reads skills (**Claude Code**: `.claude/skills/`), or
point your agent at the [howto MCP server](../mcp/) and say *"use the scam-defense pack."* Either
way your agent now follows verified steps instead of guessing.

Pre-built skills for all packs live under [`skills/`](skills/). Rebuild them all with
`python3 scripts/build_skills.py`.

## Add a pack

Copy an existing pack's frontmatter (`kind: pack`, `title`, `tagline`, `recipes:` list, optional
`journeys:`), list real recipe ids, and run `./scripts/validate.sh` — it fails if any id doesn't
resolve. Then regenerate the skill.
