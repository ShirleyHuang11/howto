---
name: compare-supplier-quotes
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

You compare supplier quotes on total landed value, not just unit price, and choose the quote that best meets cost, quality, timing, and risk constraints.

## Preconditions

- At least two supplier quotes for the same or comparable product.
- Target specs, required quantity, delivery location, and acceptable lead time.
- Access to shipping, duty, payment-fee, and currency assumptions.

## Steps

1. **Normalize the requested item.** Confirm each quote covers the same SKU, specification, packaging, certification, warranty, and quantity. → *Expect:* differences that affect comparability are visible.
2. **Record base commercial terms.** Capture unit price, minimum order quantity, volume tiers, currency, payment terms, quote expiration, and lead time. → *Expect:* each quote has the same core fields in a comparison sheet.
3. **Add logistics and import costs.** Include freight, insurance, duties, brokerage, handling, storage, and last-mile costs. → *Expect:* each quote has an estimated landed cost per sellable unit.
4. **Adjust for quality and defect risk.** Include sample results, defect allowance, returns process, replacement policy, and inspection costs. → *Expect:* lower-quality offers are not treated as equal to validated suppliers.
5. **Account for cash-flow impact.** Compare deposit, payment timing, credit terms, and currency exposure. → *Expect:* the quote's working-capital burden is visible.
6. **Score non-price factors.** Rate reliability, communication, references, compliance, lead time, and ability to scale. → *Expect:* a weighted score or written ranking beyond price.
7. **Identify negotiation points.** Mark the biggest cost or risk drivers: MOQ, freight, payment term, warranty, or tier discount. → *Expect:* a short list of asks for each supplier.
8. **Select the preferred quote.** ⚠️ *Irreversible:* issuing a purchase order or deposit commits money, so confirm landed cost, terms, and approval authority first. → *Expect:* a recommended supplier and backup are documented.

## Decision points

- Cheapest quote has weak quality evidence → request samples or inspection before selection.
- Currency differs across quotes → convert using the same exchange-rate date and add buffer.
- Lead time misses launch date → value reliability and speed over lower unit cost.

## Failure modes & recovery

- **F1 Comparing unlike specs:** detect mismatched materials, sizes, certifications, or packaging → ask suppliers to requote against one written spec.
- **F2 Hidden freight or duties:** detect quote says EXW/FOB without landed costs → request shipping quote or estimate import costs before deciding.
- **F3 Expired quote:** detect old pricing or currency change → reconfirm validity before issuing a purchase order.
- **F4 Supplier overpromises capacity:** detect vague production timeline or missing references → require milestone dates, samples, or split the order.

## Verification

The comparison includes normalized specs, total landed cost per unit, lead time, payment terms, quality risk, and a documented preferred supplier that meets the stated constraints.

## Variations

- Domestic suppliers: logistics may be simpler, but sales tax, freight class, and returns still matter.
- International suppliers: incoterms, duties, inspection, and currency risk usually dominate the comparison.
- Custom manufacturing: tooling, sample fees, and intellectual-property terms must be included.

## Safety & privacy

Medium risk because supplier selection can commit company funds and expose product plans. Keep quotes confidential, verify supplier identity, and require explicit approval before sending purchase orders or deposits.
