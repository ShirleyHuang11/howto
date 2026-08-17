---
name: get-a-price-adjustment-after-a-sale
domain: shopping
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Request a refund of the price difference when an item you bought drops in price within the retailer's adjustment window.

## Preconditions

- You have the receipt, order number, purchase date, and payment method.
- The same retailer currently sells the identical item for less.
- You can access the retailer's price adjustment policy.

## Steps

1. **Find the policy.** Search the retailer's official price adjustment or price protection terms. → *Expect:* you know the eligible window, exclusions, and channel.
2. **Confirm the exact item.** Compare SKU, model, size, color, quantity, condition, and seller. → *Expect:* the sale item is identical to what you bought.
3. **Check timing.** Count from purchase date or delivery date according to policy. → *Expect:* the request is inside or outside the allowed window.
4. **Capture proof.** Save the lower price page, ad, or shelf label with date and item details visible. → *Expect:* proof is available if the price changes again.
5. **Choose contact channel.** [BRANCH: online order | store receipt] use chat, order support, phone, or service desk as the policy directs. → *Expect:* you are contacting the team that can adjust the price.
6. **Request the adjustment.** Provide order number, item, purchase price, current lower price, and proof. → *Expect:* the agent can calculate the difference.
7. **Review exclusions and amount.** Check whether clearance, coupon, membership price, third-party seller, bundle, tax, shipping, or price-match rules limit the refund. → *Expect:* approval or denial reason is specific.
8. **Accept the credit.** Confirm refund amount and destination before the agent submits it. ⚠️ *Irreversible:* accepting a store-credit adjustment may prevent a cash refund later, so confirm refund method first. → *Expect:* confirmation shows the adjustment amount and timing.
9. **Watch the payment method.** Check account activity after the stated processing period. → *Expect:* the credit posts or you have a case number for follow-up.

## Decision points

- The lower price is from a competitor → use price-match rules, not same-retailer adjustment rules.
- The window expired → ask for a goodwill exception or consider return-and-rebuy only if policy and condition allow.
- The item was bought with a coupon → compare net price after discounts, not sticker price.
- The refund is issued as store credit → decide whether that is acceptable before accepting.

## Failure modes & recovery

- **F1 Price changes before review:** detect page no longer showing sale, recover with dated screenshot if policy accepts it.
- **F2 SKU mismatch:** detect different model or bundle, recover by finding the exact item or dropping the request.
- **F3 Wrong support queue:** detect agent says they cannot adjust, recover by contacting order support or service desk.
- **F4 Refund missing:** detect no credit after processing window, recover by following up with case number.
- **F5 Restocking risk:** detect return-and-rebuy idea with fees, recover by calculating fees before returning.

## Verification

The order, receipt, or payment account shows a posted credit for the approved price difference or a written denial explaining the policy reason.

## Variations

- Credit-card price protection: some cards require a separate claim, receipt, and dated proof.
- In-store purchase: bring receipt and live sale proof to customer service.
- Online marketplace: price adjustments may be excluded for third-party sellers.

## Safety & privacy

Share only order number and necessary receipt details. Do not send full card numbers or account passwords to support.
