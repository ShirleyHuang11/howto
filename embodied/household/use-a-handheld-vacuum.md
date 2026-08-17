---
name: use-a-handheld-vacuum
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [handheld-vacuum, dust, crumbs, filter, charging-base]
affordances: [grasp, button-press, sweep, aim, empty, dock]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [decor, glass], human_proximity: continue}
---

## Goal

Remove small dry debris from a surface or floor using a handheld vacuum and return the vacuum ready for next use.

## Preconditions

- Vacuum has charge or is plugged into a usable battery pack.
- Dust bin and filter are installed.
- Debris is dry and small enough for the vacuum intake.
- Fragile loose objects are moved away from the cleaning path.

## Steps

1. **Inspect the intake and bin.** Look for clogs, a full bin, or missing filter before turning on. → *Expect:* the vacuum is assembled and airflow path is open.
2. **Grip and power on.** Hold the handle with the intake angled toward the debris, then press the power button. → *Expect:* motor noise starts and suction is felt at the nozzle.
3. **Vacuum from far edge inward.** Move the nozzle slowly over debris with the opening close to the surface. → *Expect:* visible crumbs or dust disappear into the intake.
4. **Use short overlapping passes.** Sweep each area with slight overlap instead of fast waving. → *Expect:* no debris remains between passes.
5. **Power off before lifting away.** Press the power button while the nozzle is still near the surface. → *Expect:* suction stops and debris does not fall back out.
6. **Empty or dock if needed.** Empty the bin if it reached the fill line, then place the vacuum on its charger. → *Expect:* the vacuum is clean enough inside and seated on the base or stored safely.

## Decision points

- Debris is wet → do not vacuum unless the model is rated for wet pickup.
- Debris includes sharp fragments → use a brush and dustpan or glass cleanup procedure.
- Suction is weak → check the bin, filter, and nozzle before continuing.

## Failure modes & recovery

- **F1 No suction:** detect motor running but debris staying put → clear the intake, empty the bin, and reseat the filter.
- **F2 Debris blows away:** detect crumbs moving ahead of the nozzle → lower the intake angle and approach more slowly.
- **F3 Battery dies:** detect motor fading or stopping → dock or charge before resuming.
- **F4 Object gets caught:** detect rattling or stalled airflow → power off, remove the object, and inspect for damage.

## Verification

The target area has no visible dry debris, the vacuum bin is not overfilled, and the vacuum is powered off and stored or charging.

## Variations

- `upholstery`: use a brush attachment and lighter pressure.
- `car-interior`: use a crevice tool and remove loose coins or papers first.

## Safety & privacy

Low risk. Do not vacuum liquids, hot ash, fine hazardous powders, or private papers that should be reviewed before disposal.
