---
name: wipe-down-a-countertop
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [countertop, cloth, sponge, spray-cleaner, sink, crumbs, small-appliances]
affordances: [grasp, wipe, spray, lift, place, rinse, wring]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: continue}
---

## Goal

A kitchen counter cleared, wiped clean edge to edge including under the things that live on it, and left dry, the five-minute reset that keeps a kitchen trustworthy.

## Preconditions

- A cloth or sponge that passes the smell test (a sour sponge spreads bacteria in a thin even layer; `daily/home/wash-dishes-by-hand` F3 retires it), and water or a mild spray cleaner suited to the surface.
- Surface knowledge where it matters: natural stone (marble especially) refuses acidic cleaners (`daily/home/clean-a-bathroom`'s stone warning), wood wants damp-not-wet, laminate takes anything mild.

## Steps

1. **Clear the counter's working zones.** Dishes to the sink or machine, stray items to a temporary tray or their homes (`embodied/household/tidy-a-room`'s elsewhere-logic in miniature), small appliances slid aside or lifted. → *Expect:* bare surface in the zone being wiped; a tray of displaced items awaiting return.
2. **Sweep the solids first, into a hand or straight off the edge into the bin held below.** Crumbs and chopping debris go to the bin, not onto the floor and not into the cloth's first stroke (a crumb under a wet cloth becomes a smear with grit). ⚠️ Check for blades before sweeping blind along cluttered counters: a knife under a towel is the kitchen's classic hand injury (`daily/home/wash-dishes-by-hand`'s soaking-blade rule, dry-land edition). → *Expect:* solids in the bin; no blade met by a sweeping palm.
3. **Wipe systematically, back edge to front, in overlapping strokes.** Damp cloth or a light spray; work around the sink last (it is the dirtiest neighbor); include the backsplash's lower band and the counter's front lip, which catches drips invisibly. → *Expect:* uniform clean swath; the cloth visibly collecting rather than redistributing.
4. **Lift, wipe under, replace.** The toaster, kettle (`daily/food/make-toast`'s crumb shadow lives here), jars, and boards each get their footprint wiped and go back; wiping around resident objects is the counter version of fake dusting (`daily/home/dust-a-room` step 2). → *Expect:* no crumb halos where appliances stand.
5. **Deal with stuck spots by dwell, not force.** Dried sauce or syrup: park the wet cloth on it for a minute, then wipe; scraping with blades or green scourers wounds most surfaces. → *Expect:* fossils surrendering to patience; surface unscratched.
6. **Dry pass and cloth exit.** A wrung cloth or dry towel pass leaves the counter dry (wet counters re-collect dust and spot stone); the cloth rinses, wrings, and hangs to dry, never balled wet in the sink. → *Expect:* dry counter, returned items, cloth drying open.

## Decision points

- After raw meat or egg contact: the wipe upgrades to hot soapy water or a disinfecting cleaner on that zone, and the cloth used goes straight to the wash rather than back on the rail; cross-contamination outranks tidiness.
- Cadence: after every cooking session as `daily/food/clean-as-you-cook`'s closing move, plus this fuller lift-everything version weekly.
- Cloth discipline in shared kitchens: the counter cloth is not the floor cloth is not the dish sponge; color-coding is cheap and ends the ambiguity (`daily/home/clean-a-bathroom`'s cloth segregation, kitchen edition).

## Failure modes & recovery

- **F1 Streaky or sticky film after wiping:** too much cleaner or a spent cloth; rinse the cloth, plain-water pass, then dry pass.
- **F2 Swept crumbs to the floor by habit:** the floor now owes a sweep (`daily/home/sweep-and-mop-a-floor`); the bin-below-the-edge technique deletes this failure.
- **F3 Cleaner etched or dulled a stone patch:** stop that product on that surface permanently; etching is chemistry, not dirt, and polishing is a specialist errand. The surface-knowledge precondition exists for this.
- **F4 The counter recolonizes within hours:** the counter is the household's flat-surface magnet; the fix is homes for the colonizers (`daily/home/organize-a-closet`'s zone logic applied to mail, keys, and chargers), not more wiping.

## Verification

The counter is dry, clean edge to edge including lips, backsplash band, and under residents; solids went to the bin; the cloth is rinsed and drying; and any raw-food zone got the disinfect upgrade with its cloth retired to the wash.

## Variations

- Robots and new-kitchen visitors: treat unknown bottles as unknown chemistry; water-damp wiping is universally safe, product choices belong to the owner (`embodied/care/fetch-an-item-for-a-person`'s ask-when-unsure).
- Restaurant-style close-down: this recipe plus `daily/home/wash-dishes-by-hand` plus the floor sweep is the full kitchen reset trio.

## Safety & privacy

Low risk with one sharp edge: the blind sweep over cluttered counters. Look, then wipe. Everything else is water, patience, and the discipline of lifting what could be wiped around.
