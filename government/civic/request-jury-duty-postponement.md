---
name: request-jury-duty-postponement
domain: government
subdomain: civic
locale: [generic, us]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You ask the court to move a jury service date before the deadline and keep proof that the request was submitted or granted.

## Preconditions

- Jury summons with juror ID, court name, service date, reporting location, and response deadline.
- Calendar showing unavailable dates and acceptable alternate dates.
- Supporting documents if the court requires proof, such as travel booking, medical note, school schedule, or employer letter.

## Steps

1. **Read the summons completely.** Identify the court, juror number, service date, response deadline, and postponement instructions. → *Expect:* you know exactly where and when to respond.
2. **Check eligibility for postponement.** Courts often allow one postponement for hardship, scheduling conflict, student status, caregiver duties, medical need, or travel, but local rules control. → *Expect:* your reason fits an allowed category or needs explanation.
3. **Choose new dates carefully.** Pick dates when you can actually serve and avoid known travel, exams, medical procedures, or work deadlines. → *Expect:* you have one or more realistic alternate service windows.
4. **Submit through the required channel.** [BRANCH: online juror portal, enter juror ID and request postponement | phone, call the jury office | mail, send the signed summons section and proof] → *Expect:* the court receives a complete request before the deadline.
5. **Attach proof if required.** Upload or include only the document that supports the conflict. → *Expect:* the evidence matches the reason stated.
6. **Save the request confirmation.** Keep the portal confirmation, email, call log, mailed copy, or certified mail receipt. → *Expect:* you can prove the request was made on time.
7. **Wait for the court's decision.** ⚠️ *Irreversible:* do not skip the original report date unless the court confirms postponement or the summons explicitly says a submitted request pauses reporting. → *Expect:* you receive a granted, denied, or pending status.
8. **Record the new service date.** If granted, add the new date, check-in instructions, and any call-in requirements to your calendar. → *Expect:* the updated jury obligation is calendared.

## Decision points

- The service date is tomorrow or today → call the jury office immediately; online requests may be too late.
- You need excusal, not postponement → use the court's excusal process and evidence requirements instead.
- You never received a decision → assume you must appear or call the jury office unless the portal clearly says otherwise.
- You moved out of the jurisdiction → ask the court how to submit proof of new residence.

## Failure modes & recovery

- **F1 Request denied:** detect a denial notice → report as instructed or contact the jury office about emergency options.
- **F2 Portal cannot find juror ID:** detect login failure → check the summons for court division and ID format, then call the jury office.
- **F3 Missed response deadline:** detect an overdue summons → contact the court immediately and follow instructions to avoid contempt or penalties.
- **F4 No confirmation received:** detect no email or status change → take a screenshot of submission if possible and call before the reporting date.

## Verification

The court portal, email, letter, or jury office confirms postponement and shows the new service date, or confirms the original date still applies.

## Variations

- `us`: jury systems are local, state, or federal; each court sets its own postponement limits and proof rules.
- `federal court`: use the federal district court's eJuror or summons instructions.
- `phone-only court`: write down the clerk's name, date, time, and exact decision.

## Safety & privacy

Medium risk because ignoring a summons can create legal consequences. Do not assume a request is granted until the court says so, and redact unrelated medical or employment details from supporting documents.
