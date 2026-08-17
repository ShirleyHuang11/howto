---
name: mark-an-email-as-spam
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Move an unwanted or suspicious email to spam or junk and help future filtering.

## Preconditions

- The suspicious email is visible in your mailbox.
- You do not need to preserve it as evidence before reporting.

## Steps

1. **Select the email.** Click, tap, or checkbox the message without opening attachments or links. → *Expect:* the email is selected.
2. **Choose spam or junk.** Click or tap `Report spam`, `Junk`, `Block`, or the stop-sign icon. → *Expect:* a confirmation or immediate move begins.
3. **Confirm reporting.** If asked, choose whether to report spam, phishing, or just move to junk. → *Expect:* the message leaves the inbox.
4. **Avoid interacting with content.** Do not reply, unsubscribe, open links, or download attachments from suspicious messages. → *Expect:* no external content or attachment is opened.
5. **Check the spam folder.** Open Spam or Junk if you need to confirm where it went. → *Expect:* the email appears there or is hidden from the inbox.

## Decision points

- Message is a scam or credential request → report phishing if the app offers it.
- Message is unwanted but legitimate marketing → unsubscribe only if you trust the sender.
- Message contains threats, harassment, or legal evidence → preserve a copy before marking spam.

## Failure modes & recovery

- **F1 Legitimate email marked spam:** detect future wanted mail in Spam or Junk → mark as Not spam and add the sender to contacts.
- **F2 Spam keeps returning:** detect repeated messages from changing senders → add filters and block domains where appropriate.
- **F3 Report option missing:** detect no spam button → use move to Junk, block sender, or the message menu.

## Verification

The email no longer appears in the inbox and is listed in Spam, Junk, or the provider's reported-spam state.

## Variations

- `gmail`: use Report spam or Report phishing from the message menu.
- `outlook`: use Junk > Block or Report phishing.
- `mobile-app`: long-press the message to select it before choosing spam or junk.

## Safety & privacy

Spam reports may send message content, sender information, and headers to the provider for analysis. Do not open suspicious links or attachments while reporting.
