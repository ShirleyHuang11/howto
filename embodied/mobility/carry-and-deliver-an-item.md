---
name: carry-and-deliver-an-item
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: medium
prerequisites: [embodied/mobility/open-a-door]
status: draft
last_verified: 2026-07-20
objects: [item, source-surface, destination-surface, doors-en-route]
affordances: [grasp, lift, carry, place, door-open, navigate]
workspace: building-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [item], human_proximity: slow}
---

## Goal

A specified item is picked up from its source, transported along a route, and placed at its destination — intact, upright where required, and confirmed received where a person is the destination.

## Preconditions

- Item location and destination are known; the route between them is passable (doors operable, no stairs beyond capability).
- The item is within carrying capability (weight, size, one-hand vs two-hand/bimanual).
- Item properties assessed: fragile? liquid/open-top? orientation-sensitive? hot/cold?

## Steps

1. **Inspect the item and plan the grasp.** Rigid box → side or underside grip; open container/liquid → upright two-point hold; bag → handles; plate → underhand palm. Note "this side up" implications. → *Expect:* a grasp plan matched to the item class and a route in mind including doors.
2. **Lift correctly.** Close to the body/chassis, load over your base, knees not back (humans), both contact points engaged before full weight transfer. → *Expect:* item fully supported and stable before the first step; no slip at the interface.
3. **Set the carry posture.** Load held close, sight line kept *over* the load (never carry what blinds you), liquids level, fragiles cushioned against the body not swinging free. → *Expect:* you can see the path; the item doesn't oscillate when you walk.
4. **Navigate at load-appropriate speed.** Slow around corners and people (announce "behind you"/"excuse me" in shared spaces), wide berth from walls and furniture, extra caution at level changes (thresholds, ramps). → *Expect:* progress without contact; liquid surfaces staying calm is the live telemetry.
5. **Handle doors per `embodied/open-a-door`'s loaded-carry branch.** Set down to operate if the door demands a hand you don't have. → *Expect:* through each door with item and door both controlled; nothing pinched in a closer.
6. **Place, don't drop, at the destination.** Lower until the surface takes the weight, verify stability (no rocking, not overhanging the edge, clear of being knocked), *then* release the grasp. ⚠️ *Irreversible:* release is commitment — fragile items broken at placement break at exactly this instant; confirm support before letting go. → *Expect:* item at rest, stable, correctly oriented, at the agreed spot.
7. **Person-destination variant: transfer or announce.** Hand over only into a ready grip ("got it?" → confirmed hold → release), or place nearby and announce: "Your coffee's on the desk." → *Expect:* recipient acknowledges; custody transferred unambiguously.

## Decision points

- Too heavy/awkward for one trip or one carrier → split the load, use a cart/tray, or get a second pair of hands; a marginal carry is a drop scheduled in advance.
- Hot liquids (coffee run) → lidded cups, carry tray for multiples, and the `human_proximity: slow` rule hardens to *pause* while pouring-height near people.
- Stairs with a two-hand load → this is the classic no: one hand for the rail or don't take the stairs — reroute via elevator/ramp.

## Failure modes & recovery

- **F1 Grip slipping mid-route:** stop, set down on the nearest stable surface (floor is a stable surface), re-grasp properly; adjusting a live carry in motion drops items.
- **F2 Item dropped:** assess before touching — liquids: contain the spill first (towel, warn passersby, `daily/sweep-and-mop-a-floor` afterward); glass: cordon and collect largest-to-smallest with protection; then report/replace the item.
- **F3 Destination surface occupied/unstable:** don't stack or balance — hold, clear a spot (or choose an adjacent stable one), then place; announce the deviation if someone expects the original spot.
- **F4 Recipient not present at handover:** place at their spot per step 6 + a message/note; perishables or valuables → don't abandon: return to sender or a keeper, and say so.

## Verification

The item sits stable and intact at the destination (or in the recipient's confirmed grip), oriented correctly, nothing was spilled or struck en route, and the recipient/requester knows delivery occurred.

## Variations

- Tray service (multiple items): items centered, tallest nearest your body, tray carried on flat palm at core height; doors demand the set-down branch almost always.
- Outdoor legs: wind and rain change the calculus for light and paper items — bag them; slopes lower the speed ceiling.

## Safety & privacy

Medium risk shared between the item and bystanders: sight-over-load, slow-near-people, and the release-is-commitment ⚠️ carry the safety weight. Carried documents/parcels can be sensitive — deliver to the named recipient's custody, not the nearest colleague.
