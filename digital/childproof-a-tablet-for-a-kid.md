---
name: childproof-a-tablet-for-a-kid
domain: digital
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Configure a tablet so a child can use age-appropriate apps and content while purchases, adult content, location sharing, and settings changes are restricted.

## Preconditions

- You know the tablet passcode and parent account password.
- The child has or can use a child profile where supported.
- You have decided allowed apps, content level, screen time, and purchase rules.

## Steps

1. **Update the tablet.** Install system updates and app updates before setting restrictions. → *Expect:* parental-control options are current.
2. **Create or select a child profile.** [BRANCH: iPad | Android tablet | Amazon Fire] use Family Sharing child account, Google Family Link, or Amazon Kids profile. → *Expect:* the child uses a managed profile or child account.
3. **Set a parent passcode.** Choose a Screen Time, Family Link, or parental-control PIN that the child does not know. → *Expect:* restrictions cannot be changed from the child profile.
4. **Restrict purchases and installs.** Require approval or block app installs, in-app purchases, and paid downloads. → *Expect:* store purchases require parent approval.
5. **Set content limits.** Choose age ratings for apps, movies, websites, games, books, and search filtering. → *Expect:* adult or above-age content is blocked in the child profile.
6. **Configure screen time.** Add downtime, daily limits, bedtime, or school-hour rules. → *Expect:* the tablet shows when use is allowed and limited.
7. **Review privacy permissions.** Disable unnecessary camera, microphone, contacts, Bluetooth, and location access for child apps. → *Expect:* apps have only needed permissions.
8. **Test as the child.** Switch to the child profile and try installing an app, opening a blocked site, and using an allowed app. → *Expect:* blocked actions fail and allowed apps work.

## Decision points

- Very young child → use a dedicated kid profile with a small allowlist rather than broad age filtering.
- School tablet → follow school management rules and avoid removing required apps.
- Video apps are allowed → set content restrictions inside the video app as well as the tablet.
- Child needs messaging → limit contacts and review who can communicate.

## Failure modes & recovery

- **F1 Child can bypass limits:** detect access from parent profile or known passcode → change passcode and disable profile switching without approval.
- **F2 Allowed app blocked:** detect required app unavailable → add it to the allowlist or adjust age rating.
- **F3 Purchases still work:** detect test purchase prompt without approval → check store account and family purchase settings.
- **F4 Web filter misses content:** detect inappropriate page loads → use allowlisted websites or a safer browser mode.

## Verification

From the child profile, age-appropriate apps work, blocked websites and purchases are stopped, screen-time rules display correctly, and parent controls require the parent passcode.

## Variations

- iPad: Settings > Screen Time supports child accounts, app limits, downtime, content restrictions, and purchase controls.
- Android: Google Family Link manages app approvals, screen time, content filters, and location settings.
- Amazon Fire: Amazon Kids profiles provide age filters, time limits, and child-specific libraries.

## Safety & privacy

Medium risk because children can encounter harmful content, make purchases, or expose location and personal data. Test restrictions directly and revisit them as the child grows.
