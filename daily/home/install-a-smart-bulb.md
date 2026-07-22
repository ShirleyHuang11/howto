---
name: install-a-smart-bulb
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min-30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A smart bulb is installed in a compatible fixture, paired to its app, named clearly, and ready for routine control.

## Preconditions

- You have the smart bulb, phone, app account if required, Wi-Fi password, and access to the fixture switch.
- The fixture socket type, bulb shape, wattage equivalent, and indoor or outdoor rating match the bulb.
- Turn the fixture switch off before replacing the bulb; do not use a damaged socket or wet outdoor fixture.

## Steps

1. **Check compatibility.** Confirm socket size, enclosed-fixture rating, dimmer support, and voltage. → *Expect:* the bulb is safe for this fixture.
2. **Turn off the fixture.** Use the wall switch and let any old bulb cool. → *Expect:* the bulb can be touched safely.
3. **Install the bulb.** Screw the smart bulb in by the base, not the glass or diffuser. → *Expect:* the bulb sits snug without forcing.
4. **Turn power on.** Switch the fixture on and leave it on for pairing. → *Expect:* the bulb lights or blinks in setup mode.
5. **Open the app.** Sign in if required and choose add device or add bulb. → *Expect:* the app begins searching or shows setup instructions.
6. **Choose network band.** [BRANCH: 2.4 GHz Wi-Fi | hub or Thread] use 2.4 GHz for most Wi-Fi bulbs, or pair through the required hub or border router. → *Expect:* the bulb appears for pairing.
7. **Pair the bulb.** Follow the app prompts, enter Wi-Fi details if needed, and wait for confirmation. → *Expect:* the app shows the bulb online.
8. **Name and place it.** Give it a room and plain name like "Desk lamp" or "Porch light." → *Expect:* controls are easy to find.
9. **Group if useful.** Add the bulb to an existing room, group, or scene. → *Expect:* grouped controls affect the intended lights only.
10. **Test controls.** Turn the bulb off and on from the app, then adjust brightness or color if supported. → *Expect:* the bulb responds within a few seconds.

## Decision points

- Bulb will not enter pairing mode → power-cycle it using the maker's reset pattern.
- App cannot find the bulb → move the phone closer and confirm 2.4 GHz network access.
- Fixture is on a wall dimmer → use only bulbs rated for that dimmer, or keep the dimmer at full if the maker permits.
- Switch may be turned off by others → use a switch guard or choose a smart switch instead.

## Failure modes & recovery

- **F1 Wrong network:** pairing fails after password entry, connect the phone to the required 2.4 GHz or hub network.
- **F2 Bulb offline later:** app shows unavailable, confirm the wall switch is on and router signal reaches the fixture.
- **F3 Flicker:** bulb flickers in use, remove from incompatible dimmer or enclosed fixture if not rated.
- **F4 App account issue:** setup blocks at sign-in, reset password or use the maker's local setup option if available.

## Verification

The bulb turns on and off from the app, appears in the correct room or group, and still responds after the wall switch has remained on for one minute.

## Variations

- Voice assistants: link the bulb app to the assistant after the bulb works in its native app.
- Outdoor fixtures: use bulbs and fixtures rated for damp or wet locations.
- Hub-based bulbs: pair to the hub first, then expose the hub to other apps.

## Safety & privacy

Low risk: use only compatible fixtures, keep power off while changing bulbs, and understand that smart-light apps may collect device names, schedules, location, and network identifiers.
