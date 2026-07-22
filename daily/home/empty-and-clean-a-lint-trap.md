---
name: empty-and-clean-a-lint-trap
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

The dryer lint trap is cleared for the next load, and the screen is washed when softener film blocks airflow.

## Preconditions

- Dryer is stopped, cool enough to touch, and not running a heat cycle.
- You have a bin, warm water, dish soap, a soft brush, and a towel if the screen needs washing.
- You know whether your lint screen pulls from the door opening or the dryer top.

## Steps

1. **Remove the screen before every load.** Pull the lint trap straight out without bending the frame. → *Expect:* the mesh screen is fully exposed.
2. **Peel the lint mat off.** Start at one corner and roll the lint into itself, then put it in the bin. → *Expect:* the mesh looks open instead of fuzzy.
3. **Check for softener film.** Run a little water over the screen. [BRANCH: water beads | water passes through] beading means the screen needs washing, passing water means it can go back dry. → *Expect:* you know whether residue is blocking airflow.
4. **Wash the screen if needed.** Use warm water, dish soap, and a soft brush on both sides. → *Expect:* water sheets through the mesh evenly.
5. **Dry the screen completely.** Pat it with a towel and let it air-dry until no droplets remain. → *Expect:* the screen is dry, straight, and free of soap.
6. **Clear the slot lip.** Pick or vacuum loose lint from the trap slot entrance without dropping tools inside. → *Expect:* the screen path is unobstructed.
7. **Refit the screen.** Slide it back along its rails until it sits flush. → *Expect:* the trap is seated and the dryer door or top closes normally.

## Decision points

- Screen is torn, warped, or missing → replace it before running the dryer because lint can enter the vent path.
- Water beads after washing → repeat with dish soap, then stop using dryer sheets for a few loads.
- Lint falls deep into the slot → use a crevice vacuum tool, not fingers or a metal hanger.
- A lint warning light remains on → clean the vent path with `daily/home/clean-a-dryer-vent`.

## Failure modes & recovery

- **F1 Screen will not seat:** detect a proud or tilted frame, recover by checking for lint clumps in the slot and reinserting along the rails.
- **F2 Mesh tears during brushing:** detect a hole or loose edge, recover by ordering the exact replacement screen and pausing dryer use if lint bypasses it.
- **F3 Dryer overheats:** detect hot cabinet surfaces or shutdowns, recover by cleaning the vent and calling service if airflow remains weak.
- **F4 Lint is damp or smeared:** detect sticky lint after a load, recover by checking that clothes were spun well and the vent is not blocked.

## Verification

The lint screen is clean, dry, intact, fully seated, and water can pass through the mesh after any wash.

## Variations

- `shared-laundry`: empty the trap before and after your own load because the last user may not have done it.
- `pet-household`: expect thicker lint and clean the slot lip more often.
- `dryer-sheets`: wash the screen monthly to remove softener film.

## Safety & privacy

Low risk, but a clogged lint trap reduces airflow and can contribute to overheating. Keep fingers, metal tools, and loose lint out of the deep slot.
