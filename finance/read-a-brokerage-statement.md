---
name: read-a-brokerage-statement
domain: finance
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Understand a brokerage statement well enough to identify holdings, activity, cost basis, gains or losses, fees, dividends, and mismatches.

## Preconditions

- Recent brokerage statement PDF or mailed statement.
- Online account access if available.
- Prior statement for comparison.
- Trade confirmations if you bought or sold during the period.
- Basic understanding that investments can gain or lose value.

## Steps

1. **Confirm statement identity.** Check account owner, account number ending, period dates, and brokerage name. → *Expect:* the statement belongs to the correct account and month or quarter.
2. **Review account summary.** Compare beginning value, deposits, withdrawals, income, market change, fees, and ending value. → *Expect:* the summary arithmetic explains the change in account value.
3. **List holdings.** Read each cash position, stock, fund, bond, option, or other security with quantity, price, and market value. → *Expect:* every holding has a current value and percentage or category.
4. **Check cost basis.** For taxable accounts, review original cost, acquisition date, and covered or noncovered status. → *Expect:* you can see which positions have reliable tax basis information.
5. **Review gains and losses.** Separate realized gains/losses from unrealized gains/losses. → *Expect:* sold positions are not confused with paper changes on holdings you still own.
6. **Find income.** Look for dividends, interest, capital gain distributions, and reinvestments. → *Expect:* income entries match cash movements or added shares.
7. **Identify fees.** Check advisory fees, fund expenses if listed, margin interest, transfer fees, and commissions. → *Expect:* any direct fees are visible and explainable.
8. **Reconcile activity.** Compare deposits, withdrawals, trades, transfers, and dividends to your records. → *Expect:* no transaction is unfamiliar or duplicated.
9. **Flag questions.** Mark unfamiliar securities, negative cash, margin balance, missing cost basis, or unexpected fees for brokerage support or an adviser. → *Expect:* you have a short list of items to resolve.

## Decision points

- Taxable account with sales → cost basis and realized gains matter for taxes.
- Retirement account → tax basis may not appear, but contributions and distributions matter.
- Margin account → negative cash or margin interest means borrowed money may be involved.
- Reinvested dividends → income can be taxable even if no cash left the account.
- Statement differs from online balance → check the statement date before assuming an error.

## Failure modes & recovery

- **F1 Missing cost basis:** detect blank or noncovered basis; recover by finding purchase records or asking the broker.
- **F2 Unexpected fee:** detect advisory, transfer, inactivity, or margin charges; recover by reading the fee schedule and asking for explanation.
- **F3 Unknown holding:** detect a ticker or fund name you do not recognize; recover by checking trade history and corporate-action notices.
- **F4 Cash mismatch:** detect deposits or withdrawals not in your bank records; recover by matching dates and transfer IDs.
- **F5 Tax confusion:** detect realized gain entries you cannot classify; recover by saving the statement and waiting for official tax forms or consulting a tax professional.

## Verification

For the statement period, beginning value plus net activity plus market change equals ending value, and every unfamiliar holding, fee, or transaction is either explained or flagged.

## Variations

- `mutual-fund`: fund expense ratios may not appear as line-item fees.
- `options`: expiration, assignment, and exercise entries require special review.
- `bonds`: accrued interest and maturity dates affect income and value.
- `managed-account`: advisory fees may be billed monthly or quarterly.
- `tax-season`: official tax forms can differ from monthly statements.

## Safety & privacy

Brokerage statements expose account value, positions, tax ID fragments, and address. Share them only with trusted tax, legal, or financial professionals, and redact account numbers when full detail is not needed.
