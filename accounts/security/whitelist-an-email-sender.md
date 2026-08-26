---
name: whitelist-an-email-sender
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

You mark a legitimate sender as trusted so important messages arrive in your inbox instead of spam or quarantine.

## Preconditions

- Access to your email account.
- The sender's exact email address or domain from a message you trust.
- Confidence that the sender is legitimate, not a spoofed phishing message.

## Steps

1. **Verify the sender first.** Open a known legitimate message or get the address from the organization's official website. → *Expect:* you have the exact sender address or domain to allow.
2. **Check the current message location.** Look in spam, junk, promotions, focused inbox, or quarantine. → *Expect:* you find where the sender's mail is currently landing.
3. **Mark the message as not spam.** Use the mail client's "Not spam", "Not junk", or equivalent control. → *Expect:* the message moves to the inbox or normal mail view.
4. **Add the sender to contacts or safe senders.** Add the exact address, or the domain only if every address from that domain is trusted. → *Expect:* the address or domain appears in the safe sender list.
5. **Create an allow filter if needed.** Add a rule that messages from the sender are never sent to spam and are labeled or moved to the inbox. → *Expect:* the rule is saved and enabled.
6. **Send or request a test message.** Ask the sender to resend, or trigger a normal notification such as a password-reset email. → *Expect:* the new message lands in the intended inbox or folder.

## Decision points

- The sender domain is broad, such as a free email provider -> whitelist only the exact address, not the whole domain.
- The message asks for passwords, payment, or urgent action -> verify through the organization's website or phone number before trusting it.
- You use a work or school account -> quarantine rules may be controlled by administrators; request allowlisting through IT.

## Failure modes & recovery

- **F1 Mail still goes to spam:** a new message is junked after allowlisting -> check blocked sender lists, competing filters, and admin quarantine.
- **F2 Wrong address allowed:** a lookalike address was added -> remove it immediately and add the exact legitimate address.
- **F3 Domain allowlist is too broad:** unrelated mail from the domain floods the inbox -> replace the domain rule with specific sender addresses.
- **F4 Sender authentication fails:** mail client warns DKIM, SPF, or DMARC failed -> do not whitelist until the sender fixes its mail configuration or confirms another address.

## Verification

A newly received message from the sender appears in the inbox or chosen folder, and the sender is visible in contacts, safe senders, or an active allow rule.

## Variations

- Gmail: use "Report not spam", add the sender to Contacts, and create a filter with "Never send it to Spam".
- Outlook: use Junk settings, Safe senders and domains, and rules.
- Corporate email: administrators may need to release quarantined messages or allow a sender tenant-wide.

## Safety & privacy

Medium risk because whitelisting a malicious or spoofed sender can bypass normal protections. Confirm the sender independently before allowing it, and never whitelist a domain just because one message looks familiar.
