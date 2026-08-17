---
name: set-up-a-legacy-contact-for-your-accounts
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Designate trusted legacy contacts or account recovery instructions so family can handle important digital accounts if you die or become incapacitated.

## Preconditions

- You can sign in to the accounts you want to configure.
- You have chosen a trusted person and discussed the responsibility with them.
- You use a password manager or have a secure place for emergency instructions.

## Steps

1. **Choose priority accounts.** Start with Apple, Google, Meta/Facebook, Microsoft, password manager, cloud storage, email, financial, and domain registrar accounts. → *Expect:* you have a prioritized account list.
2. **Confirm the contact's identity.** Verify the legacy contact's current email, phone number, and legal name. → *Expect:* you will not send access instructions to an outdated contact.
3. **Add platform legacy contacts.** [BRANCH: Apple | Google | Facebook] use Apple Account > Sign-In and Security > Legacy Contact, Google Inactive Account Manager, or Facebook Memorialization Settings. → *Expect:* the platform shows the selected contact or inactive-account plan.
4. **Save access keys or instructions.** Store any generated access key, recovery code, or written instruction in your password manager or estate documents. → *Expect:* the contact can find the instructions without seeing your passwords today.
5. **Document accounts without legacy tools.** For services without legacy contacts, record the service name, account email, billing impact, and support process. → *Expect:* your executor can identify what exists and whom to contact.
6. **Avoid sharing live passwords casually.** Use emergency access features or sealed instructions instead of texting passwords. → *Expect:* everyday account security is preserved.
7. **Review annually.** Check contacts after relationship changes, moves, new phone numbers, or account changes. → *Expect:* legacy contacts and instructions remain current.

## Decision points

- Password manager supports emergency access → use it for broad account discovery.
- Financial or legal accounts are involved → align digital instructions with estate documents and local law.
- Contact is not comfortable with the role → choose someone else before adding them.
- Account contains sensitive photos or messages → decide what should be deleted, memorialized, or transferred.

## Failure modes & recovery

- **F1 Contact cannot accept invitation:** detect pending or bounced invite → verify their account email and resend.
- **F2 Access key lost:** detect missing platform key → generate a new key and replace the stored instructions.
- **F3 Account list outdated:** detect unknown billing or missing service → update the inventory during annual review.
- **F4 Instructions expose passwords:** detect plain-text secrets in email or shared docs → move them to a password manager or sealed document.

## Verification

Each priority account either shows a configured legacy contact/inactive-account plan or appears in a secure instruction list, and the trusted contact knows where the instructions are.

## Variations

- Apple: legacy contact access requires the access key and death certificate.
- Google: Inactive Account Manager can notify contacts and share selected data after inactivity.
- Password managers: emergency access features vary and may include waiting periods.

## Safety & privacy

Medium risk because this touches identity, private data, and estate access. Discuss consent, avoid live password sharing, and keep emergency instructions secured.
