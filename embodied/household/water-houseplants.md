---
name: water-houseplants
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [watering-can, houseplants, pot, saucer, faucet]
affordances: [grasp-handle, pour, carry, finger-probe, faucet-operate]
workspace: home-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [pot], human_proximity: slow}
---

## Goal

Every houseplant on the care list that needs water has been watered to drainage, without overwatering any plant or spilling on floors and furniture.

## Preconditions

- A list or known set of the home's plants and their locations.
- A watering can and a faucet.
- Saucers or trays under pots (note plants without them — they need slower pouring).

## Steps

1. **Fill the watering can at the faucet.** Room-temperature water, ~3/4 full for carrying stability. → *Expect:* can filled below the spill line; faucet fully closed after.
2. **Go to the first plant and test soil moisture.** Probe a finger (or moisture sensor) ~3 cm into the soil. [BRANCH: dry at depth → water it | moist → skip, next plant] → *Expect:* a clear dry/moist reading; when in doubt, skip — underwatering recovers, overwatering kills.
3. **Water slowly at the soil, around the base.** Pour in a slow spiral, avoiding leaves and the pot rim, until water just appears in the saucer. → *Expect:* soil darkens evenly; first drips reach the saucer; no overflow.
4. **Pause and check the saucer.** If the saucer approaches full, stop — the pot has reached drainage capacity. → *Expect:* saucer holds a shallow layer, well below its rim.
5. **Move to the next plant and repeat steps 2–4.** Refill the can at the faucet when empty. → *Expect:* each visited plant is either watered-to-drainage or skipped-as-moist.
6. **Second pass: empty any saucer still full after ~20 minutes.** Carry it level to the sink, pour out, replace. Standing water rots roots. → *Expect:* no saucer holds deep standing water.
7. **Return the can to storage and wipe any drips along the route.** → *Expect:* floors and furniture dry; can stored.

## Decision points

- Plant is severely wilted *and* soil is soggy → overwatered, not thirsty: do not water; move it to drain and flag for a human.
- Pot has no drainage hole → give a small measured amount (≈1/10 pot volume), never to saturation.
- Hanging or high-shelf plants → lower them or use a long-spout pour at slow speed; never pour above shoulder height over furniture.

## Failure modes & recovery

- **F1 Overflow onto floor/furniture:** stop pouring, set the can down, blot with a towel immediately (wood swells); check for water under the pot.
- **F2 Water runs straight through without soaking (hydrophobic soil):** water in three small passes a minute apart, or bottom-water by filling the saucer and letting it wick.
- **F3 Pot tips during watering:** stabilize with the free hand before pouring; if soil spilled, scoop it back and sweep the remainder.

## Verification

Every plant on the list was visited; each is either watered (soil dark, saucer with shallow drainage) or logged as skipped-moist; no saucer has standing water at the 20-minute check; floors along the route are dry.

## Variations

- Succulents/cacti: water only when fully dry, then deeply — the moist-skip threshold in step 2 is much stricter.
- Self-watering pots: fill the reservoir gauge instead of the topsoil; steps 3–4 are replaced by a fill-to-line.

## Safety & privacy

Low risk. Carry the can with a stable two-point grasp near people and pets; slow all motion in tight spaces around fragile pots and furniture.
