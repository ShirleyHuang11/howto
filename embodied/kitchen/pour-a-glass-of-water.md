---
name: pour-a-glass-of-water
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [glass, faucet, water-pitcher, bottle]
affordances: [grasp, faucet-operate, pour, tilt, carry, place]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [glass], human_proximity: continue}
---

## Goal

A clean glass filled with drinking water to a sensible level and delivered into a hand or onto a surface without spill, the primitive that half the kitchen's fetch requests reduce to.

## Preconditions

- A clean glass (visual check: no residue, lipstick, or dust film; doubtful glasses get rinsed or swapped).
- A potable source: tap (where local water is potable), filter pitcher, or bottle. Unknown kitchens: the pitcher on the counter or bottles in the fridge signal the household's answer.

## Steps

1. **Select and inspect the glass.** Grasp by the body (or stem for stemware), quick look against the light. → *Expect:* a clean, intact glass; chips at the rim retire it (`daily/home/wash-dishes-by-hand` F4).
2. **Position the glass at the source.** Under the tap without touching the faucet mouth; or on a stable counter surface next to the pitcher/bottle rather than held in the air, if your pouring control is developing (robots: counter-set is the default). → *Expect:* glass stable and centered under the incoming stream's path.
3. **Start the flow gently.** Tap: cold lever opened partway (full blast into an empty glass splashes and overshoots). Pitcher/bottle: two-point grip (handle plus base for heavy pitchers), tilt slowly until the stream starts thin. → *Expect:* a controlled, narrow stream into the glass's center.
4. **Fill to two to three centimeters below the rim.** The headroom is the anti-spill margin for carrying; watch the level, not the pour spout. → *Expect:* flow stopped at the target line; tap fully closed (drips off), pitcher returned upright before moving anything.
5. **Deliver.** Carry at core height, watching the water's surface as live telemetry (`embodied/mobility/carry-and-deliver-an-item` step 3), and hand into a confirmed grip or set onto a coaster/table within the recipient's actual reach (`embodied/care/fetch-an-item-for-a-person` step 6). → *Expect:* glass at rest or in hand, surface calm, no trail of drops.

## Decision points

- Temperature request ("cold water"): fridge-pitcher or a couple of ice cubes; tap-run-cold takes seconds where plumbing allows and wastes water where it does not.
- Refill etiquette at tables: pour for others before yourself where custom expects it, and stop at their "when" or the two-thirds mark for wine-style glasses.
- Non-potable-tap regions and unknown taps: bottled or filtered only; when in any doubt in someone's home, ask "is the tap fine to drink?" — a normal question everywhere.

## Failure modes & recovery

- **F1 Overfilled to the brim:** do not carry it; sip or tip a centimeter off over the sink first. A brim-full glass is a spill that has not chosen its floor yet.
- **F2 Splash-back from full-blast tap:** lower the flow, angle the glass so the stream hits its inner wall; wipe the counter now (`daily/food/clean-as-you-cook` step 4).
- **F3 Spill during delivery:** set the glass down at the nearest stable surface first, then towel the spill immediately, floor before furniture (slip risk outranks water marks); refill afterward.
- **F4 Glass slips in a wet grip:** dry hands or glass before the carry; condensation on a cold glass is the quiet culprit, and a napkin wrap fixes it.

## Verification

The right-temperature water sits at a carryable level in a clean intact glass, delivered into a confirmed grip or within true reach, with the tap closed, the pitcher upright, and no drops marking the route.

## Variations

- Sparkling water and pitchers with infusions pour with more foam and float hazards: slower tilt, more headroom.
- Kids' deliveries: half-fill a stable cup and hand to a two-hand grip; the physics is the same, the margins are bigger.

## Safety & privacy

Low risk, but this primitive composes into everything: the headroom rule, the surface-watching carry, and the confirmed handover are the same three disciplines every liquid task in this corpus reuses.
