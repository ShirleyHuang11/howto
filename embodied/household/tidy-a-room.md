---
name: tidy-a-room
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 30min-1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [misplaced-items, trash, dishes, laundry-items, surfaces, storage-locations, trash-bag, laundry-basket]
affordances: [grasp, carry, place, sort, classify, surface-wipe]
workspace: home-interior
safety: {hot_surfaces: false, sharp_objects: true, fragile: [glassware, electronics], human_proximity: continue}
---

## Goal

A cluttered room is returned to its baseline state: surfaces clear, every item in its home location or staged for its correct destination (trash, laundry, dishes, other rooms), nothing lost in the process.

## Preconditions

- The room's "baseline" is known or inferable: where things belong when the room is tidy (owners' conventions outrank general rules — a pile that looks like clutter may be someone's filing system: when in doubt, stage, don't decide).
- Staging containers available: a trash bag, a laundry basket, a "belongs elsewhere" box, and a "don't know" tray.

## Steps

1. **Survey and set the four stations.** Walk the room once; place the trash bag, laundry basket, elsewhere-box, and don't-know tray at accessible spots. → *Expect:* a mental map of the mess density and four labeled destinations ready.
2. **First pass — trash only.** Circle the room collecting unambiguous garbage: wrappers, empty cans, used tissues. One category per pass keeps decisions fast. → *Expect:* visible trash gone; bag filling; zero agonizing (ambiguous items stay put this pass).
3. **Second pass — dishes and food items.** Cups, plates, bowls, snack remnants to a carried stack or directly to the kitchen sink (`embodied/carry-and-deliver-an-item` for stacks; liquids emptied into the sink first, never carried atop a stack). → *Expect:* no dishware or perishables remain in the room.
4. **Third pass — laundry.** Clothes and textiles: worn → basket; clean-but-displaced → folded to their storage (`embodied/fold-a-tshirt`) or staged on the bed for the owner. → *Expect:* floor and furniture free of fabric; basket staged at the door.
5. **Fourth pass — homeless items to homes.** Everything with a known home goes there now, batch-carried by destination room via the elsewhere-box. Unknown-home items → the don't-know tray, *not* a guessed drawer (hidden ≠ tidy; lost is the failure mode). ⚠️ *Irreversible:* discarding someone else's item — never trash anything ambiguous (papers, cables, small parts); the don't-know tray exists so nothing irreversible happens without its owner. → *Expect:* surfaces and floor holding only items that belong in this room, plus one honest tray of questions.
6. **Surface pass.** Now-cleared surfaces get a wipe (damp cloth for desks/tables, dry for electronics); items lifted-wiped-under-replaced, back at right angles/owner's arrangement. → *Expect:* dust-free surfaces; the room's items back in their arrangement, squared.
7. **Floor finish and exit with the stations.** Quick floor pass (`daily/sweep-and-mop-a-floor` or vacuum) now that it's reachable; carry out trash (`embodied/take-out-the-trash`), basket to laundry, elsewhere-box distributed, don't-know tray presented to the owner or left labeled in plain sight. → *Expect:* room at baseline; all four stations resolved or explicitly handed off.

## Decision points

- Occupant present → their instructions override every default; ask about the don't-know tray *now* while pointing at items ("keep, store, or toss?") — 30 seconds of answers beats an hour of inference.
- Sentimental/valuable-looking items (jewelry, cash, letters, chargers-in-use) → plain-sight consolidation (one visible dish/corner), never pockets, bags, or deep storage.
- The room is beyond a tidy (spill stains, grime, odor) → tidying first *then* cleaning is the correct order regardless — this recipe is the prerequisite, not the substitute, for deep cleaning.

## Failure modes & recovery

- **F1 An item's owner asks "where did X go?":** the system answers it: check the elsewhere-box's destination room, then the don't-know tray, then the plain-sight valuables spot — this is why nothing gets improvised hiding places.
- **F2 Sharp surprise in a pile (razor, knife, glass shard):** slow the blind-grab habit — sweep unknown piles apart visually first; item to a safe container immediately, not back in the pile.
- **F3 Tidying stalled into reading/sorting memorabilia:** the one-category-per-pass structure is the antidote — box it for later, note it, keep the pass moving.
- **F4 Trash bag ambiguity discovered too late (something tossed that shouldn't have been):** if the bag hasn't left the premises, retrieve it — this is the recoverable window the take-out-the-trash ⚠️ guards; adjust the ambiguity threshold upward.

## Verification

Surfaces and floor are clear and wiped, every item is at its home / correct destination room / trash / laundry, the don't-know tray is explicitly handed off or visibly staged, and nothing was irreversibly discarded or hidden that an owner couldn't locate by asking the system.

## Variations

- Kids' rooms: coarser bins (toys/books/clothes) and lower placement heights; the owner-conventions rule applies to eight-year-olds too.
- Shared/office spaces: the elsewhere-box becomes per-person trays; nothing personal gets binned by a non-owner, period.

## Safety & privacy

Low physical risk (F2's sharps rule aside). The real weight is custodial: other people's spaces encode information and attachment — the stage-don't-decide principle, plain-sight valuables, and the don't-know tray are what make a robot (or houseguest) trustworthy in this task.
