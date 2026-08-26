---
name: write-a-post-meeting-recap
domain: communication
subdomain: correspondence
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You send a short recap that records decisions, owners, deadlines, and open questions so everyone leaves with the same understanding.

## Preconditions

- Meeting notes, agenda, or transcript.
- The attendee list and any people who need the recap but were absent.
- Agreement on where tasks are tracked, if the team uses a project tool.

## Steps

1. **Review notes immediately after the meeting.** Pull out decisions, action items, deadlines, and unresolved questions while the discussion is fresh. → *Expect:* raw notes are reduced to the items people need.
2. **Write a specific subject line.** Include the meeting topic and date, such as "Recap: Vendor migration planning, Aug 25." → *Expect:* recipients can find the recap later.
3. **Lead with outcomes.** Summarize the main decisions in one short paragraph or bullets. → *Expect:* a reader can understand what changed without reading every detail.
4. **List action items with owners and dates.** Use "Owner - task - due date" and avoid assigning work to groups without a named person. → *Expect:* every next step has a single accountable owner.
5. **Call out open questions.** Identify who will resolve each one or when it will be revisited. → *Expect:* uncertainty is visible rather than buried.
6. **Invite corrections by a deadline.** Ask recipients to reply if anything is wrong or missing. → *Expect:* silence after the deadline reasonably means the recap stands.
7. **Send and update the tracking system.** Add tasks or links where the team actually works. → *Expect:* the email and task board match.

## Decision points

- Sensitive topic discussed → send only to authorized recipients and omit unnecessary details.
- No decisions were made → frame the recap around discussion points and next steps instead.
- Disagreement remains → label it as unresolved rather than pretending consensus exists.

## Failure modes & recovery

- **F1 Missing owner:** detect an action item assigned to "team" or "everyone" → name one owner or ask the group to assign one.
- **F2 Incorrect decision recorded:** detect a correction from a participant → send a revised recap promptly with the corrected decision.
- **F3 Recap too long:** detect recipients asking what matters → move background to links and keep decisions/actions at the top.
- **F4 Private information included:** detect sensitive personnel, legal, or customer details in a broad email → recall if possible and resend a sanitized version.

## Verification

The recap is sent to the correct recipients and contains decisions, action items with owners and due dates, open questions, and a correction path.

## Variations

- Team with task software: link to the project board and create tasks before sending the recap.
- External clients: keep tone more formal and include only agreed commitments, not internal debate.
- Example:
  "Thanks all. We agreed to keep the March launch date and reduce scope to the core import flow. Maya will send the revised timeline by Friday; Alex will confirm vendor pricing by Tuesday. Please reply by noon tomorrow with corrections."

## Safety & privacy

Low risk, but a recap can become a business record. Do not include confidential, legal, personnel, or medical details unless the recipient list is authorized and the wording has been checked.
