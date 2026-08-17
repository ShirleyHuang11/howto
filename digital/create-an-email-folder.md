---
name: create-an-email-folder
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create an email folder or label to organize related messages.

## Preconditions

- You are signed in to your email account.
- You know the name and purpose of the folder or label.

## Steps

1. **Open folder controls.** Find the folder, label, or mailbox list in your mail app. → *Expect:* existing folders or labels are visible.
2. **Choose create.** Click or tap `New folder`, `Create label`, `Add mailbox`, or the plus button. → *Expect:* a naming dialog or text field appears.
3. **Name the folder.** Enter a short, clear name. → *Expect:* the typed name appears without spelling errors.
4. **Choose its location.** If asked, place it under the account or parent folder where you want it. → *Expect:* the location preview or parent folder is correct.
5. **Save the folder.** Click or tap `Create`, `Save`, or `Done`. → *Expect:* the new folder or label appears in the folder list.
6. **Move a test email if needed.** Drag or move one relevant message into the folder. → *Expect:* the message appears when the folder is opened.

## Decision points

- You want one email in multiple categories → use labels if your app supports them.
- You need strict storage separation → use folders rather than labels.
- You want automatic organization → create a rule or filter after the folder exists.

## Failure modes & recovery

- **F1 Name already exists:** detect an error or duplicate → choose a more specific name.
- **F2 Folder created under wrong account:** detect it appears in the wrong mailbox tree → move it if supported or recreate it in the correct account.
- **F3 Message disappears after moving:** detect it is not in the expected folder → search for the message and move it again.

## Verification

The new folder or label is visible in the mail app, and a moved test message appears inside it.

## Variations

- `gmail`: folders are labels; one message can have multiple labels.
- `outlook`: folders usually move messages into one location.
- `apple-mail`: use Mailbox > New Mailbox.

## Safety & privacy

Folder names can reveal projects, clients, health matters, or personal topics to anyone viewing your mailbox. Use neutral names on shared devices.
