---
name: get-a-copy-of-your-military-records
domain: government
subdomain: civic
locale: [generic, us]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You request official US military service records, such as a DD Form 214 or personnel file, from the correct records custodian and keep a trackable copy of the request.

## Preconditions

- Veteran's full name used during service, branch, approximate dates of service, date and place of birth, and service number or SSN if known.
- Proof that you are the veteran, next of kin, or otherwise authorized if the records are not public.
- A printer or scanner if using Standard Form 180 by mail or fax.

## Steps

1. **Identify the requester status.** Determine whether you are the veteran, next of kin, authorized representative, or a member of the public requesting older records. → *Expect:* you know what proof of authority is required.
2. **Gather service identifiers.** Collect branch, dates of service, date and place of birth, service number, SSN, last unit, and discharge location if known. → *Expect:* you have enough information for the records center to locate the file.
3. **Choose the request method.** [BRANCH: online request, use the National Archives veterans records portal | mail or fax, complete Standard Form 180] → *Expect:* the chosen method matches the record type and requester.
4. **Specify the records needed.** Ask for DD Form 214, separation documents, medical records, full Official Military Personnel File, or replacement medals as needed. → *Expect:* the request names the exact documents.
5. **Sign and date the request.** ⚠️ *Irreversible:* confirm identity details and mailing address before signing because inaccurate requests can be delayed or misdelivered. → *Expect:* the signature and date are present where required.
6. **Submit to the correct address or portal.** Use the address, fax number, or upload instructions shown by the National Archives or SF-180 records location table. → *Expect:* the request is transmitted to the correct custodian.
7. **Save proof of submission.** Keep the portal confirmation, fax confirmation, or mail tracking receipt. → *Expect:* you can prove when and how the request was sent.
8. **Respond to follow-up requests.** Provide authorization, death certificate, proof of relationship, or additional service details if requested. → *Expect:* the records center has what it needs to continue.

## Decision points

- The veteran separated recently → records may still be with the branch, DoD, VA, or an online military portal rather than the National Personnel Records Center.
- The record is more than 62 years old → it may be archival and available to the public under different access rules.
- You need records urgently for burial, medical care, or benefits → mark the urgent reason and follow the National Archives emergency instructions.
- The file may have been affected by the 1973 fire → provide alternate details such as unit, discharge location, and entry place.

## Failure modes & recovery

- **F1 No record located:** detect a negative search response → resubmit with alternate names, service number, unit, dates, and copies of any service documents.
- **F2 Authorization missing:** detect a request for proof of relationship or signature → send the exact authorization document requested.
- **F3 Wrong custodian:** detect a referral or rejection → send the request to the named branch, VA, state archive, or NPRC address.
- **F4 Delay with no update:** detect no response after the posted processing window → contact the records center with the tracking or request number.
- **F5 Records damaged or incomplete:** detect a fire-related or partial-record response → ask for reconstructed records and provide alternate evidence.

## Verification

You have a submission confirmation or tracking receipt, and the requested military record copy, negative search letter, or case response is received from the official custodian.

## Variations

- `us`: the National Archives uses eVetRecs and Standard Form 180 for many veterans' service record requests.
- `next of kin`: proof of death and relationship may be required for non-archival records.
- `state records`: some National Guard or state service records may be held by state agencies.

## Safety & privacy

Medium risk because service records can contain SSNs, health information, and discharge details. Send requests only to official addresses, limit copies shared with third parties, and store DD-214 copies securely.
