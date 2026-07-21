---
name: fill-and-run-a-kettle
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [electric-kettle, kettle-base, faucet, mug]
affordances: [grasp, lid-open, lid-close, pour, place, button-press]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: false, fragile: [mug], human_proximity: continue}
---

## Goal

The kettle is filled to a safe level, boiled, and has clicked itself off automatically, with hot water ready to pour and no water on the electrical base.

## Preconditions

- An electric kettle with a separate powered base, plugged into a working outlet.
- The base sits on a dry, stable counter with slack in the cord (no taut cord across a walkway).
- Potable cold tap water within carrying distance of the base.

## Steps

1. **Inspect kettle and base.** Look into the kettle: no standing stale water, no loose scale flakes; base contacts dry. → *Expect:* clean interior, dry base plate, switch in the off position.
2. **Lift the kettle off the base before filling.** Never fill it while seated: drips reach the electrical contacts. → *Expect:* kettle free in hand, base stays put on the counter.
3. **Fill at the tap between the MIN and MAX lines.** Below MIN risks dry-boiling the element; above MAX makes the spout spit boiling water at the boil. Fill only what you need: a mug's worth boils in half the time of a full kettle. → *Expect:* water level visibly between the two marks on the gauge window.
4. **Close the lid until it clicks and dry the outside.** A latched lid matters twice: it keeps steam on the auto-off sensor, and it keeps the lid shut during the pour. Wipe drips off the body and especially the underside. → *Expect:* lid latched, exterior and underside dry to the touch.
5. **Seat the kettle on the base.** Lower it on and rotate slightly until it drops fully home; most bases are 360-degree so orientation is free. → *Expect:* kettle sits flush and does not rock; on some models a standby light appears.
6. **Press the switch on.** → *Expect:* switch latches down and the indicator light comes on; heating hiss starts within about 30 seconds. No latch or no light → F1.
7. **Wait nearby for the automatic click-off.** Sound builds from hiss to rumble, then quietens just before the boil. → *Expect:* the switch flips off by itself with an audible click and the light goes out, typically 2 to 5 minutes. Steaming hard with no click → F2.
8. **Verify off, then pour.** Confirm the light is out before touching the handle. Bring the mug next to the kettle and pour slowly with the spout low. ⚠️ *Irreversible:* scald risk: steam exits the spout ahead of the water, so keep your holding hand behind the handle and never pour toward yourself. → *Expect:* mug filled without splash, kettle returned to the base, lid still shut.

## Decision points

- Water sat in the kettle overnight or longer → dump and refill; stale water tastes flat and concentrates scale.
- Visible white scale flakes floating after the boil → pour through anyway for cleaning uses only; descale before drinking (see Variations).
- Kettle body is metal and someone else may touch it → warn them or move it back from the counter edge; the body stays burn-hot for several minutes.

## Failure modes & recovery

- **F1 No power on switch-press:** re-seat the kettle with a small twist until it drops fully, then check the outlet with another device → if it still will not latch, the thermal cutout may be tripped from a recent dry-boil; let it cool 15 minutes and retry.
- **F2 Boils but never clicks off:** almost always an unlatched lid letting steam miss the sensor → switch it off manually, latch the lid, and treat the auto-off as untrusted until it passes a watched test boil.
- **F3 Dry-boil (element hiss, hot plastic smell, little water):** switch off immediately, leave the kettle on the base to cool fully → do not add cold water to a hot empty kettle (thermal shock); refill only after it is cool to the touch.
- **F4 Water on the base or contacts:** unplug at the wall before touching anything → dry the base and kettle underside completely and let air-dry 10 minutes before powering again.

## Verification

The switch has returned to off on its own (auto-off confirmed this run), the water gauge shows the expected drop after pouring, the base and counter are dry, and the kettle rests seated on its base with the lid latched.

## Variations

- Stovetop whistling kettle: no auto-off exists; the whistle is the only signal, so staying within earshot is mandatory.
- Descaling: boil a half-fill of 1:1 white vinegar and water, let stand 30 minutes, then rinse and do one boil-and-discard run before drinking use.
- Variable-temperature kettles: select the preset (e.g. 80 °C for green tea) before pressing start; the click-off happens at the set temperature, not the boil.

## Safety & privacy

Medium risk from boiling water and steam: pour with the mug beside the kettle rather than carrying open hot water, keep the base and contacts dry, and never bypass a failed auto-off by holding the switch down. No personal data involved.
