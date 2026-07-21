---
name: walk-up-a-ramp
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [ramp, handrail, floor]
affordances: [assess-slope, step, lean, grip, stabilize]
workspace: building-interior
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

The actor ascends a ramp using controlled short steps or steady drive, with posture adjusted for slope and traction.

## Preconditions

- The ramp surface is visible, stable, and intended for travel.
- The actor can see or sense the top landing.
- Footwear, wheels, or contact surfaces have adequate traction.
- Any carried load is secured close to the body or base.

## Steps

1. **Stop at the ramp base.** Pause before the slope begins and inspect the surface. → *Expect:* slope, width, handrails, and hazards are visible.
2. **Assess the incline.** Judge whether the ramp is mild, moderate, or too steep for current load and ability. → *Expect:* ascent is judged feasible or a different route is chosen.
3. **Align straight with the ramp.** Face uphill with feet, wheels, or base parallel to the ramp edges. → *Expect:* travel direction points directly up the slope.
4. **Lean slightly uphill.** Bring torso or center of mass forward enough to counter backward pull. → *Expect:* weight feels centered over the uphill travel path.
5. **Use support if available.** Place a hand on the rail or keep one side near a wall if needed. → *Expect:* support is reachable without twisting.
6. **Take shorter steps.** Step uphill with reduced stride length and full foot placement. → *Expect:* each foot lands flat and does not slide.
7. **Maintain steady pace.** Continue with even rhythm, avoiding sudden stops or side drift. [BRANCH: handrail present | no handrail] use light rail contact if present; keep arms free for balance if not. → *Expect:* ascent remains controlled.
8. **Transition onto the landing.** Step or roll fully onto the flat top area before changing direction. → *Expect:* both feet or full base are on level ground.
9. **Pause and re-balance.** Stand still on the landing before the next movement. → *Expect:* posture returns upright and stable.

## Decision points

- Ramp is too steep → use an elevator, alternate route, or assistance.
- Surface is wet, icy, loose, or cluttered → clear it or avoid the ramp.
- Another person is descending → yield on the landing or widest section.
- Load pulls backward → reduce load, use handrail, or carry closer.
- Ramp has a turn → slow before the turn and re-align after it.

## Failure modes & recovery

- **F1 Foot slips:** detect backward slide or loss of traction → stop, grip support, step down carefully, and choose another route.
- **F2 Breathing or effort spikes:** detect strain beyond comfortable level → stop on a stable section or retreat to base.
- **F3 Side drift:** detect movement toward ramp edge → shorten steps and steer back to center.
- **F4 Load shifts:** detect backward or side pull → pause, set load down if possible, and redistribute.
- **F5 Top transition catches:** detect toe, wheel, or object snag at landing lip → stop, lift or roll over slowly, and avoid twisting.

## Verification

The actor reaches the top landing with full support on level ground, no slipping, and stable posture before continuing.

## Variations

- `wheelchair`: lean forward, push short strokes, and use anti-tip support if required by the chair.
- `walker`: move walker a short distance uphill first, then step into it.
- `stroller-or-cart`: keep both hands on the handle and avoid side angles.
- `outdoor-ramp`: inspect for water, gravel, leaves, and edge drop-offs before ascent.

## Safety & privacy

Low risk on dry compliant ramps. Slow down near people, wet surfaces, and ramp edges. Do not rush the landing transition because many slips happen where slope changes to level.
