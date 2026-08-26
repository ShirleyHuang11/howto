---
name: issue-store-credit
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Issue store credit to a customer for an approved reason and record it so the customer can spend it and the business can reconcile it.

## Preconditions

- Admin access to customer records, orders, gift cards, or store-credit tools.
- A verified customer identity and an approved credit amount.
- Policy guidance for refunds, returns, appeasements, and expiration.

## Steps

1. **Confirm the reason and amount.** Review the order, return, support ticket, or promotion that authorizes the credit. → *Expect:* a documented amount and reason code.
2. **Verify the customer account.** Match the email, order number, and shipping or billing details before adding value. → *Expect:* the correct customer profile is open.
3. **Choose the credit mechanism.** [BRANCH: account credit | gift card | coupon code] Use the option your platform tracks best for liabilities and redemption. → *Expect:* a credit type selected that the customer can actually use.
4. **Set restrictions and expiration.** Apply currency, product exclusions, expiration date, and one-time-use rules if policy requires them. → *Expect:* the credit terms match the approval.
5. **Create the credit.** ⚠️ *Irreversible:* confirm customer, amount, currency, and expiration before issuing because store value may be immediately spendable. → *Expect:* the platform generates a credit balance, gift card, or code.
6. **Notify the customer.** Send the amount, how to redeem it, expiration, and any restrictions without exposing internal notes. → *Expect:* the customer receives usable redemption instructions.
7. **Record the action.** Add an internal note with reason, approver, amount, and reference number. → *Expect:* support and finance can audit why the credit exists.

## Decision points

- Customer wants cash refund and policy requires cash → process refund instead of store credit.
- Credit is compensation for a service failure → avoid restrictive terms that worsen the experience.
- Amount is unusually large → get manager approval before issuing.

## Failure modes & recovery

- **F1 Wrong customer credited:** detect mismatch after issuance → freeze or void unused credit and reissue to the correct customer.
- **F2 Credit cannot be redeemed:** detect checkout rejection → check currency, customer binding, expiration, and product exclusions.
- **F3 Duplicate appeasement:** detect multiple agents issuing credit for the same issue → revoke duplicate unused credit and update the ticket.
- **F4 Accounting mismatch:** detect untracked gift card liability → export the credit record to finance and reconcile monthly.

## Verification

The correct customer has the approved store-credit amount available, the customer has redemption instructions, and the credit record includes amount, currency, reason, and reference ID.

## Variations

- `shopify`: gift cards may require specific plan permissions.
- Marketplace sellers: platform policy may prohibit private store credit outside the marketplace.

## Safety & privacy

Medium risk because store credit has monetary value. Verify identity, do not expose internal notes to the customer, and confirm amount and currency before issuance.
