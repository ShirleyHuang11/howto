---
name: check-your-bank-statement
domain: finance
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: [have-bank-account, accounts/log-in]
status: draft
last_verified: 2026-07-20
---

## Goal

You have scanned a full statement period line by line, every charge is either recognized or resolved, and creeping subscriptions have been caught before they compound.

## Preconditions

- Access to the statement: paper, PDF, or the transactions list in the banking app.
- A quiet 30 minutes; this is a scan you do not rush, because the point is to catch the one line that is wrong.
- Rough memory of the month's larger purchases, or receipts to cross-check against.

## Steps

1. **Open the full period, oldest to newest.** Set the date range to the whole statement month so nothing falls between screens. → *Expect:* a continuous list with no gap at the period edges.
2. **Confirm opening and closing balances.** The closing balance should equal opening plus credits minus debits. If it does not, the bank made an error or you are reading two different periods. → *Expect:* the arithmetic ties out.
3. **Scan every debit against memory.** Go line by line; tick the ones you recognize. Do not skim past small amounts. Card-testing fraud starts with a charge of a dollar or less. → *Expect:* each line either recognized or flagged.
4. **Decode any unknown charge before alarm.** Copy the exact merchant string and search it; most mystery charges are legitimate businesses billing under a parent-company or payment-processor name. → *Expect:* the charge resolves to a real purchase, or stays genuinely unexplained (F1).
5. **Check the recurring charges as a group.** List every subscription and standing payment. For each ask: still using it, and did the price rise? Trials that converted and quiet annual price bumps hide here. → *Expect:* a subscription list with any dead or drifted ones marked.
6. **Verify income and expected credits landed.** Salary, refunds, transfers in. A missing credit matters as much as a wrong debit. → *Expect:* every expected deposit present and correct.
7. **Act on the flags.** Cancel the dead subscriptions; for a truly unrecognized charge follow the unknown-charge protocol below. ⚠️ *Irreversible:* do not phone a number printed next to a suspicious charge. Scammers seed fake "support" numbers into billing descriptors; use only the number on your card. → *Expect:* each flag has an action underway.

## Decision points

- Charge is unknown after searching the string → treat as the unknown-charge protocol: check with household members, check card-on-file at obvious merchants, then if still unexplained freeze the card and dispute (`finance/dispute-a-card-charge`).
- A subscription price crept up but you still use it → decide on value at the new price, not the old; renewals bank on you not re-deciding.
- Multiple tiny unfamiliar debits → this is card-testing, not a billing quirk; freeze the card now rather than waiting for a large one.

## Failure modes & recovery

- **F1 Genuinely unrecognized charge:** freeze the card in-app, then open a dispute; do not delay because the amount is small (`finance/dispute-a-card-charge`).
- **F2 Duplicate charge from one merchant:** often a pending authorization plus the settled charge that will drop off; wait 3-5 days before disputing, then dispute if both settle.
- **F3 Subscription you cannot find how to cancel:** cancel from the merchant first; if blocked, revoke it at the card (stop the recurring payment) and document that you tried the merchant.
- **F4 Statement balance does not tie out:** re-check you are viewing one full period; if it still fails, contact the bank, as the error is theirs.

## Verification

Every line on the statement is accounted for, the closing balance ties to opening plus credits minus debits, any unrecognized charge is under dispute or frozen, and each subscription has been consciously kept or cancelled.

## Variations

- Paper-only accounts: same scan, but reconcile against your own receipts since there is no searchable app history.
- `us`/`uk`: dispute windows and subscription cancellation rights differ; check the timeline before assuming a charge is too old to contest.

## Safety & privacy

Medium risk: statements expose account numbers and spending patterns. Shred paper copies, store PDFs in an encrypted or password-protected location, and never email a full statement unredacted. The recurring scam here is fake support numbers embedded in charge descriptions.
