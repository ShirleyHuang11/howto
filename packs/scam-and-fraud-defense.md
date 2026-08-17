---
name: scam-and-fraud-defense
kind: pack
title: "Scam & Fraud Defense"
tagline: "The \"don't get scammed\" kit — spot it, stop it, recover from it."
recipes:
  - digital/spot-a-phishing-email
  - digital/spot-a-scam-text-message
  - digital/spot-a-phone-scam
  - digital/spot-a-fake-website
  - digital/report-a-scam
  - digital/protect-an-elderly-relative-from-scams
  - digital/check-if-your-data-was-in-a-breach
  - finance/recognize-a-fake-invoice
  - finance/spot-a-fake-charity
  - finance/report-identity-theft
  - finance/what-to-do-if-your-card-is-stolen
  - accounts/enable-two-factor-authentication
journeys:
  - journeys/recover-from-identity-theft
---
# 🛡️ Scam & Fraud Defense

*The "don't get scammed" kit — spot it, stop it, recover from it.*

## Why this pack

Scams are the single most common way ordinary people lose money and identity, and agents are increasingly asked to help. This kit bundles the detection recipes (phishing, fake sites, scam calls/texts, deepfakes) with the response recipes (report, freeze, dispute) and the full recovery journey — so an agent can move from "is this a scam?" to "here's exactly what to do" without guessing.

## What's inside

12 recipes + 1 journey:

- [spot a phishing email](../digital/spot-a-phishing-email.md)
- [spot a scam text message](../digital/spot-a-scam-text-message.md)
- [spot a phone scam](../digital/spot-a-phone-scam.md)
- [spot a fake website](../digital/spot-a-fake-website.md)
- [report a scam](../digital/report-a-scam.md)
- [protect an elderly relative from scams](../digital/protect-an-elderly-relative-from-scams.md)
- [check if your data was in a breach](../digital/check-if-your-data-was-in-a-breach.md)
- [recognize a fake invoice](../finance/recognize-a-fake-invoice.md)
- [spot a fake charity](../finance/spot-a-fake-charity.md)
- [report identity theft](../finance/report-identity-theft.md)
- [what to do if your card is stolen](../finance/what-to-do-if-your-card-is-stolen.md)
- [enable two factor authentication](../accounts/enable-two-factor-authentication.md)
- 🗺️ [recover from identity theft](../journeys/recover-from-identity-theft.md) *(journey)*

## Install as an agent skill

```bash
python3 scripts/build_skills.py scam-and-fraud-defense
```

That writes a self-contained `packs/skills/scam-and-fraud-defense/SKILL.md` (each recipe's steps inlined). Drop it into your agent — Claude Code reads skills from `.claude/skills/` — or point your agent at the [howto MCP server](../mcp/) and ask it to consult this pack.

