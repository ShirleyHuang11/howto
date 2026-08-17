---
name: empty-a-robot-vacuum-bin
domain: embodied
subdomain: household
locale: [generic]
interface: physical
difficulty: basic
est_time: 5min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
objects: [robot-vacuum, dust-bin, filter, trash-can, charging-dock]
affordances: [grasp, button-press, pull, empty, tap, insert]
workspace: household
safety: {hot_surfaces: false, sharp_objects: false, fragile: [robot-vacuum], human_proximity: continue}
---

## Goal

Remove collected debris from a robot vacuum dust bin, reseat the bin and filter, and leave the robot ready to run.

## Preconditions

- Robot vacuum is stopped and accessible.
- Trash can is open nearby.
- Hands or grippers are dry.
- Manufacturer-specific latch locations are visible or known.

## Steps

1. **Stop and steady the robot.** Confirm it is not running, then hold the body or dock area steady. → *Expect:* wheels and brushes are not moving.
2. **Release the dust bin.** Press the bin latch and pull the bin straight out along its rails. → *Expect:* the bin separates without forcing or twisting.
3. **Hold over the trash can.** Keep the bin opening fully inside the trash perimeter. → *Expect:* any falling dust will land in the trash.
4. **Open and empty the bin.** Release the bin door and tap the side lightly until debris falls out. → *Expect:* the main chamber is visibly empty.
5. **Check the filter.** Lift or tap the filter only as the manufacturer allows, keeping dust over the trash. → *Expect:* filter is seated, dry, and not packed with loose dust.
6. **Reinsert the bin.** Close the bin door and slide the bin back until it clicks or sits flush. → *Expect:* the robot body has no protruding bin edge or open latch.

## Decision points

- Bin contains wet debris → stop, clean and dry the bin according to the manual before reinstalling.
- Filter is torn or very dirty → replace it before running the robot.
- Robot uses an auto-empty dock → verify whether the internal bin still needs manual cleaning.

## Failure modes & recovery

- **F1 Dust spills:** detect debris outside the trash can → set the bin down, clean the spill, and hold the bin deeper over the can.
- **F2 Bin will not release:** detect latch pressed but no movement → check for a second latch or wrong pull direction.
- **F3 Door left open:** detect loose flap after emptying → close it until the latch catches before reinserting.
- **F4 Bin not seated:** detect robot error light or raised bin edge → remove and reinsert along the guide rails.

## Verification

The robot vacuum dust bin is empty, closed, fully seated in the robot, and the robot shows no bin or filter error.

## Variations

- `bagged-auto-empty-dock`: replace the dock bag when indicated instead of dumping the robot bin.
- `washable-bin`: rinse only removable washable parts and dry completely before reinstalling.

## Safety & privacy

Low risk. Dust may contain allergens or private debris; empty low into the trash, avoid shaking near faces, and do not inspect personal waste beyond what safety requires.
