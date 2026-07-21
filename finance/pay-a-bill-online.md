---
name: pay-a-bill-online
domain: finance
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: [accounts/log-in, have-bank-account]
status: draft
last_verified: 2026-07-20
---

## Goal

A due bill (utility, phone, credit card, rent) is paid online before its due date, with a confirmation number saved.

## Preconditions

- The bill or an account with the biller, showing amount due and due date.
- An online payment channel: the biller's portal, your bank's bill-pay, or an accepted wallet.
- Sufficient funds in the paying account.

## Steps

1. **Read the bill.** Note amount due, due date, account/customer number, and whether the amount looks normal for the season. → *Expect:* you can state amount, date, and account number; anomalies (double last month's?) get investigated before paying.
2. **Choose the payment channel.** [BRANCH: biller's own portal | your bank's bill-pay | wallet/payment app] First time on a biller portal: reach it by typing the URL from the paper bill, never from an email link. → *Expect:* you are logged in at the correct channel (`accounts/log-in`).
3. **Locate the bill in the portal.** Billing/Payments section → current statement. → *Expect:* portal's amount due and due date match the bill in hand; mismatch → F1.
4. **Enter payment details.** Select or add the funding source; enter/confirm the amount — pay the statement balance unless intentionally paying partial. → *Expect:* a review screen: payee, amount, funding source, payment date.
5. **Check the scheduled date lands on or before the due date.** Bank bill-pay may take 1–3 business days to deliver — schedule accordingly. → *Expect:* delivery/processing date ≤ due date.
6. **Confirm the payment.** ⚠️ *Irreversible:* online payments to billers are hard to recall once processed — verify payee and amount on the review screen now. → *Expect:* a confirmation screen with a confirmation/reference number.
7. **Save the confirmation.** Screenshot or note the number with the date. → *Expect:* confirmation stored; an email receipt typically follows.
8. **Verify settlement within a few days.** Bank statement shows the debit; biller portal shows balance cleared. → *Expect:* exactly one debit of the right amount; biller balance updated.

## Decision points

- Amount looks wrong → contact the biller *before* paying; paying disputes it weakens your position.
- Cash-flow shortfall → many billers offer payment plans or due-date extensions if asked before the due date, not after.
- Recurring bill → consider autopay of the minimum with a calendar check of each statement — autopay of unchecked full balances propagates billing errors.

## Failure modes & recovery

- **F1 Portal shows a different amount than the paper bill:** the portal is usually more current (recent payments/adjustments); trust it after confirming the last-payment line explains the difference.
- **F2 Payment fails/declines:** verify funding-account balance and card expiry; retry once; then pay via the alternate channel so the due date isn't missed while investigating.
- **F3 Paid twice (double-click, or both autopay and manual):** most billers auto-credit the next cycle; call to request a refund instead if the amount is large.
- **F4 Confirmation received but biller claims non-payment later:** the confirmation number and bank debit record are the proof — supply both; the biller traces the payment.

## Verification

The confirmation number is saved, the funding account shows exactly one debit for the intended amount, and the biller's portal shows the balance paid with no late flag by the due date.

## Variations

- Rent to a private landlord: bank transfer with the reference the landlord specifies; the bank transfer record replaces the confirmation number.
- `us`: paper-check bill-pay by banks still exists — delivery can take ~5 business days; schedule further ahead.

## Safety & privacy

Medium risk: money and account numbers. Fake "bill due" emails imitate real billers — the rule from step 2 (type the URL from the paper bill) is the protection. Keep confirmations until the next statement closes the loop.
