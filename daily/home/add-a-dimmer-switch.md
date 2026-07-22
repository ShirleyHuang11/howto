---
name: add-a-dimmer-switch
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min-1h
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A compatible wall dimmer is installed on a lighting circuit after power is shut off, verified dead, and the wiring is matched correctly.

## Preconditions

- You have a dimmer rated for the bulb type and load, screwdriver, wire connectors, wire stripper, non-contact voltage tester, and the dimmer instructions.
- You know whether the switch is single-pole or three-way before buying the dimmer.
- ⚠️ *Irreversible:* do not touch conductors unless the breaker is off and all wires test dead.
- Call a licensed electrician for aluminum wiring, no ground, crowded boxes, unknown travelers, smart dimmer neutral questions, flickering not solved by compatibility, or any voltage you cannot make dead.

## Steps

1. **Confirm compatibility.** Match the dimmer to LED, CFL, incandescent, or low-voltage bulbs and keep total wattage within its rating. → *Expect:* the dimmer label supports the installed lights.
2. **Turn off the breaker.** Switch off the lighting circuit breaker and keep the switch unusable while working. → *Expect:* the controlled lights do not turn on.
3. **Test dead.** Test the voltage tester on a live source, check the switch terminals and box wires, then retest the tester. → *Expect:* no target wire shows voltage.
4. **Remove the old switch.** Take off the plate, remove mounting screws, and pull the switch out by the yoke. → *Expect:* wires are visible without strain.
5. **Document wires.** Photograph wire colors, screw colors, common terminal, travelers, neutral bundle, and ground. → *Expect:* the original layout can be restored.
6. **Wire the dimmer.** [BRANCH: single-pole | three-way] connect line, load, ground, and any traveler or common lead exactly per the dimmer instructions. → *Expect:* every connector is tight with no bare copper outside it.
7. **Fold and mount.** Tuck wires neatly, mount the dimmer straight, and attach the wall plate. → *Expect:* the dimmer sits flush without pinching wires.
8. **Restore power.** Turn the breaker on while standing clear of the switch. → *Expect:* the breaker stays on.
9. **Test the range.** Turn lights on, dim from high to low, and set trim if the dimmer has one. → *Expect:* lights dim smoothly without flicker or buzz.

## Decision points

- Bulbs are not dimmable → replace bulbs or use a standard switch.
- Three-way common wire is unclear → stop and call an electrician.
- Box has no grounding path and dimmer requires ground → call an electrician.
- Breaker trips or dimmer heats quickly → shut off power and do not use it.

## Failure modes & recovery

- **F1 Flicker at low setting:** bulbs shimmer or shut off, adjust low-end trim or use compatible dimmable bulbs.
- **F2 Switch works backward in three-way:** toggle logic is wrong, turn power off and recheck common and traveler wiring.
- **F3 Connector loose:** light cuts in and out, turn power off and remake the splice.
- **F4 Dimmer overloads:** faceplate is hot, turn power off and install a properly rated dimmer or call a pro.

## Verification

With the plate installed, the breaker stays on and the lights turn on, dim through the intended range, and remain free of heat, buzz, or visible flicker for five minutes.

## Variations

- Smart dimmers: many require a neutral wire and deeper box space.
- Multi-location dimmers: use matched companion switches specified by the maker.
- Low-voltage lighting: use a dimmer compatible with the transformer type.

## Safety & privacy

High risk: wiring mistakes can shock, burn, or start a fire. Breaker off and test dead before work, follow the dimmer diagram exactly, and use a licensed electrician for uncertain wiring.
