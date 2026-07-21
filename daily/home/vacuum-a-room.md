---
name: vacuum-a-room
domain: daily
subdomain: home
locale: [generic]
interface: physical
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

A room's floors — carpet and/or hard surface — are vacuumed edge to edge, including under and behind the reachable furniture, with the machine left ready for next time.

## Preconditions

- A working vacuum with an appropriate head (beater bar for carpet, hard-floor mode/head for bare floors) and a non-full bag/bin.
- The floor picked clear of things a vacuum shouldn't meet: cables, coins, socks, LEGO, string, and anything wet (see decision points).

## Steps

1. **Pre-flight the machine.** Bin/bag below the full line (empty it now if close), filter seated, correct head/mode for the floor, cord path planned or battery charged. → *Expect:* strong airflow at the head when switched on briefly; no rattle of yesterday's coin.
2. **Pick the floor before the vacuum sees it.** A 60-second sweep for cables, small objects, socks, and string — string and cables wrap the brush roll and end sessions early. → *Expect:* nothing on the floor but dirt and the furniture.
3. **Vacuum in slow, overlapping lanes from the far corner toward the door.** Half-a-head overlap; *slow* is the operative word — dirt pickup happens at walking-backward pace, not scrubbing pace. Carpet: one pass each in two perpendicular directions on the traffic areas. → *Expect:* visible pile-lift lanes on carpet; audible pickup crackle that fades to clean-hum per lane.
4. **Do the edges and corners with the crevice tool.** Baseboards, corners, along furniture feet — where the drift collects (`daily/home/sweep-and-mop-a-floor` knows this too). → *Expect:* the dust lines at edges are gone, not relocated.
5. **Reach the under-zones.** Under beds/sofas with the flat head or by sliding light furniture aside (and back); behind doors. Skip what genuinely can't move — but on a schedule, not forever. → *Expect:* the under-bed dust ecosystem disturbed and collected.
6. **Empty and reset.** Bin emptied into the trash (outside/bagged if dusty), filter tapped clean per the manual's cadence, brush roll checked for hair wrap (scissors along the roll's groove — cut wrap, don't yank), cord/battery restored. → *Expect:* machine stored ready; suction next time == suction this time.

## Decision points

- Wet spill or broken glass → **not this machine**: wet ruins standard vacuums (wet/dry shops excepted) and glass shreds bags and hoses — towel and `daily/home/sweep-and-mop-a-floor` for wet; careful sweep + damp-paper-towel pat for glass fines, vacuum only after the visible glass is gone.
- Robot vacuum household → this recipe becomes the *weekly deep pass* (edges, unders, direction changes) while the robot owns the daily maintenance lane; the floor-picking step becomes the robot's whole survival requirement.
- Rugs with fringe or delicate weave → beater bar off / suction-only head, run *along* the fringe never into it.

## Failure modes & recovery

- **F1 Suction died mid-room:** 90% is a full bin or clogged filter/hose — empty, tap the filter, check the hose for the sock you skipped in step 2.
- **F2 Brush roll stopped spinning:** hair/string wrap or a tripped belt — power off, flip, cut the wrap along the roll groove; a burnt-rubber smell means the belt, which is a cheap part and a known procedure per model.
- **F3 Vacuum ate a cable end/cord edge:** power off before rescuing anything from a head; inspect the cable for damage before trusting it again.
- **F4 Room smells dusty after vacuuming:** the exhaust is telling you the filter's overdue — clean/replace per the manual; HEPA filters have real lifespans.

## Verification

Lanes covered the full floor including two directions on traffic carpet, edges and reachable unders are done, the bin is emptied and the roll unwrapped, and the machine is stored charged/coiled — verifiably ready for a next session that starts at full suction.

## Variations

- Hard-floor-only homes: suction-head + weekly `daily/home/sweep-and-mop-a-floor` is the full system; the vacuum replaces the broom's dust-launching problem.
- Pet households: double the cadence, halve the F2 interval (hair wrap), and the filter schedule is not optional.

## Safety & privacy

Low risk: cords underfoot (route behind you, not across your path), stairs demand the always-a-free-hand rule, and the wet/glass exclusions above are how both you and the machine stay in service.
