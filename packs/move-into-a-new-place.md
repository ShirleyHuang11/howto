---
name: move-into-a-new-place
kind: pack
title: "Move Into a New Place"
tagline: "Everything for the first week in a new home — utilities to Wi-Fi to the breaker box."
recipes:
  - housing/set-up-utilities
  - housing/do-a-move-in-inspection
  - housing/move-house
  - housing/forward-your-mail
  - housing/set-up-broadband-in-a-new-home
  - digital/connect-to-wifi
  - digital/update-your-address-across-accounts
  - government/register-a-change-of-address
  - daily/reset-a-tripped-breaker
  - daily/find-a-water-leak
journeys:
  - journeys/buy-a-home
---
# 📦 Move Into a New Place

*Everything for the first week in a new home — utilities to Wi-Fi to the breaker box.*

## Why this pack

Moving is a burst of interdependent errands most people do rarely and forget between times. This kit covers the setup (utilities, broadband, address changes) and the "where's the breaker / why is there a leak" basics, plus the full home-buying journey.

## What's inside

10 recipes + 1 journey:

- [set up utilities](../housing/set-up-utilities.md)
- [do a move in inspection](../housing/do-a-move-in-inspection.md)
- [move house](../housing/move-house.md)
- [forward your mail](../housing/forward-your-mail.md)
- [set up broadband in a new home](../housing/set-up-broadband-in-a-new-home.md)
- [connect to wifi](../digital/connect-to-wifi.md)
- [update your address across accounts](../digital/update-your-address-across-accounts.md)
- [register a change of address](../government/register-a-change-of-address.md)
- [reset a tripped breaker](../daily/home/reset-a-tripped-breaker.md)
- [find a water leak](../daily/home/find-a-water-leak.md)
- 🗺️ [buy a home](../journeys/buy-a-home.md) *(journey)*

## Install as an agent skill

```bash
python3 scripts/build_skills.py move-into-a-new-place
```

That writes a self-contained `packs/skills/move-into-a-new-place/SKILL.md` (each recipe's steps inlined). Drop it into your agent — Claude Code reads skills from `.claude/skills/` — or point your agent at the [howto MCP server](../mcp/) and ask it to consult this pack.

