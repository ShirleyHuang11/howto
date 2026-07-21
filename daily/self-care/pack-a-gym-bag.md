---
name: pack-a-gym-bag
domain: daily
subdomain: self-care
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

A gym bag packed the night before that contains everything the workout and the after-shower need, so a missing sock never becomes the reason today's session died.

## Preconditions

- A planned workout whose type you know (gym floor, class, pool, run-commute), since the type sets the list.
- A bag with at least one separating layer: a wet/dirty compartment or a plastic/dry bag inside.

## Steps

1. **Pack the workout layer.** Shoes (the item most often forgotten because they live by the door), shorts/leggings, shirt, sports socks, and sport-specific kit (gloves, goggles and cap for the pool, towel for the mat class). → *Expect:* the full outfit physically in the bag, not "the shoes I'll grab on the way".
2. **Pack the shower layer.** Flip-flops for shared showers, towel, and travel-size toiletries that live in the bag permanently (shower gel, shampoo, deodorant). Permanent residents beat nightly decanting. → *Expect:* a small toiletry pouch that never leaves the bag.
3. **Pack the after layer.** Full change: underwear, socks, shirt, and whatever the day after the gym requires (work clothes if commuting through the session). Underwear is the most-forgotten after-item; check it explicitly. → *Expect:* tomorrow-you can dress completely from the bag.
4. **Add the small enablers.** Water bottle (filled in the morning, packed empty tonight), lock for the locker, headphones, membership card or the phone that carries it, hair ties, plasters. → *Expect:* the pocket inventory done; the lock is the one that strands people.
5. **Separate wet from dry in advance.** The empty wet-bag goes in now so the post-shower swimsuit or sweaty kit has a destination other than your clean clothes. → *Expect:* a dedicated wet compartment ready.
6. **Stage the bag at the door.** Same principle as `daily/food/pack-a-lunch`: night-you plans around morning-you's memory. → *Expect:* the bag physically between you and leaving.

## Decision points

- Morning vs evening sessions: morning trainers pack everything the night before including breakfast logistics; evening trainers pack in the morning and carry the bag to work, which makes step 3's work-clothes direction flip.
- Locker situation known? No secure lockers means the valuables plan changes: minimal wallet, phone on the gym floor with you.
- Laundry cadence: two permanent gym outfits rotating through `daily/home/do-the-laundry` beat one outfit that is always the reason you cannot go.

## Failure modes & recovery

- **F1 At the gym without shoes (or any single critical item):** salvage what the session allows (many gyms rent towels and sell socks; a barefoot-friendly stretch session beats going home), then move that item's storage location into the bag permanently.
- **F2 Yesterday's wet kit discovered fermenting in the bag:** wash kit and bag compartment promptly (`daily/home/do-the-laundry`), air the bag out, and make unpacking-on-arrival-home part of the ritual rather than a discovery.
- **F3 Bottle leaked on everything:** carry it empty or upright in an outside pocket; electronics live in a different compartment from any liquid, always.
- **F4 Bag packed but gym skipped anyway:** the bag did its job; the calendar is the other half. Book sessions like meetings (`communication/schedule-a-meeting` with yourself) and let the staged bag lower the friction.

## Verification

The bag contains the three layers (workout, shower, after) plus lock and bottle, wet and dry have separate homes, it sits at the door, and the morning requires zero decisions beyond picking it up.

## Variations

- Run-commuters: the bag lives at work with the office layer, and the run carries only keys, phone, and card.
- Pool-goers: goggles, cap, and the wet-bag graduate from optional to core; chlorine makes the rinse-and-dry cycle non-negotiable.

## Safety & privacy

Low risk. The lock and the minimal-valuables habit cover the locker room; flip-flops cover the shower floor, which is the gym's most contagious surface.
