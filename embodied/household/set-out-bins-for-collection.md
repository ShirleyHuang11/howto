---
name: set-out-bins-for-collection
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [trash-bin, recycling-bin, compost-bin, lid, curb, driveway]
affordances: [check, roll, lift, orient, place, close]
workspace: curbside
safety: {hot_surfaces: false, sharp_objects: true, fragile: [bin-lid], human_proximity: slow}
---

## Goal

Place the correct waste bins at the collection point with lids closed, access clear, and no obstruction to pedestrians, vehicles, or collectors.

## Preconditions

- Collection day and accepted bin types are known.
- Bins are not too heavy or damaged to move safely.
- The route to the curb or collection area is visible.

## Steps

1. **Confirm collection schedule.** Check which bins are due for pickup. → *Expect:* only the correct trash, recycling, compost, or yard bins are selected.
2. **Check lids and contents.** Close lids and remove prohibited overflow or loose sharp items if visible. → *Expect:* bins can roll without spilling.
3. **Grip handles securely.** Stand behind wheeled bins and keep feet clear of wheels. → *Expect:* the bin can be tipped slightly under control.
4. **Roll along a clear route.** Move slowly over thresholds, slopes, gravel, or wet surfaces. → *Expect:* the bin remains upright.
5. **Place at the collection point.** Set bins where local practice expects them, usually near curb edge but out of traffic lanes. → *Expect:* collection arms or workers can reach them.
6. **Orient bins correctly.** Face arrows, handles, or lids according to local collection markings. → *Expect:* the bin opening and wheels match collection requirements.
7. **Leave clearance.** Keep bins away from parked cars, mailboxes, hydrants, bike lanes, and sidewalks. → *Expect:* pedestrians, vehicles, and collectors have access.
8. **Return safely.** Walk back along the route and close gates or doors. → *Expect:* the property is secure and paths remain clear.

## Decision points

- Bin is too heavy → remove some contents or ask for help rather than dragging unsafely.
- Weather is windy → place bins close together or wait until the allowed set-out time.
- Sidewalk would be blocked → use the edge location that preserves pedestrian access.
- Hazardous waste is present → do not place it in regular bins; follow local disposal rules.

## Failure modes & recovery

- **F1 Bin tips:** detect loss of balance or spill → stop, upright the bin, and clean loose waste if safe.
- **F2 Wrong bin day:** detect schedule mismatch → return the bin to storage.
- **F3 Blocked access:** detect car, pole, or snowbank preventing pickup → move bin to a clearer allowed spot.
- **F4 Sharp item protrudes:** detect glass, metal, or branch sticking out → contain or remove it before collection.

## Verification

The scheduled bins are upright at the collection point, lids closed, correctly oriented, reachable by collectors, and not blocking pedestrians, traffic, hydrants, or driveways.

## Variations

- Alley collection: place bins at the assigned alley edge instead of curbside.
- Bag-only service: set sealed bags in the approved location and weight limit.
- Snow conditions: clear a flat spot so bins are visible and stable.

## Safety & privacy

Medium risk from traffic, heavy bins, sharp waste, and slips. Slow near pedestrians and vehicles, keep personal documents shredded or concealed, and avoid leaving bins where they reveal occupancy patterns more than necessary.
