---
name: set-a-kitchen-timer
domain: embodied
subdomain: kitchen
locale: [generic]
interface: physical
difficulty: basic
est_time: 1min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
objects: [timer, button, dial, display]
affordances: [read, press, turn, set, start, cancel]
workspace: kitchen
safety: {hot_surfaces: false, sharp_objects: false, fragile: [], human_proximity: continue}
---

## Goal

A kitchen timer is set to the requested duration, started, and confirmed to be counting down.

## Preconditions

- A physical timer, oven timer, microwave timer, or phone timer is available.
- The requested duration is known in minutes and seconds.
- The display or dial markings can be read.

## Steps

1. **Read the current state.** Look at the display or dial before pressing buttons. → *Expect:* timer is idle, counting, or showing a previous value.
2. **Clear if needed.** Press cancel, stop, or reset if an old value is active. → *Expect:* display returns to zero or idle.
3. **Enter minutes.** Use minute buttons, number keys, or dial turns to reach the requested minutes. → *Expect:* displayed minutes match the target.
4. **Enter seconds if needed.** Add seconds with the seconds control or number keys. → *Expect:* full displayed duration matches the requested time.
5. **Start the timer.** Press start or twist the mechanical timer past the target and back if that model requires winding. → *Expect:* countdown begins or ticking starts.
6. **Confirm counting.** Watch for at least one decrement, moving colon, or audible tick. → *Expect:* time is actively decreasing.
7. **Place within hearing range.** Set the timer where it is visible or audible but away from burners, water, and edges. → *Expect:* timer rests stable and unobstructed.
8. **Cancel when requested.** [BRANCH: timer needed | timer no longer needed] Leave it running if needed; press cancel or stop if the task is abandoned. → *Expect:* active timer state matches the cooking task.

## Decision points

- Display is unreadable → move to better light or use a different timer.
- Timer is already running for another task → do not overwrite it unless the parent task confirms.
- Mechanical timer under five minutes → wind past ten minutes first, then back to improve bell reliability.

## Failure modes & recovery

- **F1 Wrong duration:** display does not match request → cancel and re-enter from zero.
- **F2 Not started:** value is displayed but static → press start and verify a decrement.
- **F3 Silent placement:** timer cannot be heard from work area → move it closer or choose a louder device.
- **F4 Accidental cancel:** countdown disappears → re-enter the remaining known time or restart the full safe interval.

## Verification

The timer shows the requested countdown actively decreasing, or it is canceled only because the parent task no longer needs timing.

## Variations

- `oven-panel`: press Timer rather than Bake Time unless the appliance manual says otherwise.
- `phone`: confirm volume and focus mode allow the alarm.
- `voice-assistant`: repeat the displayed or spoken confirmation before leaving.

## Safety & privacy

Low risk, but missed timers can cause burned food or unsafe heat. Do not overwrite another active cooking timer without confirmation, and keep phone notifications private when using a shared device.
