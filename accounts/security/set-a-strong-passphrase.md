---
name: set-a-strong-passphrase
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

You replace a weak or reused password with a long, unique passphrase or generated password that is practical to store and use.

## Preconditions

- You can sign in to the account.
- You have a trusted password manager or another secure way to store the new credential.
- You know whether the account has password length or character restrictions.

## Steps

1. **Open password settings.** Go to Security, Login, Password, or Account settings. → *Expect:* the account offers a password-change form.
2. **Generate or choose a strong credential.** Prefer a password manager's random password; if you must memorize it, use several unrelated words with enough length and avoid quotes, names, dates, or predictable substitutions. → *Expect:* the new credential is long, unique, and not reused anywhere else.
3. **Save it in the password manager first.** Create or update the entry with the exact site domain and username. → *Expect:* the new credential is stored before the old one is replaced.
4. **Change the password.** Enter the current password and the new credential. → *Expect:* the provider confirms the password changed.
5. **Update signed-in devices if prompted.** Re-sign in only on devices you control. → *Expect:* trusted devices work with the new password.
6. **Enable or confirm 2FA.** Add authenticator, passkey, or hardware key protection if available. → *Expect:* the account requires more than the password for new logins.
7. **Search for reuse.** Check your password manager for other accounts using the old password or similar variants and replace them. → *Expect:* the old password is not reused on important accounts.

## Decision points

- Account rejects long passwords or special characters → use the maximum allowed length and a unique random value within its rules.
- You need to share access with a team → use the password manager's sharing feature or role-based access instead of sending the password in chat.
- You suspect compromise → sign out all devices after changing the password.

## Failure modes & recovery

- **F1 New password not saved:** detect password manager has only the old value → use the current signed-in session to reset it again and save carefully.
- **F2 Password pasted into wrong site:** detect a domain mismatch → change the password immediately on the real site.
- **F3 Account locks after change:** detect repeated failed sign-ins → wait out lockout or use recovery, then verify the stored password.
- **F4 Password reused elsewhere:** detect password-manager reuse warnings → replace the reused credential on every affected account.

## Verification

The account accepts the new unique passphrase or generated password, the password manager stores it for the correct domain, and 2FA is enabled or confirmed.

## Variations

- Password managers: generated 16-24 character random passwords are usually better than human-made passphrases when you do not need to memorize them.
- Work accounts: policy may require rotation, minimum length, or banned-password screening.
- Devices and apps: some old apps need app-specific passwords rather than the main password.

## Safety & privacy

Medium risk because a weak or reused password can expose money, identity, and private data. Do not share passwords by email or chat, and never enter a password after following an unverified login link.
