---
name: split-shared-household-costs
domain: finance
locale: [generic]
interface: mobile-app
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [have-payment-method, accounts/log-in]
status: draft
last_verified: 2026-07-20
---

## Goal

Shared household expenses (rent, utilities, groceries) are tracked in one agreed system so that at any moment each person knows what they owe or are owed, and balances settle cleanly on a regular schedule.

## Preconditions

- Two or more people sharing recurring costs, all reachable and willing to use one system.
- A way to move money between you (bank transfer, peer payment app, cash).
- Agreement on the split rule before any money is spent, not after.

## Steps

1. **Agree the split rule first.** Even split, income-weighted, or per-item (person X never uses the car). → *Expect:* every housemate can state the rule the same way without argument.
2. **Choose the tracking system.** [BRANCH: shared ledger app (Splitwise, Tricount) for many small entries | one shared spreadsheet for full control | a joint account funded by equal standing orders for simple even splits] → *Expect:* one system named as the single source of truth; no parallel side-tallies.
3. **Set up the group and members.** Invite everyone by the same identifier (phone or email) and confirm each person appears once. → *Expect:* member list matches the household exactly, no duplicates.
4. **Log the first shared expense.** Enter amount, payer, date, and who it splits between. → *Expect:* the app shows the balance shifting; the payer is now owed their share of it.
5. **Make logging a habit, not a reconciliation.** Enter each expense when it happens, from the receipt, before you forget the amount. → *Expect:* running balances stay believable week to week, never a mystery.
6. **Settle on a fixed cadence.** Pick a monthly date. On it, read the net balances and each debtor pays their single net figure to each creditor. ⚠️ *Irreversible:* a sent payment cannot be recalled. Confirm the recipient handle and amount before sending. → *Expect:* app "settle up" recorded; balances return to zero.
7. **Close out when someone moves out.** Do a final settle, include the deposit split and any final utility bills that arrive later, then remove them from the group. → *Expect:* the leaving person's balance is zero and both sides agree in writing (a chat message counts).

## Decision points

- One person always fronts big bills → keep them as the standing payer and settle net monthly rather than reimbursing each time.
- A bill arrives after someone moves out → agree at move-out who covers trailing bills; hold a small buffer from the deposit if the timing is uncertain.
- Split rule feels unfair after a few months → renegotiate at a settle date, forward-looking only; do not retroactively re-split past months.

## Failure modes & recovery

- **F1 Ledger drifts from reality:** balances nobody trusts → export the log, walk it line by line together, correct or delete wrong entries, re-settle from the corrected total.
- **F2 Someone stops logging:** their spending vanishes from the tally → agree that unlogged spending is not reimbursable; this makes logging self-enforcing.
- **F3 Payment sent to the wrong handle:** money gone to a stranger → contact the app's support immediately, but treat it as likely lost; always send a 1-unit test to a new handle first.
- **F4 Disputed expense:** one person contests a charge → mark it pending, not deleted; resolve before the settle date so the net figure stays clean.

## Verification

Every shared expense for the period is in the one system, the monthly settle has run, and each person's net balance reads zero (or a single agreed carried figure) that all parties can see and confirm.

## Variations

- `couples`: many use a joint account for shared costs plus separate personal accounts; the ledger rule is replaced by a funding rule (each deposits an agreed share monthly).
- `high-churn-share`: sublets and rotating guests need per-night or per-person-day splits; a ledger app with unequal shares handles this better than a spreadsheet.

## Safety & privacy

Medium risk: real money moves and payment handles are shared. Ledger apps expose your spending detail to housemates, so keep personal purchases off the shared group. Verify every recipient before sending, since peer payments are effectively irreversible.
