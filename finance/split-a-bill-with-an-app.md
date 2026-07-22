---
name: split-a-bill-with-an-app
domain: finance
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Split a shared bill with an app so everyone can see what they owe, pay securely, and settle without confusion.

## Preconditions

- Everyone agrees to use the chosen app or another documented payment method.
- You have the receipt, total paid, tax, tip, discounts, and who consumed what.
- You know whether anyone paid cash or already covered part of the bill.
- You can verify recipients by username, phone number, or email.

## Steps

1. **Pick the app.** Choose a payment or bill-splitting app everyone can access and that supports your currency and country. → *Expect:* participants know where the split will be tracked.
2. **Create the expense.** Enter merchant, date, total amount, currency, and who paid. → *Expect:* the app shows one shared expense.
3. **Choose split method.** [BRANCH: even split | itemized split] divide equally for simple bills, or assign items, tax, tip, and discounts to specific people. → *Expect:* each person's share is calculated.
4. **Review special adjustments.** Add shared appetizers, service charges, delivery fees, coupons, deposits, or cash contributions. → *Expect:* the app total matches the receipt total.
5. **Verify recipients.** Confirm names, avatars, phone numbers, or emails before requesting or sending money. → *Expect:* no payment is addressed to the wrong person.
6. **Send requests or payments.** Request money if you paid, or pay your share if someone else paid. → *Expect:* the app shows pending, paid, or settled status.
7. **Add a clear note.** Include the event, date, and item if helpful. → *Expect:* recipients can recognize the charge.
8. **Chase politely if needed.** Send one reminder after a reasonable interval and mention the exact amount and bill. → *Expect:* the recipient gets a clear reminder without a duplicate request.
9. **Settle and archive.** Mark cash payments as paid and close the expense after everyone is settled. → *Expect:* the group balance returns to zero or agreed state.

## Decision points

- The bill includes alcohol, tax, or tip → itemize if fairness matters more than speed.
- Someone cannot use the app → record cash or bank transfer manually in the split.
- The app charges fees → choose a fee-free method when possible.
- The group disagrees → use the receipt and state the calculation before sending requests.

## Failure modes & recovery

- **F1 Wrong recipient:** detect by unfamiliar profile or disputed request, recover by cancelling before payment and resending to the verified account.
- **F2 Receipt total mismatch:** detect by app total not matching the receipt, recover by checking tax, tip, discounts, and fees.
- **F3 Duplicate request:** detect by two pending requests for one person, recover by cancelling one and messaging the group.
- **F4 Cross-border issue:** detect by unavailable app or unexpected conversion fee, recover by using bank transfer or cash equivalent.

## Verification

The app shows the expense total matching the receipt and each participant marked paid, pending, or intentionally settled another way.

## Variations

- `us`: common apps differ by bank and region, and instant transfers may carry fees.
- `uk`: bank transfers are common and account confirmation may help verify recipients.
- `eu`: SEPA transfers, local wallets, and currency conversion rules vary by country.

## Safety & privacy

Low risk for small social bills, but payment apps expose contact data, notes, and transaction history. Verify recipients before paying and avoid writing sensitive details in payment notes.
