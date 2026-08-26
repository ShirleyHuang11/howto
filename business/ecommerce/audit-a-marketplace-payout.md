---
name: audit-a-marketplace-payout
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

Reconcile a marketplace payout against orders, fees, refunds, reserves, and adjustments so missing or incorrect money is identified.

## Preconditions

- Marketplace seller account access and payout report export.
- Order, refund, fee, shipping-label, tax, and reserve reports for the payout period.
- Bank deposit record for the payout.

## Steps

1. **Download the payout statement.** Export the payout summary and transaction-level detail for the exact payout ID. → *Expect:* a report listing every order, fee, refund, adjustment, and reserve movement.
2. **Match the bank deposit.** Compare payout ID, date, currency, and net amount to the bank transaction. → *Expect:* the marketplace net payout equals the bank deposit or has a documented transfer delay.
3. **Reconcile gross order revenue.** Sum included order payments and compare to order reports. → *Expect:* every paid order in the payout period is accounted for.
4. **Reconcile deductions.** Check commissions, payment fees, fulfillment fees, shipping labels, refunds, chargebacks, ads, and taxes withheld. → *Expect:* each deduction has a category and order or adjustment reference.
5. **Review reserves and holds.** Identify unavailable balances, rolling reserves, dispute holds, and pending settlements. → *Expect:* withheld funds have stated release criteria or dates.
6. **Investigate differences.** For any variance above the tolerance, open the underlying order or fee detail. → *Expect:* every variance is either explained or ready for a support claim.
7. **File disputes for errors.** ⚠️ *Irreversible:* submit claims only with exact evidence, because false or duplicate disputes can delay support. → *Expect:* marketplace support receives a claim with payout ID, transaction IDs, and variance amount.

## Decision points

- Difference is timing-related → carry it to the next payout reconciliation.
- Fee category changed → update accounting mappings before marking as an error.
- Reserve has no release date → contact marketplace support and document the case ID.

## Failure modes & recovery

- **F1 Missing order:** detect paid order absent from payout → check settlement delay, reserve, or canceled status before filing a claim.
- **F2 Duplicate refund deduction:** detect same refund deducted twice → collect order and transaction IDs and dispute the duplicate.
- **F3 Tax confusion:** detect tax collected but not paid out → confirm marketplace facilitator rules.
- **F4 Currency mismatch:** detect payout in converted currency → reconcile using marketplace exchange-rate details.

## Verification

The payout net amount ties to the bank deposit within the stated tolerance, and every variance has an explanation, carry-forward entry, or submitted support case ID.

## Variations

- `amazon`: settlement reports include many fee types and reserve balances; reconcile by transaction type.
- `etsy`: ads, labels, listing fees, and payment account activity may all reduce payout.

## Safety & privacy

Medium risk because payout exports contain customer and financial data. Store reports securely, share only necessary transaction IDs with support, and avoid exposing bank details.
