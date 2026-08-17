---
name: digital-security-basics
kind: pack
title: "Digital Security Basics"
tagline: "Lock down your online life in an afternoon."
recipes:
  - digital/create-a-strong-password
  - accounts/enable-two-factor-authentication
  - accounts/set-up-a-password-manager
  - accounts/set-up-passkeys
  - accounts/review-account-security
  - digital/secure-your-home-wifi
  - digital/back-up-your-phone
  - digital/recover-a-hacked-account
  - accounts/save-your-2fa-recovery-codes
  - digital/use-incognito-mode-correctly
---
# 🔐 Digital Security Basics

*Lock down your online life in an afternoon.*

## Why this pack

The highest-leverage hour anyone can spend on security: strong unique passwords, 2FA and passkeys, a manager, backups, and a locked-down home network. An agent can walk a user through the whole hardening pass.

## What's inside

10 recipes:

- [create a strong password](../digital/create-a-strong-password.md)
- [enable two factor authentication](../accounts/enable-two-factor-authentication.md)
- [set up a password manager](../accounts/set-up-a-password-manager.md)
- [set up passkeys](../accounts/set-up-passkeys.md)
- [review account security](../accounts/review-account-security.md)
- [secure your home wifi](../digital/secure-your-home-wifi.md)
- [back up your phone](../digital/back-up-your-phone.md)
- [recover a hacked account](../digital/recover-a-hacked-account.md)
- [save your 2fa recovery codes](../accounts/save-your-2fa-recovery-codes.md)
- [use incognito mode correctly](../digital/use-incognito-mode-correctly.md)

## Install as an agent skill

```bash
python3 scripts/build_skills.py digital-security-basics
```

That writes a self-contained `packs/skills/digital-security-basics/SKILL.md` (each recipe's steps inlined). Drop it into your agent — Claude Code reads skills from `.claude/skills/` — or point your agent at the [howto MCP server](../mcp/) and ask it to consult this pack.

