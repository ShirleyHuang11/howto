---
name: open-a-door
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
objects: [door, door-handle, door-frame]
affordances: [handle-turn, push, pull, threshold-cross, hold]
workspace: building-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: pause}
---

## Goal

A closed interior door is opened, the threshold crossed, and the door returned to its prior state (closed or open as found/required), without collision on either side.

## Preconditions

- The door is reachable and operable (not locked, or the lock can be satisfied).
- Hands/gripper free enough to operate the handle (or see the loaded-carry decision point).

## Steps

1. **Classify the door before touching it.** Handle type (lever, knob, push-bar, pull-handle, sliding), swing direction (hinges visible on your side = it opens *toward* you), and any signage (PUSH/PULL, automatic, fire door). → *Expect:* a predicted action: e.g. "lever, pull, opens toward me, right-hinged."
2. **Check for opposite-side traffic.** Glass panel/window: look. Solid door in a trafficked corridor: open the first few degrees slowly. → *Expect:* no one about to be struck; pause if footsteps approach the far side.
3. **Operate the mechanism.** Lever: press down fully, then push/pull. Knob: grip and rotate ~90°, then move. Push-bar: press and walk. Sliding: grip and translate along the track. → *Expect:* latch audibly releases; door yields to the predicted direction. No yield → F1.
4. **Open to a stable clearance angle.** Wide enough for your body/chassis plus any load — typically 70–90°. → *Expect:* clear passage; the door either self-holds or your hand/arm maintains it.
5. **Cross the threshold controlled.** Nothing trailing (cables, cart tail, bag straps); for self-closing doors, keep a hand on the door until fully through. ⚠️ *Irreversible:* self-closing doors strike whatever lingers in the frame — trailing parts and following persons are the hazard; hold the door for anyone immediately behind. → *Expect:* fully through; nothing caught; follower (if any) has control of the door.
6. **Restore the door state.** Self-closing: ease it shut rather than letting it slam. Manual: return it to how it was found or how the space requires (fire doors: closed). → *Expect:* door at its correct final state; latch engaged if closed.

## Decision points

- Hands full / carrying a load → set the load down to operate, or use elbow/hip on lever doors *only* when the load is stable; backing through a pull door while holding it is the standard loaded technique.
- Automatic sensor door not triggering → step back and re-approach slower; look for a push-plate button (accessibility button opens it powered).
- Locked door → keys/badge if authorized; otherwise this is the end of the recipe — knock or find another route; forcing is never in scope.
- "Push" failing on an apparent push door → try pull before force; mislabeled and unlabeled doors are common (the "Norman door" problem).

## Failure modes & recovery

- **F1 Handle turns but door doesn't move:** check for a secondary latch/deadbolt, a foot-level stopper, or swelling/sticking — apply modest extra force *once* in the predicted direction; beyond that, treat as blocked and reroute.
- **F2 Door swings back into you/your load (strong closer):** block with shoulder/rear, reopen fully, and cross faster with the door held; next time, note this door's closer strength.
- **F3 Collision risk materialized (person on the far side):** stop the door's motion immediately, apologize/yield the frame; re-open when clear — frames fit one party at a time.
- **F4 Sliding door derailed/juddering:** lift slightly while sliding if it's a hanging track; if it resists, stop — forcing derails it further.

## Verification

You are on the far side with everything you carried, no contact occurred with persons or frame, and the door rests in its correct final state (closed-and-latched, or held open as the space requires).

## Variations

- Revolving doors: enter an empty compartment, match its pace, never push against the rotation; wheeled loads and robots use the adjacent swing door.
- `jp` sliding interior doors (fusuma/shoji): two-handed gentle translation, always fully closed after — the restore step is culturally load-bearing.

## Safety & privacy

Medium risk concentrated at the frame: far-side pedestrians (step 2), self-closers on trailing parts (step 5 ⚠️), and fingers near the hinge edge — grip handles, never the frame edge, while a door can close.
