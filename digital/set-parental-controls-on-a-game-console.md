---
name: set-parental-controls-on-a-game-console
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A game console uses a family account setup with age limits, spending controls, screen time rules, and chat settings that match the child's needs.

## Preconditions

- You have administrator access to the console or platform account.
- The child has or will have a separate child account.
- You know the child's age and the household rules for games, spending, and online play.

## Steps

1. **Update the console.** Install pending system updates before changing account controls. → *Expect:* parental-control menus match current platform options.
2. **Create or open the family group.** Sign in as the adult organizer and add the child's account to the family. → *Expect:* the child appears under family members.
3. **Set age limits.** Choose content ratings for games, apps, videos, and web access based on age and maturity. → *Expect:* games above the rating require approval or are blocked.
4. **Require purchase approval.** Turn on spending limits, wallet restrictions, or adult approval for purchases. → *Expect:* the child cannot buy games or add-ons without permission.
5. **Set screen time.** [BRANCH: schedule | daily limit] choose allowed hours, total time per day, or both. → *Expect:* the console shows when play is allowed.
6. **Adjust chat and multiplayer.** Limit voice chat, text chat, friend requests, user-generated content, and cross-play as needed. → *Expect:* communication settings match the household rule.
7. **Protect the adult account.** Set a console passcode or require the adult password before changing controls. → *Expect:* the child cannot disable restrictions from the console.
8. **Test with the child account.** Try launching a blocked game, making a purchase, and opening chat. → *Expect:* restrictions trigger exactly where expected.

## Decision points

- The child needs online play with known friends → allow multiplayer but restrict chat and friend requests.
- Spending is the main concern → require approval and remove saved payment methods from the child account.
- Different children share a console → create separate child accounts instead of one shared profile.

## Failure modes & recovery

- **F1 Controls apply to wrong profile:** detect when the child can bypass limits, recover by assigning restrictions to the child's actual account.
- **F2 Adult account left unlocked:** detect when settings can be changed without a password, recover by adding a passcode and signing out.
- **F3 Game blocked unexpectedly:** detect a suitable game asking for approval, recover by approving that title or adjusting age rating.
- **F4 Purchases still go through:** detect a completed child purchase, recover by removing saved payment, enabling approval, and requesting a refund if eligible.

## Verification

When signed in as the child, over-age content, unapproved purchases, out-of-hours play, and restricted chat are blocked or require adult approval.

## Variations

- `nintendo-switch`: the Parental Controls mobile app is often the easiest way to manage play time and restrictions.
- `playstation`: Family Management controls age levels, spending, communication, and play time.
- `xbox`: Microsoft Family Safety manages Xbox and Windows controls through child accounts.

## Safety & privacy

Parental controls affect communication, spending, location-like presence, and social access. Tell children what is restricted, protect adult credentials, and review settings as the child matures.
