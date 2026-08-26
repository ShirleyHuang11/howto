---
name: set-a-stop-loss
domain: finance
subdomain: optimize
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You place a stop-loss or stop-limit sell order that defines an exit trigger for a holding while understanding gap and execution risks.

## Preconditions

- Brokerage account access and an existing position.
- Ticker, share quantity, cost basis, and desired exit level.
- Understanding of stop market versus stop limit.
- Awareness of tax consequences and short-term volatility.

## Steps

1. **Confirm the position and objective.** Open holdings and verify ticker, quantity, unrealized gain or loss, and why you want an automatic exit. → *Expect:* a specific position and exit rationale.
2. **Choose stop type.** [BRANCH: stop market, prioritizes execution after trigger | stop limit, controls minimum sale price but may not execute] → *Expect:* order type matches the risk you accept.
3. **Set trigger and limit prices.** Choose a stop price based on risk tolerance, chart levels, or portfolio rules; set a limit price only if using stop limit. → *Expect:* exact trigger and optional limit values.
4. **Check tax and wash-sale implications.** Review whether a sale creates taxable gain, harvested loss, or replacement restrictions. → *Expect:* tax impact is understood before the order is placed.
5. **Preview the order.** Enter sell, ticker, quantity, stop type, stop price, limit price if any, and duration. → *Expect:* preview shows the correct position and estimated proceeds.
6. **Submit the stop order.** ⚠️ *Irreversible:* confirm sell direction, ticker, quantity, stop price, limit price, and account before submitting. → *Expect:* brokerage shows an open stop order.
7. **Monitor for corporate actions and price changes.** Revisit after dividends, splits, earnings, or major volatility. → *Expect:* the stop remains intentional and not stale.
8. **Cancel before selling manually.** If you sell the position another way, cancel the stop order. ⚠️ *Irreversible:* confirm cancellation before placing other sell orders to avoid overselling. → *Expect:* no orphaned stop order remains.

## Decision points

- Security is very volatile → wider stops or position sizing may work better than tight stops.
- Overnight gap risk matters → a stop market can fill far below the trigger; a stop limit may not fill.
- Long-term holding with tax gains → decide whether automatic sale conflicts with investment and tax plan.

## Failure modes & recovery

- **F1 Stop triggered by temporary dip:** detect sale followed by quick recovery → reassess stop distance and avoid immediate emotional re-entry.
- **F2 Stop-limit does not execute:** detect price gaps below limit → decide whether to place a new order or hold.
- **F3 Oversell risk:** detect position sold manually while stop remains open → cancel open stop orders immediately.
- **F4 Wrong share quantity:** detect order covers too many shares → modify or cancel before trigger.

## Verification

The brokerage shows an open stop order with the intended ticker, quantity, trigger, order type, and duration, or a triggered sale whose execution is documented.

## Variations

- Trailing stop: trigger follows the price by a fixed amount or percentage, useful when protecting gains.
- Options or leveraged ETFs: stops can behave poorly due to spreads and volatility; use smaller size or specialist tools.

## Safety & privacy

Medium risk because orders may execute during volatility and create taxable events. Confirm every order field, understand gap risk, and cancel stale stops when your position changes.
