---
name: set-up-parental-controls-on-an-account
domain: accounts
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: [accounts/log-in]
status: draft
last_verified: 2026-08-25
---

## Goal

You configure age-appropriate account controls for a child or teen, including content limits, spending controls, privacy settings, and recovery access.

## Preconditions

- You are the parent, guardian, or authorized account manager.
- The child has an account or child profile supported by the service.
- You know the child's age, device type, and the controls you intend to apply.

## Steps

1. **Open the family or parental-control settings.** Look for Family, Parent dashboard, Supervision, Screen time, Content restrictions, or Child account. → *Expect:* the service shows managed child profiles or an option to add one.
2. **Add or select the child's account.** Link the child profile, send an invite, or sign in on the child's device as required. → *Expect:* the child account appears under your family or supervision dashboard.
3. **Set age and content limits.** Choose ratings, app categories, search filters, communication limits, or web restrictions that match the child's age and household rules. → *Expect:* the dashboard shows active content restrictions.
4. **Set purchase and spending controls.** Require approval for purchases, disable in-app purchases, set spending limits, or remove saved payment methods. → *Expect:* purchases require approval or are blocked.
5. **Configure privacy and contact settings.** Limit public profiles, location sharing, friend requests, direct messages, and discoverability where supported. → *Expect:* strangers have reduced ability to contact or find the child.
6. **Set time limits if needed.** Configure device schedules, app limits, bedtime, or downtime windows. → *Expect:* the account shows active time rules with correct days and times.
7. **Secure parent access.** Use a strong parent password and 2FA so the child or others cannot change controls. → *Expect:* control changes require parent authentication.
8. **Test from the child's device.** Try an age-restricted app, purchase, contact request, or time-limit boundary. → *Expect:* the control behaves as configured.

## Decision points

- The child is a teen → prefer transparent rules and review reports together rather than only hidden monitoring.
- The service does not support child accounts → use device-level controls and avoid falsifying birth dates when it affects legal protections.
- Safety risk involves contact from a specific person → block and report that account in addition to general controls.

## Failure modes & recovery

- **F1 Controls not applying:** detect unrestricted access on the child device → confirm the child is signed into the managed account and sync is working.
- **F2 Purchase still succeeds:** detect a charge without approval → remove payment methods, request a refund, and check family purchase settings.
- **F3 Child bypasses controls:** detect alternate account, browser, VPN, or device use → address the bypass directly and secure devices at the operating-system level.
- **F4 Parent locked out:** detect lost parent password or 2FA → recover the parent account before attempting more changes.

## Verification

The family dashboard shows the child account with active content, purchase, privacy, and time controls, and a test from the child device confirms the restrictions work.

## Variations

- Apple, Google, Microsoft, Nintendo, Sony, Meta, and streaming services all use different names and scopes for family controls.
- `us`: children's privacy rules may affect account creation and parental consent for users under 13.
- Schools: school-managed devices may override or limit family controls.

## Safety & privacy

Medium risk because controls affect a child's privacy, safety, spending, and access. Confirm you are authorized to manage the account, keep parent credentials secure, and use monitoring in a way that matches the child's age and safety needs.
