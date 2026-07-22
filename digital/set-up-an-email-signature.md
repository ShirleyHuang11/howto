---
name: set-up-an-email-signature
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Outgoing email ends with a short, readable signature that gives people the right name, role, and contact details without cluttering replies.

## Preconditions

- You can sign in to the email app or webmail account.
- You know the name, role, organization, phone number, and links you want to share.
- You can send a test email to yourself or another account.

## Steps

1. **Draft the core signature.** Write two to four lines: name, role or team, organization if needed, and one contact method. → *Expect:* the signature is readable without scrolling.
2. **Keep links as text.** Use normal linked text for website, scheduling page, or profile links instead of image-only badges. → *Expect:* the signature still makes sense if images are blocked.
3. **Avoid heavy formatting.** Use plain fonts, one optional divider, and no large logo unless your workplace requires it. → *Expect:* the signature looks clean in a narrow message pane.
4. **Open signature settings.** In your email app, find Settings > Signature or Settings > See all settings > Signature. → *Expect:* you see an editor for new messages and sometimes replies.
5. **Paste the main signature.** Add the short version for new messages and save it as the default for the account. → *Expect:* a new compose window inserts the signature automatically.
6. **Create a reply variant.** [BRANCH: full signature | reply signature] use the full version for new threads and a one-line version for replies, such as name plus phone. → *Expect:* replies stay compact.
7. **Set a mobile version.** In the phone email app, replace "Sent from my phone" with a short signature or turn the mobile signature off. → *Expect:* mobile messages no longer add a generic footer.
8. **Send a test.** Email yourself from web and mobile, then view the result on a phone and a computer. → *Expect:* line breaks, links, and contact details display correctly.

## Decision points

- You handle external customers → include role, organization, and one reliable contact method.
- You mostly email friends or classmates → name only, or no signature, may be better.
- Your employer provides a required template → use it, but still check the reply and mobile versions.

## Failure modes & recovery

- **F1 Signature duplicates in replies:** detect when a thread shows repeated full blocks, recover by setting a shorter reply signature.
- **F2 Images show as attachments:** detect when recipients see logo files attached, recover by removing image logos or using hosted links.
- **F3 Wrong account uses signature:** detect when personal mail gets a work footer, recover by setting signatures per account.
- **F4 Links break:** detect when a test click opens the wrong page, recover by editing the hyperlink target, not only the visible text.

## Verification

A new email and a reply from each device show the intended signature, with correct contact details and working text links.

## Variations

- `gmail`: signatures are under See all settings > General > Signature and can be assigned separately for new emails and replies.
- `outlook`: signatures can be app-specific, so check both desktop Outlook and Outlook on the web.
- `mobile-only`: keep the signature to one or two lines because phone clients often wrap long contact blocks badly.

## Safety & privacy

Do not include home addresses, personal phone numbers, pronouns, credentials, or legal disclaimers unless you deliberately want every recipient to receive them. A signature is copied into forwarded threads.
