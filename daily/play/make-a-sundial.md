---
name: make-a-sundial
domain: daily
subdomain: play
locale: [generic]
interface: physical
difficulty: intermediate
est_time: 1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Make a simple sundial that uses a shadow to show local solar time and teaches why clock time can differ.

## Preconditions

- A sunny day and an outdoor spot that stays sunny for several hours.
- A flat board, stiff cardboard, or pavement area.
- A straight stick, pencil, or dowel to use as the gnomon.
- Your approximate latitude, from a map or weather app.

## Steps

1. **Choose the base.** Put the board or markable surface on level ground where shadows will not be blocked. → *Expect:* the surface stays still and the sun reaches it.
2. **Set the gnomon angle.** Tilt the gnomon so it points toward the celestial pole at an angle equal to your latitude above the surface. → *Expect:* a 40 degree latitude uses a gnomon about 40 degrees above the base.
3. **Aim it north or south.** In the northern hemisphere, point the raised end toward true north; in the southern hemisphere, point it toward true south. → *Expect:* the gnomon points along the local meridian, not just where a phone compass first guesses.
4. **Secure the gnomon.** Tape, glue, or wedge it so the angle does not change. → *Expect:* the shadow moves, but the stick does not wobble.
5. **Mark the first hour.** At a known clock time, mark the shadow tip and label the clock time. → *Expect:* one clear tick mark appears at the shadow tip.
6. **Keep marking through the day.** Return each hour and mark the new shadow tip. → *Expect:* a curved or fan-shaped set of hour marks builds across the base.
7. **Note true time differences.** Write down whether daylight saving time is active and how far you are from the center of your time zone. → *Expect:* you understand why noon by the clock may not match the shortest shadow.
8. **Find solar noon.** The shortest shadow of the day is local solar noon. → *Expect:* the noon mark may be offset from 12:00 on the clock.
9. **Use the dial later.** Place the dial in the same orientation and read the shadow against your marks. → *Expect:* the reading is close on sunny days when the base and gnomon are aligned.

## Decision points

- You want a quick toy dial → hold a vertical stick and mark shadows hourly, accepting seasonal inaccuracy.
- You want a reusable dial → build the latitude-angled gnomon and mark carefully over a full day.
- Phone compass disagrees with maps → use true north from a map line, not magnetic north, for better results.
- Clouds interrupt marking → keep the marks you have and finish another sunny day with the dial in the same orientation.

## Failure modes & recovery

- **F1 Wandering base:** detect when old marks no longer line up, recover by taping the base down or adding alignment marks on the ground.
- **F2 Wrong gnomon angle:** detect when readings drift badly across the day, recover by resetting the angle to local latitude.
- **F3 Magnetic north error:** detect a consistent time offset, recover by realigning to true north or true south.
- **F4 Clock-time surprise:** detect noon mark far from 12:00, recover by accounting for daylight saving and time-zone position.

## Verification

On a sunny later hour, the gnomon shadow falls near the matching marked hour when the dial is returned to its original orientation.

## Variations

- Classroom version: mark every 30 minutes and compare shadow length as well as direction.
- Pavement version: chalk a vertical-stick dial for one-day use.
- Portable version: add a north arrow and leveling mark so the dial can be set up again.

## Safety & privacy

Low risk. Do not stare at the sun, keep tools away from walkways, and avoid leaving tape or chalk where it is not allowed.
