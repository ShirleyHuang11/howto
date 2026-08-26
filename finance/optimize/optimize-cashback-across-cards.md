---
name: optimize-cashback-across-cards
domain: finance
subdomain: optimize
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You route everyday purchases to the cards that earn the highest net cash back while avoiding fees, interest, and missed category enrollment.

## Preconditions

- Current list of credit cards, reward rates, rotating categories, caps, and annual fees.
- Access to each issuer rewards portal.
- A monthly budget by spending category.
- Ability to pay all cards in full.

## Steps

1. **Inventory each card's earning rules.** Record base rate, bonus categories, quarterly categories, merchant limitations, caps, and foreign transaction fees. → *Expect:* a table of cards and earning rates.
2. **Activate required categories.** Enroll in quarterly or merchant offers before spending in those categories. → *Expect:* the issuer portal shows activated offers or categories.
3. **Map your real spending categories.** Use recent statements to estimate monthly spend on groceries, dining, gas, transit, travel, online shopping, and utilities. → *Expect:* category totals that reflect actual behavior.
4. **Assign a primary card for each category.** Choose the highest net reward after caps, fees, and merchant acceptance. → *Expect:* a simple card-to-category map.
5. **Set cap alerts.** Track bonus-category caps so spending switches to the next best card after the cap is reached. → *Expect:* alerts or spreadsheet formulas show remaining bonus capacity.
6. **Label cards or wallet entries.** Rename mobile-wallet cards or add small physical labels if helpful. → *Expect:* the right card is easy to choose at checkout.
7. **Review statements monthly.** Check that purchases coded into expected merchant categories and that cash back posted correctly. → *Expect:* rewards match the planned earning rates or exceptions are identified.
8. **Redeem cash back efficiently.** Choose statement credit, deposit, or eligible redemption that preserves full value. ⚠️ *Irreversible:* confirm redemption value and destination before submitting. → *Expect:* rewards are redeemed at the intended value.

## Decision points

- Merchant coding is inconsistent → use the card with best base rate there unless testing a small purchase confirms bonus coding.
- Annual fee card underperforms → compare yearly extra rewards against the fee and downgrade or cancel only after considering credit impact.
- Carrying balances occurs → stop optimizing rewards and prioritize debt payoff.

## Failure modes & recovery

- **F1 Category not activated:** detect purchases earned base rate → activate now and ask issuer whether retroactive credit is possible.
- **F2 Bonus cap exceeded:** detect lower rewards after cap → switch future purchases to the next best card.
- **F3 Redemption devalued:** detect gift card or merchandise gives less than cash value → choose cash-equivalent redemption instead.
- **F4 Missed payment:** detect late fee or interest → pay immediately, request fee waiver, and simplify card use.

## Verification

For the current cycle, each major spending category has an assigned card, required categories are activated, rewards post at expected rates, and all statement balances are paid in full.

## Variations

- `us`: rotating 5% category cards often require quarterly activation and have category caps.
- Travel rewards setup: replace cash value with a conservative cents-per-point value before comparing cards.

## Safety & privacy

Medium risk because multiple credit accounts are involved. Do not increase spending for rewards, store account credentials securely, and never sacrifice on-time full payment for marginal cash back.
