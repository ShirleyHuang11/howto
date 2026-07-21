---
name: report-a-problem-to-the-city
domain: government
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Report a local issue such as a pothole, broken streetlight, missed trash pickup, graffiti, or blocked sidewalk to the correct city service channel.

## Preconditions

- The problem location, ideally with street address, nearest cross street, or map pin.
- A short description and optional photo.
- Access to 311, a city app, city website, or phone service.

## Steps

1. **Make sure it belongs to the city.** Check whether the issue is on public property, a city street, park, sidewalk, or utility area. → *Expect:* you know the likely responsible agency.
2. **Capture the location.** Note address, cross street, landmark, side of street, floor, or GPS pin. → *Expect:* someone who has never been there could find it.
3. **Take a useful photo if safe.** Photograph the issue and nearby context without stepping into traffic or private property. → *Expect:* photo shows both the defect and where it is.
4. **Choose the reporting channel.** [BRANCH: 311 phone | city app | web form] Use the channel your city supports for that issue type. → *Expect:* the channel offers a matching category.
5. **Pick the closest category.** Select pothole, streetlight, sanitation, noise, tree, water leak, or other closest label. → *Expect:* form asks questions relevant to the problem.
6. **Describe the problem plainly.** Include size, severity, when noticed, hazards, and whether access is blocked. → *Expect:* report can be triaged without a callback.
7. **Submit contact details only if needed.** Provide email or phone if you want updates or the city requires it. → *Expect:* required fields are complete without extra personal information.
8. **Save the reference number.** Copy or screenshot the ticket ID after submitting. → *Expect:* you can look up or cite the report later.
9. **Follow up if unresolved.** Check status after the normal service window or report again with the reference number if conditions worsen. → *Expect:* follow-up includes the original ticket.

## Decision points

- Immediate danger such as live wire, gas smell, fire, or injury risk → call emergency services instead of 311.
- Issue is on private property → contact property owner, landlord, utility, or code enforcement as appropriate.
- Report category is missing → choose general service request and describe the exact issue.
- Multiple reports exist → add a new report only if you have new detail or the hazard changed.

## Failure modes & recovery

- **F1 Wrong jurisdiction:** detect city says not responsible, recover by asking for the responsible agency or county/state contact.
- **F2 Vague location:** detect ticket closed as unable to locate, recover with cross street, side of street, landmark, and photo.
- **F3 No reference number:** detect no way to track, recover by checking email confirmation or resubmitting if necessary.
- **F4 Unsafe photo attempt:** detect need to stand in traffic or restricted areas, recover by skipping photo and describing the hazard from safety.

## Verification

You have a submitted city service request with a reference number, location, category, and description accurate enough for a crew to find the issue.

## Variations

- Phone report: ask the operator to repeat the ticket number before ending the call.
- Mobile app: allow location permission only while using the app if you need a map pin.
- Anonymous report: some cities allow it, but you may not receive status updates.

## Safety & privacy

Low risk. Do not trespass or enter traffic for photos, and avoid including faces, license plates, or private interiors unless necessary for the report.
