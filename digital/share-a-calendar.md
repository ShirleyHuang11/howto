---
name: share-a-calendar
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Another person can see or use the correct calendar with the permission level you intend, and you know how to revoke access later.

## Preconditions

- You can sign in to the calendar account that owns the calendar.
- You know the recipient's email address or have access to a shareable subscription link.
- You know whether the other person should view only or edit.

## Steps

1. **Choose the exact calendar.** In calendar settings, select the calendar you want to share, not the whole account. → *Expect:* settings show one named calendar.
2. **Review current events.** Check whether private appointments, addresses, notes, or meeting links are visible on that calendar. → *Expect:* you know what the recipient might see.
3. **Pick the sharing method.** [BRANCH: invite by email | share link] use an email invite for named access or a subscription link for read-only viewing when supported. → *Expect:* the sharing panel shows an invite field or link option.
4. **Set permission level.** Choose free/busy only, view details, make changes, or manage sharing based on the recipient's role. → *Expect:* the selected permission appears beside the recipient or link.
5. **Send the invite or link.** Share it through the calendar app or copy the subscription link into a message. → *Expect:* the recipient receives access instructions.
6. **Have them subscribe or accept.** Ask the recipient to accept the invite or add the subscription link in their calendar app. → *Expect:* the calendar appears in their calendar list.
7. **Test visibility.** Create or identify a harmless test event and ask what they can see or edit. → *Expect:* their access matches the permission level.
8. **Record how to revoke.** Return to sharing settings and note where Remove, Stop sharing, or permission changes live. → *Expect:* you can remove access later without searching.

## Decision points

- You need collaboration → grant edit access only to people who should change events.
- You need privacy → share free/busy only or move sensitive events to a separate private calendar.
- You shared a public link → assume anyone with the link may see it until you disable the link.

## Failure modes & recovery

- **F1 Recipient cannot open calendar:** detect when the invite errors or link does nothing, recover by checking the email address and using the recipient's supported calendar app.
- **F2 Too much detail visible:** detect when titles or notes are exposed, recover by lowering permission or moving sensitive events elsewhere.
- **F3 Edits happen unexpectedly:** detect changed or deleted events, recover by reducing permission to view-only and restoring events from calendar trash if available.
- **F4 Old access remains:** detect former recipients still listed, recover by removing them or regenerating the share link if the platform allows it.

## Verification

The recipient can see the selected calendar at the intended permission level, and you can identify the control that revokes their access.

## Variations

- `google-calendar`: sharing controls are easiest on the web under Settings for my calendars.
- `apple-calendar`: iCloud calendars support private sharing by Apple ID and public read-only links.
- `outlook`: organization policies may limit external sharing or hide details by default.

## Safety & privacy

Calendar entries can reveal location, habits, health appointments, school schedules, meeting links, and travel. Share the least permission that works and remove access when it is no longer needed.
