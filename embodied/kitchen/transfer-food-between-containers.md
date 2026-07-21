---
name: transfer-food-between-containers
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [source-container, destination-container, food, spatula, spoon]
affordances: [grasp, align, tilt, scrape, pour, place]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [bowl, plate], human_proximity: continue}
---

## Goal

Food is moved from one container to another with minimal spill and without crushing or contaminating it.

## Preconditions

- The destination container is clean, large enough, and stable.
- The source container can be lifted or tilted safely.
- A spatula or spoon is available for guiding and scraping.

## Steps

1. **Place the destination.** Set the destination container on a flat surface directly in front of the source container. → *Expect:* the destination does not slide when nudged.
2. **Check capacity.** Compare the food volume with the destination headroom before lifting anything. → *Expect:* the destination has visible room above the expected fill level.
3. **Align the rims.** Bring the source rim just above or slightly inside the destination rim without touching dirty outer surfaces to food. → *Expect:* a short transfer gap exists and both openings overlap.
4. **Set the guiding tool.** Hold the spatula or spoon at the lower lip of the source container to guide food flow. → *Expect:* the tool blocks food from escaping sideways.
5. **Tilt slowly.** Rotate the source container toward the destination until food begins moving. → *Expect:* food crosses the rim in a controlled stream or slide.
6. **Scrape the trailing food.** Use the spatula with light pressure along the inner wall, pushing food toward the aligned rim. → *Expect:* remaining food gathers at the pour edge and drops into the destination.
7. **Pause before overflow.** [BRANCH: destination still has headroom | destination nearly full] Continue if there is room; stop and choose a larger container if the level is within two centimeters of the rim. → *Expect:* no food reaches the outside rim.
8. **Right and set down.** Return the source container upright before moving it away, then set it down on the work surface. → *Expect:* no trailing drip or falling piece follows the source container.

## Decision points

- Food is liquid or saucy → keep a lower tilt angle and use the tool as a dam at the rim.
- Food is chunky or sticky → scrape in small batches rather than one steep dump.
- Container is heavy → keep it on the counter and tip only the near edge.

## Failure modes & recovery

- **F1 Spill at rim:** food lands outside the destination → stop tilt, wipe the surface, realign rims closer, and resume slower.
- **F2 Destination slides:** container moves during contact → add a towel under it or hold the outer wall with the free hand.
- **F3 Food sticks:** material clings to the source wall → use firmer spatula pressure and shorter scraping strokes.
- **F4 Overfill:** food nears the rim → stop, transfer some into a second container, then continue only with headroom.

## Verification

The intended food is inside the destination container, the destination remains below its rim, and visible spills are absent or wiped.

## Variations

- `pan-to-plate`: use a spatula under solids and keep the pan lip low to avoid splatter.
- `bowl-to-storage`: scrape around the full circumference before closing the storage lid.
- `dry-goods`: pour in pulses and tap the container lightly to settle volume.

## Safety & privacy

Low risk for room-temperature food, with higher care needed for glass or ceramic containers. Keep rims close, avoid steep dumping, and slow down when a person stands near the transfer path.
