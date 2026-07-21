---
name: set-up-a-fraud-alert
domain: finance
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Place a fraud alert on your credit file so lenders are warned to verify identity before opening new credit.

## Preconditions

- You can identify yourself to at least one major credit bureau.
- You have a phone number where lenders can reach you for verification.
- You know whether you need an initial fraud alert, extended fraud alert, or active-duty alert where available.
- You understand that a fraud alert is not the same as a full credit freeze.

## Steps

1. **Choose one credit bureau.** In systems like the United States, contact one major bureau because it must notify the others. → *Expect:* you have the official bureau website or phone number.
2. **Open the fraud-alert request.** Use the bureau's official fraud alert, identity theft, or credit protection page. → *Expect:* the page describes alert types and duration.
3. **Select the alert type.** [BRANCH: initial alert | extended alert | active-duty alert] choose the one that matches your situation and documentation. → *Expect:* the form shows the expected expiration period.
4. **Enter identity details.** Provide name, address, date of birth, national ID digits if required, and contact phone. → *Expect:* the bureau can match your credit file.
5. **Upload documents if required.** For extended alerts, provide the official identity-theft report or required proof. → *Expect:* the upload or mail instructions confirm the accepted document type.
6. **Submit the alert request.** Review the phone number carefully before final submission. → *Expect:* the bureau accepts the request or gives a reference number.
7. **Save confirmation.** Download or screenshot the alert confirmation, expiration date, and any case number. → *Expect:* you can prove when the alert was placed.
8. **Check the other bureaus.** Wait the stated transfer time, then confirm alerts appear at the other major bureaus. → *Expect:* all relevant credit files show an active fraud alert.
9. **Decide whether to freeze too.** If you want to block most new credit, set up freezes in addition to the alert. → *Expect:* you understand the alert warns lenders while a freeze blocks access until thawed.
10. **Record renewal date.** Add a calendar reminder before the alert expires. → *Expect:* you will be prompted to renew if risk remains.
11. **Answer verification calls carefully.** If a lender calls, verify the lender through a known number before sharing information. → *Expect:* you do not disclose data to an unknown caller.
12. **Monitor reports.** Review credit reports or alerts for accounts opened despite the warning. → *Expect:* any suspicious application is found quickly.

## Decision points

- You already know your identity was stolen → choose extended alert if your locale supports it and you have the report.
- You only suspect exposure → use an initial alert and consider a freeze.
- You need to apply for credit soon → a fraud alert may be less disruptive than a freeze, but lenders may call to verify.
- Your phone number is compromised → fix carrier security before listing that number for verification.

## Failure modes & recovery

- **F1 Bureau cannot match you:** detect identity questions failing, recover by using mail verification with ID and address proof.
- **F2 Other bureaus missing alert:** detect no alert after the transfer window, recover by placing alerts directly with each bureau.
- **F3 Wrong callback number:** detect confirmation showing an old number, recover by updating the alert immediately.
- **F4 Confused with freeze:** detect new credit still possible, recover by adding full credit freezes.
- **F5 Expired alert:** detect no active alert on a report, recover by renewing before continuing fraud cleanup.

## Verification

Each relevant credit bureau shows an active fraud alert with the correct contact phone number and an expiration date you have recorded.

## Variations

- United States: an initial fraud alert generally lasts one year, while an extended alert requires an identity-theft report.
- Active-duty military: an active-duty alert can reduce prescreened credit offers while deployed.
- No credit file: the bureau may require mail documents before creating or flagging a file.
- Business credit: business bureaus may have separate alert or monitoring processes.

## Safety & privacy

A fraud alert reduces risk but does not stop every lender. Use official bureau sites, avoid paid lookalike services unless intentionally chosen, and combine alerts with freezes when preventing new accounts matters most.
