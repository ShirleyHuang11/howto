---
name: harvest-a-tax-loss
domain: finance
subdomain: optimize
locale: [generic]
interface: web
difficulty: advanced
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You sell a losing taxable investment and, if desired, buy a non-substantially-identical replacement so the portfolio stays invested while preserving a valid tax-loss harvest.

## Preconditions

- Taxable brokerage account access, not a retirement account.
- Cost basis and unrealized gain/loss data.
- Understanding of local tax rules, including wash-sale or equivalent restrictions.
- A replacement investment that maintains exposure without violating the rules.

## Steps

1. **Confirm the account is taxable.** Verify the position is held in a taxable account where realized losses can matter. → *Expect:* the position is eligible for tax-loss consideration.
2. **Review unrealized loss and tax lots.** Open cost basis details and identify lots with meaningful losses after trading costs and bid-ask spread. → *Expect:* specific lots and estimated losses are known.
3. **Check for wash-sale exposure.** Review purchases of the same or substantially identical security across all accounts during the restricted window. → *Expect:* no recent or planned trades will invalidate the loss, or risks are identified.
4. **Select a replacement.** Choose a similar but not substantially identical fund or security if you want to stay invested. → *Expect:* replacement exposure is documented and rule risk is acceptable.
5. **Place the sale order.** Sell the selected losing lots using the brokerage's tax-lot selection tool. ⚠️ *Irreversible:* confirm account, ticker, lot selection, quantity, order type, and estimated loss before submitting. → *Expect:* sale order is submitted and later filled.
6. **Buy the replacement if planned.** Use a limit order or marketable order appropriate for liquidity. ⚠️ *Irreversible:* confirm ticker, amount, and price before submitting. → *Expect:* replacement position is filled or pending.
7. **Disable conflicting automatic buys.** Pause dividend reinvestment or recurring purchases that could trigger a wash sale. → *Expect:* no automatic same-security purchases are scheduled during the restricted window.
8. **Save tax records.** Download trade confirmations and note the harvested loss amount and replacement security. → *Expect:* records are ready for tax reporting.

## Decision points

- Loss is small → skip harvesting if trading spread, time, or tax complexity outweighs benefit.
- Replacement is too different → accept tracking error only if it fits the investment plan.
- Unsure about wash-sale rules → consult a tax professional before trading.

## Failure modes & recovery

- **F1 Wash sale triggered:** detect brokerage flags disallowed loss → record adjusted basis and avoid further conflicting purchases.
- **F2 Wrong lot sold:** detect default average-cost or FIFO selection used → contact brokerage immediately; correction may be possible only before settlement or cutoff.
- **F3 Out of market unintentionally:** detect replacement order not filled → adjust limit or reassess whether holding cash is acceptable.
- **F4 Tax benefit overestimated:** detect capital gains or income limits differ from assumptions → update tax projection before harvesting more.

## Verification

The targeted tax lots have been sold in the taxable account, the realized loss appears in brokerage records, no known wash-sale conflict exists, and any replacement holding is documented.

## Variations

- `us`: wash-sale rules commonly look 30 days before and after the sale and can include other accounts.
- ETF or mutual fund: replacement selection should avoid substantially identical index exposure while preserving broad allocation.

## Safety & privacy

Medium risk because investment trades and tax outcomes are involved. This is not tax advice; verify rules for your jurisdiction, confirm every order before submitting, and keep complete records.
