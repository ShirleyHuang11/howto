---
name: unclog-a-garbage-disposal
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A jammed or clogged garbage disposal is cleared, reset, and tested without putting hands near powered blades.

## Preconditions

- You can reach the wall switch, plug, breaker, or under-sink outlet for the disposal.
- You have a flashlight, tongs or pliers, a bucket or towel, and the disposal hex key or a 1/4 inch Allen key.
- The sink is not full of chemical drain cleaner.
- You are willing to stop if the unit leaks, hums after clearing, or smells electrical.

## Steps

1. **Kill power completely.** Turn the disposal switch off and unplug it under the sink or switch off its breaker. ⚠️ *Irreversible:* moving blades can amputate fingers; never put a hand into a disposal that can receive power. → *Expect:* switch and plug or breaker are both off.
2. **Confirm it is dead.** Flip the wall switch once while standing clear, then return it to off. → *Expect:* no hum, spin, or vibration occurs.
3. **Look into the chamber.** Shine a flashlight through the drain opening and inspect around the grinding plate. → *Expect:* visible food sludge, a stuck object, or a clear chamber.
4. **Remove loose objects with tools.** Use tongs or pliers to lift out glass, metal, bones, or fibrous debris. [BRANCH: object visible | no object visible] → *Expect:* foreign material is out of the chamber or nothing reachable remains.
5. **Free the flywheel from below.** Insert the hex key into the bottom center socket and turn back and forth until it moves freely. → *Expect:* resistance breaks loose and the key can swing both directions.
6. **Press the reset button.** Find the small red or black button on the bottom or side and press it once. → *Expect:* the button clicks in or is already seated.
7. **Flush with cold water.** Restore power only after tools are out, run cold water, and pulse the switch for 1 second. → *Expect:* the disposal spins without humming and water begins to drain.
8. **Clear remaining slow drainage.** Keep cold water running and pulse several short bursts, not one long grind. → *Expect:* water level falls and no object rattles inside.

## Decision points

- If glass is suspected, do not reach in; remove pieces only with pliers and inspect with light.
- If the unit hums but does not spin after the hex key turns freely, stop and recheck the reset and power.
- If both sink bowls back up, the clog may be in the trap or drain line, not only in the disposal.
- If water leaks from the disposal body, replacement is usually safer than repair.

## Failure modes & recovery

- **F1 Power not isolated:** detect hum or movement during the confirmation flip, recover by unplugging or turning off the breaker.
- **F2 Hex socket missing:** detect no center socket underneath, recover by using a disposal wrench from above or calling the model-specific method.
- **F3 Reset pops again:** detect the button immediately trips after testing, recover by stopping and letting the motor cool before one retry.
- **F4 Object rattles:** detect clanking during pulse, recover by cutting power again and retrieving the object with tools.
- **F5 Drain still slow:** detect standing water after spinning, recover by cleaning the P-trap rather than grinding longer.

## Verification

With cold water running, the disposal starts instantly, spins smoothly for three short pulses, drains the sink, and remains dry underneath.

## Variations

- Batch-feed disposals: the stopper is part of the safety switch; remove it only after power is off.
- Air-switch models: unplug under the sink because the counter button can be confusing.
- Septic systems: avoid heavy use and check local guidance for disposal compatibility.

## Safety & privacy

High risk comes from hidden power and sharp debris. Power off and unplug first, use tools instead of fingers, avoid chemical drain cleaners, and stop if electrical smell, smoke, or leaks appear.
