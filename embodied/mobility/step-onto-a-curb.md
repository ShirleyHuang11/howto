---
name: step-onto-a-curb
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [curb, sidewalk, shoes, walking-surface]
affordances: [look, balance, step-up, weight-transfer, clear-foot]
workspace: mobility
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: slow}
---

## Goal

The person steps from a lower walking surface onto a curb or sidewalk, clears both feet, and continues facing the direction of travel.

## Preconditions

- The curb edge and landing area are visible.
- Shoes or feet have enough traction for the surface.
- Hands are free enough for balance, or a rail, cane, or helper is available.
- Traffic, bicycles, and other people are not creating immediate conflict.

## Steps

1. **Slow before the curb.** Reduce pace a step or two before reaching the edge. → *Expect:* the body is balanced and not rushing into the curb.
2. **Judge the height.** Look at the curb face and landing surface. → *Expect:* the rise appears within comfortable step height and the landing is clear.
3. **Choose the lead foot.** Pick the stronger or more stable foot for the first step up. → *Expect:* the lead foot is close to the curb and pointed forward.
4. **Place the lead foot up.** Lift the lead foot onto the sidewalk, setting the whole sole down if space allows. → *Expect:* the lead foot is flat and secure on top.
5. **Transfer weight.** Shift body weight over the lead foot while keeping the torso upright. → *Expect:* the lead leg supports the body without wobble.
6. **Clear the trailing foot.** Lift the back foot high enough to avoid catching the curb edge. → *Expect:* the trailing toes pass over the edge cleanly.
7. **Set the trailing foot down.** Place it beside or slightly ahead of the lead foot. → *Expect:* both feet are on the higher surface.
8. **Look ahead and continue.** Raise gaze from the curb to the path ahead before walking on. → *Expect:* forward path, obstacles, and people are visible.

## Decision points

- Curb is too high -> find a curb cut, ramp, lower section, or ask for support.
- Surface is wet, icy, sandy, or broken -> slow further and use support if available.
- Carrying a load blocks view -> pause and reposition the load before stepping.
- Someone is close beside you -> slow and leave room before transferring weight.

## Failure modes & recovery

- **F1 Toe catch:** trailing foot bumps the curb, stop and regain balance before moving again.
- **F2 Lead foot slips:** sole shifts on landing, step back down if safe or use support before retrying.
- **F3 Misjudged height:** knee or hip feels overextended, step down and find a lower route.
- **F4 Blocked path:** another person or object enters the landing area, pause before stepping up.

## Verification

Both feet are fully on the sidewalk or curb-top surface, balance is stable, and gaze is back on the forward path.

## Variations

- `cane`: place the cane on the higher surface first if that matches the user's trained gait pattern.
- `stroller`: use a curb cut when possible; otherwise tip front wheels up before stepping.
- `low-light`: pause longer and use lighting or tactile cues to confirm the curb edge.

## Safety & privacy

Medium fall risk. Slow near edges, keep the landing clear, and choose a ramp or assistance when height or footing is uncertain.
