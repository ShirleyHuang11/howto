---
name: check-your-coolant-level
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You verify the engine coolant level safely and decide whether to top up, monitor, or seek repair.

## Preconditions

- The vehicle is parked on level ground, engine off, and cooled down unless the manual says otherwise.
- You have the correct coolant specification from the owner's manual if topping up may be needed.
- You can identify the translucent coolant reservoir and its MIN/MAX or LOW/FULL markings.

## Steps

1. **Let the engine cool.** Wait until the upper radiator area is cool enough to touch and pressure has dropped. ⚠️ *Hazard:* hot coolant can spray and cause severe burns if opened under pressure. → *Expect:* the engine bay is safe to inspect without steam or hissing.
2. **Locate the coolant reservoir.** Find the plastic tank connected to the radiator system, not the washer-fluid tank. → *Expect:* the cap or tank label refers to engine coolant or antifreeze.
3. **Read the level against the marks.** View the tank from the side with the vehicle level. → *Expect:* the coolant level is clearly below, within, or above the marked range.
4. **Inspect for warning signs.** Look for puddles, crusty residue, sweet smell, steam, oily film in coolant, or repeated low level. → *Expect:* leak or contamination clues are documented or absent.
5. **Top up only if appropriate.** [BRANCH: level slightly low and correct coolant available, add to the MAX/FULL cold mark | coolant very low, leaking, contaminated, or unknown type, do not guess; arrange service] → *Expect:* the tank is at the correct mark or service is planned.
6. **Secure the cap.** Tighten the reservoir cap fully and wipe spills from painted surfaces. → *Expect:* the cooling system reservoir is closed and clean.
7. **Monitor after driving.** Recheck after one normal trip and a full cool-down if the level was low. → *Expect:* the level stays stable or a leak pattern is identified.

## Decision points

- Temperature warning or overheating occurred → use `transit/vehicle/handle-an-overheating-engine`; do not treat this as a simple top-up.
- Coolant is empty or drops again quickly → arrange inspection before driving far.
- Wrong coolant was added → do not keep mixing; ask a mechanic whether a flush is needed.

## Failure modes & recovery

- **F1 Opened while hot:** detect hiss, steam, or cap pressure → stop turning, move away, let it cool fully, and seek help if burned.
- **F2 Mistaken fluid tank:** detect blue washer fluid or windshield icon → close it and locate the coolant reservoir by hose routing/manual.
- **F3 Cannot see level:** detect stained opaque plastic → use a flashlight or have service check; do not overfill blindly.
- **F4 Repeated low coolant:** detect needing top-up more than once → inspect for leaks and pressure-test the system.

## Verification

With the engine cold and vehicle level, the coolant reservoir reads within the marked range, the cap is secure, and no active leak or overheating warning is present.

## Variations

- Pressurized reservoir systems: some vehicles use the reservoir as the pressure cap; treat it like a hot radiator cap.
- Hybrid/EV: there may be separate coolant loops; only service the reservoir specified by the manual.
- Concentrate vs premix: premixed coolant is ready to add; concentrate must be diluted correctly with suitable water.

## Safety & privacy

Medium risk from burns, engine damage, and toxic fluid. Confirm the engine is cool before opening anything, use the correct coolant, and keep antifreeze away from children and pets.
