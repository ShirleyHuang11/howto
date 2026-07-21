---
name: avoid-a-wire-transfer-scam
domain: finance
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Avoid sending a wire transfer to a scammer by verifying the recipient and payment instructions before any money leaves.

## Preconditions

- You have received wire instructions, a payment request, or a change to previous instructions.
- You have a known contact channel for the real recipient, such as a saved phone number, signed contract, or in-person contact.
- You have not relied only on an email, text, chat, or caller-provided number.
- You understand wire transfers can be difficult or impossible to reverse.

## Steps

1. **Pause the payment.** Treat urgency, secrecy, or changed instructions as a reason to slow down. → *Expect:* no transfer has been submitted.
2. **Identify the payment context.** Note whether this is a house closing, vendor invoice, payroll, family request, investment, or executive instruction. → *Expect:* you know who should independently confirm it.
3. **Compare instructions to prior records.** Check recipient name, bank, routing number, account number, address, and memo against known documents. → *Expect:* any changed field is obvious.
4. **Verify out-of-band.** Contact the recipient using a phone number or channel you already had before the request, not one in the new message. → *Expect:* a trusted person confirms or denies the instructions.
5. **Use a callback for title-company wires.** For real estate, call the title company or closing attorney from the signed engagement letter. → *Expect:* the closing contact verbally confirms exact wire details.
6. **Challenge fake-boss requests.** If a boss or executive asks for a wire, verify through an internal directory, video call, or established approval system. → *Expect:* the request survives normal approval rather than only chat pressure.
7. **Check account-name match.** Ask your bank whether recipient name matching, confirmation of payee, or warning flags are available. → *Expect:* the bank screen does not show a mismatch or unexplained warning.
8. **Send a tiny test only if policy allows.** For large first-time transfers, ask the recipient and bank whether a small test transfer is appropriate. → *Expect:* the recipient confirms receipt through the trusted channel.
9. **Get written internal approval.** For business wires, require the normal approver and a second reviewer for changed instructions. → *Expect:* approval is recorded outside the suspicious email thread.
10. **Submit only verified instructions.** Enter details from the trusted source and review every digit. ⚠️ *Irreversible:* wire transfers may not be recoverable after release, so do not send if any verification is incomplete. → *Expect:* the transfer confirmation matches the verified recipient and amount.
11. **Save the confirmation.** Store the bank confirmation, verified instructions, callback notes, and approver names. → *Expect:* you can prove how the recipient was verified.
12. **Monitor for receipt.** Ask the real recipient to confirm receipt through the trusted channel. → *Expect:* the intended recipient reports the wire arrived.

## Decision points

- Instructions changed by email → stop and verify by phone using a previously known number.
- The requester demands secrecy → treat it as a scam signal and escalate to a manager, bank, or family member.
- The bank warns of mismatch → do not override without independent confirmation.
- You already sent the wire → call the bank's fraud department immediately and request a recall.

## Failure modes & recovery

- **F1 Compromised email thread:** detect familiar tone but changed banking details, recover by calling a known number and ignoring numbers in the thread.
- **F2 Fake-boss pressure:** detect urgent confidential payment demands, recover by using internal approval policy and direct manager verification.
- **F3 Title-company redirect:** detect last-minute closing instructions, recover by calling the title company from original paperwork.
- **F4 Bank recall needed:** detect money sent to wrong account, recover by calling the bank immediately with the confirmation number and filing a fraud report.
- **F5 Social-engineered callback:** detect the caller gives you the number to verify, recover by finding the number from independent records.

## Verification

Before any wire is released, the recipient identity and every account detail have been confirmed through a trusted out-of-band channel and saved with the transfer record.

## Variations

- International wire: verify SWIFT or IBAN, intermediary bank, currency, fees, and sanctions-screening delays.
- Business wire: require dual control, callback logs, and vendor master-file approval.
- Real estate closing: expect scammers to target the last few days before closing.
- Family emergency: verify through a known number or another family member before sending anything.

## Safety & privacy

Wire scams are high risk because the money can disappear quickly. Never rely only on the message that supplied the instructions, and do not let urgency, secrecy, or authority override out-of-band verification.
