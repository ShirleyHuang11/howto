---
name: add-a-trusted-contact-for-recovery
domain: accounts
subdomain: security
locale: [generic]
interface: web
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You add a trusted recovery contact or legacy helper so account recovery is easier without giving that person your password.

## Preconditions

- Access to the account's security settings.
- A trusted person who agrees to help with recovery.
- Their correct email, phone number, or account identifier.

## Steps

1. **Confirm the feature's purpose.** Read whether the contact can help recover access, receive emergency codes, or manage legacy access after death. → *Expect:* you understand exactly what authority the contact will and will not have.
2. **Choose a trustworthy contact.** Pick someone reachable, stable, and unlikely to misuse the role. → *Expect:* you have one or more contacts who have agreed.
3. **Open recovery or security settings.** Look for trusted contacts, recovery contacts, account recovery, legacy contacts, or emergency access. → *Expect:* the account displays a page for adding helpers.
4. **Add the contact using the exact identifier.** Enter their email, phone, username, or platform account. → *Expect:* the contact appears as invited, pending, or active.
5. **Ask the contact to accept if required.** Have them approve the role from their own account or email. → *Expect:* the status changes from pending to active.
6. **Review what they can see.** Confirm whether they can access recovery codes, receive notifications, or request emergency access. → *Expect:* permissions match what you intended.
7. **Store a note in your password manager.** Record who the contact is and when to review the setting. → *Expect:* you can later audit or remove stale contacts.

## Decision points

- The service grants emergency access to saved passwords -> choose a person with strong security habits and a clear agreement.
- The contact changes phone number or email -> update the setting immediately.
- You need estate planning, not routine recovery -> use legal documents and legacy-contact features, not informal password sharing.

## Failure modes & recovery

- **F1 Contact invite expires:** status remains pending -> resend the invitation and confirm the recipient address.
- **F2 Wrong person added:** an outdated or typoed email is used -> remove it immediately and add the correct contact.
- **F3 Contact cannot help during recovery:** they lost their own account access -> add a second trusted contact or update recovery methods.
- **F4 Permissions are broader than expected:** contact can access sensitive data -> remove the contact or choose a narrower recovery method.

## Verification

The account security page shows the trusted contact as active or accepted, and your password manager note records the contact and review date.

## Variations

- Apple: Account Recovery Contacts can help generate a recovery code but do not receive your password.
- Password managers: emergency access may release vault access after a waiting period unless you deny it.
- Social platforms: trusted-contact features change often; use current security settings and backup codes as a fallback.

## Safety & privacy

Medium risk because a recovery contact can influence account access. Never give them your password, confirm the exact person before adding, and review trusted contacts after relationship changes.
