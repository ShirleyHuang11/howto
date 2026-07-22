---
name: balance-radiators
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Radiators heat more evenly across rooms by slowing the hottest radiators at their lockshield valves and giving colder radiators more flow.

## Preconditions

- Heating system is working, cool enough to touch at the start, and all radiator valves are accessible.
- You have a radiator key for bleeding, an adjustable spanner, cloths, and a way to note valve turns.
- You understand which valve is the thermostatic or hand valve and which is the lockshield valve.

## Steps

1. **Bleed air first.** With heating off and cool, bleed radiators that have cold tops, then close the bleed valve. → *Expect:* water appears steadily and trapped air is gone.
2. **Open valves fully.** Open each thermostatic valve and remove lockshield caps to open each lockshield fully. → *Expect:* all radiators can receive full flow.
3. **Turn heating on.** Let the system warm from cold and note which radiators heat first. → *Expect:* faster radiators reveal where flow is strongest.
4. **Throttle the fastest radiator.** Close its lockshield fully, then reopen about a quarter to half turn. → *Expect:* that radiator still heats but warms more slowly.
5. **Move through the house.** Adjust each early-hot radiator in small increments, waiting several minutes between changes. → *Expect:* colder rooms begin warming closer to the rest.
6. **Leave cold rooms more open.** Keep lockshields more open on radiators that heat last. [BRANCH: one cold radiator | whole zone cold] one radiator suggests valve or air, a zone suggests pump or controls. → *Expect:* heat distribution becomes more even.
7. **Replace caps and record settings.** Note approximate lockshield turns for each room. → *Expect:* settings can be restored if someone changes a valve.

## Decision points

- Radiator is cold at the top → bleed before balancing again.
- Radiator is cold at the bottom → sludge may need flushing rather than valve balancing.
- Lockshield leaks when turned → stop, tighten packing gently if designed for it, or call a heating engineer.
- Boiler pressure drops after bleeding → refill to the boiler maker's cold pressure range.

## Failure modes & recovery

- **F1 Room gets colder:** detect a radiator that no longer reaches temperature, recover by opening its lockshield an eighth turn and waiting.
- **F2 Valve sticks:** detect no change after turning, recover by freeing the pin on thermostatic valves or getting service for seized lockshields.
- **F3 Pressure falls:** detect low boiler pressure after bleeding, recover by refilling according to the boiler instructions.
- **F4 Noise appears:** detect rushing or whistling, recover by opening overly restricted lockshields slightly.

## Verification

After one full warm-up, all occupied rooms reach usable heat without one radiator becoming hot much earlier than the rest.

## Variations

- `thermostatic-valves`: set room comfort with thermostatic valves after balancing, not during the first pass.
- `two-story-home`: upstairs often heats faster and may need more throttling.
- `communal-heating`: do not adjust shared system valves without building approval.

## Safety & privacy

Medium risk from hot water, sharp valve edges, and boiler pressure changes. Work slowly, keep cloths ready, and stop if a valve leaks.
