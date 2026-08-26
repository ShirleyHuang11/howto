---
name: set-up-a-shipping-rate
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You configure an ecommerce shipping rate that charges customers accurately and appears only for eligible products, destinations, and order conditions.

## Preconditions

- Shipping zones, carrier/service, package weights, dimensions, handling cost, and delivery promises.
- Product weights and shipping profiles already entered or ready to edit.
- Admin access to shipping settings and checkout preview.

## Steps

1. **Define the rate purpose.** Decide whether the rate is flat, free over threshold, weight-based, carrier-calculated, local delivery, or pickup. → *Expect:* one shipping rule with a clear use case.
2. **Choose eligible destinations.** Select countries, regions, postal codes, or local delivery radius where the rate should appear. → *Expect:* the rate will not show for unsupported locations.
3. **Assign products or profiles.** Link the rate to the correct product group, warehouse, vendor, or fulfillment location. → *Expect:* only eligible items can use the rate.
4. **Set price and conditions.** Enter shipping price, free-shipping threshold, weight/order-value limits, handling fee, and delivery estimate. → *Expect:* the rule reflects both customer promise and cost coverage.
5. **Check margin impact.** Test representative carts to compare charged shipping against expected carrier/fulfillment cost. → *Expect:* the rate does not routinely create unintended losses.
6. **Save the shipping rate.** ⚠️ *Irreversible:* before enabling, confirm destinations, products, price, conditions, and delivery promise because customers can select the rate at checkout. → *Expect:* the rate appears in shipping settings as active.
7. **Test checkout edge cases.** Try eligible/ineligible addresses, light/heavy carts, threshold just below/above, and mixed product carts. → *Expect:* the rate appears and disappears exactly as intended.
8. **Document the customer-facing promise.** Update shipping policy pages, product pages, or FAQ if the new rate changes timing or eligibility. → *Expect:* public wording matches checkout behavior.
9. **Monitor first orders.** Compare charged shipping, label cost, delivery time, and support contacts. → *Expect:* real orders validate the rate or reveal needed adjustments.

## Decision points

- Actual carrier cost varies widely → use carrier-calculated or zone-based rates instead of one flat rate.
- Heavy or oversized products exist → assign them to a separate profile with surcharges.
- Free shipping is desired → raise item margin or set a threshold that protects contribution margin.
- Some destinations are unreliable → exclude them or use tracked services only.

## Failure modes & recovery

- **F1 No rates at checkout:** detect customers cannot complete purchase → check product profile, address zone, weight, and fulfillment location.
- **F2 Rate appears for wrong region:** detect undercharged distant shipments → narrow zone or split rates immediately.
- **F3 Mixed-cart conflict:** detect products from different profiles blocking checkout → add compatible combined rates or separate fulfillment logic.
- **F4 Delivery promise too aggressive:** detect late shipments → adjust displayed estimate and carrier service.

## Verification

Checkout shows the new shipping rate only for intended products, destinations, and cart conditions, with a charge and delivery promise matching the configured rule.

## Variations

- Carrier-calculated rates: product weights, box dimensions, and origin address must be accurate.
- Local delivery: radius, cutoff time, and delivery days matter more than carrier service.
- Marketplace: shipping templates may require category-specific handling times.

## Safety & privacy

Medium risk because incorrect shipping rates can cost money or mislead customers. Confirm destination eligibility, customer charge, and delivery promise before activation.
