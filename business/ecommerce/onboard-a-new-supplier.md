---
name: onboard-a-new-supplier
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You qualify a new supplier, collect the required business and payment information, and make them ready for purchase orders without exposing the business to preventable fraud or quality risk.

## Preconditions

- A product or service need and authority to evaluate suppliers.
- Supplier contact details, catalog or quote, and business identity information.
- Internal requirements for tax forms, payment terms, insurance, compliance, or quality checks.

## Steps

1. **Define the supply requirement.** Specify SKU, quantity, quality standard, lead time, packaging, certifications, and target landed cost. → *Expect:* a clear requirement the supplier can confirm or decline.
2. **Verify business legitimacy.** Check company registration, website, references, address, and whether contact email matches the business domain. → *Expect:* evidence that the supplier is a real operating business.
3. **Request onboarding documents.** Collect tax form, banking instructions through a secure channel, insurance or compliance certificates, catalog, and price list as applicable. → *Expect:* required documents are received or missing items are listed.
4. **Review product fit and quality risk.** Compare samples, specifications, photos, certifications, and warranty terms against your requirement. → *Expect:* the supplier's offering meets the minimum standard or gaps are documented.
5. **Agree on commercial terms.** Confirm unit price, minimum order quantity, payment terms, incoterms or shipping responsibility, lead time, returns, defects, and chargeback process. → *Expect:* terms are written in a quote, contract, or supplier profile.
6. **Set up the supplier record.** Enter legal name, contact, addresses, tax status, payment terms, currency, and approved SKUs in the purchasing system. → *Expect:* the supplier appears in the system but is not yet paid without approval.
7. **Verify payment instructions independently.** Call a known supplier phone number or use an approved vendor-verification process before activating bank details. → *Expect:* payment account details are confirmed outside the original email thread.
8. **Approve initial purchasing.** ⚠️ *Irreversible:* purchase orders and deposits commit money, so confirm supplier identity, terms, and approval authority first. → *Expect:* supplier status changes to approved for a limited first order or pilot.
9. **Document first-order controls.** Set sample inspection, smaller initial quantity, deposit cap, or pre-shipment photos. → *Expect:* the first purchase has defined acceptance checks.

## Decision points

- Supplier asks for full prepayment → limit exposure with samples, escrow, trade assurance, or a smaller pilot order.
- Bank details changed by email → pause setup and verify by a trusted phone number before payment.
- Certifications are required by law or marketplace policy → do not onboard until documents are validated.

## Failure modes & recovery

- **F1 Fake supplier identity:** detect inconsistent domain, address, references, or registration → stop onboarding and find an independently verifiable supplier.
- **F2 Bank-detail fraud:** detect last-minute wire changes or pressure → freeze payment setup and revalidate through known contacts.
- **F3 Quality mismatch after first order:** detect failed samples or inspection → reject shipment under agreed terms and update supplier status.
- **F4 Hidden landed cost:** detect duties, freight, or packaging not included → recalculate cost and renegotiate before issuing purchase orders.

## Verification

The supplier has a complete approved profile, independently verified payment details, documented commercial terms, and first-order controls before any purchase order or deposit is released.

## Variations

- International suppliers: add sanctions screening, import duties, incoterms, and customs documentation.
- Food, cosmetics, or medical products: require regulatory compliance evidence before approval.
- Marketplace wholesale: platform verification can help but does not replace payment and quality checks.

## Safety & privacy

Medium risk because onboarding can expose payment accounts, tax data, and purchasing authority. Use secure document exchange, independently verify banking changes, and require explicit approval before deposits or purchase orders.
