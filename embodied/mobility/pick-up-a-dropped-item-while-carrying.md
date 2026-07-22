---
name: pick-up-a-dropped-item-while-carrying
domain: embodied
subdomain: mobility
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 1min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
objects: [carried-load, dropped-item, floor, hand, bag]
affordances: [stabilize, set-down, bend, grasp, lift, restack]
workspace: mobility
safety: {hot_surfaces: false, sharp_objects: false, fragile: [carried-load, dropped-item], human_proximity: slow}
---

## Goal

The dropped item is retrieved while the current carried load remains secure and the actor maintains balance.

## Preconditions

- Dropped item is visible and reachable without stepping into danger.
- Current load can be stabilized, transferred, or set down.
- Floor surface is dry enough for a controlled bend.

## Steps

1. **Stop walking.** Plant both feet before reacting to the dropped item. → *Expect:* body and load stop moving forward.
2. **Secure the current load.** Hug it to the torso, tighten bag handles, or shift it to one arm. → *Expect:* load does not slide when one hand loosens.
3. **Choose retrieval method.** [BRANCH: load secure | load unstable] continue or set the load on a stable surface first. → *Expect:* at least one hand can reach safely.
4. **Approach the item.** Step close enough that the item is between the feet or just ahead. → *Expect:* no overreach is needed.
5. **Bend at knees or hips.** Keep back controlled and head clear of obstacles. → *Expect:* hand lowers toward the item while balance stays centered.
6. **Grasp the item.** Pinch or wrap fingers around the item before lifting. → *Expect:* item is captured and does not skid away.
7. **Rise with control.** Push through legs and keep the load close to the body. → *Expect:* item and carried load both remain held.
8. **Restack and resume.** Place the retrieved item into the bag, on top of the stack, or in a secure hand. → *Expect:* walking can resume without loose pieces.

## Decision points

- Load blocks view of the floor → set it down before bending.
- Item rolled under furniture or traffic → reposition or ask for help instead of lunging.
- Item is sharp, hot, wet, or unknown → use a tool or treat it as a separate safety task.

## Failure modes & recovery

- **F1 Load slips:** carried objects shift during bend → stop, lower the load to a surface, and restack.
- **F2 Overreach:** hand cannot reach item with feet planted → stand up, step closer, and bend again.
- **F3 Balance loss:** weight shifts onto toes or one side → release the reach and stabilize before retrying.
- **F4 Item trapped:** item cannot be grasped directly → slide it into open space with a foot or tool, then pick it up.

## Verification

The dropped item is back in hand, bag, or stack, the original load is secure, and the actor is upright and balanced.

## Variations

- Carrying hot liquid: set it down first before retrieving anything.
- Crowded hallway: step aside with the load before bending so others can pass.

## Safety & privacy

Medium risk from falls, dropped fragile objects, and reduced awareness while bending. Slow down near people and set the load down when balance is uncertain.
