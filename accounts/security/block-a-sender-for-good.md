---
name: block-a-sender-for-good
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: basic
est_time: 15min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You stop unwanted email from a sender by blocking, filtering, unsubscribing when safe, and reporting abuse when needed.

## Preconditions

- Access to your email account.
- At least one message from the sender.
- A decision whether the message is legitimate marketing, harassment, or phishing.

## Steps

1. **Classify the unwanted message.** Decide whether it is a legitimate mailing list, spam, phishing, or harassment. → *Expect:* you know whether to unsubscribe, block, report, or preserve evidence.
2. **Use unsubscribe only for legitimate senders.** If the sender is a known company or list you joined, use the built-in unsubscribe link or mail-client unsubscribe button. → *Expect:* you receive an unsubscribe confirmation or the client shows the list as unsubscribed.
3. **Block the sender address.** Use the mail client's block control on the message or add the address to blocked senders. → *Expect:* future messages from that address are sent to spam, trash, or rejected.
4. **Create a deletion or archive filter for repeat patterns.** Match the exact sender, subject pattern, or domain only when it will not catch wanted mail. → *Expect:* the rule is saved and active.
5. **Report phishing or abuse.** Use "Report phishing" for credential theft, or report harassment to the platform, employer, school, or law enforcement if threats are involved. → *Expect:* the report is submitted and the message is flagged.
6. **Preserve evidence before deleting serious messages.** Save headers, screenshots, or original messages when harassment, threats, fraud, or legal issues are involved. → *Expect:* evidence is stored somewhere you control before mail is removed from the inbox.

## Decision points

- Message is from a company you recognize -> unsubscribe first, then block if it continues.
- Message is suspicious or asks for login/payment -> do not click unsubscribe; report phishing and block.
- Sender changes addresses constantly -> filter on stable patterns cautiously, or use provider-level spam reporting.

## Failure modes & recovery

- **F1 Wanted mail gets caught:** a rule deletes legitimate messages -> disable the rule and search trash, spam, and archive for recoverable messages.
- **F2 Sender evades blocks:** similar addresses keep appearing -> block the domain only if safe, or create a keyword rule with narrow criteria.
- **F3 Unsubscribe increases spam:** suspicious sender sends more mail after you click -> stop interacting, report spam, and block.
- **F4 Threats escalate:** messages include threats or stalking -> preserve evidence, stop replying, and contact platform safety teams or local authorities.

## Verification

A test or subsequent message from the blocked sender is routed to spam/trash or does not appear in the inbox, and the block or filter is visible in mail settings.

## Variations

- Gmail: "Block sender" sends future mail to spam; filters can delete or archive matching messages.
- Outlook: blocked senders are managed under Junk email settings.
- Work or school email: persistent spam may need an administrator to block at the mail gateway.

## Safety & privacy

Medium risk because overbroad filters can erase important mail and serious abuse may need evidence. Do not click links in suspicious emails, and preserve threatening or fraudulent messages before deleting them.
