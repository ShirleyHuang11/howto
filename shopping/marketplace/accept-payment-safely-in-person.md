---
name: accept-payment-safely-in-person
domain: shopping
subdomain: marketplace
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You accept in-person payment for a marketplace sale only after confirming the funds are real, final enough for the item value, and matched to the buyer and item.

## Preconditions

- A buyer, item, agreed price, and meetup plan.
- Your chosen payment methods set up before the meeting.
- A way to verify payment independently, such as your banking app, payment app, or cash-counting process.

## Steps

1. **Set payment terms before the meetup.** Tell the buyer which methods you accept, whether exact cash is required, and that the item is released only after you verify payment. → *Expect:* the buyer knows the payment rule before traveling.
2. **Choose a safe verification setup.** Meet where you have signal, lighting, cameras, and enough time to open your own app or count cash. → *Expect:* you can verify funds without pressure or poor connectivity.
3. **Inspect the buyer's payment attempt calmly.** [BRANCH: cash | instant payment app | platform in-person checkout] Watch for the agreed amount, correct recipient, and no unusual refund or overpayment story. → *Expect:* the attempted payment matches the sale terms.
4. **Verify in your own account.** Count cash yourself or open your own app from your phone; never rely on the buyer's screenshot, email, or sound notification. → *Expect:* your account or hand-counted cash shows the full agreed amount.
5. **Handle overpayment or third-party payment as a stop sign.** Decline any request to refund extra money, accept a "business account upgrade" fee, or release the item before funds clear. → *Expect:* suspicious payment patterns end the transaction instead of continuing.
6. **Give a simple receipt for higher-value sales.** Include date, item, serial number if relevant, amount paid, payment method, and "sold as described" where lawful. → *Expect:* both parties have a basic record of what changed hands.
7. **Release the item only after confirmation.** ⚠️ *Irreversible:* once the buyer leaves, recovery is unlikely; confirm the money first, then hand over the item. → *Expect:* item handoff occurs after verified payment.
8. **Record and secure proceeds.** Move cash out of public view or leave the meetup area before reorganizing money; screenshot your own settled receipt if useful. → *Expect:* proceeds are secured and the listing can be marked sold.

## Decision points

- Payment app shows pending, review, hold, or reversible status → keep the item until the status is acceptable for the item value.
- Buyer wants to pay from someone else's account → require the payer to be present or use cash/platform checkout.
- High-value item → prefer bank lobby, platform escrow, or another method with stronger verification.
- Buyer pressures you to hurry → pause or cancel; urgency is common in scams.

## Failure modes & recovery

- **F1 Fake payment screen:** detect a polished screenshot or app animation but no incoming funds → refuse release and ask for a verifiable method.
- **F2 Counterfeit cash:** detect suspicious bills or mismatched feel/security features → meet at a bank or reject the bills.
- **F3 Reversal after handoff:** detect a chargeback or unauthorized-payment claim → submit receipt, messages, meetup evidence, and item photos to the payment provider.
- **F4 Poor signal:** detect inability to load your own account → move to a location with signal or reschedule; do not release based on trust.

## Verification

The full agreed payment is confirmed by cash in hand or by your own account showing the incoming payment, and the item is released only after that confirmation.

## Variations

- Cash sale: exact bills reduce change handling and counterfeit risk.
- Payment app sale: use only accounts you control and know how to verify.
- Platform checkout: follow the platform's in-person completion flow exactly to preserve seller protection.

## Safety & privacy

Medium risk because money and physical safety are involved. Meet publicly, do not reveal unnecessary banking details, refuse overpayment/refund schemes, and keep the item until your own verification succeeds.
