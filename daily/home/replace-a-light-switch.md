---
name: replace-a-light-switch
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A like-for-like light switch is replaced safely, with power verified off before touching conductors and the wiring restored correctly.

## Preconditions

- Replacement switch with the same type and rating: single-pole, 3-way, dimmer, or smart switch as applicable.
- Screwdrivers, non-contact voltage tester, optional multimeter, wire stripper, and flashlight.
- Access to the breaker panel.
- Comfort stopping and calling an electrician if wiring does not match the expected pattern.

## Steps

1. **Identify the switch type.** Remove nothing yet; note whether one switch or multiple switches control the light → *Expect:* you know whether the replacement is single-pole, 3-way, dimmer, or smart.
2. **Turn the breaker off.** Switch off the breaker controlling the circuit; ⚠️ *Irreversible:* touching live wiring can cause serious injury, so do not continue until power is proven off → *Expect:* the light controlled by the switch no longer turns on.
3. **Verify dead.** Test the switch, cover screws, and wires with a voltage tester before touching them → *Expect:* the tester shows no voltage on all conductors in the box.
4. **Remove the cover and photograph wiring.** Take clear photos of wire colors, screw colors, and terminal positions → *Expect:* you have a reference showing every connection.
5. **Label special wires.** Mark common, traveler, line, load, neutral, or ground if present [BRANCH: single-pole | 3-way | smart switch] → *Expect:* wires can be returned to equivalent terminals.
6. **Move wires to the new switch.** Transfer one wire at a time to the matching screw or approved clamp → *Expect:* bare copper is fully under the terminal with no loose strands.
7. **Ground the switch.** Attach the bare or green ground wire to the green screw if present → *Expect:* the metal yoke is grounded when a ground is available.
8. **Mount and restore power.** Fold wires neatly, screw the switch into the box, install the cover, then turn the breaker on → *Expect:* the switch sits straight and the breaker stays on.
9. **Test operation.** Turn the light on and off from every control location → *Expect:* the light works normally and no buzzing, heat, or flicker appears.

## Decision points

- Tester shows voltage after breaker is off → stop and find the correct breaker.
- Box contains unfamiliar wiring, aluminum wire, or no ground where required → call a qualified electrician.
- Smart switch requires neutral and none is present → use a no-neutral model approved for the load or choose a standard switch.
- Breaker trips after installation → turn it off and recheck wiring before any further attempt.

## Failure modes & recovery

- **F1 Wrong switch type:** detect missing terminals or wrong behavior, recover by buying the matching switch type.
- **F2 Reversed 3-way common:** detect switches only work in one position, recover by using the photo to put common on the common screw.
- **F3 Loose connection:** detect flicker, buzzing, or heat, recover by turning power off and tightening the terminal.
- **F4 Nicked conductor:** detect cut copper strands, recover by trimming and stripping a fresh end.
- **F5 Unknown live feed:** detect unexpected voltage in the box, recover by stopping and calling an electrician.

## Verification

With the cover installed, the switch controls the light correctly from all locations, the breaker stays on, and the switch does not buzz or feel warm after several minutes.

## Variations

- Dimmer: confirm LED compatibility and load rating.
- 3-way: the dark common screw matters more than wire color.
- Older homes: wire colors may not follow modern expectations.
- Smart switch: follow the manufacturer's neutral, ground, and traveler requirements exactly.

## Safety & privacy

High electrical risk. Breaker off is not enough by itself; verify dead before touching wiring, and stop if the box does not match the photos or the replacement instructions.
