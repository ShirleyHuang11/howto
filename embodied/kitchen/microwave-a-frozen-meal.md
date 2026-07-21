---
name: microwave-a-frozen-meal
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: [daily/food/use-a-microwave]
status: draft
last_verified: 2026-07-20
objects: [microwave, frozen-meal, meal-tray, film-lid, plate, fork]
affordances: [package-read, film-pierce, door-open, button-press, stir, carry, place]
workspace: kitchen
safety: {hot_surfaces: true, sharp_objects: false, fragile: [plate], human_proximity: continue}
---

## Goal

A packaged frozen meal is microwaved per its own instructions, actually hot in the center, and served without a steam burn, the task that looks trivial and stalls robots and teenagers alike on the package-reading step.

## Preconditions

- A frozen ready-meal whose packaging is intact, and a microwave (`daily/food/use-a-microwave` supplies the general rules: no metal, watch the container class).
- The package's instructions located: usually a panel with wattage-keyed times ("900W: 4 min, stir, 2 min").

## Steps

1. **Read the package's microwave panel first, fully.** Wattage rows, piercing or lid instructions, the mid-cook stir, and the stand time. The instructions differ meaningfully per meal; the guess-and-nuke path produces lava edges around an ice core. → *Expect:* the times for your oven's wattage known (the wattage is on the microwave's door sticker or inside frame).
2. **Prepare the package as instructed.** Typically: remove the outer sleeve, pierce the film lid several times (or peel a corner), leave the tray on. Metal-crisping sleeves stay in only when the panel explicitly says so. → *Expect:* film vented or peeled per the panel; no unvetted metal.
3. **Center the tray and run the first heating stage.** Set the panel's first time; start. → *Expect:* rotation, rising steam through the vents; sauce bubbling at the edges by the stage's end.
4. **Do the mid-cook stir or rotate, exactly as told.** ⚠️ hot film and escaping steam: peel away from your face and fingers (the `daily/food/use-a-microwave` steam rule at its sharpest). Stir from the edges inward for stirrable meals; rotate or re-cover the rest. → *Expect:* frozen center broken up and redistributed; film handled without a scald.
5. **Run the second stage and the stand time.** The stand minutes on the panel are cooking, not waiting: the heat equalizes into the center then. → *Expect:* full time run, then the tray resting untouched for its stated stand.
6. **Verify steaming-hot-throughout before serving.** Stir once more and check the center: visibly steaming, uncomfortably hot to a testing bite. Lukewarm centers in meat, rice, or fish meals re-run in 30-second bursts (`daily/food/use-a-microwave` step 7's standard; `daily/food/cook-rice`'s reheat rules agree). → *Expect:* steam from the center, not just the edges.
7. **Serve with tray physics respected.** The tray is floppy and hot: carry on a plate, peel film fully away from yourself, and the tray recycles per its symbol once cool (`daily/home/sort-recycling`). → *Expect:* meal plated or eaten from the tray on a plate, no dropped-tray floor sauce.

## Decision points

- No wattage match on the panel (your oven is weaker): add roughly 10 to 20 percent time per stage and lean harder on the stir and the center check; stronger oven: subtract cautiously, the check still governs.
- Two meals at once: they do not share a microwave well; run sequentially or accept nearly doubled times with extra stirring.
- The meal says oven-only: it means it (crisping and browning need real heat); microwaving it anyway yields hot sadness, which is a choice but an informed one.

## Failure modes & recovery

- **F1 Ice-core center at serving:** stages skipped or stir omitted; stir hard and burst-heat in 30 to 60 second rounds until the center steams.
- **F2 Sauce eruption over the tray rim:** vents were insufficient or power too high for the sauce class; wipe the turntable now (`daily/food/use-a-microwave` F2), cover better, and drop to 70 percent power for the remainder.
- **F3 Film welded to the food:** peeled too late while molten; lift what lifts, and accept the panel's peel-timing instruction as earned wisdom.
- **F4 Tray buckled during carry, meal on the floor:** the plate-under-tray rule exists for this; clean per slip-risk priority (`embodied/kitchen/pour-a-glass-of-water` F3's floor-first logic).

## Verification

The panel's stages, stir, and stand were followed for your wattage, the center passes the steaming test, the film never met your face, and the tray traveled on a plate.

## Variations

- Home-frozen portions (`daily/food/portion-and-freeze-meals`) have no panel: defrost setting or 50 percent power with stirring, then full power to steaming; the center check does all the governing.
- Rice-heavy and fish meals: strictest on the steaming-hot standard; pastry items: microwave soggily or oven properly, per the honesty in the decision points.

## Safety & privacy

Medium risk is steam and molten sauce at the film's edge, plus the floppy-tray carry. The package's own panel is the recipe's authority; this file exists to make an agent actually read it.
