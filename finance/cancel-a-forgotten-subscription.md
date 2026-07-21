---
name: cancel-a-forgotten-subscription
domain: finance
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Find and cancel an unwanted recurring subscription, preserve proof, and watch the next billing cycle for mistakes.

## Preconditions

- Recent bank, credit card, payment app, or app store statements.
- Access to the email address or account used for the subscription.
- Login credentials or password reset access.
- Calendar or reminder app.
- Ability to contact the merchant if self-service cancellation fails.

## Steps

1. **Find the charge.** Search statements for the merchant name, processor name, app store, amount, and billing date. → *Expect:* you know who charged you and when it repeats.
2. **Trace the account.** Search email for receipts, welcome messages, renewal notices, and the charge amount. → *Expect:* you identify the login email or platform that manages the subscription.
3. **Choose the cancel path.** [BRANCH: merchant website | mobile app | app store subscription settings | payment provider] Use the path where the subscription was created. → *Expect:* you reach a subscription, billing, plan, or membership page.
4. **Review renewal terms.** Note next charge date, current plan, cancellation effective date, and refund policy. → *Expect:* you know whether access ends immediately or at period end.
5. **Cancel the subscription.** Follow prompts until the final confirmation button is complete. ⚠️ *Irreversible:* cancellation may remove promotional pricing or access, so confirm you no longer need the service. → *Expect:* the page says canceled, expires, or will not renew.
6. **Capture proof.** Screenshot the cancellation confirmation, confirmation number, email, or account page. → *Expect:* proof includes merchant, account, date, and cancellation status.
7. **Ask for a refund if appropriate.** If the renewal was accidental, unused, or hard to cancel, contact support politely with date and amount. → *Expect:* you receive a refund decision, ticket number, or chat transcript.
8. **Set a billing reminder.** Add a reminder for a few days after the next expected charge date. → *Expect:* you will check whether another charge posts.
9. **Watch the next cycle.** Review the statement after the reminder and dispute only if the merchant keeps billing after cancellation. → *Expect:* no new charge appears or you have evidence for a dispute.

## Decision points

- Charge came through Apple, Google, Roku, Amazon, PayPal, or a card network token → cancel through that platform first.
- Merchant offers pause instead of cancel → choose cancel if you want billing stopped.
- You cannot log in → use password reset, receipt links, or support with charge details.
- Free trial is still active → cancel before the trial deadline and verify no renewal.
- Merchant keeps billing → escalate to card dispute or payment-token block with proof.

## Failure modes & recovery

- **F1 Merchant name unclear:** detect a processor descriptor you do not recognize; recover by searching the descriptor and amount in email and statements.
- **F2 Cancel loop:** detect repeated offers without confirmation; recover by using chat, email, or phone support and asking for written confirmation.
- **F3 Wrong platform:** detect no subscription on the merchant site; recover by checking app store and payment provider subscriptions.
- **F4 Charge after cancellation:** detect a new charge after proof date; recover by requesting refund and disputing with the card issuer if needed.
- **F5 Refund denied:** detect a support denial; recover by deciding whether dispute rights, consumer agency complaint, or no further action fits the amount.

## Verification

The subscription page or support message states the subscription is canceled or will not renew, and the next statement shows no new recurring charge.

## Variations

- `app-store`: iOS and Android subscriptions are canceled in account subscription settings, not inside every app.
- `annual-plan`: refund rules may differ after renewal.
- `family-plan`: canceling may affect other users.
- `trial`: screenshot the cancellation before the trial converts.
- `card-replacement`: replacing a card may not stop tokenized recurring billing.

## Safety & privacy

Cancellation workflows may expose payment details and account history. Do not share full card numbers in support chat, and keep cancellation proof until at least one clean billing cycle passes.
