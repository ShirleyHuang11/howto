---
name: create-a-strong-password
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Create a password that is long, unique to one account, and practical to store without reuse.

## Preconditions

- You are creating or changing a password on a legitimate account page.
- You can use a password manager, browser manager, or written emergency record.
- You are not sharing the password with another person.

## Steps

1. **Confirm the account page.** Check the URL and start from a bookmark or official app if possible. → *Expect:* the password is being entered on the real service.
2. **Choose a storage handoff.** [BRANCH: password manager | browser password manager | written temporary note] decide where the password will live before generating it. → *Expect:* there is a place to save the password immediately.
3. **Favor length over complexity tricks.** Use a random manager password or a passphrase of at least four unrelated words if you must type it manually. → *Expect:* the password is long enough to resist guessing without being impossible to enter.
4. **Make it unique.** Do not reuse a password pattern from email, banking, work, school, or shopping accounts. → *Expect:* this exact password belongs to one account only.
5. **Avoid personal clues.** Do not use birthdays, pet names, teams, addresses, lyrics, quotes, or keyboard paths. → *Expect:* someone who knows you could not guess the password.
6. **Save before submitting if allowed.** Store the password in the manager entry with the correct site name and username. → *Expect:* the manager can fill or reveal it before you lose the form.
7. **Submit and update the saved entry.** If the site forces symbols or length changes, update the manager entry to the exact accepted password. → *Expect:* the account accepts the password and the saved copy matches.
8. **Add account recovery protection.** Turn on multi-factor authentication where available and update recovery email or phone. → *Expect:* a stolen password alone is not enough to sign in.
9. **Remove temporary copies.** ⚠️ *Irreversible:* deleting the only copy can lock you out, so verify the saved entry first. → *Expect:* sticky notes, screenshots, and clipboard copies are gone after the manager entry works.

## Decision points

- The site limits password length severely → use the maximum length allowed and enable multi-factor authentication.
- You must remember it without a manager → use a long unrelated-word passphrase and store recovery information securely.
- The account is shared → create separate users or use a manager's sharing feature instead of texting the password.
- The manager suggests a password the site rejects → adjust inside the generator and save the accepted version.
- The account protects money or email → prioritize uniqueness and multi-factor authentication.

## Failure modes & recovery

- **F1 Password reuse:** detect the same or patterned password on multiple sites, recover by changing the most important accounts first.
- **F2 Lost new password:** detect the manager did not save it, recover immediately through the still-open session or password reset.
- **F3 Personal clue:** detect names, dates, or favorite words, recover by generating a random password or unrelated passphrase.
- **F4 Wrong saved URL:** detect manager filling on a lookalike site, recover by editing the entry URL to the official domain.
- **F5 Clipboard leak:** detect password copied on a shared device, recover by clearing clipboard or restarting the device.

## Verification

You can sign out and sign back in using the saved password, and that password is not used on any other account.

## Variations

- Work accounts: follow the organization's manager and rotation policy.
- Mobile-only accounts: use the phone's built-in password manager if it syncs to your recovery device.
- High-risk accounts: add a hardware security key if the service supports it.
- Kids or elders: set up recovery options before relying on memory.

## Safety & privacy

Medium risk because account takeover can expose money, messages, and identity. Never send passwords in chat, email, or screenshots, and never enter them after following a suspicious link.
