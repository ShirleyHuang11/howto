---
name: pay-your-mortgage-online
domain: housing
subdomain: owning
locale: [generic, us]
interface: web
difficulty: basic
est_time: 15min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-02
---

## Goal

You make an online mortgage payment to the correct servicer, for the correct loan, with proof that the payment was submitted and scheduled on time.

## Preconditions

- Your current mortgage servicer name, official website or app, loan number, and login credentials.
- Bank routing and account number or saved payment method.
- Current statement showing amount due, due date, late-fee date, and escrow or shortage amounts if any.

## Steps

1. **Confirm the servicer and URL from trusted records.** Use your statement, closing transfer notice, or saved bookmark; avoid links in unexpected emails. → *Expect:* you are on the legitimate servicer site.
2. **Log in with multifactor authentication.** Verify the displayed borrower name, property address, and loan number. → *Expect:* the account matches your mortgage.
3. **Review the amount due.** Check principal and interest, escrow, fees, late charges, and any optional extra-principal field. → *Expect:* you know exactly what will be paid and how it will be applied.
4. **Choose the payment date.** Schedule before the cutoff and before any late-fee or grace-period deadline. → *Expect:* the site shows a payment date that counts as timely under the servicer's rules.
5. **Select the funding account.** Confirm the bank name, last four digits, and whether the payment is ACH, debit, or another method with fees. → *Expect:* the correct account and any convenience fee are visible.
6. **Review before submitting.** ⚠️ *Irreversible:* once submitted, an ACH payment may be difficult to cancel; confirm amount, date, funding account, and loan number first. → *Expect:* the final review screen matches your intent.
7. **Submit the payment.** Save or print the confirmation number and screenshot. → *Expect:* the portal shows scheduled, pending, or submitted status with a timestamp.
8. **Verify bank and loan posting.** Check the bank withdrawal and mortgage transaction history after processing. → *Expect:* the payment clears and the mortgage balance or next due date updates.

## Decision points

- Servicer recently changed → use the official transfer notice and avoid paying the old servicer after the transfer effective date.
- Payment is close to late deadline → consider phone payment confirmation or expedited method if available.
- You are paying extra principal → ensure the portal applies the extra amount to principal, not future payments.

## Failure modes & recovery

- **F1 Wrong servicer scam:** detect unfamiliar URL or urgent email link → stop, use your statement or call the published servicer number.
- **F2 Payment not posted:** detect bank debit but no mortgage credit → provide confirmation number and bank trace details to the servicer.
- **F3 NSF or returned ACH:** detect returned payment or fee → pay immediately with confirmed funds and ask about fee waiver if appropriate.
- **F4 Extra payment misapplied:** detect funds posted as suspense or next month's payment → request reallocation to principal in writing.

## Verification

You have a confirmation number, the bank account shows the correct debit, and the mortgage portal shows the payment posted to the correct loan with the next due date updated.

## Variations

- `autopay`: confirm draft date, amount type, escrow changes, and how to cancel before enabling.
- `biweekly-payment-plan`: verify whether it is servicer-run, fee-free, and actually applies extra principal.

## Safety & privacy

Medium risk from payment errors, phishing, and bank-account exposure. Use only trusted servicer channels, protect login credentials, and explicitly confirm payment details before submission.
