---
name: install-a-smart-lock
domain: housing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Install a smart lock that physically locks correctly, connects to the app, has working access codes, and has a battery-dead entry plan.

## Preconditions

- You are allowed to modify the door lock and have landlord or owner approval if needed.
- The smart lock is compatible with the door thickness, deadbolt type, backset, and phone platform.
- You have the original keys, new lock parts, batteries, screwdriver, phone, and account access.
- The existing door closes and deadbolts smoothly before installation.

## Steps

1. **Check compatibility before removing anything.** Confirm deadbolt style, bore holes, door thickness, handedness, and Wi-Fi or hub requirements. → *Expect:* the lock kit matches the door and network setup.
2. **Document the old lock.** Photograph the inside, outside, latch, strike, and screw positions. → *Expect:* you can restore the old hardware if needed.
3. **Remove old hardware with the door open.** Take off the thumb turn, exterior cylinder or keypad area, and mounting plate while keeping the latch supported. → *Expect:* the deadbolt opening is exposed and undamaged.
4. **Mount the smart lock hardware.** Install latch, exterior keypad, cable, mounting plate, and interior motor exactly as the guide specifies. → *Expect:* parts sit flush and cables are not pinched.
5. **Calibrate bolt travel.** Run the app or lock calibration while the door is open, then again closed if required. → *Expect:* the motor learns full locked and unlocked positions.
6. **Pair the app and update settings.** Add the lock to the account, apply firmware updates, set auto-lock carefully, and name the door. → *Expect:* the app shows the lock online or locally reachable.
7. **Create access codes.** Add unique codes for household members and temporary codes for guests or workers. → *Expect:* each code opens the lock and can be revoked individually.
8. **Test every entry method.** Try app, keypad, physical key, inside thumb turn, and voice or hub access if enabled. [BRANCH: works | jams] adjust before relying on it. → *Expect:* all intended methods operate reliably.
9. **Plan for battery failure.** ⚠️ *Irreversible:* do not throw away or seal away the backup key until you have tested it and stored it outside the locked area. → *Expect:* a battery-dead plan exists, using backup key, external battery contacts, or trusted access.

## Decision points

- Door deadbolt binds by hand → fix alignment before installing a motorized lock.
- Rental or shared door → confirm whether app-based access logs and code changes are allowed.
- Wi-Fi lock drains batteries quickly → use a hub, bridge, or lower-power mode if supported.
- Guests need access → use expiring codes instead of sharing your main code.

## Failure modes & recovery

- **F1 Motor stalls or jams:** detect grinding, failed lock status, or partial bolt travel → realign strike and recalibrate.
- **F2 Lock will not pair:** detect app timeout → move phone closer, check hub, replace batteries, and reset only per manual.
- **F3 Code opens at wrong time:** detect active stale code → revoke it and audit all codes.
- **F4 Battery dies:** detect keypad unresponsive → use backup key or emergency power contacts, then replace batteries.
- **F5 App account compromised:** detect unknown users or events → change password, revoke codes, enable two-factor authentication if available.

## Verification

The smart lock locks and unlocks from keypad, app, inside control, and backup key, reports correct status, and has a tested battery-dead access method.

## Variations

- `retrofit-lock`: interior-only models keep the exterior keyway and often avoid changing keys.
- `rental`: choose reversible hardware and preserve original lock parts.
- `hub-required`: test remote locking only after hub placement is stable.
- `cold-climate`: use high-quality batteries rated for low temperature if the lock is exposed.

## Safety & privacy

Smart locks combine physical security with account security. Use unique codes, remove old guests, secure the app account, and keep a backup key accessible outside the locked home. Medium risk comes from lockout, weak installation, battery failure, and access logs revealing household routines.
