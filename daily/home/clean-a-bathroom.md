---
name: clean-a-bathroom
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

The bathroom's four zones — toilet, sink/mirror, shower/tub, floor — are cleaned and disinfected in the right order, with chemicals never mixed and the room left dry and aired.

## Preconditions

- Supplies: bathroom/all-purpose cleaner, toilet-bowl cleaner + brush, glass cleaner (or vinegar solution), cloths/sponges **color-coded or kept separate** (toilet cloths never touch the sink), gloves.
- Ventilation available: window or working fan.
- **One product per zone at a time — never combine cleaners** (bleach + acid/ammonia produces toxic gas; this rule outranks every other line in this file).

## Steps

1. **Ventilate, glove up, and clear the surfaces.** Window open/fan on; bottles, toothbrushes, and towels off the counters; bath mat out (to `daily/home/do-the-laundry`). → *Expect:* airflow moving, surfaces bare, gloves on.
2. **Start the soak timers first.** Toilet-bowl cleaner around the bowl's rim, brush later; spray the shower/tub surfaces with cleaner. Dwell time is the active ingredient — let both sit while you do the sink zone. → *Expect:* two zones soaking; you're not scrubbing anything yet.
3. **Clean the sink zone.** Spray and wipe the basin, taps, and counter (cloths A); scrub the drain collar and the tap bases where grime rings. → *Expect:* basin and taps gleaming; hair and paste residue gone.
4. **Do the mirror and glass.** Glass cleaner, wipe in one direction with a dry-side finish. → *Expect:* streak-free at an angle to the light.
5. **Return to the shower/tub and scrub with the grain of the grime.** Walls top-down, fixtures, then the basin/tray; a brush for grout lines; rinse everything down with the shower head. → *Expect:* soap scum yields after its soak; water sheets off surfaces rather than beading on film.
6. **Finish the toilet — outside first, bowl last, its own cloths (B).** Wipe tank, lid, seat top, seat underside, rim exterior, base and the floor around it; then brush the soaked bowl under the rim and flush with the lid down. → *Expect:* every touched surface disinfected; bowl clean under the rim; brush rinsed in the flush and drip-dried in its holder.
7. **Floor last, door-to-corner logic reversed.** Sweep/vacuum hair first, then mop from the far corner to the door (`daily/home/sweep-and-mop-a-floor`), including behind the toilet base. → *Expect:* floor uniformly clean, you exiting over wet floor's edge, not across it.
8. **Reset the room.** Cloths to a hot wash (A and B still segregated), gloves washed then off, hands washed anyway; fresh towels/mat back once the floor dries; fan running until the room is dry. → *Expect:* dry, aired, restocked bathroom; cleaning kit stored with the toilet cloths marked.

## Decision points

- Mold spots on grout/sealant → a dedicated mold product on its *own* day (never same-session with other chemicals), ventilation doubled; recurring mold = a moisture problem (`fan use, squeegee habit`), not a cleaning problem.
- Hard-water scale on glass/taps → vinegar or citric-acid based descaler, *never* on natural stone surfaces (it etches marble) — check what your counter is before acids come out.
- Daily-maintenance mode (2 minutes) → squeegee the shower glass, quick sink wipe, toilet brush swirl — the deep clean above then happens fortnightly instead of weekly.

## Failure modes & recovery

- **F1 Mixed-chemical smell (sharp, chlorine-like):** leave the room *now*, ventilate fully, don't return until the air clears; identify what combined and physically separate those products' storage.
- **F2 Toilet cloth ambiguity ("which cloth was this?"):** treat unknown as contaminated — hot-wash everything and re-establish the color code; this is why the code exists.
- **F3 Grout stays grim after scrubbing:** it's stained, not dirty — a baking-soda paste + dwell time, or accept that grout has a cosmetic lifespan and stop burning effort.
- **F4 Slipped on the wet floor:** the exit-over-the-edge rule (step 7) plus no-socks-on-wet-tile; block the door for the dry time as in `daily/home/sweep-and-mop-a-floor`.

## Verification

All four zones pass a look-and-touch check (no film, no rings, no hair), the bowl is clean under the rim, cloths A/B went to the wash still segregated, no two chemicals ever shared a surface or a session, and the room is drying with air moving.

## Variations

- Shared apartments: a rotation chart plus this recipe as the definition of "cleaned" prevents the standards war.
- `jp` unit bathrooms (one-piece wet rooms): the whole room is a shower — the zones merge and the drain-and-dry step becomes the finale.

## Safety & privacy

Medium risk, chemical not biological: the never-mix rule, gloves, and ventilation carry it. The toilet-cloth segregation is the hygiene line that makes everything else true.
