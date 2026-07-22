---
name: schedule-an-email-to-send-later
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min-10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

An email is composed, scheduled for the intended future time, verified in the queued folder, and still cancelable before it sends.

## Preconditions

- An email account in a mail app or webmail service that supports scheduled send.
- The recipient address, message, attachments, and intended send date and time zone.

## Steps

1. **Compose the email normally.** Add recipients, subject, body, signature, and attachments before scheduling. → *Expect:* the draft is complete and ready to send.
2. **Proofread before scheduling.** Check names, dates, links, attachments, and whether reply-all is appropriate. → *Expect:* no obvious correction remains.
3. **Open schedule send.** [BRANCH: Gmail | Outlook | Apple Mail or other] Use the arrow beside Send, Schedule send, Delay delivery, or Send Later option. → *Expect:* a date and time picker appears.
4. **Choose the send time.** Pick the intended date, local time, and time zone if the app shows one. → *Expect:* the scheduled time displays clearly before confirmation.
5. **Confirm scheduling.** Click or tap Schedule, Send later, or OK. → *Expect:* the message leaves Drafts and moves to Scheduled, Outbox, or Send Later.
6. **Verify the queued message.** Open the scheduled folder and confirm recipient, subject, attachments, and send time. → *Expect:* the message is queued for the intended time.
7. **Edit or cancel if needed.** Open the scheduled message before send time, cancel scheduled send, edit the draft, then reschedule. → *Expect:* the old queued version is gone or replaced.
8. **Keep the account available.** Leave internet and account access normal; some desktop clients send only when the app or device is online. → *Expect:* the service or app can send at the scheduled time.

## Decision points

- Webmail service handles scheduled send in the cloud → the message can send even if your computer is off.
- Desktop app stores delayed mail locally → keep the app open and connected or use webmail instead.
- Recipient is in another region → schedule by their working hours and confirm the time zone shown by the app.

## Failure modes & recovery

- **F1 Message still in Drafts:** detect no scheduled folder entry, recover by using the schedule send menu again and confirming the final button.
- **F2 Wrong time zone:** detect the queued time is off, recover by canceling and rescheduling with the displayed time zone checked.
- **F3 Attachment missing:** detect no attachment icon in the queued message, recover by canceling, attaching the file, and rescheduling.
- **F4 Local client did not send:** detect the message remains in Outbox after time passed, recover by opening the app, reconnecting internet, or rescheduling from webmail.

## Verification

The scheduled folder shows the email queued for the intended date, time, recipients, and attachments.

## Variations

- Gmail: Schedule send is under the arrow beside Send on web and the three-dot menu on mobile.
- Outlook: Delay Delivery, Schedule Send, or Send Later wording varies between classic, new, web, and mobile clients.
- Apple Mail: Send Later requires the device to be online at the scheduled time on some setups.

## Safety & privacy

Scheduled emails can send after context changes, such as a canceled meeting or resolved dispute. Recheck sensitive messages before the send time and cancel any queued mail that should no longer go out.
