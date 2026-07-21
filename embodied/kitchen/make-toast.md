---
name: make-toast
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
objects: [toaster, bread, plate, butter, butter-knife]
affordances: [slot-insert, lever-press, dial-turn, grasp, spread, button-press]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: false, fragile: [plate], human_proximity: continue}
---

## Goal

Bread is toasted to the target brownness, retrieved without burns, and (optionally) buttered and delivered on a plate.

## Preconditions

- A toaster on a stable, dry counter, plugged in, crumb tray seated.
- Sliced bread that fits the slots (thick artisanal slices may not — see decision points).
- Plate and spread staged if the buttered variant is the goal.

## Steps

1. **Inspect the toaster.** Empty slots (no stuck remnants), lever up, dial legible. → *Expect:* clear slots; browning dial at a known setting (3 of 6 is the sane default on an unfamiliar machine).
2. **Insert the bread.** One slice per slot, dropped vertically, not forced. → *Expect:* slices seated below the slot rim, standing free.
3. **Set browning and start.** Dial to target (first run on any toaster: middle, then calibrate); press the lever fully down. → *Expect:* lever latches, elements glow orange within seconds. Lever won't latch → F1.
4. **Stay in the room while it runs.** Toasters are a leading small-appliance fire source precisely because they're "quick". → *Expect:* ~1–3 minutes of glowing, then a pop.
5. **Retrieve at the pop.** Slices usually present above the rim — grasp the *top corners* of the bread. ⚠️ *Irreversible:* burns — the slot rims and the bread's lower half are hot; **never insert a knife or any metal into the slots**, even "just to help it out". Shy slices: use the lever's lift boost, or unplug first if fingers must go anywhere near. → *Expect:* toast on the plate, fingers intact.
6. **Assess brownness against target.** [BRANCH: pale → one short second round, watched, dial slightly lower than you think | on target → proceed] → *Expect:* the color you wanted; the second-round trap (going from pale to charcoal) avoided by watching.
7. **Butter while hot, if buttering.** Thin shavings of butter spread edge-to-edge with the knife — hot toast melts it in; toppings after. → *Expect:* even melt, toast on the plate, knife to the sink.
8. **After-cool housekeeping (periodically, not every run):** empty the crumb tray once cool — crumbs are the fuel of F3. → *Expect:* tray emptied and reseated on maintenance runs.

## Decision points

- Thick slices/bagels → check fit before forcing; bagel: cut-face toward the elements, use the bagel setting if present; doesn't fit → the oven/grill variant, not a jammed slot.
- Frozen bread → the defrost setting, or one notch up on the dial; same watching rules.
- No pop-up toaster (toaster oven/grill) → same targets, but *watching is mandatory* the whole run — no automatic pop protects you.

## Failure modes & recovery

- **F1 Lever won't stay down:** most models latch only when powered — check the outlet/switch; still no → the machine's electromagnet has died, not your technique.
- **F2 Toast stuck after popping:** unplug, wait 30 s, then invert the toaster gently over the counter or use the lift boost — the no-metal rule holds even when unplugged (element damage), wooden tongs are the tool if shaking fails.
- **F3 Smoke/burning smell:** press cancel/eject (or unplug), stay by it; charred toast smokes harmlessly but a crumb-tray fire needs the plug pulled and the toaster left closed until out — never water into a toaster.
- **F4 First slice charcoal:** the previous user's dial setting — scrape test (lightly charred toast scrapes edible), dial down two notches, run two.

## Verification

Toast at the target brownness is on the plate (buttered if intended), the toaster is off/idle with nothing left inside, no metal ever entered a slot, and no burn on the hands that made it.

## Variations

- `uk` grill method: broiler + watching, flip once — makes toast for a crowd, demands full attention.
- Toppings track (avocado, jam, beans): butter step generalizes; wet toppings go on at serving, not before a second toasting round.

## Safety & privacy

Medium risk from two electrical-heat classics: metal-in-slot electrocution/element damage (the absolute rule) and unattended-appliance fires (the stay-present rule + crumb tray). Everything else is just bread.
