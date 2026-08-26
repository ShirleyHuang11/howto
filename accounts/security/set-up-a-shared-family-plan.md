---
name: set-up-a-shared-family-plan
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You set up a shared family plan so members can use shared subscriptions or purchases while keeping private accounts, payment control, and child safeguards separate.

## Preconditions

- The organizer's account is active and secured.
- Each invited member has or can create their own account.
- You know the plan's cost, member limit, region rules, and purchase-sharing behavior.

## Steps

1. **Review the plan rules before inviting anyone.** Check member limits, household requirements, billing date, shared storage, purchase sharing, and cancellation effects. → *Expect:* you know what will be shared and what will remain private.
2. **Secure the organizer account.** Confirm a strong password, recovery methods, and two-factor authentication. → *Expect:* the account that controls billing cannot be easily taken over.
3. **Choose member roles.** Decide who is organizer, adult member, child account, or managed profile. → *Expect:* each person has the least-privileged role that fits.
4. **Configure billing and purchase approvals.** Add the intended payment method and enable ask-to-buy or spending approval for children where available. → *Expect:* charges route through the chosen payment method and approvals are active if needed.
5. **Send invitations through the official interface.** Invite members by their account email or phone number. → *Expect:* each invitation appears as pending or accepted in family settings.
6. **Set privacy and sharing options.** Turn on only the services you mean to share, such as storage or media subscriptions, and leave sensitive data private. → *Expect:* sharing settings reflect the household's consent.
7. **Confirm member access.** Ask each person to accept and verify they can use the shared benefit. → *Expect:* the plan shows all intended members as active and entitled.

## Decision points

- A member is a child -> create or use a child account with age-appropriate parental controls instead of sharing an adult login.
- Members live in different countries or app-store regions -> the plan may reject the invitation or limit sharing.
- You only need one shared subscription -> compare a family plan with separate accounts before changing billing.

## Failure modes & recovery

- **F1 Invitation fails:** member cannot join -> verify account email, country/region, age, and existing family membership.
- **F2 Unwanted purchases appear:** family payment is charged unexpectedly -> enable purchase approvals, remove purchase sharing, or remove the member.
- **F3 Private data is shared unintentionally:** photos, location, or calendars appear -> turn off that specific sharing feature and review consent.
- **F4 Organizer loses access:** billing and controls become stuck -> recover the organizer account before making membership changes.

## Verification

Family settings show the intended organizer and members, the shared subscription or storage is active for members, and purchase or child approval settings match the plan.

## Variations

- Apple Family Sharing: supports purchase sharing, subscriptions, iCloud storage, Ask to Buy, and location sharing as separate toggles.
- Google Families: supports Play purchases, YouTube or Google One plans, and supervised child accounts through Family Link.
- Streaming services: household rules and profile privacy vary by provider.

## Safety & privacy

Medium risk because family plans affect billing, child controls, purchases, and location or media sharing. Do not share one password among family members; use individual accounts and explicit consent for location or content sharing.
