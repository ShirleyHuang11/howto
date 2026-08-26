---
name: cancel-a-free-trial-before-it-charges
domain: shopping
subdomain: buying
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

You cancel a free trial before paid billing begins and preserve proof that no future charge should occur.

## Preconditions

- You can log into the account that started the trial.
- You know the trial start date, billing date, account email, and payment method used.
- You are willing to lose trial access if cancellation ends benefits immediately.

## Steps

1. **Find the billing page.** Open account settings, subscription, plan, or app-store subscription management. → *Expect:* the active trial and next billing date are visible.
2. **Record current terms.** Note plan name, trial end date, price after trial, and whether canceling ends access now or at period end. → *Expect:* you know the consequence of canceling.
3. **Start cancellation.** Click cancel, manage plan, or turn off renewal, following all required confirmation screens. → *Expect:* the service presents a cancellation path or retention offer.
4. **Decline unwanted retention offers.** Ignore discounts, pauses, or upgrades unless you intentionally choose to continue. → *Expect:* the cancellation flow reaches a final confirmation screen.
5. **Confirm cancellation.** ⚠️ *Irreversible:* if cancellation ends access immediately, confirm you no longer need the trial before finalizing. → *Expect:* the account shows canceled, expires on a date, or auto-renew off.
6. **Save proof.** Download or screenshot the confirmation, email, plan status, and cancellation timestamp. → *Expect:* you have evidence if a charge later appears.
7. **Check the payment method.** Verify no pending or posted charge appears after the trial end date. → *Expect:* the card or wallet has no unexpected paid subscription charge.

## Decision points

- Canceling ends access immediately → wait until just before the deadline only if you set a reliable reminder.
- Subscription was started through an app store → cancel in that app store, not only on the merchant website.
- You want the service at a lower price → accept a retention offer only if the new billing terms are clear.
- Cancellation button is missing → use support chat or email before the billing deadline.

## Failure modes & recovery

- **F1 Wrong billing platform:** detect website says billing is managed elsewhere → cancel through app store, phone carrier, or payment provider.
- **F2 Incomplete cancellation:** detect status still says active or renews → repeat until auto-renew is off and save proof.
- **F3 Late charge:** detect a posted charge after cancellation → request refund with confirmation proof.
- **F4 Multiple accounts:** detect another email still has a trial → search inboxes and payment statements for merchant name.

## Verification

The subscription status shows canceled or auto-renew off before the paid billing date, confirmation proof is saved, and no paid charge posts after the trial deadline.

## Variations

- `ios`: cancel under Apple ID subscriptions.
- `android`: cancel under Google Play subscriptions.
- `b2b-software`: some trials require admin-owner access or support tickets to cancel.

## Safety & privacy

Medium risk because missed cancellation causes charges. Do not rely only on deleting the app, and keep cancellation proof until after the first expected billing date passes.
