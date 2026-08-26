---
name: fulfill-a-dropship-order
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You send a customer order to a dropship supplier, confirm fulfillment details, and update the customer-facing order with accurate tracking.

## Preconditions

- Paid customer order with validated shipping address and fraud status.
- Supplier portal or integration access and current supplier stock/cost.
- Store policy for substitutions, delays, and customer communication.

## Steps

1. **Review the customer order.** Confirm payment captured or authorized, fraud status acceptable, SKU, quantity, shipping method, and customer address. → *Expect:* the order is ready to fulfill.
2. **Confirm supplier availability.** Check supplier stock, cost, handling time, shipping options, and any variant mapping. → *Expect:* supplier can ship the exact item within the promised window.
3. **Compare margin before purchase.** Include supplier cost, dropship fee, shipping, payment fees, and expected store revenue. → *Expect:* the order remains profitable or is flagged for approval.
4. **Create the supplier order.** Enter customer shipping address, SKU, quantity, shipping speed, and blind-shipping/gift-message requirements. → *Expect:* a supplier checkout or draft order matches the customer order.
5. **Submit payment to supplier.** ⚠️ *Irreversible:* before placing the supplier order, confirm SKU, address, shipping method, cost, and cancellation window. → *Expect:* supplier order number is issued.
6. **Record supplier order details.** Save supplier order ID, cost, estimated ship date, and expected tracking source in the customer order notes. → *Expect:* support can trace fulfillment without asking the supplier again.
7. **Update customer status.** Mark the order in progress or fulfilled only according to platform rules; do not add tracking until real tracking exists. → *Expect:* the customer sees an accurate status.
8. **Upload tracking when available.** Verify carrier, tracking number, destination, and movement before notifying the customer. → *Expect:* customer receives valid tracking for the shipment.
9. **Monitor delivery and exceptions.** Watch for supplier cancellations, out-of-stock notices, split shipments, or carrier delays. → *Expect:* problems are caught before the customer has to chase them.

## Decision points

- Supplier is out of stock → offer substitute, delayed shipment, or refund before taking supplier payment.
- Supplier cost rose above margin floor → seek approval or cancel/refund according to policy.
- Customer paid for expedited shipping → use an equivalent supplier service or notify/refund shipping difference.
- Address validation fails → contact customer before submitting supplier order.

## Failure modes & recovery

- **F1 Wrong variant mapping:** detect supplier SKU does not match customer option → stop order submission and correct mapping.
- **F2 Supplier cancels after payment:** detect cancellation email or no fulfillment → source alternate supplier or notify/refund customer.
- **F3 Fake or stale tracking:** detect tracking that never moves or points to wrong destination → request supplier correction and do not mark delivered.
- **F4 Branded invoice included:** detect supplier may include its own receipt → enable blind shipping or choose a supplier that supports it.

## Verification

The supplier order is confirmed for the correct SKU/address, supplier details are recorded on the customer order, and valid tracking is uploaded once the supplier ships.

## Variations

- Automated integration: audit mapped SKUs and exception queue instead of manually placing each order.
- International dropship: disclose longer delivery windows and import responsibility clearly.
- Print-on-demand: proof artwork, personalization, and production status before fulfillment.

## Safety & privacy

Medium risk because customer address and supplier payment are involved. Share only fulfillment-required customer data with the supplier, confirm address/SKU before payment, and avoid suppliers that misuse customer contact information.
