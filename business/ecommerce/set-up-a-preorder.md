---
name: set-up-a-preorder
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Set up a preorder product so customers can buy or reserve it with clear timing, payment, cancellation, and fulfillment expectations.

## Preconditions

- Admin access to product, inventory, payment, and preorder settings.
- Confirmed supplier production or arrival date with buffer.
- Policy for charging now versus later, cancellations, refunds, and delays.

## Steps

1. **Confirm supply and timeline.** Verify purchase order, production status, expected arrival, and quantity available for preorder. → *Expect:* a realistic ship window and preorder quantity cap.
2. **Choose payment timing.** [BRANCH: charge now | authorize later | deposit] Match the method to platform capability and local rules. → *Expect:* the customer payment flow is defined.
3. **Configure preorder inventory.** Set the product to accept preorders only up to the approved quantity and prevent oversell beyond the cap. → *Expect:* available preorder units match committed supply.
4. **Write transparent product messaging.** State preorder status, expected ship window, payment timing, cancellation policy, and what happens if delayed. → *Expect:* the product page clearly differs from in-stock items.
5. **Set checkout and order tags.** Add preorder labels to cart, checkout, confirmation email, and fulfillment workflow. → *Expect:* customers and operations can identify preorder orders.
6. **Test the full purchase path.** Place a test preorder and inspect payment, confirmation, inventory, taxes, and fulfillment hold. ⚠️ *Irreversible:* do not launch until customers cannot mistake the item for immediate shipment. → *Expect:* the test order is marked as preorder and not released for immediate fulfillment.
7. **Publish and monitor.** Track units sold, payment status, customer questions, supplier updates, and delay risk. → *Expect:* preorder sales remain within cap and customers receive updates.

## Decision points

- Supplier date is uncertain → collect email signups instead of taking payment.
- Legal rules restrict charging before shipment → use authorization, deposit, or invoice later.
- Preorder sells faster than supply → close sales at the cap and create a waitlist.

## Failure modes & recovery

- **F1 Oversold preorder:** detect units sold above committed supply → stop sales, allocate by order time, and notify affected customers.
- **F2 Delay after launch:** detect supplier date slipping → email customers with new date and refund/cancel options.
- **F3 Fulfillment ships early incorrectly:** detect warehouse picking preorder orders → add hold tags and exclude preorder orders from pick queues.
- **F4 Payment authorization expires:** detect failed capture before shipment → request updated payment or use charge-now terms if allowed.

## Verification

The live product clearly shows preorder terms, checkout and confirmation label the order as preorder, sales cannot exceed the quantity cap, and a test order is held for later fulfillment.

## Variations

- `kickstarter-style`: use crowdfunding terms rather than ordinary preorder promises.
- Limited editions: disclose allocation rules and do not sell more units than production allows.

## Safety & privacy

Medium risk because customers may pay before receiving goods. Disclose timing and cancellation terms plainly, cap inventory, and communicate delays quickly.
