---
name: transfer-a-phone-number-to-a-new-carrier
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min-2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Your existing phone number is ported to a new carrier while the old account remains active until the transfer completes.

## Preconditions

- The phone number is active with the old carrier.
- The phone is compatible with the new carrier or you have a new device or SIM.
- You can sign in to the old carrier or contact its official support.
- You know the account holder name, billing address, and any required account security details.

## Steps

1. **Do not cancel the old line.** Keep the old carrier account active until the port finishes. ⚠️ *Irreversible:* canceling first can lose the number; confirm the new carrier has completed the port before closing anything. → *Expect:* the old line still works or is still listed as active.
2. **Collect port details.** Get the old carrier account number, transfer PIN or port PIN, billing ZIP or postal code, and account holder name. → *Expect:* the details are current and copied exactly.
3. **Start with the new carrier.** Open the new carrier's official activation, checkout, store, or support flow. → *Expect:* the new carrier asks whether to keep an existing number.
4. **Enter transfer information.** Provide the phone number and matching old-carrier details. → *Expect:* the new carrier accepts the request or names the mismatch.
5. **Install SIM or eSIM.** Follow the new carrier instructions for physical SIM, eSIM, or device activation. → *Expect:* the phone shows the new carrier or activation pending.
6. **Wait for port completion.** Keep both carriers' messages available and do not repeat the request unless instructed. → *Expect:* calls, texts, and data shift to the new carrier.
7. **Verify the number.** Call and text another phone, then receive a call and text back. → *Expect:* the transferred number sends and receives normally.
8. **Confirm old account closure.** Check the old carrier after the port; the transferred line should close automatically or show final billing. → *Expect:* the old number is no longer active as a billable old-carrier line.

## Decision points

- Port PIN expires -> generate a fresh PIN from the old carrier and update the new carrier request.
- Information mismatch -> compare every character of name, address, account number, and PIN.
- Phone shows SOS or no service after completion -> restart, check SIM or eSIM status, then contact the new carrier.
- Multiple lines share one account -> confirm only the intended number is being transferred.

## Failure modes & recovery

- **F1 Old line canceled early:** number is inactive before porting, contact the old carrier immediately for reinstatement.
- **F2 Port rejected:** new carrier reports mismatch, correct the old-carrier details and resubmit.
- **F3 Two-factor messages fail:** texts do not arrive after port, use backup codes or wait for carrier routing to settle.
- **F4 Final bill surprise:** old carrier bills extra service or device balance, review final bill and dispute errors quickly.

## Verification

The same phone number works for outbound and inbound calls and texts on the new carrier, and the old carrier no longer bills that active line.

## Variations

- `business-account`: an authorized account manager may need to approve the port.
- `prepaid`: account number may be hidden in the app or available only from support.
- `landline-or-voip`: ports can take longer and may require a service address.

## Safety & privacy

High risk because losing control of a number can affect banking and account recovery. Keep the old line active, protect the port PIN, and monitor critical accounts after transfer.
