---
name: find-your-polling-place
domain: government
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Find the correct polling place for your address and election, then prepare the documents and access information needed to vote.

## Preconditions

- You know your current residential address.
- You know the election date or voting period.
- You can use an official election website, phone line, mailed notice, or local election office.
- You can check accessibility, transport, and identification requirements before leaving.

## Steps

1. **Use the official lookup.** Search the official election office, electoral commission, or local authority polling place tool. → *Expect:* the source is government-run or election-office-run.
2. **Enter your address carefully.** Use residence address, apartment number, postal code, and name if requested. → *Expect:* the lookup returns your assigned polling place or voting district.
3. **Confirm the election.** Make sure the result applies to the specific election, date, and voting method. → *Expect:* the polling place matches the election you plan to vote in.
4. **Record hours.** Note opening time, closing time, early voting dates, and any holiday or runoff schedule. → *Expect:* you know when voting is available.
5. **Check ID rules.** Review accepted identification, proof of address, voter card, or exception process. → *Expect:* you know what to bring and what to do if you lack it.
6. **Check what else to bring.** Bring registration confirmation, sample ballot, required documents, and any allowed assistance forms. → *Expect:* your voting materials are ready.
7. **Review accessibility.** Check accessible entrance, parking, language help, curbside voting, or assistance rights. → *Expect:* access needs have a plan.
8. **Plan arrival.** Choose transport, parking, queue time, and backup timing before polls close. → *Expect:* the travel plan fits voting hours.
9. **Verify before leaving.** Recheck the official source on voting day in case of location changes. → *Expect:* the latest polling place and hours are confirmed.

## Decision points

- Lookup shows no match → call the election office instead of guessing.
- You are assigned to a precinct → go to that place unless official rules allow vote centers.
- You requested a mail ballot → check whether in-person voting requires bringing or cancelling it.
- You need help voting → review assistance and accessibility rights before arrival.

## Failure modes & recovery

- **F1 Wrong precinct:** detect by poll worker saying you are not on the list, recover by calling election officials or requesting provisional options.
- **F2 ID problem:** detect by ID refusal, recover by using accepted alternatives or the official cure process.
- **F3 Location changed:** detect by closed site or notice, recover by checking official emergency updates.
- **F4 Accessibility barrier:** detect by inaccessible entrance or equipment, recover by asking poll workers for the required accommodation process.

## Verification

The official election source confirms your polling place address, election date, voting hours, ID rules, and accessibility plan.

## Variations

- `us`: precinct assignment, vote centers, ID rules, provisional ballots, and poll hours vary by state and county.
- `uk`: polling cards list the polling station, and photo ID rules differ by election and nation.
- `eu`: polling locations, voter cards, residence rules, and accessibility support vary by member state.

## Safety & privacy

Low risk, but voter address and eligibility data are sensitive. Use official lookup tools, avoid posting your full voter details publicly, and report intimidation to election officials.
