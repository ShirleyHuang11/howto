---
name: resolve-a-failed-payment
domain: digital
subdomain: transactions
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in, have-payment-method]
status: draft
last_verified: 2026-08-25
---

## Goal

You identify why a payment failed, fix the correct cause, and complete the transaction only once at the intended price.

## Preconditions

- You are using the merchant's official checkout or billing page.
- You have access to the payment method and issuer app or bank account.
- You know the expected total, currency, and deadline for the transaction.

## Steps

1. **Read the exact failure message.** Note whether the payment was declined, timed out, authentication failed, address mismatch occurred, or the merchant could not process it. → *Expect:* you have a specific error category rather than a vague "it failed."
2. **Check whether money moved.** Open the card, bank, or wallet account and look for pending authorizations. → *Expect:* you know whether there is no charge, a pending hold, or a posted payment.
3. **Verify checkout details.** Confirm card number, expiration, CVV, billing address, ZIP/postal code, name, currency, and total. → *Expect:* all payment fields match the issuer records.
4. **Fix the most likely cause.** [BRANCH: expired card, update card | insufficient funds, choose another method | fraud block, approve in issuer app | address mismatch, correct billing address | processor timeout, wait and retry once] → *Expect:* the error source is addressed before another attempt.
5. **Retry deliberately.** ⚠️ *Irreversible:* before clicking Pay again, confirm the cart, total, shipping, and quantity have not changed and no duplicate order exists. → *Expect:* the retry produces either an order confirmation or a new, documented error.
6. **Save the result.** If successful, save the order number; if failed, save the error and timestamp. → *Expect:* there is a record showing whether payment completed.
7. **Clear duplicate holds if needed.** If multiple pending authorizations appear without orders, contact the merchant and issuer with timestamps. → *Expect:* you know which holds will expire automatically or need release.

## Decision points

- A limited item or fare may change price → re-check total before every retry.
- Multiple failed attempts create fraud flags → stop after two or three attempts and contact issuer or merchant support.
- Payment failed for a subscription → update the billing method before the grace period ends.
- Authorization posted but no order exists → do not pay again until the merchant confirms whether an order was created.

## Failure modes & recovery

- **F1 Duplicate order:** detect two confirmations or two posted charges → contact merchant immediately to cancel one before shipment or service activation.
- **F2 Pending holds reduce available funds:** detect multiple authorizations → ask merchant to void unused authorizations or wait for issuer release.
- **F3 Fraud block persists:** detect issuer approval but merchant still declines → use another card or payment method after confirming no order exists.
- **F4 Price changes during retry:** detect higher total after failure → abandon or accept only if within your maximum price.

## Verification

Exactly one successful order, bill payment, or subscription payment exists at the intended total, or the payment remains unresolved with no posted charge and a documented support case or next action.

## Variations

- `mobile-wallet`: failed tokenized payments may require re-adding the card to the wallet.
- `international`: currency conversion, travel notices, or regional fraud rules can cause declines.
- `subscription`: failed renewal may require both card update and manual retry.

## Safety & privacy

Medium risk because repeated payment attempts can create duplicate charges or fraud locks. Verify the total and order status before retrying, use official support only, and never send full card details by chat or email.
