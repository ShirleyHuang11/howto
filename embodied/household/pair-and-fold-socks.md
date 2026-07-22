---
name: pair-and-fold-socks
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [sock, cuff, heel, toe, odd-sock-bin]
affordances: [sort, match, align, fold, roll, tuck, place]
workspace: laundry area
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

Clean socks are matched by pattern and size, folded or rolled without overstretching cuffs, and unmatched socks are placed in an odd-sock bin.

## Preconditions

- Socks are clean and dry.
- A flat surface is available for sorting.
- Odd-sock bin or holding area is ready.

## Steps

1. **Spread socks flat.** Place socks on the surface with toes pointing roughly the same direction and cuffs visible. → *Expect:* patterns, sizes, and wear marks can be compared.
2. **Match by pattern first.** Pair socks with the same color, texture, logo, and stripe or knit pattern. → *Expect:* likely pairs form without needing to stretch them.
3. **Confirm by size and wear.** Align toe to toe and heel to heel, checking cuff height and fabric thickness. → *Expect:* each pair has matching length and shape.
4. **Set odd socks aside.** Place any unmatched sock in the odd-sock bin rather than forcing a weak match. → *Expect:* sorting area contains only confirmed pairs.
5. **Choose fold or roll.** [BRANCH: fold-over cuff | roll] use fold-over for drawers and roll for travel or compact storage. → *Expect:* both socks in a pair are stacked evenly.
6. **Fold-over method.** Lay one sock on the other, align toes and cuffs, then fold only the outer cuff over the pair with light tension. → *Expect:* cuff holds the pair without whitening or stretching.
7. **Roll method.** Stack the pair, roll from toes toward cuffs using gentle pressure, then tuck the last cuff edge around the roll if needed. → *Expect:* roll stays together and the cuff is not strained.
8. **Place the pair.** Put folded pairs in the drawer with cuffs visible for identification. → *Expect:* pairs remain together and are easy to select later.

## Decision points

- Elastic is weak or old → avoid fold-over and use a loose flat fold.
- Socks differ only by size → compare heel position and cuff width before pairing.
- Athletic compression socks → roll loosely or lay flat to protect elastic.

## Failure modes & recovery

- **F1 False pair:** toe length, heel shape, or pattern mismatch appears after alignment → split the pair and return both to sorting.
- **F2 Overstretched cuff:** cuff flares or elastic crackles → stop folding over cuffs and use loose rolls for that sock type.
- **F3 Missing mate:** no matching sock remains → put the single in the odd-sock bin and revisit after the next laundry load.
- **F4 Lint or debris inside:** sock feels gritty while folding → turn it inside out, shake it clean, and refold.

## Verification

Every stored pair contains two matching socks held together without stretched cuffs, and every unmatched sock is in the odd-sock bin.

## Variations

- Dress socks: fold flat once instead of rolling tightly to prevent creases.
- Children's socks: match by size marking or wear pattern because designs may repeat across sizes.
- Drawer organizer: place pairs upright in rows so patterns remain visible.

## Safety & privacy

Low risk. Avoid snapping elastic near the face, and do not force damp socks into a drawer because trapped moisture can cause odor or mildew.
