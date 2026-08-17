---
name: cc-and-bcc-an-email
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 2min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Send an email with visible copy recipients in `Cc` and private copy recipients in `Bcc`.

## Preconditions

- You have an email account open in a mail app or webmail.
- You know which recipients should be visible to everyone and which should be hidden.

## Steps

1. **Start the message.** Open a new message or reply draft. → *Expect:* the compose window is open.
2. **Add primary recipients.** Put the people expected to act on the message in `To`. → *Expect:* each primary recipient appears in the `To` field.
3. **Show copy fields.** Click or tap `Cc`, `Bcc`, or `Cc/Bcc` if those fields are hidden. → *Expect:* separate `Cc` and `Bcc` fields are visible.
4. **Add visible copy recipients.** Put people who should be kept informed in `Cc`. → *Expect:* the copied recipients are visible in the `Cc` field.
5. **Add private copy recipients.** Put recipients whose addresses should not be shown to others in `Bcc`. → *Expect:* the private recipients appear only in the `Bcc` field.
6. **Review recipient etiquette.** Confirm everyone in `To` and `Cc` can appropriately see each other's addresses, and use `Bcc` for large groups or privacy-sensitive lists. → *Expect:* no private address is exposed in `To` or `Cc`.
7. **Send the email.** Click or tap `Send` after checking subject and body. → *Expect:* the message leaves the outbox or appears in Sent.

## Decision points

- Large group or announcement → put your own address in `To` and the list in `Bcc`.
- Recipient is expected to act → use `To`, not `Cc`.
- Recipient should not be visible to others → use `Bcc`.

## Failure modes & recovery

- **F1 Bcc field hidden:** detect the field is missing → choose `Cc/Bcc`, more options, or expand recipient fields.
- **F2 Address in wrong field:** detect a private address in `To` or `Cc` → move it to `Bcc` before sending.
- **F3 Sent with exposed recipients:** detect after sending → send a brief correction and avoid replying to the exposed thread; you cannot retract the exposed addresses from recipients' inboxes.

## Verification

The sent message shows intended people in `To` and `Cc`, and `Bcc` recipients are not visible to other recipients.

## Variations

- `web`: Gmail, Outlook, and Yahoo usually show `Cc` and `Bcc` links beside the `To` field.
- `mobile-app`: recipient fields may expand only after tapping the arrow beside `To`.

## Safety & privacy

Email addresses can reveal identities, affiliations, customers, patients, or private groups. Use `Bcc` for mass email, but do not use it to secretly include someone in a sensitive conversation where transparency is expected.
