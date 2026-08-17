---
name: help-someone-find-misplaced-glasses
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [person, glasses, case, table, chair, bed]
affordances: [ask, search, lift, inspect, retrieve, hand-over]
workspace: care-space
safety: {hot_surfaces: false, sharp_objects: false, fragile: [glasses], human_proximity: slow}
---

## Goal

Help someone locate misplaced glasses and return them without damaging the glasses or disturbing private belongings unnecessarily.

## Preconditions

- The person wants help searching.
- Likely recent locations are known or can be asked about.
- Permission is granted before opening drawers, bags, or private areas.

## Steps

1. **Ask for last known use.** Ask where the glasses were last worn, removed, or cleaned. → *Expect:* one or more likely search areas are identified.
2. **Check the person first.** Look at head, neckline, lap, pockets, bedcovers, and nearby chair arms. → *Expect:* glasses are found there or ruled out.
3. **Search visible surfaces.** Inspect tables, counters, nightstands, bathroom sinks, and cases without moving private items yet. → *Expect:* obvious locations are checked.
4. **Lift soft items carefully.** Raise blankets, towels, papers, or clothing one layer at a time. → *Expect:* hidden glasses are not crushed or flung.
5. **Ask before private search.** Request permission before opening drawers, bags, cabinets, or mail piles. → *Expect:* consent is given or the area is skipped.
6. **Check unsafe spots.** Look under chairs, near floor edges, and beside beds before anyone steps or sits. → *Expect:* glasses are recovered or protected from damage.
7. **Return the glasses safely.** Hand them over by the frame or place them in the person's hand or case as preferred. → *Expect:* the person has control of the glasses.
8. **Store or mark the location.** If requested, place the case in a consistent reachable spot. → *Expect:* the person knows where the glasses are now.

## Decision points

- Person does not consent to a search area → skip that area.
- Glasses are found damaged → stop using them and report the damage.
- Person becomes anxious → slow down, narrate locations checked, and ask where to continue.
- Search area has hazards → move tripping or sharp hazards only as needed and with permission.

## Failure modes & recovery

- **F1 Glasses under fabric:** detect hard shape or frame outline → lift fabric slowly and retrieve by frame.
- **F2 Private item exposed:** detect documents, medication, or valuables → stop looking there unless explicitly permitted.
- **F3 Lens scratched:** detect glasses sliding lens-down → pick up by frame and place in case.
- **F4 Search repeats:** detect same area checked twice → list checked areas aloud and move to next likely location.

## Verification

The glasses are found and returned intact to the person or placed in a known case/location, with private areas searched only by permission.

## Variations

- Low vision: describe each checked location aloud and hand glasses directly.
- Shared room: verify the glasses belong to the person before handing them over.
- Multiple pairs: ask which pair is needed before stopping the search.

## Safety & privacy

Low physical risk but meaningful privacy risk. Ask before opening personal spaces, handle lenses by the frame, and keep medications, papers, and valuables confidential.
