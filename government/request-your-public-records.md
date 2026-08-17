---
name: request-your-public-records
domain: government
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Submit a public records request to the correct government office and track it to production, denial, or appeal.

## Preconditions

- You can describe the records wanted, the agency likely to hold them, and the date range.
- You know whether you want inspection, electronic copies, certified copies, or paper copies.
- You have proof of identity or authorization if requesting your own protected records.
- You can receive email, mail, portal messages, or phone calls about fees and deadlines.

## Steps

1. **Define the records narrowly.** Write the subject, agency program, names, addresses, case numbers, dates, and document types you want. → *Expect:* the request can be understood without a records clerk guessing.
2. **Find the custodian.** Search the official agency site for "public records", "FOIA", "open records", "records request", or "clerk". → *Expect:* you have the correct portal, email, mail address, or form.
3. **Check exemptions and identity rules.** Read whether the records may be redacted for privacy, law enforcement, personnel, medical, juvenile, or trade-secret reasons. → *Expect:* you know what may be withheld and what proof is needed.
4. **Draft the request.** Ask for existing records, not explanations, and request electronic delivery plus advance notice of fees over a set amount. → *Expect:* the text names the records, date range, format, and fee limit.
5. **Submit through the official channel.** [BRANCH: portal | email | mail | in-person] Send the request and attach ID or authorization only if required. → *Expect:* you receive a tracking number, timestamp, email copy, or stamped receipt.
6. **Calendar the response deadline.** Record the statutory or agency response date and any allowed extension. → *Expect:* you know when a late response becomes actionable.
7. **Respond to fee or clarification notices.** Approve reasonable fees, narrow the request, or clarify search terms in writing. ⚠️ *Irreversible:* paid search or copy fees may be nonrefundable once work begins, so approve only what you accept. → *Expect:* the agency confirms the request remains active.
8. **Review the production.** Check that files open, dates match, redactions are labeled, and withheld records are explained. → *Expect:* you can tell whether the response satisfies the request.
9. **Appeal or close the request.** [BRANCH: complete | incomplete | denied] Save the production if complete, or file the listed appeal/administrative review before the deadline. → *Expect:* the request has a final disposition or an active appeal.

## Decision points

- You want answers to questions → ask for records that would contain the answers, because public-records laws usually require existing documents only.
- The request is broad and expensive → narrow by date range, office, sender, recipient, keyword, or record type.
- Records involve you personally → an identity-verification or privacy-act route may produce more than a general public request.
- Agency says another office holds the records → ask for a referral and submit to the named custodian.

## Failure modes & recovery

- **F1 No acknowledgement:** detect silence past the expected acknowledgement window → recover by forwarding the original request and asking for the tracking number.
- **F2 Overbroad denial:** detect a demand to narrow without specifics → recover by asking which search terms, date ranges, or custodians are causing burden.
- **F3 Excessive fee estimate:** detect fees above your limit → recover by narrowing the request or asking for a fee waiver if allowed.
- **F4 Heavy redaction:** detect withheld text with exemption codes → recover by requesting the exemption log or appealing unsupported redactions.
- **F5 Wrong format:** detect scans, unreadable files, or missing attachments → recover by asking for the native electronic format or replacement files.

## Verification

You have a tracking number and either the requested records, a written denial with appeal rights, or a documented clarification/fee decision still within deadline.

## Variations

- `us-federal`: use FOIA.gov or the agency FOIA office; federal requests can have multi-track processing and administrative appeals.
- `us-state-local`: state open-records laws have different deadlines, fee rules, and appeal offices.
- `personal-records`: medical, tax, school, immigration, and law-enforcement records may use separate privacy statutes or consent forms.
- `certified-copy`: request certification at the start because it may require paper handling and extra fees.

## Safety & privacy

Requests and responses can become public logs. Do not include unnecessary Social Security numbers, medical facts, or account numbers; send identity proof only through the agency's instructed secure channel.
