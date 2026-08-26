---
name: flag-a-suspicious-order
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

You mark a suspicious ecommerce order so it cannot be fulfilled accidentally while the team reviews fraud, payment, or policy risk.

## Preconditions

- Access to the ecommerce admin and permission to edit order notes, tags, or holds.
- A suspicious signal such as payment warning, customer complaint, address mismatch, or unusual order pattern.
- The order is not already shipped or delivered.

## Steps

1. **Open the exact order.** Match order number, customer name, email, amount, and creation time before taking action. → *Expect:* you are viewing the intended order record.
2. **Identify the suspicious signal.** Record the payment warning, unusual address, velocity issue, high-risk item, duplicate order, or customer report. → *Expect:* the reason for concern is specific and visible.
3. **Apply a visible fraud-review tag or hold.** Use the platform's hold, tag, or internal status such as `fraud-review` or `do-not-ship`. → *Expect:* the order list and order detail show the review marker.
4. **Pause fulfillment.** Cancel pending warehouse release, hold the fulfillment request, or notify the fulfillment team according to workflow. → *Expect:* the order cannot be picked, packed, shipped, or digitally delivered automatically.
5. **Add an internal note.** Include the risk signal, source, timestamp, and next reviewer or queue. → *Expect:* the note explains why the order is flagged without exposing unnecessary personal data.
6. **Notify the responsible reviewer.** Send the order link through the approved internal channel, not a public customer thread. → *Expect:* the fraud or operations owner has the order and expected next action.
7. **Confirm the flag persists.** Refresh the order and check any automation rules that might remove holds. → *Expect:* the order remains held after refresh and no fulfillment event is queued.

## Decision points

- Order has already shipped → flag for dispute monitoring and carrier intercept if possible instead of fulfillment hold.
- Signal is a customer typo rather than fraud → note it and route to support rather than fraud cancellation.
- Item is digital or instant-delivery → disable delivery first, then investigate.

## Failure modes & recovery

- **F1 Wrong order flagged:** detect mismatched customer or order number → remove the flag, document the correction, and flag the correct order.
- **F2 Fulfillment automation ignores tags:** detect warehouse release despite the marker → use a true fulfillment hold or cancel the fulfillment request.
- **F3 Customer sees internal accusation:** detect risky wording in customer-facing notes → move sensitive details to private notes and use neutral customer language.
- **F4 Flag never reviewed:** detect stale flagged orders → assign an owner and review deadline to avoid delayed legitimate shipments.

## Verification

The target order has a visible internal suspicious-order marker, an explanatory private note, and an active fulfillment hold or equivalent control preventing shipment or delivery.

## Variations

- Shopify: use order tags, payment capture hold, and fulfillment hold where available.
- WooCommerce: use order status plus private order notes and warehouse integration controls.
- Marketplace seller portal: use the platform's fraud-report or support escalation path if local holds are unavailable.

## Safety & privacy

Medium risk because a wrong flag can delay customer property and a missed flag can cause financial loss. Keep notes factual, private, and minimal; require human confirmation before canceling or accusing a customer.
