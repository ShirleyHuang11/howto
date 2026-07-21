---
name: mash-with-a-fork
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 3min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [fork, bowl, food]
affordances: [grasp, stabilize, press, drag, rotate, inspect]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [bowl], human_proximity: continue}
---

## Goal

Soft food is mashed with a fork to the target texture while the bowl stays stable.

## Preconditions

- Food is soft enough to yield under fork pressure.
- A sturdy bowl or plate is on a non-slip surface.
- A fork is clean and strong enough not to bend under moderate pressure.

## Steps

1. **Stabilize the bowl.** Hold the rim with the support hand or set it on a damp towel. → *Expect:* the bowl does not slide under a test push.
2. **Grip the fork.** Hold the handle with tines angled downward and wrist aligned over the food. → *Expect:* fork tines contact the food squarely.
3. **Press down.** Push the tines into one piece of food with steady vertical pressure. → *Expect:* the food flattens or splits under the fork.
4. **Drag through.** Pull the fork toward the near side while maintaining light downward force. → *Expect:* mashed food spreads into a rough paste or smaller pieces.
5. **Rotate the bowl.** Turn the bowl a quarter turn or move to an unmashed section. → *Expect:* whole pieces are presented under the fork.
6. **Repeat in passes.** Press and drag across the full surface, reducing force as pieces become smaller. → *Expect:* texture becomes more uniform with each pass.
7. **Check texture.** [BRANCH: chunky target | smooth target] Stop when chunks match target; continue shorter strokes for smoother texture. → *Expect:* visible texture matches the parent recipe.
8. **Scrape and gather.** Use the fork side to pull mash from the bowl wall back to the center. → *Expect:* mash is consolidated and ready for seasoning or serving.

## Decision points

- Food resists fork pressure → it is undercooked or too firm for this primitive; cook or cut smaller first.
- Bowl slides repeatedly → add a towel or switch to a heavier bowl.
- Texture becomes gluey → stop mashing and fold gently if mixing continues.

## Failure modes & recovery

- **F1 Bowl slips:** bowl moves with the fork → stop, stabilize with towel or hand, and resume with smaller strokes.
- **F2 Fork bends:** tines deform under pressure → switch to a stronger fork or potato masher.
- **F3 Uneven texture:** whole pieces remain at edges → rotate bowl and mash the perimeter inward.
- **F4 Food splatters:** pressure ejects mash over the rim → reduce force and press deeper inside the bowl.

## Verification

The food is mashed to the target chunk size or smoothness, gathered in the bowl, and the bowl remains stable and intact.

## Variations

- `banana`: use light pressure and stop before watery texture forms.
- `avocado`: mash with lime or seasoning only after the first coarse pass if requested.
- `potato`: use a larger bowl and avoid overworking if fluffy texture matters.

## Safety & privacy

Low risk. Fork tines are not treated as sharp objects here, but keep the support hand on the bowl rim and away from the pressing zone.
