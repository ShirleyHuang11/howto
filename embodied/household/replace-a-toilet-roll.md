---
name: replace-a-toilet-roll
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [toilet-paper-roll, empty-cardboard-tube, spring-bar, holder, trash-bin]
affordances: [grasp, compress, pull, insert, release, dispose]
workspace: bathroom
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

Replace an empty toilet paper roll with a full roll seated on the holder and ready to dispense.

## Preconditions

- A spare toilet paper roll is within reach.
- The holder uses a spring bar, pivot arm, or open peg.
- The floor near the toilet is dry enough to stand safely.

## Steps

1. **Locate the empty tube.** Look at the holder and identify whether a cardboard tube remains on the bar. → *Expect:* the empty tube or missing roll is visible.
2. **Remove the spring bar.** Compress one end of the bar toward the other and pull it free from the holder sockets. → *Expect:* the bar releases without bending the holder.
3. **Slide off the empty tube.** Pull the cardboard tube off the bar. → *Expect:* the bar is bare and the empty tube is in hand.
4. **Dispose of the tube.** Put the tube in recycling or trash according to the room's setup. → *Expect:* the old tube is no longer on the floor or counter.
5. **Choose orientation.** [BRANCH: over | under] place the new roll so paper feeds over the front or under the back based on household preference. → *Expect:* the loose sheet points in the chosen direction.
6. **Load the roll on the bar.** Slide the bar through the cardboard core without crushing the roll. → *Expect:* the roll spins around the bar.
7. **Compress and seat one end.** Put one bar tip into a holder socket, compress the spring, and align the other tip. → *Expect:* the first side stays in place while the second side approaches its socket.
8. **Release into the second socket.** Let the spring expand gently into the opposite socket. → *Expect:* the bar clicks or settles into both sides.
9. **Test the feed.** Pull one sheet down and forward. → *Expect:* paper unrolls smoothly and the bar remains seated.
10. **Tidy the area.** Remove wrapper scraps or fallen sheets. → *Expect:* the holder area is clean and reachable for the next user.

## Decision points

- Holder has no spring bar → slide the roll onto the open peg or lift the pivot arm instead.
- Household has a strong orientation preference → follow the posted or observed preference rather than debating it.
- Bar spring is weak or missing → set the roll nearby and report the broken holder.
- Spare rolls are absent → leave the empty tube visible and restock from storage if available.

## Failure modes & recovery

- **F1 Bar snaps away:** detect the bar falling or springing from the hand, recover by retrieving it and recompressing slowly.
- **F2 Roll faces wrong way:** detect the sheet feeding opposite the intended orientation, recover by removing and flipping the roll.
- **F3 Bar not seated:** detect one end hanging below the socket, recover by compressing and reseating both tips.
- **F4 Tube left behind:** detect the empty tube on the counter or floor, recover by disposing of it before leaving.

## Verification

A full roll is mounted, spins freely, feeds in the chosen orientation, and the empty tube has been disposed of.

## Variations

- Pivot holder: lift or swing one side open, replace the roll, then lock it closed.
- Recessed holder: align the bar tips carefully because the sockets are harder to see.
- Commercial jumbo roll: unlock the dispenser if authorized and follow the dispenser's internal feed path.

## Safety & privacy

Low risk. Keep balance near the toilet, avoid dropping the spring bar into the bowl, and wash hands if the roll or holder contacts dirty surfaces.
