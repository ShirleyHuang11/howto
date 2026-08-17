---
name: rebalance-a-portfolio
domain: finance
locale: [generic]
interface: web
difficulty: advanced
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Bring an investment portfolio back toward a chosen target allocation while considering taxes, fees, account types, and trading consequences.

## Preconditions

- You have a written target allocation by asset class or fund.
- You can access each investment account and current balances.
- You know which accounts are taxable, tax-deferred, tax-free, employer-sponsored, or restricted.
- You understand that selling investments can create taxes and that trades can lose value.

## Steps

1. **List current holdings.** Export balances, tickers, asset classes, account types, and cash positions from each account. → *Expect:* one current portfolio view is available.
2. **Compare against targets.** Calculate current percentages and differences from the target allocation. → *Expect:* overweight and underweight categories are visible.
3. **Set rebalance bands.** Decide whether differences are large enough to act based on your written rule. → *Expect:* only categories outside the rule are marked for action.
4. **Prefer new contributions.** Direct new deposits, dividends, or payroll contributions toward underweight categories first. → *Expect:* some or all imbalance can be corrected without selling.
5. **Choose trade locations.** If trades are needed, prioritize tax-advantaged accounts when suitable and check taxable gains before selling. → *Expect:* proposed trades are mapped to accounts with tax impact noted.
6. **Review costs and restrictions.** Check transaction fees, bid-ask spreads, short-term redemption fees, wash-sale issues, and employer-plan trading limits. → *Expect:* trade plan avoids avoidable costs and rule violations.
7. **Place trades carefully.** Enter orders for the chosen funds or securities and confirm tickers, dollars or shares, account, and order type. ⚠️ *Irreversible:* submitted market orders may execute quickly and cannot always be canceled, so verify every order ticket first. → *Expect:* orders are accepted, filled, or waiting with status visible.
8. **Record the new allocation.** Save confirmations and update the allocation spreadsheet after trades settle. → *Expect:* the portfolio is back inside the target bands or has a documented reason not to be.

## Decision points

- Taxable gains are large → consider rebalancing with contributions, charitable giving, or smaller staged trades.
- Account has employer restrictions → follow plan rules before trading.
- Target allocation changed because goals changed → update the written plan before placing trades.
- Market is volatile → use limit orders or staged trades if order execution price matters.

## Failure modes & recovery

- **F1 Wrong ticker traded:** detect order confirmation with unexpected fund or security → recover by canceling if open or placing a corrective trade after reviewing tax impact.
- **F2 Taxable gain surprise:** detect estimated gains or tax forms after sale → recover by setting aside cash and consulting tax guidance before further selling.
- **F3 Cash left idle:** detect settlement fund balance not assigned → recover by investing or documenting the intended reserve.
- **F4 Allocation math wrong:** detect percentages not totaling 100% or missing accounts → recover by rebuilding the portfolio view from statements.

## Verification

After settlement, the recorded portfolio allocation is within the chosen rebalance bands or the remaining deviation is documented with a tax, fee, or restriction reason.

## Variations

- `us-taxable`: capital gains, losses, wash sales, and holding periods can affect after-tax results.
- `retirement-account`: trades may avoid current tax but still have plan rules and investment-menu limits.
- `robo-advisor`: the platform may automate rebalancing and tax-loss harvesting.

## Safety & privacy

Medium risk from market loss, tax consequences, and account exposure. Use official account sites, verify order tickets before submission, and keep allocation records private.
