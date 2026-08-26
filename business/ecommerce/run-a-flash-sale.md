---
name: run-a-flash-sale
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: advanced
est_time: 1h-2h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You run a time-limited ecommerce flash sale with controlled inventory, tested checkout, and a clean shutdown at the advertised end time.

## Preconditions

- Sale objective, eligible SKUs, discount, inventory cap, start/end time, and traffic source.
- Confirmed margin floor and fulfillment capacity for expected order volume.
- Admin access to discounts, product scheduling, inventory, and analytics.

## Steps

1. **Define sale constraints.** Set start/end time, timezone, eligible products, inventory cap, customer limit, and revenue or sell-through target. → *Expect:* the sale has measurable boundaries.
2. **Check inventory and fulfillment capacity.** Confirm sellable units, warehouse staffing, packaging, carrier pickup, and backorder settings. → *Expect:* sale volume can be fulfilled within the promised window.
3. **Configure the discount.** Create automatic sale prices or coupon rules with eligibility, usage limits, stacking prevention, and exact schedule. → *Expect:* the discount exists but is bounded.
4. **Prepare customer-facing messaging.** Update banners, email, ads, product pages, and terms with the same start/end time and exclusions. → *Expect:* public messaging matches the backend rule.
5. **Load-test critical paths if traffic will spike.** Check home page, product page, cart, checkout, payment, and inventory decrement behavior. → *Expect:* the store can handle expected demand or the plan is scaled down.
6. **Test checkout before launch.** Use an eligible cart and ineligible cart to verify price, shipping, tax, stock limits, and discount stacking. → *Expect:* sale pricing appears only where intended.
7. **Launch the flash sale.** ⚠️ *Irreversible:* before activation or campaign send, confirm time, products, discount, inventory caps, links, and rollback plan because customers can buy immediately. → *Expect:* sale is live and traffic reaches the correct products.
8. **Monitor during the sale.** Watch orders, payment failures, site errors, inventory depletion, coupon abuse, and customer support volume. → *Expect:* problems are detected while there is still time to intervene.
9. **End the sale cleanly.** Disable discounts, remove banners, stop ads/emails, and verify product prices return to normal. → *Expect:* customers can no longer redeem the flash-sale offer after the end time.
10. **Review results.** Compare revenue, margin, sell-through, new customers, refunds, and operational issues against the target. → *Expect:* sale outcome is documented for the next campaign.

## Decision points

- Inventory sells faster than expected → end early only if terms allow or switch to sold-out messaging.
- Checkout errors increase → pause traffic sources and fix the blocking issue before continuing.
- Discount leaks before start → rotate code or tighten customer eligibility.
- Fulfillment capacity is exceeded → stop promotion and update delivery promises immediately.

## Failure modes & recovery

- **F1 Discount fails at launch:** detect eligible carts not receiving sale price → pause campaign traffic, fix rule, and communicate if necessary.
- **F2 Oversell:** detect inventory below zero or backorders disabled incorrectly → stop sale for affected SKUs and contact customers in order priority.
- **F3 Sale does not end:** detect discount still active after deadline → disable manually, audit late orders, and correct scheduling timezone.
- **F4 Site performance failure:** detect checkout timeouts or payment errors → reduce traffic, disable heavy scripts, and preserve carts where possible.
- **F5 Margin collapse:** detect stacked discounts or free-shipping combination below floor → disable stacking and review affected orders.

## Verification

The flash sale starts and ends at the intended times, eligible carts receive the correct discount during the window only, inventory stays within cap or is handled by sold-out logic, and post-sale prices return to normal.

## Variations

- Marketplace flash deal: platform approval, deal fees, and inventory commitments may apply.
- VIP early access: segment eligibility and leaked-code prevention are critical.
- Clearance flash sale: final-sale terms and return policy must be visible before checkout.

## Safety & privacy

Medium risk because high-volume discounts can create financial and customer-service problems quickly. Confirm margin, inventory caps, timing, and customer terms before launch, and avoid misleading scarcity claims.
