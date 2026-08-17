---
name: read-a-401k-statement
domain: finance
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Read a 401k statement well enough to understand contributions, employer match, investments, fees, performance, loans, and vesting.

## Preconditions

- You have the latest statement or retirement-plan portal access.
- You know the statement period and employer plan name.
- You can compare payroll deductions if available.

## Steps

1. **Confirm the statement period.** Check beginning date, ending date, participant name, and plan name. → *Expect:* you know which months or quarter the statement covers.
2. **Review balance changes.** Compare beginning balance, contributions, employer match, rollovers, gains or losses, fees, loans, withdrawals, and ending balance. → *Expect:* the ending balance can be explained by listed activity.
3. **Check contributions.** Match employee contributions to payroll deductions and note traditional pre-tax, Roth, after-tax, and catch-up categories. → *Expect:* contributions are going to the intended source.
4. **Check employer match.** Compare employer contribution amount to the plan match formula if shown. → *Expect:* missing or unexpected match amounts are visible.
5. **Read vesting.** Find vested balance versus total balance for employer contributions. → *Expect:* you know how much would be yours if you left now.
6. **Review investments.** Note fund names, asset classes, allocation percentages, target-date fund year, and any concentrated company stock. → *Expect:* the portfolio mix is clear.
7. **Review fees and expenses.** Find administrative fees, loan fees, advisory fees, and fund expense ratios if provided. → *Expect:* recurring costs are identified.
8. **Look for loans or restrictions.** Check outstanding loan balance, payment schedule, blackout notices, required minimum distribution notices, or beneficiary warnings. → *Expect:* obligations and action items are visible.
9. **Save or flag follow-up.** Download the statement and write questions for HR, plan administrator, or a financial professional. → *Expect:* you have a record and a short list of unresolved items.

## Decision points

- Contributions do not match payroll → contact payroll or the plan administrator with pay stubs and statement dates.
- Employer match seems missing → check eligibility, vesting, true-up timing, and plan formula.
- Allocation does not match risk tolerance or age → review investment choices before changing funds.
- Fees look high or confusing → request the fee disclosure and compare lower-cost plan options if available.

## Failure modes & recovery

- **F1 Missing statement:** detect no recent statement, recover by logging into the plan portal or requesting one from the administrator.
- **F2 Payroll mismatch:** detect contribution difference, recover by comparing pay dates inside the statement period.
- **F3 Unvested surprise:** detect total balance larger than vested balance, recover by reading the vesting schedule before job changes.
- **F4 Fund confusion:** detect duplicate or unclear fund names, recover by opening fund fact sheets and ticker symbols.
- **F5 Loan overlooked:** detect loan balance or default warning, recover by confirming payroll repayment and separation rules.

## Verification

You can state the statement period, ending vested balance, contribution totals, employer match, investment allocation, fees, and any loan or action item.

## Variations

- `us`: 401k statements follow plan-specific rules; 403b, 457, TSP, and SIMPLE plans have different labels.
- Target-date funds: the year usually approximates retirement timing but still has fees and asset mix to review.
- Former employer plan: rollover, fees, and address updates may matter more than payroll deductions.

## Safety & privacy

Retirement statements reveal identity, employer, balances, and beneficiaries. Do not share login credentials, and confirm implications before changing investments, loans, or withdrawals.
