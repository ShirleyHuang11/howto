---
name: apply-for-a-social-security-card
domain: government
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Apply for an original or replacement Social Security card through the official agency while protecting the number from misuse.

## Preconditions

- You are applying in a jurisdiction that uses Social Security numbers, such as the United States.
- You know whether the request is original, replacement, corrected, or name-change related.
- You have proof of identity, age, citizenship, immigration status, or name change as required.
- You can use the official agency website, mail, or local office process.

## Steps

1. **Confirm eligibility.** Check official Social Security Administration rules for who may receive a number or replacement card. → *Expect:* the application type and eligibility are clear.
2. **Identify required documents.** List documents proving identity, age, citizenship or lawful status, and legal name change if relevant. → *Expect:* every required evidence category has an acceptable document.
3. **Check replacement limits.** Review annual and lifetime replacement-card limits and exceptions. → *Expect:* you know whether the request counts toward a limit.
4. **Choose the submission path.** [BRANCH: online | in-person | mail] use the official online service if eligible, otherwise prepare for office visit or mail submission. → *Expect:* the correct channel is selected.
5. **Complete the official form.** Enter name, date of birth, place of birth, parents' names if required, citizenship status, and contact details accurately. → *Expect:* the application matches supporting documents.
6. **Submit original or certified documents only if required.** Use the agency's stated document rules and avoid sending irreplaceable records unless required. → *Expect:* documents meet the evidence standard.
7. **Keep proof of submission.** Save confirmation, appointment details, mailing receipt, or office receipt. → *Expect:* you can track the application.
8. **Watch for the card by mail.** Monitor the expected delivery window and secure the mailbox. → *Expect:* the card arrives or the agency gives a status update.
9. **Store the card safely.** Put the card in a secure place and do not carry it daily unless specifically needed. → *Expect:* the number is protected from routine loss.

## Decision points

- You only need the number → do not request a replacement card unless a card is actually required.
- Your name changed → update supporting identity records in the order required by the agency.
- You are outside the issuing country → use the embassy, consulate, or agency international process.
- Documents conflict → correct the source record before submitting if possible.

## Failure modes & recovery

- **F1 Unacceptable document:** detect by agency rejection, recover by using the official document list and certified records.
- **F2 Mail loss:** detect by missed delivery window, recover by contacting the agency and watching for identity misuse.
- **F3 Limit reached:** detect by replacement denial, recover by asking whether an exception applies.
- **F4 Scam site:** detect by fees or non-government domain for a free card, recover by leaving the site and using the official agency.

## Verification

The official application is submitted or appointment is booked, required documents are identified, and the Social Security card or status notice is received.

## Variations

- `us`: the Social Security Administration issues cards, many replacements are free, and online eligibility depends on state, age, and record status.
- `uk`: National Insurance numbers are different from Social Security cards and use a separate process.
- `eu`: social insurance numbers, tax identifiers, and health numbers are country-specific and not interchangeable.

## Safety & privacy

Medium risk because the number can enable identity fraud. Use only official government channels, do not email the number casually, and keep the physical card secured.
