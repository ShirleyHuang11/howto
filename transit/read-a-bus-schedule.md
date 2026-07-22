---
name: read-a-bus-schedule
domain: transit
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Read a bus schedule well enough to choose the correct route, direction, stop, and departure time.

## Preconditions

- You know your starting location and destination.
- You have access to a posted schedule, transit website, printed timetable, or live-time app.
- You can identify today's date and whether it is a weekday, Saturday, Sunday, or holiday.

## Steps

1. **Find the route number.** Use a map, trip planner, or system map to identify the bus route serving both origin and destination. → *Expect:* you have a route number or letter to look up.
2. **Choose the correct direction.** Read the endpoint or major destination shown for each direction, not just the route number. → *Expect:* the bus direction matches where you need to go.
3. **Find your boarding stop.** Locate the stop name, stop ID, or nearest intersection in the schedule or app. → *Expect:* the stop appears on the route in the correct direction.
4. **Select the right service day column.** [BRANCH: weekday | Saturday | Sunday/holiday] use the column or table for the actual day of travel. → *Expect:* times match today's service pattern.
5. **Read across from a timepoint.** If your exact stop is not listed, use the nearest earlier timepoint and add walking or waiting buffer. → *Expect:* you have a conservative departure estimate.
6. **Check frequency notes.** Look for "every 10 minutes," school-day notes, express-only stops, limited service, or footnotes. → *Expect:* you know whether every bus stops for you.
7. **Confirm with live-time data.** Use the transit app, stop QR code, text number, or real-time board close to departure. → *Expect:* the next bus countdown agrees with the scheduled pattern or explains a delay.
8. **Plan to arrive early.** Reach the stop 3-5 minutes before scheduled time, more for infrequent routes. → *Expect:* an early bus does not leave without you.
9. **Match the headsign when boarding.** Check route number and destination on the bus before stepping on. → *Expect:* the vehicle matches the schedule you selected.

## Decision points

- Exact stop is not in the table → use the closest earlier listed timepoint because buses can arrive between listed stops.
- App and paper disagree → trust real-time data for today, but verify detours or holiday service alerts.
- Route has branches → match the branch letter, endpoint, or street deviation before boarding.
- Service is infrequent → build a backup route or rideshare threshold before leaving.

## Failure modes & recovery

- **F1 Wrong direction:** the endpoint is opposite your destination → cross to the opposite stop and recheck the headsign.
- **F2 Weekend table mistake:** no bus arrives at the weekday time → switch to the correct day table and re-plan.
- **F3 Express skip:** the bus passes your stop → use a local service or walk to an express stop listed for that route.
- **F4 Live app stale:** countdown freezes or jumps → check the agency alert page or posted stop ID by text.
- **F5 Missed last bus:** no later trips are listed → use night service, rail, taxi, or a preplanned pickup.

## Verification

You can state the route, direction, boarding stop, service-day table, and next usable departure time before going to the stop.

## Variations

- Printed timetables: timepoints are often not every stop, so read the map and footnotes together.
- Transit apps: live times usually show countdowns, while scheduled times show clock times.
- Rural buses: some stops may require advance booking or flagging.
- Holiday service: agencies may run Sunday schedules on holidays even when the holiday falls on a weekday.

## Safety & privacy

Low risk. Wait in a visible place, keep the phone charged, avoid sharing your live location publicly, and confirm the bus headsign instead of following a crowd.
