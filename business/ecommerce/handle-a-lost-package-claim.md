---
name: handle-a-lost-package-claim
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

You investigate a customer's lost-package claim, choose a fair resolution, and file any carrier or insurance claim with the necessary evidence.

## Preconditions

- Customer order number, tracking number, ship date, delivery address, and customer claim message.
- Store policy for lost shipments, replacements, refunds, and carrier claims.
- Access to carrier tracking, label purchase record, and fulfillment evidence.

## Steps

1. **Open the order and tracking.** Confirm order status, address, carrier, service, tracking events, and delivery scan. → *Expect:* a timeline from shipment to the claimed problem.
2. **Classify the loss scenario.** [BRANCH: no movement | delayed in transit | marked delivered | returned to sender] Identify which carrier process applies. → *Expect:* the claim path matches the tracking state.
3. **Verify address and fulfillment evidence.** Check label address, package weight, pickup/drop-off scan, packing photo if available, and any signature/GPS proof. → *Expect:* evidence shows whether shipment was sent correctly.
4. **Ask the customer for practical checks.** For delivered scans, ask them to check household members, mailroom, neighbors, parcel lockers, and delivery photo/location. → *Expect:* simple misdelivery possibilities are ruled out.
5. **Contact the carrier or open a trace.** Submit tracking number, shipper details, package description, and delivery issue through the carrier process. → *Expect:* carrier trace or case number is created.
6. **Choose customer resolution.** Based on policy and evidence, offer replacement, refund, wait for trace, or denial for unsupported claims. → *Expect:* customer has a clear next step and timeline.
7. **Issue replacement or refund if approved.** ⚠️ *Irreversible:* before reshipping or refunding, confirm order number, address, claim evidence, amount, and whether insurance/carrier recovery is separate. → *Expect:* customer resolution is recorded.
8. **File insurance or carrier claim.** Upload invoice, label, tracking, proof of value, photos, and customer statement within deadline. → *Expect:* claim submission confirmation and case number are saved.
9. **Close the loop.** Update order notes, fraud/risk flags if needed, and prevention settings such as signature for high-value shipments. → *Expect:* order history shows final outcome and prevention action.

## Decision points

- Tracking never received carrier scan → investigate warehouse handoff before blaming carrier.
- Package marked delivered with photo/signature → follow delivered-not-received policy and evaluate fraud risk.
- Customer needs item urgently → replacement may be better than waiting for carrier claim.
- Claim deadline is near → file with available evidence and add supplemental documents if allowed.

## Failure modes & recovery

- **F1 Carrier denies claim for insufficient proof:** detect claim rejected → resubmit allowed documents such as invoice, label, and acceptance scan if appeal is available.
- **F2 Customer chargeback starts:** detect payment dispute while claim is open → coordinate through dispute workflow and avoid duplicate refund.
- **F3 Wrong address entered by customer:** detect label matches customer-provided address → apply policy, offer paid reshipment if returned.
- **F4 Repeat lost-package pattern:** detect multiple claims from same customer/address → require signature or restrict future shipments according to policy.

## Verification

The lost-package case has a documented tracking investigation, customer resolution, and carrier/insurance claim number when eligible, with no duplicate refund or replacement left unresolved.

## Variations

- Marketplace order: platform delivery-protection rules may decide refund responsibility.
- High-value shipment: signature, insurance, and police report may be required.
- International shipment: postal investigations and customs delays can take longer.

## Safety & privacy

Medium risk because customer addresses and refunds are involved. Share tracking evidence only through approved systems, avoid accusing customers without evidence, and verify amounts before refunding or reshipping.
