---
name: money-starter
kind: pack
title: "Money Starter"
tagline: "Take control of your money — budget, bank, build credit, don't get burned."
recipes:
  - finance/create-a-simple-budget
  - finance/open-a-bank-account
  - finance/build-an-emergency-fund
  - finance/check-your-credit-report
  - finance/pay-a-bill-online
  - digital/set-up-autopay
  - finance/track-your-spending
  - finance/dispute-a-card-charge
  - finance/understand-your-credit-score
  - finance/set-up-direct-deposit
journeys:
  - journeys/get-out-of-debt
---
# 💰 Money Starter

*Take control of your money — budget, bank, build credit, don't get burned.*

## Why this pack

The foundational money moves for a first paycheck or a fresh start: budget, bank account, autopay, credit, and disputing a bad charge — plus the get-out-of-debt journey when the balance is already there.

## What's inside

10 recipes + 1 journey:

- [create a simple budget](../finance/create-a-simple-budget.md)
- [open a bank account](../finance/open-a-bank-account.md)
- [build an emergency fund](../finance/build-an-emergency-fund.md)
- [check your credit report](../finance/check-your-credit-report.md)
- [pay a bill online](../finance/pay-a-bill-online.md)
- [set up autopay](../digital/set-up-autopay.md)
- [track your spending](../finance/track-your-spending.md)
- [dispute a card charge](../finance/dispute-a-card-charge.md)
- [understand your credit score](../finance/understand-your-credit-score.md)
- [set up direct deposit](../finance/set-up-direct-deposit.md)
- 🗺️ [get out of debt](../journeys/get-out-of-debt.md) *(journey)*

## Install as an agent skill

```bash
python3 scripts/build_skills.py money-starter
```

That writes a self-contained `packs/skills/money-starter/SKILL.md` (each recipe's steps inlined). Drop it into your agent — Claude Code reads skills from `.claude/skills/` — or point your agent at the [howto MCP server](../mcp/) and ask it to consult this pack.

