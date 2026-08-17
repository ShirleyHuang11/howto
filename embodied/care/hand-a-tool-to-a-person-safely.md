---
name: hand-a-tool-to-a-person-safely
domain: embodied
subdomain: care
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [tool, handle, person, hand]
affordances: [grasp, orient, present, wait, release]
workspace: caregiving or shared workspace
safety: {hot_surfaces: false, sharp_objects: true, fragile: [], human_proximity: pause}
---

## Goal

A tool is transferred to a person handle-first, with release only after the person has control.

## Preconditions

- The person has requested or agreed to receive the tool.
- The tool is safe to touch at the handle.
- The handoff path is clear and visible to both parties.

## Steps

1. **Identify the safe grip area.** Locate the handle or non-working end of the tool. → *Expect:* sharp, hot, or active parts are oriented away from the person.
2. **Grip the working end safely if needed.** Hold the tool so the handle points toward the person and hazards point down or away. → *Expect:* the handle is unobstructed for the receiver.
3. **Announce the handoff.** Pause near the person and present the tool at chest or hand height. → *Expect:* the person looks at the tool or extends a hand.
4. **Move slowly into reach.** Advance the handle until it is within the person's open grasp without touching their body. → *Expect:* the person can close fingers around the handle.
5. **Wait for secure grasp.** Maintain your grip until the person has wrapped fingers around the handle. → *Expect:* the tool is supported by both parties.
6. **Confirm transfer.** Reduce grip force slightly while observing whether the tool remains steady in the person's hand. → *Expect:* the person supports the tool without dropping or twisting.
7. **Release and withdraw.** Let go fully and move your hand away from the tool path. → *Expect:* the person holds the tool alone and hazardous ends remain clear.

## Decision points

- Person is not looking or ready → wait and do not extend into their space.
- Tool has a sharp edge or point → keep the hazardous end under your control until the handle is grasped.
- Person has limited grip strength → place the tool on a nearby surface instead of direct handoff.

## Failure modes & recovery

- **F1 Person does not grasp:** detect by no hand contact or unclear attention → hold position, repeat the offer, or set the tool down safely.
- **F2 Tool slips:** detect by downward motion during transfer → regrip immediately if safe or lower to a surface.
- **F3 Hazard points toward person:** detect by blade, tip, or active end facing the receiver → rotate the tool away before continuing.

## Verification

The person has sole stable control of the tool by its handle, and no sharp, hot, or active part is directed toward either person.

## Variations

- Scissors or knife: hold the closed blade side and present the handle first.
- Powered tool: turn it off and keep fingers away from triggers during transfer.

## Safety & privacy

Human proximity requires pausing until the receiver is ready. Respect personal space and do not hand over a tool unless the person consents.
