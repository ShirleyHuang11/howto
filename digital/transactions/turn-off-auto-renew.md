---
name: turn-off-auto-renew
domain: digital
subdomain: transactions
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You turn off automatic renewal while keeping the current paid term active until its expiration date.

## Preconditions

- You can access the subscription, domain, insurance, membership, or service account.
- You know whether you want to stop renewal only or cancel access immediately.
- You have checked any renewal deadline, grace period, and data-retention rule.

## Steps

1. **Open the active plan settings.** Sign in and navigate to billing, subscription, membership, domain, or renewal settings. → *Expect:* the current plan, renewal date, and auto-renew status are visible.
2. **Separate auto-renew from cancellation.** Read the labels carefully so you choose "turn off auto-renew" or "disable renewal," not "cancel now" unless that is intended. → *Expect:* the page indicates the current term remains active after renewal is disabled.
3. **Check what will happen at expiration.** Review whether service stops, enters a grace period, downgrades, or deletes data. → *Expect:* you know the exact expiration date and consequence.
4. **Disable auto-renew.** Toggle auto-renew off or choose Do not renew. ⚠️ *Irreversible:* for domains, insurance, or scarce plans, confirm you are willing to lose the asset or coverage after expiration. → *Expect:* the toggle changes to off or the renewal action moves to manual.
5. **Complete any confirmation prompt.** Confirm through password, multi-factor, survey, or final modal if required. → *Expect:* the account status says auto-renew is off, expires on a date, or renewal canceled.
6. **Save evidence.** Save the confirmation page or email showing the disabled renewal and expiration date. → *Expect:* proof is stored with the account name and date.
7. **Add a manual review reminder.** Put the expiration date and a decision deadline on your calendar. → *Expect:* you have a reminder before service, coverage, or ownership ends.

## Decision points

- You need continued access after the term → set a reminder to renew manually before expiration.
- The service only offers full cancellation → verify whether cancellation preserves access through the paid period before proceeding.
- Renewal price is negotiable → contact support or compare alternatives before disabling renewal.
- Asset is critical, such as a domain name → consider leaving auto-renew on with a spending alert instead.

## Failure modes & recovery

- **F1 Toggle silently re-enables:** detect auto-renew back on after saving → repeat the action, clear any required payment-profile prompt, and contact support with screenshots.
- **F2 Wrong product disabled:** detect another plan or domain was selected → re-enable the needed product immediately and disable the correct one.
- **F3 Access ended immediately:** detect service loss after selecting the wrong cancellation action → contact support quickly and request reinstatement to the paid-through date.
- **F4 Renewal still charges:** detect a charge after the off date → provide saved proof to the merchant and request a refund, then dispute if unresolved.

## Verification

The account shows auto-renew disabled for the correct product, the current term's expiration date is visible, and a confirmation record has been saved.

## Variations

- `domain-registrar`: disabling auto-renew can eventually release the domain; note redemption fees and deadlines.
- `app-store`: renewal toggles may live in Apple or Google subscription settings.
- `membership`: benefits may continue until the paid-through date even when renewal is off.

## Safety & privacy

Medium risk because disabling renewal can cause loss of service, coverage, or digital assets later. Confirm the product and expiration date, save proof, and avoid exposing account or payment details in shared screenshots.
