---
name: set-up-parental-controls
domain: digital
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [have-admin-access]
status: draft
last_verified: 2026-07-20
---

## Goal

A child's device and accounts have age-appropriate limits configured through the platform's own family tools, and the child understands the rules well enough that the controls back up a conversation rather than replace it.

## Preconditions

- Admin access to the device and to the family account that will manage it (the parent's account, not the child's).
- The child's real date of birth; age drives most default protections and cannot be faked without weakening them.
- Ten quiet minutes with the child, ideally before you lock anything down.

## Steps

1. **Create or link the child's account under a family group.** Use the OS/platform family tool (Family Sharing, Family Link, Microsoft Family, console family) with the child's true age. → *Expect:* the child account appears as a supervised member under your account.
2. **Have the conversation first.** Tell the child what you are turning on and why, and agree on the rules together. Controls a child does not understand become a game to defeat. → *Expect:* the child can restate the main rule in their own words.
3. **Set content age ratings.** Cap app store, video, and browser content to an age band you have discussed, not the strictest possible setting. → *Expect:* a test search for above-band content is blocked or filtered.
4. **Set screen-time and downtime limits.** Configure a daily time budget and a bedtime "downtime" window; allow the apps a child genuinely needs (calls to family, homework) during downtime. → *Expect:* the device shows the schedule and warns as the limit approaches.
5. **Configure purchase and install approval.** Require your approval for new installs and any purchase. ⚠️ *Irreversible:* in-app purchases can spend real money instantly; turn on "ask to buy" and remove any stored card the child can reach before handing the device over. → *Expect:* a test install request lands on your device for approval.
6. **Tune privacy and communication.** Limit who can contact the child, turn off precise location sharing to strangers, and switch profiles to private where the app allows. → *Expect:* the child's profile is not publicly searchable; contact is restricted to approved people.
7. **Record recovery details and schedule a review.** Save the family account password in your password manager, and put a calendar note to revisit the settings as the child gets older. → *Expect:* credentials stored; a review date set.

## Decision points

- Older teen pushing back → loosen deliberately and explain the trade; controls that outlast trust get bypassed via a friend's device or a second account.
- Shared family device → per-user profiles so each child gets their own age band, rather than one lowest-common setting for everyone.
- Child needs an unfiltered tool for school → allow that specific app rather than dropping the whole filter.

## Failure modes & recovery

- **F1 Child created a second, unmanaged account:** supervision only covers linked accounts; check the device for other logins and bring them into the family group.
- **F2 Limits not enforcing:** the device may need the child signed in to the supervised account, not a guest or parent login; verify the active user.
- **F3 Filter blocks legitimate schoolwork:** add the specific site or app to an allow list rather than lowering the whole content level.
- **F4 Location or contact setting silently reset after an app update:** re-check the sensitive toggles after major updates; treat the review reminder as the safety net.

## Verification

The child's account is supervised under your family group with an age-appropriate content level, a screen-time schedule that actually triggers, purchase approval routed to you, restricted contact and location, and a child who can explain the top rule. The family password is stored and a review is scheduled.

## Variations

- `mobile-app`: iOS Screen Time and Android Family Link cover phones and tablets; set them per child, not per device.
- Game consoles and smart TVs: each has its own family area with separate ratings; a locked phone plus an open console is a common gap.

## Safety & privacy

Medium risk: these tools handle a child's location, contacts, and your payment methods. The controls are a floor, not a substitute for supervision and conversation. Store the managing password where the child cannot reach it, and revisit as the child matures so the limits grow with them rather than becoming something to route around.
