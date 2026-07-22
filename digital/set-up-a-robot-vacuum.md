---
name: set-up-a-robot-vacuum
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 45min-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

A robot vacuum is charged, connected to its app, mapped, restricted from problem areas, and scheduled with basic maintenance understood.

## Preconditions

- A robot vacuum, dock, phone, maker app account if required, and the home Wi-Fi password.
- Floors are cleared of cords, socks, pet waste, loose rugs, and fragile low objects.

## Steps

1. **Place the dock.** Put it against a wall on hard floor with open space around it, near power and Wi-Fi. → *Expect:* the dock sits flat and the charging light works.
2. **Charge the vacuum.** Seat the robot on the dock until the app or indicator shows enough charge for setup. → *Expect:* the robot reports charging.
3. **Install and pair the app.** Use the official app, add the model, and follow Wi-Fi pairing prompts. → *Expect:* the robot appears online in the app.
4. **Prepare the home for mapping.** Open interior doors, lift cords, secure rug tassels, and block areas that could trap the robot. → *Expect:* the floor is passable for a first mapping run.
5. **Run mapping.** [BRANCH: mapping-only run | clean-and-map run] Use mapping-only if offered; otherwise start a full clean and let it finish. → *Expect:* the app shows a map or room outline.
6. **Name rooms and set zones.** Label rooms, split or merge boundaries, and add no-go zones for cords, pet bowls, stairs, thick rugs, or delicate areas. → *Expect:* the map shows named rooms and restricted areas.
7. **Test a targeted clean.** Send the vacuum to one room or zone and watch the start of the run. → *Expect:* it leaves the dock, cleans the chosen area, and returns or asks for help.
8. **Set a schedule.** Pick times when floors are clear and people are not sleeping, and avoid times pets may be loose with messes. → *Expect:* the schedule shows correct days, time, suction or mop mode.
9. **Empty and maintain.** Empty the bin, clean brushes, remove hair, wash or replace filters as allowed, and fill mop tanks only with approved liquid. → *Expect:* the robot reports ready with no maintenance alert.

## Decision points

- Home has stairs → no-go zones help, but physical barriers are safer for early runs.
- Vacuum includes a camera → review privacy settings and map-sharing options before enabling remote viewing.
- Pets are present → run only after checking the floor, because robot vacuums can spread accidents.

## Failure modes & recovery

- **F1 Cannot dock:** detect the robot wanders near the dock or dies nearby, recover by moving the dock to a clearer flat location.
- **F2 Bad map:** detect warped rooms or missing areas, recover by clearing floors and remapping in good lighting if the model uses cameras.
- **F3 Gets stuck repeatedly:** detect alerts in the same spot, recover by adding a no-go zone or removing the obstacle.
- **F4 Weak cleaning:** detect debris left behind, recover by emptying the bin, cleaning brushes, and increasing suction for that room.

## Verification

The robot completes a targeted cleaning run, returns to the dock, and the app shows a saved map with no-go zones and a schedule.

## Variations

- Self-empty docks: install the dust bag and check the dock path before enabling auto-empty.
- Mop models: attach pads and water tanks only for floors approved for damp mopping.
- Multi-floor homes: create separate maps if the app supports them, and move the dock only as instructed.

## Safety & privacy

Robot vacuums can damage cords, drag liquids, mark delicate floors, and collect maps of your home. Clear hazards, review camera and map privacy settings, and maintain filters for dust control.
