---
name: replace-a-blown-car-fuse
domain: transit
subdomain: vehicle
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You replace a blown automotive fuse with the correct amperage and confirm the circuit works without bypassing the vehicle's protection.

## Preconditions

- The vehicle is parked, off, and secured.
- You have the owner's manual or fuse-box diagram and a replacement fuse of the same type and amperage.
- You have a fuse puller or needle-nose pliers with insulated handles.

## Steps

1. **Identify the failed circuit.** Note what stopped working, such as a power outlet, radio, wiper, or light. → *Expect:* you know which fuse label to look for.
2. **Find the correct fuse box.** Use the manual for interior, engine-bay, or trunk fuse locations. → *Expect:* the relevant fuse panel is accessible.
3. **Turn off the vehicle and circuit.** Remove the key or power down the vehicle before pulling fuses. → *Expect:* the circuit is not energized by normal operation.
4. **Match the diagram to the fuse.** Locate the fuse by label and position, not by guessing from color alone. → *Expect:* the candidate fuse matches the failed circuit in the diagram.
5. **Inspect or test the fuse.** Pull it straight out and check for a broken metal link or test continuity with a meter. → *Expect:* the fuse is confirmed blown or intact.
6. **Install the same amperage fuse.** ⚠️ *Irreversible:* never install a higher-amp fuse or foil bypass; that can overheat wiring and start a fire. → *Expect:* the replacement matches the original amp rating and seats fully.
7. **Test the circuit once.** Turn the vehicle/accessory on and try the failed function. → *Expect:* the function works and the fuse does not immediately blow.
8. **Replace the cover and record the result.** Note the fuse position, rating, and date. → *Expect:* the fuse box is closed and future diagnosis has context.

## Decision points

- Replacement fuse blows immediately → stop using that circuit and have the short diagnosed.
- Fuse is intact → the fault is elsewhere; do not keep replacing fuses.
- Safety-critical circuit fails, such as brake lights, wipers, or headlights → avoid driving until repaired.

## Failure modes & recovery

- **F1 Wrong fuse pulled:** detect another system stops working or the diagram does not match → reinstall it in the same slot and recheck the manual.
- **F2 No spare fuse:** detect the vehicle has no matching spare → buy the exact type and rating; do not borrow from safety systems.
- **F3 Corroded fuse box:** detect green corrosion or water → stop and seek service; electrical diagnosis may be needed.
- **F4 Fuse difficult to remove:** detect cracking plastic or slipping tool → use the proper fuse puller and pull straight.

## Verification

The failed accessory or light works with a same-rating replacement fuse installed, the fuse does not blow again during a short test, and the fuse-panel cover is back in place.

## Variations

- Blade fuses: mini, low-profile mini, micro, and standard sizes are not interchangeable even at the same amperage.
- Older glass fuses: match length and amperage markings exactly.
- EV/hybrid: do not touch high-voltage service disconnects or orange-cabled systems.

## Safety & privacy

Medium risk from electrical fire and safety-system failure. Confirm the fuse rating before installation, and never bypass a fuse or upsize it to stop repeated failures.
