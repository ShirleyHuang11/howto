---
name: clean-a-washing-machine-filter
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

The washer pump filter is drained, cleared of lint and objects, and resealed so the machine can drain properly.

## Preconditions

- Washer is off, cool, and not holding a hot wash.
- You have towels, a shallow tray, gloves, a small brush, and access to the lower front flap or service panel.
- You accept that trapped water may spill and have protected nearby flooring.

## Steps

1. **Switch the washer off.** Unplug it or turn it off at the breaker if the outlet is hidden. → *Expect:* the panel is dark and the drum is stopped.
2. **Open the pump access flap.** Locate the small lower door and place towels under it. [BRANCH: drain hose present | no drain hose] use the hose first if present, otherwise drain slowly through the filter cap. → *Expect:* the filter cap and drain path are visible.
3. **Drain the trapped water.** Pull the small hose plug or crack the cap slowly into the tray, emptying the tray as needed. → *Expect:* water flow slows to drips.
4. **Remove the filter cap.** Turn the cap counterclockwise while keeping towels in place. → *Expect:* the filter comes free without a rush of water.
5. **Clear debris.** Remove coins, hair pins, lint, buttons, and fabric scraps from the filter and cavity. → *Expect:* the impeller area is visible and clear.
6. **Brush and inspect the seal.** Rinse the cap, brush lint from threads, and check the rubber seal for grit. → *Expect:* the seal sits clean and undamaged.
7. **Reseal the filter.** Thread the cap by hand until snug, close the drain hose plug, and wipe the area dry. → *Expect:* the cap is straight and the flap closes.
8. **Run a leak check.** Restore power and run a short drain or rinse cycle while watching the flap area. → *Expect:* the pump drains and no water appears at the cap.

## Decision points

- Water gushes faster than the tray can catch → tighten the cap, empty the tray, and continue in smaller turns.
- Cap will not turn → check the manual for lock tabs and avoid pliers that can crack the cap.
- Impeller is blocked by a hard object → remove only visible loose debris, then call service if it will not spin.
- Seal is torn or cap cross-threads → replace the cap assembly before using the washer.

## Failure modes & recovery

- **F1 Filter leaks after cleaning:** detect drips during the check cycle, recover by powering off, draining again, cleaning the seal, and reseating the cap.
- **F2 Washer still will not drain:** detect standing water or an error code, recover by checking the drain hose for kinks and calling service for pump faults.
- **F3 Cap is cross-threaded:** detect uneven resistance, recover by backing it out and threading again by hand.
- **F4 Odor remains:** detect sour smell after the filter is clear, recover with a hot maintenance wash and door gasket cleaning.

## Verification

A short drain or rinse cycle completes with no pump error and no leakage from the filter access area.

## Variations

- `top-loader`: many top-loaders hide or omit user-serviceable pump filters, so follow the manual.
- `laundry-pedestal`: remove the drawer or lower trim for tray clearance.
- `shared-laundry`: place a note while the machine is open so no one starts it.

## Safety & privacy

Medium risk because water can damage floors and hidden objects can be sharp. Keep power off while the filter is open and never reach into a moving pump.
