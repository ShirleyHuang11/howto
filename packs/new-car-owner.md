---
name: new-car-owner
kind: pack
title: "New Car Owner"
tagline: "Keep it running and handle the bad days — oil to flat to insurance claim."
recipes:
  - daily/refuel-a-car
  - daily/check-your-engine-oil
  - daily/check-tire-pressure
  - daily/change-a-flat-tire
  - daily/jump-start-a-car
  - daily/replace-a-windshield-wiper
  - daily/get-car-insurance-quotes
  - daily/file-a-car-insurance-claim
  - daily/renew-your-car-registration
  - daily/deal-with-a-car-that-wont-start
---
# 🚗 New Car Owner

*Keep it running and handle the bad days — oil to flat to insurance claim.*

## Why this pack

The maintenance and roadside basics a new driver needs, plus the paperwork (registration, insurance quotes and claims) that nobody teaches you.

## What's inside

10 recipes:

- [refuel a car](../daily/errands/refuel-a-car.md)
- [check your engine oil](../daily/errands/check-your-engine-oil.md)
- [check tire pressure](../daily/errands/check-tire-pressure.md)
- [change a flat tire](../daily/errands/change-a-flat-tire.md)
- [jump start a car](../daily/errands/jump-start-a-car.md)
- [replace a windshield wiper](../daily/errands/replace-a-windshield-wiper.md)
- [get car insurance quotes](../daily/errands/get-car-insurance-quotes.md)
- [file a car insurance claim](../daily/errands/file-a-car-insurance-claim.md)
- [renew your car registration](../daily/errands/renew-your-car-registration.md)
- [deal with a car that wont start](../daily/errands/deal-with-a-car-that-wont-start.md)

## Install as an agent skill

```bash
python3 scripts/build_skills.py new-car-owner
```

That writes a self-contained `packs/skills/new-car-owner/SKILL.md` (each recipe's steps inlined). Drop it into your agent — Claude Code reads skills from `.claude/skills/` — or point your agent at the [howto MCP server](../mcp/) and ask it to consult this pack.

