---
name: recognize-a-fake-invoice
domain: finance
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Decide whether an invoice is legitimate before paying it, especially when details, pressure, or vendor identity look wrong.

## Preconditions

- You have the invoice, email, letter, portal notice, or payment request.
- You can access prior purchase orders, contracts, statements, or vendor records if they exist.
- You have a known contact channel for the vendor or requester.
- You have authority to pause payment until verification is complete.

## Steps

1. **Pause payment.** Do not click payment links or send money while checking the invoice. → *Expect:* no payment has been initiated.
2. **Check the vendor identity.** Compare name, logo, address, tax ID, email domain, and phone number with past records. → *Expect:* differences are visible instead of hidden in the message.
3. **Match the business reason.** Find the order, subscription, shipment, medical visit, repair, or contract tied to the charge. → *Expect:* there is a real event that explains the invoice.
4. **Inspect payment details.** Look for new bank accounts, changed remit-to addresses, personal payment apps, gift cards, or crypto requests. → *Expect:* suspicious payment changes are flagged before payment.
5. **Look for pressure tactics.** Note threats of immediate collection, legal action, account closure, or late fees that do not match normal terms. → *Expect:* urgency is treated as a risk signal.
6. **Verify out-of-band.** Contact the vendor using a saved number, contract, prior invoice, or official portal, not the contact details on the suspect invoice. → *Expect:* a known contact confirms whether the invoice exists.
7. **Confirm amount and due date.** Ask the known contact to verify invoice number, balance, due date, and payment instructions. → *Expect:* details match exactly or the invoice is rejected.
8. **Check internal approvals.** For work invoices, match purchase order, receiving record, approver, and vendor master file. → *Expect:* normal approval evidence exists.
9. **Reject fake invoices in writing.** If fake, mark it disputed or fraudulent and warn relevant accounting or household members. → *Expect:* nobody else pays the same invoice.
10. **Pay only through verified channels.** Use the official portal or saved vendor payment profile. ⚠️ *Irreversible:* bank transfers, gift cards, crypto, and some instant payments may not be recoverable, so never pay blindly. → *Expect:* payment confirmation names the verified vendor and invoice.
11. **Save the review trail.** Keep the invoice, verification notes, and payment confirmation or fraud report. → *Expect:* the decision can be audited later.
12. **Block or report the sender.** Report phishing to your email provider, company security team, or the impersonated vendor. → *Expect:* the sender is blocked or the threat is documented.

## Decision points

- The vendor is unfamiliar → require proof of the order before paying.
- Bank details changed → verify with a known contact and a second approver.
- The invoice is for a domain, listing, or directory you did not order → treat it as likely solicitation or fraud.
- A real vendor confirms compromise → ask for clean instructions through a secure portal.

## Failure modes & recovery

- **F1 Lookalike domain:** detect one-letter changes or unusual top-level domains, recover by contacting the vendor through known records.
- **F2 Real vendor, fake bank:** detect matching invoice text but new bank details, recover by freezing payment and verifying with accounting.
- **F3 Duplicate invoice:** detect an invoice number already paid, recover by sending proof of payment and refusing duplicate payment.
- **F4 Subscription trap:** detect fine print that it is a solicitation, recover by marking it not ordered and not payable.
- **F5 Paid fake invoice:** detect payment to a fraudster, recover by calling the bank immediately and filing a fraud report.

## Verification

The invoice is either confirmed by a known vendor contact with matching amount and payment details, or it is marked fraudulent and no payment is made.

## Variations

- Small business: use a vendor master file and require callback approval for bank changes.
- Household bill: sign in to the official provider portal instead of using links in email.
- Medical invoice: match it to an explanation of benefits before paying.
- International vendor: verify currency, tax details, and bank account changes separately.

## Safety & privacy

Fake invoices exploit routine payment habits. Do not expose bank information to unknown senders, do not call numbers printed only on the suspect invoice, and treat irreversible payment methods as a hard stop until verified.
