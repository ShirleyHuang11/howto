---
name: merge-duplicate-accounts
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You combine or reconcile duplicate accounts without losing purchases, records, subscriptions, messages, or identity verification.

## Preconditions

- You can sign in to both accounts or can recover access to them.
- You know which account should remain primary.
- You have reviewed important data, billing, subscriptions, and login methods on both accounts.

## Steps

1. **Confirm the accounts are truly duplicates.** Compare email addresses, usernames, customer IDs, purchase history, identity records, and organization memberships. → *Expect:* both accounts belong to the same person or entity and should be reconciled.
2. **Choose the primary account.** Prefer the account with verified identity, active subscriptions, most complete history, or organization access. → *Expect:* one account is designated as the account to keep.
3. **Back up or export important data.** Download receipts, messages, files, certificates, contacts, or profile data from both accounts where possible. → *Expect:* important records are saved before any merge or closure.
4. **Check whether self-service merge exists.** Look for Merge accounts, Link accounts, Transfer purchases, or Combine profiles in settings or help. → *Expect:* you know whether the provider supports merging and what data transfers.
5. **Resolve conflicting login methods.** Remove duplicate social sign-ins, update email addresses, and confirm recovery methods on the primary account. → *Expect:* the primary account has a clean, unique login path.
6. **Submit the merge or support request.** Provide both account identifiers and specify which account should remain. ⚠️ *Irreversible:* confirm the retained account and data-loss warnings before approving a merge or deletion. → *Expect:* the provider confirms the merge, opens a case, or explains unsupported items.
7. **Verify transferred data.** Check subscriptions, purchases, balances, profile details, saved addresses, and access rights in the primary account. → *Expect:* expected data appears in the primary account.
8. **Close or secure the duplicate.** If merging is impossible, remove payment methods and sensitive data from the duplicate, then close it only after records are saved. → *Expect:* the duplicate no longer creates billing or identity risk.

## Decision points

- Provider does not support merging → pick one primary account and manually transfer what the provider allows.
- Duplicate account has purchases or legal records → do not close it until support confirms whether those records transfer.
- Accounts belong to different people → do not merge; transfer ownership or share access instead.

## Failure modes & recovery

- **F1 Data not transferable:** detect missing purchases, credits, or messages → keep the duplicate open or request manual support escalation.
- **F2 Wrong account retained:** detect the empty account became primary → contact support immediately with case number and exported records.
- **F3 Email conflict:** detect "email already in use" → change the duplicate email to a temporary address you control before assigning it to the primary account.
- **F4 Subscription billed twice:** detect duplicate charges → cancel one subscription and request a refund with account IDs.

## Verification

The primary account contains the expected records and access, only one active subscription or billing path remains, and the duplicate is closed, emptied, or clearly documented as retained.

## Variations

- Financial, medical, and government accounts: duplicates may require support or identity verification and may not be mergeable.
- Shopping accounts: purchase history and store credits often cannot be transferred without support.
- Workspaces: duplicate personal and organization accounts may need an admin to migrate ownership or membership.

## Safety & privacy

Medium risk because merging can affect money, records, identity, and access. Export important data first and explicitly confirm which account will remain before approving any irreversible merge or closure.
