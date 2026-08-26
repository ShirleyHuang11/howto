---
name: request-records-from-a-past-provider
domain: healthcare
subdomain: navigation
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

You obtain medical records from a previous provider and send them to yourself or a new clinician.

## Preconditions

- Provider or facility name, approximate treatment dates, and location.
- Your legal name used at the time, date of birth, contact information, and ID if requested.
- The receiving clinician's fax, portal, mailing address, or secure email if records should be sent directly.

## Steps

1. **Identify the records needed.** Specify visit notes, immunizations, labs, imaging reports, images, medication history, operative reports, or the full chart. → *Expect:* the request is specific enough for records staff.
2. **Find the records request process.** Check the provider website for "medical records," "health information management," or "release of information." → *Expect:* you have the correct form or portal workflow.
3. **Complete the authorization.** Provide identity details, date range, records requested, recipient, delivery method, expiration date, and signature. → *Expect:* the form is complete and signed.
4. **Submit through the approved channel.** Upload, fax, mail, portal-message, or deliver the form as instructed. → *Expect:* you receive a confirmation, fax receipt, portal message, or copy of the sent request.
5. **Ask about fees and timing.** Confirm whether patient-directed electronic copies are free or low cost and when to expect delivery. → *Expect:* cost and processing timeframe are known.
6. **Track the request.** Save the date, method, confirmation, and phone number for follow-up. → *Expect:* you can prove when and how you requested records.
7. **Verify the received file.** Check that the patient name, dates, provider, and requested documents are present. → *Expect:* the records match the request.
8. **Forward securely if needed.** Send records through a portal, encrypted method, fax, or direct provider-to-provider channel. → *Expect:* the new clinician confirms receipt.

## Decision points

- Records are urgently needed for care → ask the new clinician to request them directly and mark the request urgent.
- Provider closed or merged → contact the successor practice, hospital system, state licensing board, or records custodian.
- You need imaging itself, not just the report → request the image files or imaging portal access.

## Failure modes & recovery

- **F1 Request rejected:** detect returned form for missing signature, date, or recipient → correct the form and resubmit.
- **F2 Wrong patient or date range:** detect missing visits or mismatched identifiers → provide former name, address, and exact dates.
- **F3 Records delayed:** detect no response by the stated deadline → call release of information and document the follow-up.
- **F4 New doctor cannot open files:** detect unreadable CD or portal link → ask for a different format or direct transfer.

## Verification

The requested records have been received by you or the destination clinician, the date range is correct, and the receiving office confirms they can access them.

## Variations

- `us`: HIPAA gives patients a right to access most records, usually within 30 days; some state rules are faster or more specific.
- Mental health notes: psychotherapy process notes may be treated differently from regular treatment records.
- Minors or deceased patients: legal authority, guardianship, executor status, or next-of-kin rules may be required.

## Safety & privacy

Medium risk because medical records contain sensitive identity and health information. Use secure delivery, verify recipient addresses and fax numbers, and keep copies in a private location.
