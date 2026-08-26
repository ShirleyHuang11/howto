---
name: checkout-under-a-budget
domain: shopping
subdomain: buying
locale: [generic]
interface: web
difficulty: basic
est_time: 20min
risk: medium
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-08-25
---

## Goal

You complete checkout for a needed purchase only if the final charged amount stays at or below a fixed budget.

## Preconditions

- You know the item or list of items you need.
- You have a hard maximum budget including tax, shipping, fees, and tips.
- You have a valid delivery address and payment method.

## Steps

1. **Write the all-in budget.** Set the maximum total you will accept before opening checkout. → *Expect:* a single number that includes every charge.
2. **Add only needed items.** Put the required item or approved substitutes in the cart and remove impulse add-ons. → *Expect:* the cart contents match the shopping goal.
3. **Estimate unavoidable charges.** Enter delivery address or pickup location so taxes, shipping, handling, deposits, and service fees appear. → *Expect:* the cart shows a realistic subtotal and total.
4. **Apply eligible discounts.** Add legitimate coupons, account credits, gift cards, or free-shipping thresholds that do not require wasteful padding. → *Expect:* discounts appear as line items.
5. **Adjust the cart if over budget.** [BRANCH: remove nonessential items | choose pickup | switch to lower-cost substitute | wait for sale] → *Expect:* the revised total is at or below budget or checkout is paused.
6. **Review the final payment page.** Check item, quantity, shipping speed, delivery address, return policy, subscription status, and final total. → *Expect:* there are no surprise fees or unwanted recurring charges.
7. **Submit payment only under budget.** ⚠️ *Irreversible:* click place order only when the final charge is at or below the written budget. → *Expect:* order confirmation shows a charged amount within budget.

## Decision points

- Final total exceeds budget by any amount → revise the cart or do not buy.
- Free shipping requires unnecessary items → compare total with paid shipping before padding.
- Faster shipping pushes total over budget → choose slower shipping unless deadline requires it.
- A substitute is cheaper but lower quality → accept only if it still satisfies the original need.

## Failure modes & recovery

- **F1 Late fee reveal:** detect service or handling fees only at final checkout → recalculate and abandon if over budget.
- **F2 Quantity error:** detect duplicate items or wrong pack size → correct before payment.
- **F3 Auto-renew default:** detect subscription or membership selected → remove unless intentionally budgeted.
- **F4 Payment authorization mismatch:** detect a higher pending charge than confirmation → contact merchant or cancel promptly.

## Verification

The order confirmation shows the intended item set and a final charged amount less than or equal to the stated all-in budget, with no unwanted subscription or add-on.

## Variations

- `grocery-delivery`: include tip, substitutions, bag fees, and temporary authorization holds.
- `marketplace`: compare seller shipping charges separately before choosing.
- `pickup`: verify pickup location and deadline so savings do not create a missed pickup.

## Safety & privacy

Medium risk because payment is involved. Do not save cards on unfamiliar sites unless needed, and stop checkout if the final payment page exceeds the budget.
