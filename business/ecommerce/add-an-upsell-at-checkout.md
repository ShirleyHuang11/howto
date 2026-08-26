---
name: add-an-upsell-at-checkout
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Add a relevant checkout upsell that increases order value without surprising the customer or degrading checkout completion.

## Preconditions

- Admin access to the store and checkout customization or upsell app.
- A low-friction add-on product with adequate stock and known margin.
- Baseline checkout conversion and average order value metrics.

## Steps

1. **Pick a product that fits the cart context.** Choose an accessory, refill, warranty, gift wrap, or expedited service that is useful for the items already in cart. → *Expect:* one upsell candidate with a clear reason to appear.
2. **Set eligibility rules.** Limit the offer by cart contents, order value, inventory, destination, and customer type. → *Expect:* the upsell appears only where it is relevant and fulfillable.
3. **Price the offer and check margin.** Include product cost, extra packaging, fees, and any shipping impact before setting a discount. → *Expect:* the upsell remains profitable after all incremental costs.
4. **Write concise offer text.** State the item, price, and benefit plainly; avoid countdown pressure or hidden recurring charges. → *Expect:* the customer can understand the offer without leaving checkout.
5. **Configure the checkout placement.** Add the upsell in the approved checkout extension, post-purchase page, or cart drawer. → *Expect:* the admin shows the offer enabled with the intended placement and rules.
6. **Test accepting and declining.** Use a test cart to accept, remove, and decline the upsell across desktop and mobile. ⚠️ *Irreversible:* do not publish until the customer can complete checkout either way. → *Expect:* totals, taxes, shipping, and order contents update correctly.
7. **Publish with a measurement window.** Set a review date and monitor attach rate, checkout conversion, refunds, and support contacts. → *Expect:* the upsell is live and performance can be compared against the baseline.

## Decision points

- Checkout conversion drops materially → disable or move the upsell to post-purchase.
- Add-on changes shipping class → show it earlier in cart or choose a lighter product.
- Upsell stock is low → hide the offer automatically below the reorder threshold.

## Failure modes & recovery

- **F1 Unexpected charge complaint:** detect customer support tickets about the upsell → confirm opt-in wording, refund affected customers if needed, and rewrite the offer.
- **F2 Discount stacking loss:** detect orders where coupon plus upsell discount erases margin → exclude the upsell from coupons or lower the discount.
- **F3 Mobile layout break:** detect blocked buttons or overlapping text → disable the placement and fix responsive styling before relaunch.
- **F4 Fulfillment miss:** detect orders shipping without the add-on → update pick lists and order tags so warehouse staff see the upsell item.

## Verification

In a test checkout, the eligible upsell appears, can be accepted or declined, updates the order total correctly, and a completed test order contains the exact upsell line item.

## Variations

- `shopify-plus`: checkout extensions provide deeper checkout placement controls.
- `post-purchase`: card authorization rules may limit which items can be added after payment.

## Safety & privacy

Medium risk because checkout changes affect payments. Make the upsell opt-in, disclose the exact price, and confirm the final order summary before enabling it for live buyers.
