---
name: run-a-potluck
domain: daily
subdomain: social
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h-4h
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

A shared meal happens where the dishes cover a real menu (not seven desserts), everyone can tell what they can safely eat, and every container goes home with its owner.

## Preconditions

- A confirmed date, venue with table space and some way to keep hot things warm, and a guest list of roughly 6-30 people.
- A shared signup sheet everyone can edit: a group chat pinned message works for small groups, a shared doc or signup tool for larger ones.
- Host willing to do light coordination; a potluck with zero coordination is where the seven-desserts problem comes from.

## Steps

1. **Publish a category signup, not an open list.** Slots by category with counts, sized to the guest list: mains (1 per 4-5 guests), sides, salads, desserts (cap these), drinks, plus one "staples" line the host owns. → *Expect:* the sheet shows named slots with limits; guests claim a slot with a specific dish, not just "I'll bring something."
2. **Ask for dietary constraints in the same message.** One question: allergies or hard restrictions in the group? Relay the answers onto the sheet so cooks see them before shopping. → *Expect:* constraints (nut allergy, vegetarian, halal, gluten-free) visible at the top of the sheet.
3. **Nudge duplicates and gaps at T-minus 3 days.** Message anyone whose dish duplicates another; note unclaimed slots. → *Expect:* each category at or under its cap; remaining gaps are known to the host.
4. **Host covers the gaps and the invisible items.** The host's job is the unglamorous backbone: one reliable main as insurance, rice or bread, serving utensils, ice, plates and cups if disposable, trash bags, and a stack of blank labels with a marker. → *Expect:* even if two guests flake, there is a complete meal.
5. **Stage the table by course with labels on arrival.** As each dish lands, its cook (or the host) writes a label: dish name, key allergens (nuts, dairy, gluten, shellfish), and veg/not. Keep raw-meat-adjacent utensils separate; one serving utensil per dish, never shared across dishes. → *Expect:* every dish labeled before eating starts; no utensil migrates between dishes.
6. **Mark containers with owners' names.** Masking tape and marker on the underside of each container as it arrives, done by the door. → *Expect:* every container traceable to a person; this 10-second habit is what gets containers home.
7. **Manage the hot-food window.** Serve within roughly 2 hours of dishes landing at room temperature; hot dishes go out in waves rather than all sitting from minute one. → *Expect:* nothing perishable sits out much past the 2-hour mark (see F4).
8. **Run the leftovers-and-containers exit.** Last 20 minutes: owners reclaim containers by the tape names; leftovers get offered around and packed into whatever spare containers exist, with the host keeping only what they will actually eat. → *Expect:* guests leave with their own containers; the host is not hosting a container orphanage.

## Decision points

- Fewer than 8 guests → skip the tooling; a pinned group-chat message with categories is enough, but keep the dessert cap.
- A guest asks "what should I bring?" with no opinion → assign the emptiest slot directly; open-ended answers produce desserts.
- Someone with a severe allergy attending → their safe options should be whole dishes made without the allergen, not "picked around"; tell relevant cooks directly, and accept that shared-utensil cross-contact means truly severe cases need dedicated dishes.
- Venue has no oven or outlets → shift the signup toward room-temperature dishes and ask hot-dish cooks to arrive last, food still hot.

## Failure modes & recovery

- **F1 Seven desserts anyway:** signup was open-format or people ignored slots → detect at the T-minus-3 nudge; convert the excess by direct asks ("could yours become a fruit salad side?") and host-buy the missing main.
- **F2 Flake gap at showtime:** a claimed main never arrives → the host insurance main covers it; if two mains flake, stretch with the staples (rice, bread) and reorder serving so gaps are not obvious.
- **F3 Unlabeled mystery dish:** cook wandered off before labeling → track them down before serving starts; an unlabeled dish is effectively off-limits to every allergic guest.
- **F4 Food safety drift:** mayo salads and meat dishes sitting out for 3+ hours in a warm room → assign someone to sweep perishables to the fridge or ice at the 2-hour mark; when in doubt at cleanup, discard rather than send home.
- **F5 Container diaspora:** no names on containers, so the host keeps a shelf of orphans for months → the door-tape step prevents it; for orphans that happen anyway, photo to the group chat within a day, then donate whatever is unclaimed in two weeks.

## Verification

The meal had at least one main per 4-5 guests and desserts within the cap, every dish carried a legible allergen label before serving, no perishable dish exceeded the 2-hour window unrefrigerated, and within a day of the event the host holds zero unclaimed containers.

## Variations

- Workplace version: signup by team channel, fridge and microwave logistics dominate, and label rules matter more (colleagues know each other's diets less well than friends do).
- Themed potluck (taco bar, soup night): categories become components (proteins, toppings, bases); duplication risk drops, host-staples burden rises.

## Safety & privacy

Low risk overall. The real hazards are allergen cross-contact (labels plus one-utensil-per-dish is the mitigation) and time-temperature abuse of perishables. Dietary information volunteered by guests is mildly personal; put the constraint on the sheet, not the medical story behind it.
