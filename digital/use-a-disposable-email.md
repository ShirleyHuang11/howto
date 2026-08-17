---
name: use-a-disposable-email
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Use a disposable or relay email address for low-trust signups without losing access to accounts you may need later.

## Preconditions

- You know whether the account is temporary or important.
- You can access a disposable inbox or email relay service.

## Steps

1. **Classify the signup.** Decide whether the site is throwaway, low-trust, or important for purchases, identity, work, or recovery. → *Expect:* you know whether disposable email is appropriate.
2. **Choose address type.** [BRANCH: temporary inbox | forwarding relay] use temporary inboxes only for throwaway access; use relay aliases when future recovery matters. → *Expect:* the address lifespan matches the account.
3. **Create the address.** Generate or copy the disposable address and use it only for that specific site. → *Expect:* the site receives a unique address.
4. **Complete verification.** Open the disposable inbox or relay mailbox and use the confirmation code or link. → *Expect:* the account verifies successfully.
5. **Save recovery details when needed.** For relay aliases, store the alias and site name in your password manager. → *Expect:* you can identify and manage the alias later.
6. **Disable or discard.** When the signup is no longer needed, disable the relay alias or abandon the temporary inbox. → *Expect:* future spam to that address stops or becomes irrelevant.

## Decision points

- The account controls purchases, tickets, government services, banking, health, or work → do not use a temporary inbox.
- The site blocks disposable domains → use a reputable relay or provider alias.
- You may need password resets later → use a forwarding alias, not a disappearing mailbox.

## Failure modes & recovery

- **F1 Verification never arrives:** detect no code in the disposable inbox → recover by checking spam, trying a relay alias, or using a normal address.
- **F2 Account recovery lost:** detect the temporary inbox expired → recover through the site's support process if identity proof is available.
- **F3 Alias linked across sites:** detect the same disposable address reused → recover by creating separate aliases for future signups.

## Verification

The signup is verified, the address type matches the account importance, and any reusable alias is recorded in your password manager.

## Variations

- `mobile-app`: some apps require opening verification links on the same device.
- `shopping`: use relay aliases for receipts and returns.
- `forums`: temporary inboxes work only when losing the account would not matter.

## Safety & privacy

Medium risk because disposable email can lock you out of accounts. It reduces spam exposure but does not make payments, device fingerprints, IP addresses, or profile details anonymous.
