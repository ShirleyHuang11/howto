---
name: decide-whether-to-refinance-a-mortgage
domain: housing
subdomain: owning
locale: [generic, us]
interface: web
difficulty: advanced
est_time: 2h-14d
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-02
---

## Goal

You decide whether refinancing improves your mortgage situation after considering interest rate, closing costs, loan term, cash-out risk, taxes, and how long you expect to keep the home.

## Preconditions

- Current mortgage statement with balance, rate, term, payment, escrow, and payoff details.
- Credit score estimate, income and debt information, and home value estimate.
- At least two refinance quotes or loan estimates when you are close to applying.

## Steps

1. **Define the reason to refinance.** [BRANCH: lower rate | shorter term | lower payment | remove mortgage insurance | cash out equity | switch loan type] → *Expect:* the goal is specific enough to compare offers.
2. **Calculate the current loan baseline.** Record remaining balance, interest rate, remaining term, monthly principal and interest, escrow, and any prepayment penalty. → *Expect:* you know what happens if you do nothing.
3. **Estimate total refinance costs.** Include lender fees, title, appraisal, recording, points, escrow setup, prepaid interest, and taxes where applicable. → *Expect:* costs are separated from monthly payment savings.
4. **Compare break-even time.** Divide net closing costs by monthly savings, adjusting for rolled-in costs and term changes. → *Expect:* you know how many months before savings exceed costs.
5. **Check lifetime interest and term reset.** A lower payment can cost more if a new 30-year term restarts amortization. → *Expect:* you compare total interest, not only payment.
6. **Evaluate cash-out carefully.** Treat equity borrowing as secured debt against your home, not free cash. → *Expect:* the new loan balance and foreclosure risk are explicit.
7. **Request official Loan Estimates.** Apply with selected lenders within a focused shopping window and compare APR, rate, points, costs, and cash to close. → *Expect:* offers are comparable on the same disclosure format.
8. **Choose, pause, or decline.** ⚠️ *Irreversible:* before locking and signing closing documents, confirm the refinance meets your goal and you understand the right of rescission if applicable. → *Expect:* you have a documented go/no-go decision.

## Decision points

- You plan to move before break-even → refinancing likely does not pay off.
- You need payment relief → compare refinance with recast, modification, budgeting, or hardship options.
- Cash-out funds will pay unsecured debt → address spending pattern and rate risk before securing debt with the home.

## Failure modes & recovery

- **F1 Payment looks lower but term restarts:** detect higher lifetime interest → compare amortization schedules and consider a shorter term or extra principal payments.
- **F2 Closing costs hidden in balance:** detect loan amount larger than payoff → include rolled costs in break-even and equity calculations.
- **F3 Rate lock expires:** detect delayed closing → ask about extension cost and whether re-locking is better.
- **F4 Appraisal too low:** detect pricing changes or denial → ask about reconsideration of value, lower loan amount, or pausing.

## Verification

You have compared your current loan with refinance offers using payment, closing costs, break-even date, total interest, new term, and risk, and you have a written decision that matches your goal.

## Variations

- `us-primary-residence`: many refinance transactions include a three-business-day right of rescission after signing, but purchase loans generally do not.
- `adjustable-rate-to-fixed`: value may come from payment stability even if immediate savings are small.

## Safety & privacy

Medium risk from large debt, credit pulls, closing costs, and home-secured borrowing. Share financial documents only through lender portals and do not sign until figures match the final Closing Disclosure.
