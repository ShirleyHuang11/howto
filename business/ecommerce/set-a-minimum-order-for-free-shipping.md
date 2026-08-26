---
name: set-a-minimum-order-for-free-shipping
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You set a free-shipping threshold that encourages larger carts while protecting margin, then verify checkout applies it correctly.

## Preconditions

- Access to shipping settings in the ecommerce platform.
- Recent average order value, gross margin, shipping cost, and product weight data.
- Authority to change shipping promotions.

## Steps

1. **Calculate the current economics.** Record average order value, average gross margin, average shipping cost, and contribution margin by order size. → *Expect:* a minimum order value that can absorb shipping without wiping out profit.
2. **Choose the threshold.** Set it slightly above average order value or at a bundle-friendly amount that customers can reasonably reach. → *Expect:* a target threshold with a margin rationale.
3. **Define eligible regions and products.** Exclude oversized, hazardous, wholesale, subscription, or international orders if they do not fit the economics. → *Expect:* a clear eligibility list.
4. **Create the shipping rule.** Add a free-shipping rate with minimum subtotal, eligible zones, and product exclusions as supported by the platform. → *Expect:* the shipping settings show free shipping only above the threshold.
5. **Add cart messaging.** Show progress such as "Add X more for free shipping" using subtotal rules that match checkout. → *Expect:* the cart message updates as items are added or removed.
6. **Test below, at, and above the threshold.** Use representative carts and addresses in eligible and excluded zones. → *Expect:* free shipping appears only when the subtotal and destination qualify.
7. **Publish the threshold.** ⚠️ *Irreversible:* once advertised, customers may rely on it, so confirm exclusions and dates before promoting. → *Expect:* product, cart, and policy pages state the same free-shipping terms.
8. **Monitor order mix.** Track average order value, shipping cost as a percent of revenue, conversion, and support tickets. → *Expect:* the threshold improves cart value without excessive shipping subsidy.

## Decision points

- Shipping cost varies sharply by region → create region-specific thresholds or exclude high-cost zones.
- Products are heavy or bulky → use weight-based exceptions instead of a storewide rule.
- Average order value is far below profitable threshold → test bundles before adding a high free-shipping minimum.

## Failure modes & recovery

- **F1 Free shipping applies too broadly:** detect oversized or international orders receiving free shipping → pause the rule and add exclusions or zones.
- **F2 Cart message disagrees with checkout:** detect customer complaints or failed tests → align the message logic with subtotal, discounts, and tax handling.
- **F3 Threshold reduces conversion:** detect fewer orders and higher abandonment → lower the threshold, add cheaper paid shipping, or make the offer seasonal.
- **F4 Margin erosion:** detect shipping subsidy above the planned cap → raise the threshold or limit eligible SKUs.

## Verification

Checkout grants free shipping for an eligible cart at or above the threshold and rejects it for below-threshold or excluded carts, with matching terms visible in cart and shipping policy text.

## Variations

- Shopify: configure shipping rates by market and profile; check whether discounts affect subtotal eligibility.
- WooCommerce: confirm coupon interactions and shipping-class exclusions.
- Marketplace stores: free-shipping thresholds may be controlled by the marketplace campaign tool.

## Safety & privacy

Medium risk because shipping promotions affect margins and customer purchase decisions. Confirm exclusions before publishing and avoid hiding mandatory fees until late checkout.
