---
name: flag-an-important-email
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Mark an email as important so it is easier to find or follow up later.

## Preconditions

- The email is visible in your inbox, search results, or thread view.
- Your email app supports flags, stars, pins, or importance markers.

## Steps

1. **Open or select the email.** Click, tap, or checkbox the message you want to mark. → *Expect:* the message is highlighted or open.
2. **Find the marker control.** Look for a flag, star, pin, importance marker, or more-options menu. → *Expect:* the marking control is visible.
3. **Apply the marker.** Click or tap the flag, star, or equivalent action. → *Expect:* the message shows the selected marker.
4. **Confirm follow-up visibility.** Open the flagged, starred, important, or pinned view if your app has one. → *Expect:* the marked email appears in that view.

## Decision points

- You need a deadline → create a task, reminder, or snooze instead of only flagging.
- You need a category → use labels or folders in addition to a flag.
- The message is from an unsafe sender → do not open attachments just to decide whether to flag it.

## Failure modes & recovery

- **F1 Marker missing:** detect no flag or star is visible → use the message menu or enable the column in settings.
- **F2 Email not in flagged view:** detect the view is empty → refresh or check whether your app uses a different name such as Starred or Important.
- **F3 Too many flagged messages:** detect the marker no longer helps prioritize → clear old flags or move action items to a task list.

## Verification

The email displays a flag, star, pin, or importance marker and appears in the corresponding filtered view.

## Variations

- `gmail`: use the star or More > Mark as important.
- `outlook`: use the flag for follow-up or pin for inbox priority.
- `apple-mail`: use the flag button or Message > Flag.

## Safety & privacy

Flags can reveal priority if someone else can view your mailbox, but they do not send any notice to the sender.
