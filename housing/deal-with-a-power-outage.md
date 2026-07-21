---
name: deal-with-a-power-outage
domain: housing
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

When the power goes out you quickly determine whether the fault is yours or the grid's, report it if needed, keep your food and household safe, and light the home without creating a fire or carbon-monoxide hazard.

## Preconditions

- Knowing where your consumer unit / breaker panel is and how to read it.
- A charged phone and at least one battery light or torch reachable in the dark.
- Your electricity supplier's fault number, or a way to look it up.

## Steps

1. **Check whether it is just you or the whole street.** Look at neighbours' lights and streetlights. [BRANCH: neighbours also dark → grid outage, go to step 4 | only your home dark → likely your circuit, go to step 2] → *Expect:* a clear yours-or-grid verdict.
2. **Check the breaker panel.** Look for a tripped main or a single switch flipped to off/middle. → *Expect:* you can see which breaker, if any, has tripped.
3. **Reset a tripped breaker once.** Push it fully off then back on. If it trips again immediately, leave it off. ⚠️ *Irreversible:* a breaker that trips repeatedly is protecting you from a fault; do not tape or force it, unplug suspect appliances and call an electrician. → *Expect:* power restored, or the breaker holding off with the faulty circuit isolated.
4. **Report a grid outage to the network operator, not just the supplier.** Use the outage hotline or app; give your address and ask for an estimated restoration time. → *Expect:* a logged report and, usually, an ETA.
5. **Keep fridge and freezer doors shut.** A closed fridge holds safe temperature ~4 hours, a full freezer ~48 hours (24 if half full). → *Expect:* doors staying closed; no "just checking" openings.
6. **Light the home safely.** Use battery lights or torches first. ⚠️ *Irreversible:* never run a generator, barbecue, or fuel heater indoors or in a garage (carbon monoxide kills silently); candles are a fire risk near fabric and children. → *Expect:* rooms lit without an open flame or an indoor engine.
7. **Turn off and unplug sensitive electronics.** Computers, TVs, and the boiler control can be hit by the surge when power returns. Leave one light switched on as a restoration indicator. → *Expect:* sensitive devices unplugged; one telltale light left on.
8. **When power returns, restore gradually and check food.** Reconnect appliances one at a time; inspect fridge/freezer contents against the temperature rules. → *Expect:* everything powered, and any spoiled food identified.

## Decision points

- Breaker trips repeatedly, burning smell, or scorched socket → stop resetting, isolate the circuit, call an electrician (or emergency services if smoke).
- Outage with medical equipment or vulnerable residents → tell the network operator you are on a priority register; use backup power or relocate.
- Wires down outside or flooding near electrics → treat as dangerous, keep clear, and call the emergency line.

## Failure modes & recovery

- **F1 RCD/main trips the whole house:** one faulty appliance is the usual cause → unplug everything on the dead circuit, reset, then reconnect items one by one to find the culprit.
- **F2 Food safety uncertain:** doors were opened, ETA unknown → "when in doubt, throw it out"; perishables above 5°C for over 2 hours are unsafe, never taste-test.
- **F3 Carbon-monoxide risk from improvised heat/power:** headache, dizziness, nausea indoors → get everyone into fresh air immediately and never run combustion engines or grills inside.
- **F4 Surge damage on restoration:** devices left plugged → unplug during the outage and use surge protectors; a telltale light warns you before you reconnect the rest.

## Verification

You have correctly identified the fault as yours or the grid's, reset a single tripped breaker or reported a grid outage with a reference, kept fridge/freezer closed, lit the home without any indoor flame or engine, and on restoration reconnected devices safely and discarded any unsafe food.

## Variations

- `us`: report to your utility's outage map/line; breaker panels use flip-style breakers rather than a single RCD.
- `uk`: call 105 to reach the local network operator for grid faults; the consumer unit uses RCDs and MCBs.

## Safety & privacy

Medium risk, dominated by two lethal hazards: carbon monoxide from running generators, grills, or fuel heaters indoors, and electrical fault from repeatedly resetting a tripping breaker. Both have a hard rule: never bring combustion indoors, and never override a breaker that will not hold.
