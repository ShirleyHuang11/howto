---
name: create-an-app-specific-password
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

You create a limited app-specific password for an older mail, calendar, or device app without revealing your main account password.

## Preconditions

- The account supports app-specific passwords.
- Two-factor authentication is enabled if the provider requires it.
- You know the exact app or device that needs the password.

## Steps

1. **Confirm an app-specific password is necessary.** Use this only for apps that cannot use modern OAuth sign-in. → *Expect:* the target app fails normal secure sign-in or explicitly asks for an app password.
2. **Open account security settings.** Navigate to passwords, sign-in methods, app passwords, or security keys. → *Expect:* you find the app-password management page.
3. **Name the password clearly.** Use a label such as "Mac Mail old laptop" or "Scanner SMTP". → *Expect:* the future purpose is obvious in the password list.
4. **Generate the app-specific password.** Confirm the prompt and copy the generated password once. → *Expect:* the provider displays a unique password for that app.
5. **Enter it only in the intended app.** Paste it into the app's password field, not into websites or unrelated apps. → *Expect:* the app connects successfully without your main password.
6. **Store or document appropriately.** Prefer not to store the generated password if it can be revoked and recreated; record the label and date in your password manager. → *Expect:* you can identify and revoke it later.
7. **Remove unused app passwords.** Delete old, unknown, or duplicate app passwords. → *Expect:* only current app-specific passwords remain active.

## Decision points

- App supports modern sign-in -> use OAuth or the provider's normal sign-in instead of app-specific passwords.
- The app is on a shared or untrusted device -> do not create the password; use a trusted app or webmail.
- You suspect compromise -> revoke all app-specific passwords and regenerate only the ones still needed.

## Failure modes & recovery

- **F1 Option is missing:** no app-password menu appears -> enable two-factor authentication or check whether the provider removed support.
- **F2 Password is copied incorrectly:** app rejects the password -> generate a new password and paste it without spaces if required.
- **F3 Wrong app uses the password:** access appears from an unexpected device -> revoke the password immediately and check account activity.
- **F4 Password cannot be viewed again:** provider hides it after creation -> revoke and create a new one.

## Verification

The intended app connects successfully, the provider's security page lists the app-specific password by label, and unused app passwords are revoked.

## Variations

- Google, Apple, Yahoo, and some Microsoft accounts support app passwords only under certain two-factor or account-type conditions.
- Work or school accounts may disable app passwords by administrator policy.
- SMTP devices such as scanners may need app passwords when they cannot use modern authentication.

## Safety & privacy

Medium risk because app-specific passwords can bypass normal two-factor prompts for that app. Create them only for trusted devices, label them clearly, and revoke them when the app or device is retired.
