---
name: slide-a-book-off-a-shelf
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [book, shelf, neighboring-books]
affordances: [locate, press, slide, grasp, pull, support]
workspace: bookshelf
safety: {hot_surfaces: false, sharp_objects: false, fragile: [book-cover, shelf-edge], human_proximity: continue}
---

## Goal

One selected book is removed from the shelf without pulling down neighboring books.

## Preconditions

- The selected book is identified.
- Shelf is reachable and stable.
- There is enough front clearance to remove the book.

## Steps

1. **Locate the selected spine.** Read or match the spine and identify its left and right neighbors. → *Expect:* the target book boundaries are visible.
2. **Create a small gap.** Press neighboring books slightly away from the target with flat finger pressure. → *Expect:* a narrow clearance appears on at least one side.
3. **Grip the upper spine.** Pinch the target book near the top spine edge without hooking fragile paper. → *Expect:* the book moves slightly while neighbors stay in place.
4. **Slide outward partway.** Pull the book straight forward 3-6 cm while keeping it vertical. → *Expect:* enough cover edge protrudes for a full grip.
5. **Transfer to cover support.** Grip the protruding book with one hand on each side or one hand under the bottom edge. → *Expect:* the book weight is supported beyond the spine.
6. **Remove fully.** Pull straight out until the back cover clears the shelf row. → *Expect:* the book is free and neighboring books remain upright.
7. **Close the shelf gap.** Push neighboring books together or move a bookend inward. → *Expect:* the remaining row is upright and supported.

## Decision points

- Book is tight in the row → push from the back if accessible or remove an adjacent book first.
- Spine is fragile → avoid pulling by the top cap and use side pressure to expose the cover.
- Book is large or heavy → support the bottom edge before full removal.

## Failure modes & recovery

- **F1 Neighbor book falls:** detect by adjacent book tipping outward → catch or push it back and add bookend support.
- **F2 Spine separates:** detect by cover flexing away from pages → stop pulling by spine and support the covers instead.
- **F3 Book catches on shelf lip:** detect by halted forward motion at bottom edge → lift the front edge slightly and continue straight out.

## Verification

The selected book is fully removed and the remaining books stand upright without falling or leaning unsupported.

## Variations

- Deep shelf: pull until both hands can support the book before lifting.
- Tight row: remove a thinner neighboring book first to create working space.

## Safety & privacy

Avoid dropping heavy books on feet or exposing private titles in shared spaces when privacy matters.
