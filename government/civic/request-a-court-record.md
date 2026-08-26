---
name: request-a-court-record
domain: government
subdomain: civic
locale: [generic, us]
interface: mixed
difficulty: intermediate
est_time: 30min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You locate the correct court record and request an ordinary, certified, or exemplified copy through the court's approved process.

## Preconditions

- Case number if known, or party names, approximate filing date, county, court level, and case type.
- Your ID and relationship to the case if requesting restricted records.
- Payment method for search, copy, certification, or mailing fees.

## Steps

1. **Identify the court that holds the file.** Determine whether the case is federal, state, county, municipal, probate, family, traffic, or appellate. → *Expect:* one clerk's office or online docket system is the likely custodian.
2. **Search the public docket.** Use the court portal, PACER for federal cases, or the clerk's index to confirm case number and available documents. → *Expect:* the case record, docket entry, or no-record result is found.
3. **Decide what copy type you need.** Choose plain copy, certified copy, exemplified copy, transcript, audio, or docket sheet based on the requesting agency's requirement. → *Expect:* the requested copy type matches its intended use.
4. **Check access restrictions.** Family, juvenile, sealed, adoption, mental health, and some criminal records may require a party request, judge order, or ID. → *Expect:* you know whether the record is public or restricted.
5. **Submit the request.** Use the clerk portal, records email, form, mail request, or in-person counter and include case number, document title, date, copy type, delivery method, and contact information. → *Expect:* the clerk acknowledges the request or gives a fee quote.
6. **Pay fees through the official channel.** Pay only the court, authorized vendor, or PACER system. → *Expect:* payment receipt links to the request.
7. **Review the delivered record.** Check case number, document title, pages, seal, certification language, and legibility. → *Expect:* the copy is usable for the receiving party.
8. **Request correction if incomplete.** Contact the clerk with the receipt and describe missing pages, wrong certification, or wrong case. → *Expect:* the clerk reissues or explains the limitation.

## Decision points

- You need a transcript → contact the court reporter or transcript office, not just the clerk.
- The record is sealed or confidential → ask for the procedure to request access; do not assume the clerk can release it.
- You need it for another country → ask whether an exemplified copy or apostille is required.

## Failure modes & recovery

- **F1 No case found:** search terms fail → try alternate names, maiden names, business names, county, or date range.
- **F2 Wrong court:** clerk has no file → ask which court level or county inherited the record.
- **F3 Certification missing:** receiving agency rejects a plain copy → order a certified copy with seal and clerk signature.
- **F4 Restricted access denied:** clerk refuses release → provide proof of party status or file the required motion.

## Verification

You have the requested court record with the correct case number, document name, page count, and certification or seal if ordered.

## Variations

- `us-federal`: use PACER for many federal docket documents; sealed and transcript items follow separate rules.
- `state-local`: county clerks, district courts, and municipal courts use different portals and fee schedules.

## Safety & privacy

Medium risk because court records may contain addresses, financial details, criminal history, or family information. Share only with the party that requires it, and store certified copies securely.
