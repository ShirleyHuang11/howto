---
name: plan-a-commute
domain: transit
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1h
risk: low
prerequisites: [transit/navigate-with-a-maps-app]
status: draft
last_verified: 2026-07-20
---

## Goal

You have a reliable everyday route between two fixed points (home and work or school), chosen by comparing modes, padded with a sensible time buffer, and backed by a known alternative for when the primary route fails.

## Preconditions

- A fixed origin and destination and the time you must arrive.
- A maps app or local transit planner for the area.
- Willingness to do one real trial run before relying on the plan.

## Steps

1. **Fix the hard arrival time.** Work back from when you must be there, not from when you like to leave. → *Expect:* a target arrival time written down.
2. **Compare modes on the real timetable.** Check walk, bike, bus, train, and drive for your actual departure window, not an off-peak average. → *Expect:* a door-to-door time and cost for each viable mode at rush hour.
3. **Choose the primary mode on total reliability, not raw speed.** A slightly slower option with predictable timing beats a fast one that swings wildly with traffic. → *Expect:* one primary route with a typical and a bad-day time.
4. **Apply the buffer rule.** Add padding equal to the route's variability: roughly 15 percent for a steady rail run, more for traffic-dependent driving. Leave by (arrival time minus typical time minus buffer). → *Expect:* a fixed departure time that absorbs a normal bad day.
5. **Pick a concrete backup route.** Identify one alternative that fails independently of the first: a different line, a bus parallel to the train, or a bike-plus-transit combo. → *Expect:* a named plan B you could start within minutes, not a vague idea.
6. **Do a trial run at the real time.** Ride the full route on a normal weekday at your intended departure time before you depend on it. → *Expect:* the trial arrives with buffer to spare; note any surprise (a slow transfer, a crowded platform).
7. **Adjust from the trial, then lock it in.** Fix the departure time and buffer from what you actually observed, not the app estimate. → *Expect:* a settled leave-time and route you can repeat daily.
8. **Set up live disruption alerts.** Follow the line or road on the transit app so you learn of delays before you leave home. → *Expect:* you get notified of a disruption in time to switch to plan B.

## Decision points

- Two modes are close on time → weight in comfort, cost, and whether you can use the time (reading on a train vs driving); reliability still breaks ties.
- Primary route has a single point of failure (one bridge, one line) → treat the backup as mandatory, not optional, and know its departure points cold.
- Arrival time is strict (shift start, school gate) → increase the buffer; the cost of being early is minutes, the cost of being late is real.

## Failure modes & recovery

- **F1 Chronically arriving late:** buffer too small → increase it from observed bad-day times, or move the whole plan earlier; do not just hope traffic improves.
- **F2 Primary route disrupted mid-journey:** delay alert or stopped service → switch to the pre-chosen backup immediately rather than waiting it out; the decision was made in advance for exactly this.
- **F3 Backup is actually the same failure:** both routes share a choke point → replan so plan B fails independently (different corridor or mode).
- **F4 Trial run was misleading:** you tested off-peak or on a light day → redo it on a normal busy weekday; a plan validated on an easy day is not validated.

## Verification

You have a written primary route with a fixed departure time and buffer, a genuinely independent backup route, and a trial run that arrived on time with margin to spare.

## Variations

- `hybrid-schedule`: commuting only some days lets you pick off-peak departures; recheck timetables, since off-peak service is thinner and gaps are longer.
- `multimodal`: park-and-ride or bike-and-train needs the buffer applied at each handoff, since delays compound across legs.

## Safety & privacy

Low risk. The main hazards are the stress and knock-on effects of running late, addressed by an honest buffer and a real backup. If you share a live location or commute pattern through an app, review who can see it, since a fixed daily route is predictable information.
