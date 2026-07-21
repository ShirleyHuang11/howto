---
name: save-for-a-big-purchase
domain: finance
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 1h
risk: medium
prerequisites: [have-payment-method, accounts/log-in]
status: draft
last_verified: 2026-07-20
---

## Goal

A specific large purchase is funded on time by a deliberate plan: a target amount and date, an automatic transfer that siphons money before you can spend it, and the money parked somewhere separate and slightly hard to reach.

## Preconditions

- A concrete goal with a known cost and a rough deadline.
- A bank or app that supports scheduled internal transfers or sub-accounts.
- Predictable enough income to commit a fixed amount each pay cycle.

## Steps

1. **Pin the real target amount.** Add tax, delivery, and a 5 to 10 percent buffer to the sticker price. → *Expect:* one number you would actually hand over, not the advertised price.
2. **Set the goal date and do the math.** Divide the target by the number of pay cycles until the date. That per-cycle figure is your contribution. → *Expect:* a per-paycheck amount; if it feels impossible, extend the date or cut the target now, not later.
3. **Open a separate parking spot.** A named savings sub-account or a distinct high-yield account, not your checking account. → *Expect:* an empty account visibly labeled for this goal, separate from spending money.
4. **Automate the siphon.** Schedule a transfer of the per-cycle amount, dated the day after payday, from checking into the goal account. ⚠️ *Irreversible:* automating means money leaves before you budget the rest, so set the amount you can truly spare, then live on what remains. → *Expect:* a recurring transfer confirmed; first run lands next cycle.
5. **Make withdrawal deliberately slightly annoying.** Use an account without a linked debit card, or one with a 1 to 2 day transfer delay back to checking. → *Expect:* the money is reachable in an emergency but not tappable at a checkout.
6. **Check progress monthly, adjust rarely.** Confirm the transfers ran and the balance tracks the plan line. → *Expect:* balance at or above (cycles elapsed × contribution); if behind, raise the contribution or move the date, do not just hope.
7. **Spend from the parked money, then stop the siphon.** When the target is hit, buy, then cancel the recurring transfer. → *Expect:* purchase funded from savings, automatic transfer switched off so it does not silently continue.

## Decision points

- Deadline is under a few months away → keep the money in cash-equivalent savings; do not chase yield in anything that can drop in value before you need it.
- Deadline is years away → a slightly higher-yield vehicle may fit, but only if a temporary dip would not force you to sell at the wrong time.
- Income is irregular → siphon a percentage of each deposit rather than a fixed amount, so lean months do not overdraw you.

## Failure modes & recovery

- **F1 Automatic transfer overdraws checking:** payday timing shifted → move the transfer date later in the cycle and keep a one-cycle buffer in checking.
- **F2 You keep raiding the goal account:** balance never grows → move it to a different bank with no debit card and a transfer delay; distance is the whole point.
- **F3 Falling behind the plan line:** monthly check shows a growing gap → recompute the per-cycle figure against the remaining cycles and reset the transfer, or push the date; small early corrections beat a last-minute shortfall.
- **F4 Price rose before you finished:** target now short → the buffer from step 1 absorbs small rises; for a large jump, extend the date rather than buying underfunded on credit.

## Verification

The goal account holds at least the target amount by the goal date, the money never got spent on anything else en route, and the automatic transfer is cancelled once the purchase is made.

## Variations

- `windfall`: a bonus or refund can front-load the goal; park it immediately on arrival before it blends into spending money.
- `sinking-fund`: for recurring big costs (annual insurance, holidays), keep the siphon running permanently and spend from the account each cycle instead of stopping.

## Safety & privacy

Medium risk: this is your money and the main hazard is an automatic transfer overdrawing your spending account, or locking funds you suddenly need. Keep an accessible emergency buffer separate from this goal, and never fund the automation to a level that leaves you short before the next payday.
