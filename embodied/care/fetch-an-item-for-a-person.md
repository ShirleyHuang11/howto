---
name: fetch-an-item-for-a-person
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 10min
risk: medium
prerequisites: [embodied/mobility/open-a-door, embodied/mobility/carry-and-deliver-an-item]
status: draft
last_verified: 2026-07-20
objects: [requested-item, similar-items, rooms, person]
affordances: [navigate, search, grasp, carry, handover, ask-clarification]
workspace: home-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [requested-item], human_proximity: slow}
---

## Goal

A person's request — "bring me my glasses / the remote / my blue pills" — ends with the *correct* item in their confirmed possession, with ambiguity resolved by asking rather than guessing.

## Preconditions

- A clear-enough request naming an item; the requester remains reachable for clarification (this recipe leans on that).
- The home's layout is known or explorable; likely locations for common items learned or inferable (glasses: bedside, reading spots; remote: sofa region; keys: entry surfaces).

## Steps

1. **Parse the request into item + distinguishing features + likely location.** "My glasses" → whose, which pair (reading vs. distance), where last seen. Missing features that matter → ask *now*, one compact question: "The reading glasses or the black ones?" → *Expect:* a search target specific enough that a wrong-item pickup would be surprising.
2. **Search likely locations in probability order.** The item's home spot → where the person last was → adjacent surfaces. Search visually before disturbing things; lift-and-look under papers/cushions with restoration (`embodied/household/tidy-a-room` principles: nothing hidden, nothing rearranged). → *Expect:* candidate found within 2–3 locations, rooms left as found.
3. **Verify the candidate against the distinguishing features.** Right color/type/label? **Medication special case:** the label must match the person's name and the named medicine exactly — ⚠️ *Irreversible:* delivering the wrong person's medication or the wrong drug is the category's serious harm; when any doubt exists, bring the *labeled container* to the person rather than loose items, and say what you observed: "This says 5 mg — is that the one?" → *Expect:* a candidate that matches every stated feature, or an explicit doubt being surfaced.
4. **If not found after the likely locations: report and re-scope, don't spiral.** Return (or call out) with what you checked: "Not on the nightstand or the sofa — where else should I look?" The requester's memory usually solves it in one exchange. → *Expect:* a new location hint or a redefined target; the search stays collaborative.
5. **Carry it back per its fragility.** Glasses by the frame (never lenses), liquids upright, the phone not stacked under the book (`embodied/mobility/carry-and-deliver-an-item`). → *Expect:* item intact and clean on arrival.
6. **Hand over into confirmed possession.** Into a ready hand ("got it?"), or placed at their stated spot within easy reach — for limited-mobility requesters, *within actual reach* matters more than proximity: on the tray table, not the far counter. → *Expect:* the person confirms it's the right item, in hand or in reach.

## Decision points

- Multiple matching candidates (two pairs of black glasses) → bring both or ask with the distinguishing detail you can see: "There's a scratched pair and a newer pair — which?" Guessing between valid candidates is how wrong items get delivered confidently.
- The requested item is somewhere private (another person's room, a bag, a drawer) → permission boundary: ask the owner or the requester to confirm before opening bags/drawers that aren't the requester's own.
- The request is for something potentially unsafe for the requester (alcohol with certain meds, the car keys during recovery, a third dessert against stated care rules) → not a silent veto and not silent compliance: surface it — "Happy to — the care sheet says to check this one; should I?" The human decides; the flag is the job.

## Failure modes & recovery

- **F1 Delivered the wrong item anyway:** retrieve the right one with the *new* distinguishing information the mistake produced; log the item's confusable twin for next time.
- **F2 Item genuinely lost (not in any location, requester out of ideas):** escalate to a systematic sweep of the last-used context (`tidy-a-room`'s pass structure finds lost things as a side effect) or the household's lost-item spots; report the negative result honestly rather than trickling hope.
- **F3 Item damaged in transit (dropped glasses):** report immediately with the state ("the arm bent — I'm sorry"), don't deliver damage silently; the trust cost of silence exceeds the incident.
- **F4 Requester unreachable at handover (asleep, stepped out):** perishables/meds → don't abandon at the spot: hold or return them and message; ordinary items → the stated spot + a note/message closes the loop.

## Verification

The person has the correct item confirmed (name-matched, for anything medical), within actual reach; searched rooms are as they were; any ambiguity, damage, or safety flag traveled *to the person* rather than being absorbed silently.

## Variations

- Repeat care contexts: build the person's item map (where their things live, their medication schedule's names) — fetch quality compounds with memory, exactly like `daily/social/greet-a-neighbor`'s banked details.
- Fetch-from-outside (mail, deliveries at the door): compose with `embodied/mobility/open-a-door` and the package-verification habit (right addressee before bringing it in).

## Safety & privacy

Medium risk concentrated in the medication ⚠️ and the permission boundaries: labels are read, doubts are voiced, private spaces need consent, and care rules produce flags rather than either silent enforcement or silent bypass. A good fetcher is trusted *because* it asks.
