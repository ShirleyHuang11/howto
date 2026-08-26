---
name: transfer-account-ownership
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: advanced
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You transfer ownership of an account, workspace, subscription, domain, page, or asset to the correct person without leaving old access or billing behind.

## Preconditions

- You are the current owner or have authority to request the transfer.
- The new owner has an active account and can accept ownership.
- You understand what ownership controls: billing, data, users, legal responsibility, domains, or public content.

## Steps

1. **Identify the ownership object.** Confirm whether you are transferring an entire account, organization, workspace, project, domain, subscription, page, or asset. → *Expect:* the exact item and current owner are known.
2. **Check provider rules.** Read transfer, admin, billing, and data-retention rules for the service. → *Expect:* you know whether transfer is self-service, support-assisted, or prohibited.
3. **Prepare the new owner.** Ask them to create or verify their account, enable 2FA, and confirm the correct email address or user ID. → *Expect:* the recipient is ready to accept securely.
4. **Back up critical records.** Export invoices, ownership proof, access lists, DNS records, content, or project data as appropriate. → *Expect:* records exist outside the account before control changes.
5. **Initiate the transfer.** Use Transfer ownership, Make owner, Change primary admin, Registrant transfer, or support request. ⚠️ *Irreversible:* confirm the recipient identity and what control you will lose before submitting. → *Expect:* the service sends an acceptance request or immediately changes the owner.
6. **Have the new owner accept.** Ask them to accept from their own official account or email, not a forwarded link. → *Expect:* the account shows the new owner as owner, primary admin, registrant, or billing owner.
7. **Update billing and legal details.** Move payment methods, tax information, business address, domain registrant details, and invoices as required. → *Expect:* future charges and legal notices go to the new owner.
8. **Remove old access.** Downgrade or remove previous owners, employees, contractors, app passwords, API keys, and recovery methods that should not remain. → *Expect:* only authorized people retain access.

## Decision points

- Transfer affects a domain name → confirm registrar locks, authorization codes, DNS continuity, and ICANN contact requirements before starting.
- Transfer is part of employment offboarding → coordinate with HR, legal, and IT so ownership does not move to a personal account.
- The new owner is outside the organization → check data-sharing and contract restrictions first.

## Failure modes & recovery

- **F1 Recipient cannot accept:** detect expired invite or wrong email → cancel and reissue to the correct verified account.
- **F2 Billing remains with old owner:** detect charges after transfer → update billing owner and payment method, then request refund if needed.
- **F3 Access lost too early:** detect old owner cannot complete required cleanup → ask new owner to grant temporary admin access or contact support.
- **F4 Transfer blocked:** detect policy, unpaid invoice, lock, or verification hold → resolve the blocker before retrying.

## Verification

The service shows the intended person or entity as owner, billing and legal details point to them, and old owners or unauthorized users no longer have privileged access.

## Variations

- Domain registrars: ownership transfer may require unlocking the domain, obtaining an authorization code, and waiting through transfer periods.
- SaaS workspaces: owner transfer may be instant if both users are in the same organization.
- Social pages: page ownership and ad-account ownership may be separate and both need review.

## Safety & privacy

Medium risk because ownership transfer can move control of money, legal records, public assets, and private data. Confirm the recipient identity through a separate channel before approving any irreversible transfer.
