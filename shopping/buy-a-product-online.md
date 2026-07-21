---
name: buy-a-product-online
domain: shopping
locale: [generic]
interface: web
difficulty: basic
est_time: 20min
risk: medium
prerequisites: [accounts/create-an-online-account, have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

A specific product is ordered from an online store, paid for, and confirmed, with a receipt and delivery estimate in hand.

## Preconditions

- You know the product (or the need it must satisfy) and a budget.
- A payment method accepted online (card, PayPal-style wallet, or local equivalent).
- A delivery address.

## Steps

1. **Identify the exact product.** Search the store or a comparison engine; pin down model/size/variant. → *Expect:* a product page whose title, photos, and specs match what you intend to buy.
2. **Vet the listing.** Check seller rating, review count and recency, return policy, and total price including shipping and tax. [BRANCH: marketplace third-party seller | first-party store] Third-party sellers need closer scrutiny. → *Expect:* no red flags — price far below market, stock photos only, or no return policy are exits.
3. **Add to cart and open the cart.** Select variant (size/color) first. → *Expect:* cart shows the right item, variant, quantity, and unit price.
4. **Proceed to checkout.** Sign in or use guest checkout. → *Expect:* an address form or your stored address.
5. **Enter delivery address and choose shipping speed.** → *Expect:* an order summary showing item, address, shipping method, and a final total.
6. **Enter payment and review the final total.** ⚠️ *Irreversible:* the next click charges your payment method — confirm item, variant, quantity, address, and total now. → *Expect:* totals match step 2's expectation; no surprise fees.
7. **Place the order.** → *Expect:* an on-screen confirmation with an order number.
8. **Capture the receipt.** Save/screenshot the confirmation email with order number and delivery estimate. → *Expect:* the email arrives within minutes and matches the on-screen order.

## Decision points

- Total at checkout exceeds the listed price materially (fees, import duties) → abandon cart and re-evaluate step 2.
- Item goes out of stock at checkout → decide: wait, alternative seller, or alternative product.
- Payment declined → F1.

## Failure modes & recovery

- **F1 Payment declined:** verify card details and limits; try a second method; contact the bank if two methods fail (fraud block is common for first-time merchants).
- **F2 No confirmation email:** check spam; verify the order appears in the account's order history; if neither, check whether the charge posted before re-ordering (avoid double purchase).
- **F3 Order confirmed but seller cancels:** payment is auto-refunded — verify the refund posts within the stated window, then return to step 2.

## Verification

Order history shows the order as confirmed/processing with the correct item and address, a receipt email exists, and the pending charge equals the confirmed total.

## Variations

- `mobile-app`: wallet payments (Apple/Google Pay) skip card entry; the review-before-pay screen is the ⚠️ step.
- Cross-border purchases: import duty may be collected at delivery — factor it into step 2's total.

## Safety & privacy

Medium risk: money and address disclosure. Prefer payment methods with dispute rights (credit card, wallet) over direct bank transfer; a merchant that only accepts irreversible payment is a red flag.
