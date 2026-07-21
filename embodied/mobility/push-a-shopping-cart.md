---
name: push-a-shopping-cart
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [shopping-cart, groceries, aisle, cart-return-bay, other-shoppers]
affordances: [grasp, push, steer, brake, load, turn]
workspace: retail-store
safety: {hot_surfaces: false, sharp_objects: false, fragile: [eggs, produce, glass-jars], human_proximity: slow}
---

## Goal

A shopping cart is pushed through a store under control: loaded so it stays balanced and stable, steered cleanly around corners and other shoppers, and returned to a cart bay at the end without blocking aisles or drifting into cars.

## Preconditions

- A cart with all four wheels rolling (no locked or badly shimmying caster).
- Two-handed grip available on the handle bar.
- Known aisle layout or willingness to travel at yielding speed.

## Steps

1. **Check the cart before loading.** Push it a meter and watch the front casters. A hard shimmy or a locked wheel makes it fight your steering. → *Expect:* the cart tracks straight with a light push, no pull to one side.
2. **Load heavy and low first.** Put the heavy items (cans, bottles, milk) on the floor of the basket or centered over the rear axle, not stacked high or hung on the front end. → *Expect:* center of mass low and slightly rear-biased; cart does not tip forward when you lift the handle.
3. **Keep fragile items on top and braced.** Eggs, bread, produce, and glass go last, resting on the flat of the load or in the child seat, wedged so they cannot slide on turns. → *Expect:* fragile items visible and not under any weight.
4. **Push from behind with both hands.** Walk close to the handle so the cart is an extension of your reach, not out at arm's length where it swings wide. → *Expect:* straight-line travel with small steering corrections only.
5. **Take corners wide and slow.** Slow before the turn, swing the rear of the cart out slightly so the front does not clip the shelf end-cap, and straighten early. → *Expect:* no contact with shelving or the end-cap display; the load does not shift.
6. **Yield in the aisle.** Keep the cart to one side so others can pass; when stopping to reach a shelf, pull fully to the side, not across the center. [BRANCH: aisle clear → proceed at walking pace | shopper or cart approaching → stop or edge right and let them pass] → *Expect:* a clear lane past you at all times; no cart-to-cart standoff.
7. **Control speed on ramps and slopes.** ⚠️ *Irreversible:* a loaded cart on a slope can run away into traffic or a person. Keep both hands on the handle downhill and never let go of a moving loaded cart. → *Expect:* the cart never rolls unattended; you set it down only when it is stopped and, if a brake exists, engaged.
8. **Return to a cart bay.** Steer into the nearest corral or return rack, nest the cart into the row front-to-back, and push until it seats against the cart ahead. → *Expect:* the cart is fully nested inside the bay, not left protruding into a parking lane or walkway.

## Decision points

- One caster locks up mid-trip → transfer the load to a sound cart rather than fighting the drift for the whole store.
- Steep parking-lot slope → take the flattest path to the bay and keep speed to a walk; a runaway cart is the top parking-lot hazard.
- Bay is full and overflowing → nest against the outermost cart and push the row tight rather than abandoning yours loose.

## Failure modes & recovery

- **F1 Cart pulls to one side:** a shimmying or gummed caster → reduce speed, add a little rear weight, or swap carts if it is unmanageable.
- **F2 Load topples on a turn:** heavy item stacked high shifted → stop, restack heavy-low, and re-brace the fragile layer before continuing.
- **F3 Clipped an end-cap:** turned too tight and too fast → back off, swing wider, slow the approach to every corner after.
- **F4 Runaway on a slope:** cart accelerates away → do not chase and grab the front (you will be run over); the fix is prevention, never releasing a loaded cart on any incline.

## Verification

All items arrive intact (no crushed produce, no broken glass), the cart caused no collision with shelves, people, or vehicles, and it ends fully nested in a cart bay rather than loose in an aisle or lot.

## Variations

- `us-warehouse`: oversized flatbed carts steer from the front and need even wider corners and longer stopping distance.
- Two-tier or child-seat carts: the seat is the correct place for eggs and bread, with the child harness strap used to wedge them.

## Safety & privacy

Medium risk: the real hazards are a runaway cart on a slope and crushed or broken goods from bad loading. Human proximity is slow: pass people at walking pace, yield in aisles, and never let go of a loaded moving cart. No personal data involved.
