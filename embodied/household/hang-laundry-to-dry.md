---
name: hang-laundry-to-dry
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: low
prerequisites: [embodied/household/load-a-washing-machine]
status: draft
last_verified: 2026-07-20
objects: [drying-rack, clothesline, clothespins, wet-laundry, laundry-basket, hangers]
affordances: [grasp-fabric, shake, hang, pin, carry, place]
workspace: home-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A washed load is hung to dry with air space and shape preserved, so it dries fast, wrinkles less, and smells like laundry rather than a damp cellar.

## Preconditions

- A finished wash moved promptly (`daily/home/do-the-laundry` step 7: sour-smell prevention starts at the machine door).
- A drying setup: rack, line, or rail, in moving air. Indoors: a ventilated room, ideally with a cracked window or a fan; drying in still, cold rooms breeds the damp smell and feeds mold on walls.
- Clothespins for outdoor lines; hangers for shirts if wardrobe-drying.

## Steps

1. **Shake each piece out hard before hanging.** Two sharp snaps per item unrolls the spin-cycle knots, releases wrinkles, and halves ironing later (`daily/home/iron-a-shirt` gratitude included). → *Expect:* items going up as flat panels, not twisted ropes.
2. **Hang heavy and slow-drying items on the outside or windward positions.** Towels, jeans, hoodies get the airiest spots with maximum spacing; quick-dry synthetics fill the inner rungs. → *Expect:* the load arranged by drying difficulty, thickest pieces catching the most air.
3. **Preserve garment shape as you hang.** Shirts on hangers (buttoned once at the collar) or by the hem, not the shoulders (pin-shoulders make peaks); trousers by the waistband or cuffs, straightened along the crease; knits *never* hang — they stretch; they lie flat on the rack's top or a towel. → *Expect:* nothing hanging by a point that will dent or stretch it.
4. **Give everything a finger of air space.** Overlapping fabric dries at the speed of its slowest layer; a crammed rack is a mildew experiment. Two rack loads beat one compressed one. → *Expect:* visible gaps between all items; airflow paths through the rack.
5. **Open the details.** Unfold cuffs and collars, open pockets outward, unroll waistbands, hang socks in pairs by the toes. The folded-over hem is where damp hides at the six-hour check. → *Expect:* every double-layer spot spread open.
6. **Position for air and check back.** Rack near the open window or fan (not touching a cold exterior wall), line-loads pinned firmly at two points per item. Rotate or flip thick items at the half-dry point. → *Expect:* full dryness in hours (breezy outdoors) to a day (indoors); waistbands and seams pass the `daily/errands/use-a-laundromat` step 6 touch test before anything folds away.

## Decision points

- Outdoor line weather call: sun and wind are the best dryer ever built, but check the sky honestly and mind pollen seasons for allergy households; strong sun fades darks, so hang those inside out.
- Radiator drying: on a rail *near*, not a wet pile *on*, the radiator; direct draping blocks heat, marks fabric, and pushes room humidity to window-condensation levels.
- Space crunch: doorframe rails, shower-rod hangers, and stacked-shift drying (quick synthetics first, replaced by heavies at midday) expand a small flat's capacity.

## Failure modes & recovery

- **F1 Damp smell on "dry" clothes:** they packed away with a wet seam, or dried too slowly in still air; re-wash (drying locks the smell otherwise, per `do-the-laundry` F4) and fix the airflow next round.
- **F2 Stretched knit shoulders or peaked t-shirts:** hung wrong for the garment; the shape rules in step 3 are per-item law. Shoulder peaks iron out; stretched knits mostly do not.
- **F3 Rain surprise on the outdoor line:** re-spin in the machine if soaked, then indoor-finish; a light sprinkle just extends the day.
- **F4 Rack collapse or line failure:** overloaded beyond its stated capacity, usually by wet jeans en masse; re-hang with the heavy items redistributed and the floor-touched pieces shaken and inspected (re-wash only what actually met dirt).

## Verification

Every item hangs shaken-flat with air space, by a shape-safe point, details opened, thickest pieces in the best air; the room has moving air; and at collection every seam and waistband passes the touch test before folding (`embodied/household/fold-a-tshirt` receives them warm-dry, ideally).

## Variations

- Dryer-owning households still route the never-tumble list here (`do-the-laundry` step 7's wool-and-elastic ⚠️); this recipe is that list's destination.
- `jp` balcony poles and `eu` cellar lines encode the same physics in local hardware; the finger-of-air rule is universal.

## Safety & privacy

Low risk. Two notes: indoor humidity goes somewhere, so ventilate the drying room (mold on walls is the slow cost), and outdoor lines display your wardrobe to the street, which some households reasonably route around by drying smalls inside.
