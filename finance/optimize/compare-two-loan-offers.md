---
name: compare-two-loan-offers
domain: finance
subdomain: optimize
locale: [generic]
interface: web
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You compare two loan offers by total cost, monthly payment, fees, flexibility, and risk so you can choose the cheaper suitable loan.

## Preconditions

- Two written loan estimates or offers with APR, interest rate, term, fees, payment, and prepayment terms.
- Desired loan amount and repayment horizon.
- Credit score or eligibility context if offers are conditional.
- Calculator or spreadsheet for total-cost comparison.

## Steps

1. **Normalize the loan amount.** Confirm both offers are for the same principal amount or adjust calculations to a common amount. → *Expect:* offers can be compared on equal footing.
2. **Record all key terms.** Capture APR, nominal rate, term, payment, origination fee, closing costs, points, prepayment penalty, late fees, and variable-rate terms. → *Expect:* a side-by-side term table.
3. **Calculate total repayment.** Multiply payment by number of payments and add upfront fees not included in the payment. → *Expect:* estimated total cost for each offer.
4. **Separate APR from cash-flow fit.** Compare APR for cost and monthly payment for affordability. → *Expect:* you know which offer is cheaper and which is easier monthly.
5. **Check rate variability and penalties.** Identify variable-rate resets, balloon payments, collateral requirements, and prepayment limits. → *Expect:* hidden risk terms are visible.
6. **Test early payoff scenarios.** If you expect to refinance or repay early, calculate cost through that month rather than full term. → *Expect:* best offer under likely payoff timing is known.
7. **Ask lenders to clarify missing items.** Request written confirmation of any unclear fee, condition, or expiration date. → *Expect:* no critical blank terms remain.
8. **Choose or reject offers.** ⚠️ *Irreversible:* before signing, confirm final APR, amount financed, payment schedule, and fees match the selected offer. → *Expect:* a documented choice with the reason.

## Decision points

- Lower payment has much longer term → choose only if cash-flow relief is worth higher total interest.
- APRs are close but fees differ → use early-payoff scenario to see which is cheaper for your expected timeline.
- Offer is conditional on add-ons → exclude optional insurance or products unless independently useful.

## Failure modes & recovery

- **F1 Comparing rate instead of APR:** detect one loan has high fees hidden outside rate → use APR and total repayment instead.
- **F2 Teaser rate trap:** detect introductory or variable rate → model the reset payment before accepting.
- **F3 Prepayment penalty missed:** detect fee for early payoff → include it in refinance or early payoff scenario.
- **F4 Conditional offer changes:** detect final documents differ from quote → pause signing and ask for corrected documents.

## Verification

A side-by-side comparison shows each offer's APR, monthly payment, total repayment, upfront fees, and early-payoff cost, and the selected offer has the lowest acceptable cost for the chosen constraints.

## Variations

- Mortgage: use standardized loan estimates and compare cash to close, points, and rate-lock expiration.
- Auto loan: include dealer incentives, manufacturer financing, and any required add-ons in the total price.

## Safety & privacy

Medium risk because loan documents expose identity and debt obligations. Use written offers, avoid pressure signing, and confirm final documents match the comparison before accepting.
