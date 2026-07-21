---
name: read-a-train-timetable
domain: transit
locale: [generic]
interface: mixed
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Find the correct train, direction, departure time, arrival time, transfers, service days, and timetable symbols before going to the station.

## Preconditions

- You know your origin station, destination station, and target date.
- You can access the timetable online, in an app, or on a posted station board.
- You know whether you need to arrive by a fixed time or leave after a fixed time.

## Steps

1. **Identify the route line.** Match your origin and destination to a named line, route number, or corridor on the map. → *Expect:* one line or set of lines can serve the trip.
2. **Choose the travel direction.** Use the line's endpoint names to pick the direction that passes your destination. → *Expect:* the destination appears after your origin in that direction.
3. **Select the correct service day.** [BRANCH: weekday | Saturday | Sunday/holiday] open the schedule for the actual date, not the nearest normal day. → *Expect:* the heading or date range matches your travel day.
4. **Decide departure or arrival search.** If you must be somewhere on time, search by arrival; otherwise search by departure. → *Expect:* the timetable rows are being read from the right time target.
5. **Read across the station row or column.** Follow the same train row from origin time to destination time, keeping your finger or cursor on one row. → *Expect:* one departure time and one arrival time belong to the same train.
6. **Check transfers.** If the destination is blank or requires a change, note the transfer station, platform if shown, and connecting train time. → *Expect:* every leg has a train number or departure time.
7. **Decode symbols and footnotes.** Look up letters, icons, and marks for express service, request stops, no bicycles, seat reservations, or limited service. → *Expect:* no symbol beside your train is unexplained.
8. **Add station time.** Include walking to the platform, ticket purchase, and any security or gate time. → *Expect:* you know when to arrive at the origin station.
9. **Save the itinerary.** Screenshot or write the line, direction, times, transfer point, and platform notes. → *Expect:* the plan is usable without reloading the timetable.

## Decision points

- Destination has multiple stations → choose the station closest to the final address, then recheck which line serves it.
- Timetable has both departure and arrival columns → use departure at your origin and arrival at your destination, not train-start or train-end times.
- Express train skips stations → use it only if both origin and destination are listed for that train.
- Service day is a holiday or special event → confirm the agency's special schedule before relying on a weekday table.

## Failure modes & recovery

- **F1 Wrong direction:** detect the train's endpoint is opposite your destination, recover by switching to the opposite platform or next return train.
- **F2 Mixed rows:** detect impossible travel time or a transfer before departure, recover by rereading one row at a time.
- **F3 Footnote missed:** detect a symbol or letter near the time, recover by reading the timetable legend before boarding.
- **F4 Service not running:** detect blank times or "no service" for the date, recover by choosing another line, bus bridge, or later service day.
- **F5 Transfer too tight:** detect less than the agency's minimum transfer time, recover by choosing an earlier first train.

## Verification

You can state the line, direction, origin departure time, destination arrival time, transfer details if any, service day, and meaning of every symbol on the chosen trip.

## Variations

- Paper poster: read the station index first, then trace the row with a straight edge.
- Mobile app: switch off "leave now" if you are planning for a future date.
- Long-distance rail: train numbers and reservation rules matter as much as line names.
- Real-time boards: use them to confirm platform and delay status after reading the scheduled timetable.

## Safety & privacy

Low risk. Avoid standing near platform edges while reading a phone, and avoid posting screenshots that reveal regular commute times or home and work stations.
