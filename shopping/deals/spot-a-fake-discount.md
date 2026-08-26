---
name: spot-a-fake-discount
domain: shopping
subdomain: deals
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You determine whether a promoted discount is genuine, then buy only if the final price is actually competitive.

## Preconditions

- You have the advertised deal page, product name, and sale deadline.
- You can compare historical prices or competitor prices.
- You have a maximum final price before evaluating the promotion.

## Steps

1. **Capture the advertised claim.** Note the sale price, claimed original price, percent off, code, deadline, and seller. → *Expect:* the discount claim is documented.
2. **Verify the exact product.** Check model number, size, condition, generation, warranty, and included accessories. → *Expect:* the sale item is not a downgraded variant.
3. **Check price history.** Use price trackers, archived pages, previous receipts, or retailer history to see recent normal prices. → *Expect:* you know whether the reference price was recently real.
4. **Compare live competitors.** Search the exact item at reputable sellers and include shipping, taxes, and required fees. → *Expect:* a market price range for the same item.
5. **Look for pressure tactics.** Treat countdown timers, inflated "was" prices, and limited stock claims as unproven until price data supports them. → *Expect:* urgency does not override the price evidence.
6. **Decide based on final value.** Buy only if the final delivered cost is below your cap and competitive with real market pricing. ⚠️ *Irreversible:* confirm the discount remains applied at checkout before paying. → *Expect:* either a confirmed order at a genuine deal price or no purchase.

## Decision points

- The "original" price is far above recent market price → ignore the percent-off claim and judge sale price alone.
- Competitors match the price without a sale → treat the discount as marketing, not urgency.
- The deal is for refurbished, open-box, or third-party stock → compare against equivalent condition only.
- The discount requires costly add-ons → include those costs before deciding.

## Failure modes & recovery

- **F1 Anchor-price inflation:** detect unrealistic list price → use recent street price instead.
- **F2 Variant mismatch:** detect lower memory, smaller size, or older model → compare only exact specs.
- **F3 Checkout bait-and-switch:** detect price changes at payment → abandon or contact support before ordering.
- **F4 Return-policy downgrade:** detect final-sale or restocking fees → buy only if the discount compensates for that risk.

## Verification

The final decision is backed by documented market comparison: either the order total is below the preset cap and below comparable market prices, or the fake discount is rejected with no payment made.

## Variations

- `marketplace`: distinguish platform seller from third-party seller before trusting warranty and returns.
- `fashion`: reference prices are often inflated; compare recent sold prices and similar retailers.
- `software`: lifetime-deal discounts need extra scrutiny of renewal, support, and cancellation terms.

## Safety & privacy

Medium risk because urgency can push bad purchases. Do not enter payment information on unfamiliar deal sites, and keep screenshots of terms if the price is unusually low.
