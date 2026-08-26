---
name: set-up-login-alerts
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

You enable alerts for new or risky sign-ins so you can quickly spot unauthorized account access.

## Preconditions

- You can sign in to the account.
- Your recovery email and phone number are current.
- You can receive email, SMS, push, or authenticator notifications on a device you control.

## Steps

1. **Open notification or security settings.** Look for Security alerts, Login alerts, New sign-in notifications, Account activity alerts, or Notifications. → *Expect:* a settings page lists available account-security notifications.
2. **Enable new-device and new-location alerts.** Turn on alerts for unfamiliar devices, browsers, countries, or IP addresses. → *Expect:* the setting shows enabled for at least one reliable channel.
3. **Enable high-risk account-change alerts.** Turn on alerts for password changes, recovery changes, 2FA changes, payment changes, and connected-app grants if available. → *Expect:* critical security events are selected.
4. **Choose delivery channels you will notice.** Prefer email plus push or authenticator notification; add SMS only if it is the provider's available option. → *Expect:* alerts route to a current mailbox or device you control.
5. **Send or trigger a test alert if possible.** Use the provider's test option, or sign in from a private browser window and verify the alert arrives. → *Expect:* a legitimate alert appears with device, time, and location details.
6. **Review alert wording and sender.** Note the official sender domain or in-app notification style so phishing messages are easier to spot later. → *Expect:* you know what a real alert looks like without needing to click links.
7. **Save the settings and record the date.** Keep the account security page open until the saved state is visible. → *Expect:* the alert settings remain enabled after refresh.

## Decision points

- Alerts are unavailable → use the account's recent-activity page as a recurring manual check.
- You receive an alert you do not recognize → do not click email links; open the service directly and change password plus 2FA.
- SMS is the only alert channel → use it, but keep stronger 2FA enabled because SMS can be vulnerable to SIM swap.

## Failure modes & recovery

- **F1 Alerts do not arrive:** detect no email, push, or SMS after a test → check spam, notification permissions, phone number formatting, and blocked sender lists.
- **F2 Too many alerts:** detect repeated alerts from your normal VPN or browser → mark the device trusted only if it is truly yours.
- **F3 Fake alert email:** detect a scary message with mismatched sender or link → open the service manually in a browser instead of clicking.
- **F4 Alerts sent to old contact:** detect delivery to a stale email or phone → update recovery contact information before relying on alerts.

## Verification

The account shows login and security-change alerts enabled, and a test or recent login produces an alert on a current device or mailbox.

## Variations

- Financial accounts: alerts may be split among security, transactions, profile changes, and card controls.
- Social accounts: login alerts may appear under Privacy, Security, or Where you're logged in.
- Managed accounts: administrators may enforce or suppress some alerts centrally.

## Safety & privacy

Medium risk because alerts expose login metadata and protect identity. Never rely on alert links alone; when responding to a warning, navigate to the account directly or use the official app.
