---
name: file-a-police-report-online
domain: government
locale: [generic]
interface: web
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Submit a non-emergency police report through the correct official portal and keep proof that the agency received it.

## Preconditions

- The incident is not happening now, no one is in immediate danger, and no urgent medical help is needed.
- You know the incident type, date, approximate time, location, and whether there are suspects, witnesses, vehicles, or serial numbers.
- You have photos, screenshots, receipts, account records, or other evidence ready to upload.
- You have contact information where an officer or records clerk can reach you.

## Steps

1. **Confirm online reporting is allowed.** Read the police department's online reporting rules for your incident type, location, dollar limits, suspect information, and evidence. → *Expect:* you know the incident can be reported online or that you must call/visit instead.
2. **Identify the correct jurisdiction.** Match the incident location to city police, county sheriff, campus police, transit police, or state patrol. → *Expect:* the portal belongs to the agency responsible for that address.
3. **Gather incident details.** Prepare names, phone numbers, addresses, dates, item descriptions, values, serial numbers, license plates, and a short factual timeline. → *Expect:* the report can be completed without guessing.
4. **Open the official report form.** Use the agency website, not an ad or third-party form, and create an account only if required. → *Expect:* the page shows the agency name, online report categories, and privacy notice.
5. **Complete the narrative.** State what happened, when, where, who was involved, and what evidence exists; avoid speculation or legal conclusions. → *Expect:* the narrative is clear enough for an officer to understand the event.
6. **Upload supporting files.** Attach photos, screenshots, invoices, serial-number records, or identity-theft documents if the portal accepts them. → *Expect:* each upload shows as attached or queued.
7. **Review and submit.** Verify spelling, contact details, incident address, dates, and dollar amounts before filing. ⚠️ *Irreversible:* false police reports can carry criminal penalties, so correct uncertain statements before submitting. → *Expect:* the portal returns a temporary report number, confirmation page, or email receipt.
8. **Save the confirmation.** Download or print the receipt, copy the report number, and save the submitted narrative and attachments. → *Expect:* you can prove when and where the report was filed.
9. **Follow agency instructions.** Watch for approval, rejection, officer contact, or a request for an in-person statement. → *Expect:* you know the next status check date and response method.

## Decision points

- Emergency, threat, injury, active crime, or suspect still nearby → call emergency services or the local non-emergency number instead of using the portal.
- Incident happened in another city or county → file with that jurisdiction, even if you live elsewhere.
- Portal rejects the category → use the listed non-emergency number or records counter instructions.
- Insurance needs a final report number → wait for the approved number, because temporary numbers may not satisfy claims.

## Failure modes & recovery

- **F1 Wrong jurisdiction:** detect a rejection or "outside city limits" message → recover by filing with the agency for the incident address and keep the rejection notice.
- **F2 Portal times out:** detect lost form data or session expiry → recover by drafting the narrative offline, then paste into a fresh session.
- **F3 Evidence too large:** detect upload size or file-type errors → recover by compressing images, converting to PDF/JPG, or noting that evidence is available on request.
- **F4 Report rejected:** detect an email saying online reporting is unavailable → recover by calling the non-emergency line and giving the temporary report number.
- **F5 No follow-up:** detect no confirmation after the stated review window → recover by contacting records or online-reporting support with the temporary number.

## Verification

You have an official confirmation, temporary or final report number, incident summary, and saved copy of every file submitted.

## Variations

- `us`: online reporting commonly covers theft, vandalism, lost property, harassing calls, and identity theft when no suspect is present.
- `traffic-crash`: many jurisdictions use a separate crash-report portal with driver, insurance, and vehicle fields.
- `identity-theft`: some agencies issue an identity-theft report needed for credit bureaus and creditors.
- `jurisdiction-specific`: dollar thresholds, incident categories, and response timelines vary by city, county, campus, and state.

## Safety & privacy

Police reports may become public records and can include addresses, phone numbers, allegations, and victim information. Share only truthful facts, redact private copies before sending to insurers, and use emergency channels for immediate danger.
