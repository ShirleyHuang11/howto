---
name: write-a-nudge-to-a-late-payer
domain: communication
subdomain: correspondence
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You send a polite, firm payment reminder that makes the unpaid amount, due date, and next payment step unmistakable.

## Preconditions

- The invoice, contract, order, rent ledger, or written agreement showing the amount owed.
- Payment instructions and any late-fee terms.
- A record of previous reminders, if any.

## Steps

1. **Confirm the payment is actually late.** Check bank deposits, payment processor status, mailed checks, and invoice terms. → *Expect:* the balance due and days overdue are accurate.
2. **Gather the payment details.** Note invoice number, amount, original due date, and accepted payment methods. → *Expect:* the recipient can pay without asking for missing information.
3. **Write a neutral subject line.** Use "Payment reminder: Invoice 1042 due August 15" or similar. → *Expect:* the message is recognizable and not accusatory.
4. **State the facts and request payment.** Include the amount, due date, and a specific requested payment date. → *Expect:* the ask is clear and easy to act on.
5. **Attach or link the invoice.** Include payment instructions and a contact path for disputes. → *Expect:* the recipient has everything needed to pay or raise a real issue.
6. **Send and schedule a follow-up.** Record when the nudge was sent and the next escalation date. → *Expect:* you have a dated collection trail.

## Decision points

- First reminder and relationship matters → keep it friendly and assume oversight.
- Repeated nonpayment → reference earlier reminders and the contract's late-fee or service-suspension terms.
- Recipient disputes the charge → pause escalation on the disputed portion and resolve the facts in writing.

## Failure modes & recovery

- **F1 Payment already sent:** detect proof of payment or a pending processor transfer → verify your account and thank them once confirmed.
- **F2 Wrong invoice details:** detect an incorrect amount, due date, or recipient → send a corrected apology note and updated invoice.
- **F3 No response:** detect silence after the requested date → send a firmer follow-up or follow the contract's collection process.
- **F4 Legal overreach:** detect threats not allowed by the contract or law → remove them and use accurate consequences only.

## Verification

The reminder has been sent, the invoice details are correct, and the follow-up date is recorded; success is complete when payment posts or the recipient confirms a dispute with specifics.

## Variations

- Freelancer: include a payment link and pause new work only if the contract allows it.
- Rent or regulated debt: follow local notice rules before charging late fees, reporting, or beginning collection.
- Example:
  "Hi Sam, I am following up on Invoice 1042 for $850, due August 15. I may have missed your payment; if so, please send the confirmation. Otherwise, please pay by August 29 using the link below or let me know if there is an issue."

## Safety & privacy

Medium risk because payment messages can affect money and legal rights. Do not share invoice details with unauthorized people, do not threaten consequences you cannot lawfully take, and confirm the debt before escalating.
