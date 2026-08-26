---
name: freeze-your-childs-online-accounts
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You temporarily lock down a child's online accounts after a safety, privacy, billing, or misuse concern while preserving evidence and access for the parent or guardian.

## Preconditions

- Legal authority as parent or guardian, or consent from the child where appropriate.
- Access to the child's device, family-management dashboard, or account recovery channels.
- A clear reason for the freeze, such as harassment, overspending, account compromise, or unsafe contact.

## Steps

1. **Identify the accounts and devices involved.** List social, gaming, school, messaging, app-store, and payment-linked accounts. → *Expect:* you have a complete target list.
2. **Preserve important evidence.** Save screenshots, usernames, transaction IDs, messages, or URLs before deleting or blocking. → *Expect:* evidence needed for support, school, or law enforcement is stored.
3. **Use family controls first where available.** Pause app access, screen time, purchases, chat, multiplayer, or location sharing through the official family dashboard. → *Expect:* the dashboard shows restrictions active.
4. **Change passwords or revoke sessions if compromised.** Use account recovery or parent controls to secure accounts. → *Expect:* unknown sessions are logged out and new login requires current credentials.
5. **Disable spending and subscriptions.** Remove saved payment methods, require approval, or cancel risky subscriptions. → *Expect:* new purchases require parent approval or fail.
6. **Report abuse or impersonation.** Use platform safety tools for harassment, grooming, threats, or impersonation. → *Expect:* report IDs or confirmation emails are recorded.
7. **Set a review time and restoration criteria.** Decide when and how access can be restored safely. → *Expect:* the freeze is temporary, documented, and tied to clear conditions.

## Decision points

- Immediate danger, threats, exploitation, or self-harm appears -> contact emergency services or local child-protection resources immediately.
- School account is involved -> coordinate with the school rather than changing passwords unilaterally.
- Child is old enough for shared decision-making -> explain the safety reason and agree on a restoration plan.

## Failure modes & recovery

- **F1 Parent lacks access:** account recovery goes to the child's email or phone -> use family organizer tools, platform minor-support channels, or device-level controls.
- **F2 Evidence is deleted:** messages vanish after blocking -> preserve screenshots and URLs before taking destructive actions.
- **F3 Child creates new accounts:** restrictions are bypassed -> adjust device app installs, app-store approvals, and router or DNS controls.
- **F4 Legitimate school access is blocked:** assignments or messages are missed -> restore school tools or coordinate with teachers.

## Verification

Family dashboards, app-store settings, or account pages show restrictions active, payments disabled or approval-gated, and report or evidence records are saved.

## Variations

- Apple Family Sharing and Screen Time: use Ask to Buy, app limits, communication safety, and content restrictions.
- Google Family Link: manage app installs, screen time, Chrome filters, and supervised account settings.
- Gaming platforms: restrict chat, purchases, multiplayer, friend requests, and user-generated content separately.

## Safety & privacy

Medium risk because this affects a child's privacy, safety, money, and access to school or social support. Preserve evidence before deleting, use the least restrictive control that solves the problem, and escalate urgent safety threats to qualified authorities.
