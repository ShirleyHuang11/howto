---
name: dispute-a-charge-in-an-app
domain: digital
subdomain: transactions
locale: [generic]
interface: mobile-app
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You dispute an incorrect, unauthorized, duplicate, or undelivered charge through the bank, card, or payment app and keep enough evidence to track the case.

## Preconditions

- You can access the financial app that shows the transaction.
- You have checked whether the charge is pending or posted and gathered receipts, cancellation proof, merchant messages, or delivery records.
- You are prepared to answer truthfully; false disputes can lead to account closure or legal consequences.

## Steps

1. **Identify the exact transaction.** Open the posted transaction and confirm merchant descriptor, date, amount, card, and status. → *Expect:* you can distinguish the disputed charge from authorizations, tips, or legitimate duplicates.
2. **Try the merchant path when appropriate.** For non-fraud issues, contact the merchant first and save the response or lack of response. → *Expect:* you have merchant evidence or a reason to escalate directly.
3. **Open the dispute flow.** In the financial app, choose Report a problem, Dispute charge, Get help, or similar. → *Expect:* the app asks for the dispute reason and transaction details.
4. **Choose the accurate reason.** [BRANCH: unauthorized, select fraud/unauthorized and be ready to replace the card | duplicate, select duplicate charge | canceled service, select charged after cancellation | goods not received, select non-receipt] → *Expect:* the selected category matches your evidence.
5. **Upload concise evidence.** Attach receipts, cancellation confirmations, tracking screenshots, merchant chat logs, or saved receipts. → *Expect:* the case file contains documents that directly support the claim.
6. **Submit the dispute.** ⚠️ *Irreversible:* confirm the claim is truthful and the amount is correct before submitting because the bank may contact the merchant and restrict the card. → *Expect:* the app issues a case number, provisional credit notice, or investigation timeline.
7. **Save the case record.** Screenshot or export the case number, submitted reason, amount, and expected response date. → *Expect:* you have a dated record independent of the app screen.
8. **Monitor and respond.** Check messages from the issuer and answer requests for more evidence before deadlines. → *Expect:* the dispute remains open, credited, won, denied, or awaiting your response with clear status.

## Decision points

- Charge is still pending → wait for posting unless the app explicitly allows pending fraud reports.
- Card was stolen or account compromised → lock the card and report fraud immediately.
- Merchant already refunded → track refund status instead of filing a duplicate dispute.
- Dispute amount is partial → specify the incorrect portion, such as missing item or wrong tip.

## Failure modes & recovery

- **F1 Wrong reason selected:** detect case questions that do not fit the facts → contact the issuer quickly to correct the dispute category.
- **F2 Missing evidence deadline:** detect a request you did not answer → upload documents immediately and call support if the deadline passed.
- **F3 Provisional credit reversed:** detect a lost dispute or reversal → read the denial reason and submit new evidence or merchant proof if the issuer allows appeal.
- **F4 Merchant retaliates by closing account:** detect service suspension after dispute → preserve records and resolve any legitimate balance, but do not withdraw a valid fraud dispute under pressure.

## Verification

The app shows a submitted dispute for the correct posted transaction amount, with a case number or investigation status saved, and any required evidence has been uploaded before the stated deadline.

## Variations

- `credit-card`: dispute rights and provisional credits often differ from debit-card timelines.
- `payment-app`: peer-to-peer transfers may have weaker protection; fraud and purchase disputes may be separate flows.
- `travel`: hotels, rental cars, and fuel stations may post adjusted final amounts after pending holds.

## Safety & privacy

Medium risk because disputes affect money, merchant accounts, and fraud records. Submit only truthful claims, keep evidence, lock compromised cards, and avoid uploading documents with unrelated personal data.
