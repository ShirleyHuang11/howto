---
name: use-a-pressure-cooker
domain: daily
subdomain: food
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 45min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A pressure cooker is filled correctly, sealed, brought to pressure, released safely, and opened only when depressurized.

## Preconditions

- Electric or stovetop pressure cooker with gasket, valve, and manual available.
- At least the manufacturer's minimum liquid, usually 250-375 ml for electric cookers.
- Food cut appropriately and the cooker no more than its safe fill line.

## Steps

1. **Inspect the cooker.** Check gasket seating, clean valve, intact lid, and empty condensation path. → *Expect:* no cracks, dried food, or blocked vent.
2. **Add minimum liquid.** Add the required water, stock, or thin sauce before food. → *Expect:* liquid is visible at the bottom.
3. **Respect fill limits.** Fill no more than two-thirds full, or half full for beans, grains, and foamy foods. → *Expect:* headspace remains above the food.
4. **Lock and set valve.** Close lid fully and set valve to sealing for electric models. → *Expect:* lid indicator and valve position match the manual.
5. **Come to pressure.** Heat or start program and wait for the pressure indicator to rise. → *Expect:* steam vents briefly, then pressure locks and timing begins.
6. **Cook for the recipe time.** Maintain stable pressure on stovetop or let electric cooker regulate itself. → *Expect:* no constant violent venting after pressure is reached.
7. **Choose release method.** [BRANCH: natural release for meat, beans, soups | quick release for vegetables and eggs] → *Expect:* release method matches food texture and foam risk.
8. **Release safely.** For quick release, turn valve with a spoon handle and keep hands and face away. ⚠️ *Irreversible:* steam can cause severe burns; never lean over the valve or force the lid. → *Expect:* steam exits upward and pressure indicator drops only when done.
9. **Open away from you.** Unlock only after pressure is fully gone, then tilt lid so steam vents away. → *Expect:* lid opens without resistance.
10. **Check food and reduce if needed.** Simmer uncovered if sauce is thin, or pressure-cook a few more minutes if underdone. → *Expect:* food reaches target tenderness without excess liquid.

## Decision points

- Food foams, such as beans or oatmeal → never quick release unless the manual and recipe say it is safe.
- Cooker will not seal → check gasket, valve position, and whether there is enough thin liquid.
- Recipe uses dairy or thickeners → add them after pressure cooking to avoid scorching and clogging.

## Failure modes & recovery

- **F1 Burn warning or scorching:** detect by warning, smell, or no pressure → turn off, release safely, scrape nothing burnt into food, and add thin liquid.
- **F2 Steam leaks around lid:** detect by continuous side steam → stop, cool, reseat gasket, and inspect for damage.
- **F3 Food sprays from valve:** detect by foam or liquid at vent → close valve if safe, let natural release, and clean valve after cooling.
- **F4 Lid stuck:** detect by resistance after cooking → wait longer; never pry, run under water only if manual permits.

## Verification

The cooker reached pressure, released until the indicator dropped, opened without force, and the food is cooked to the intended tenderness.

## Variations

- `stovetop`: lower heat after pressure is reached to maintain gentle steady pressure.
- `electric`: allow extra time for coming to pressure; programmed minutes are not total elapsed time.
- `beans`: soak if desired, fill only halfway, and use natural release to prevent foaming through the valve.

## Safety & privacy

High risk from pressure, steam, and blocked valves. Keep vents clean, use enough thin liquid, respect fill limits, quick-release away from people, and never force a pressurized lid.
