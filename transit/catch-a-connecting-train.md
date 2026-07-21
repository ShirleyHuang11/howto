---
name: catch-a-connecting-train
domain: transit
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 15min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Move from one train to a connecting train with enough time to board the correct service or recover from a missed connection.

## Preconditions

- You have the origin train, connection station, destination, and ticket or fare media.
- You can read station boards, app updates, or printed timetables.
- You know whether the ticket is flexible or tied to a specific train.

## Steps

1. **Check the connection before boarding.** Look up arrival time, departure time, platform if known, and minimum transfer time. → *Expect:* the planned connection has enough minutes on paper.
2. **Watch delay updates en route.** Check the app, conductor announcements, or onboard screen before the connection station. → *Expect:* you know whether the first train is on time.
3. **Gather before arrival.** Pack bags, put the ticket where you can reach it, and move toward the exit if allowed. → *Expect:* you are ready to step off when doors open.
4. **Read the station board first.** At the station, check destination, train number, departure time, and platform. → *Expect:* the connecting platform is confirmed from live information.
5. **Follow platform signs.** Use stairs, elevators, or passageways marked for the platform, keeping to the walking side where local custom applies. → *Expect:* you are moving toward the correct track without blocking others.
6. **Confirm at the platform.** Check the train number, destination, intermediate stops, and car restrictions before boarding. → *Expect:* the train at the platform matches your connection.
7. **Board before door close.** Enter an open door with your party and bags, then move away from the doorway. → *Expect:* you and your bags are on the connecting train before departure.
8. **Use the missed-connection plan if needed.** [BRANCH: protected connection | unprotected connection] ask staff for rebooking if protected, or search the next valid service if unprotected. → *Expect:* you have a next train, rebooked ticket, or support case.
9. **Update anyone waiting.** Send the new arrival time if the connection changed. → *Expect:* pickup, hotel, or meeting plans reflect the latest arrival.

## Decision points

- Transfer time is below the agency minimum → choose an earlier first train or later connection.
- Arrival platform changed → trust live boards over old screenshots.
- You need an elevator → add transfer time and check station accessibility alerts.
- The ticket is train-specific → ask staff before boarding a later train.
- The last train is the connection → build a taxi, hotel, or alternate-route backup before travel.

## Failure modes & recovery

- **F1 Platform change:** detect board or announcement changes, recover by following live signs and rechecking train number.
- **F2 Tight transfer:** detect arrival close to departure, recover by preparing early and moving directly to the platform.
- **F3 Wrong train:** detect destination or train number mismatch, recover by stepping off before departure.
- **F4 Missed protected connection:** detect delay caused by prior train, recover by asking staff or app support for rebooking.
- **F5 Missed unprotected connection:** detect separate tickets or fare systems, recover by buying the next valid fare if needed.

## Verification

You are on the connecting train that matches the live board's destination, train number, and departure time, or you have a confirmed replacement plan.

## Variations

- Commuter rail: platform tracks may post only a few minutes before departure.
- Intercity rail: train number matters more than color or line name.
- International trips: border, security, or ticket checks can make minimum transfer times longer.
- Traveling with children or luggage: add a buffer because elevators and crowds slow movement.

## Safety & privacy

Do not run on stairs, cross tracks, or force closing doors. Keep tickets and bags secure in crowded transfer tunnels, and avoid sharing full itinerary screenshots publicly.
