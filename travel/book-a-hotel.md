---
name: book-a-hotel
domain: travel
locale: [generic]
interface: web
difficulty: basic
est_time: 45min
risk: medium
prerequisites: [have-payment-method]
status: draft
last_verified: 2026-07-20
---

## Goal

A hotel room is booked for the right city, dates, and party — at a location that serves the trip — with cancellation terms you chose on purpose and the confirmation saved.

## Preconditions

- Trip dates and city; the *reason* for the trip (which fixes the right neighborhood: near the venue, the station, the beach).
- Party size and needs (beds, accessibility, parking, kitchen).
- A payment card; some bookings charge now, some at the property.

## Steps

1. **Fix the location target before the hotel.** Map your trip's anchor points (venue, office, station); the right hotel is *near your days*, not near the city's name. → *Expect:* a target area drawn on the map view of any booking engine.
2. **Search with real filters.** Dates, party size, then the honest filters: your price band, review score ≥8-ish, and the needs from preconditions (breakfast, parking, twin beds). → *Expect:* a shortlist of 3–5 plausible properties inside the target area.
3. **Read reviews for patterns, not verdicts.** Skim recent reviews for repeated specifics ("street noise", "great staff", "photos flatter the rooms") — one grump is noise, a chorus is signal. Check the photos' dates/room types against what you'd book. → *Expect:* a top choice whose weaknesses you know and accept.
4. **Compare the booking channels for that hotel.** The OTA price vs. the hotel's own site (often matches, sometimes beats with perks; and direct bookings resolve problems far better). Watch the total: taxes, city fees, and "resort fees" land at checkout or at the desk. → *Expect:* the true total price known on your chosen channel.
5. **Choose the cancellation class deliberately.** [BRANCH: refundable rate (costs a bit more, cancels free until a date) | nonrefundable (cheaper, locked)] Any trip with moving parts (flights, health, weather season) argues refundable. → *Expect:* the cancellation deadline and penalty stated and screenshot-worthy.
6. **Book: enter guest name(s) matching ID, arrival time estimate, requests (high floor, quiet side) in the notes.** ⚠️ *Irreversible:* nonrefundable rates commit at this click — recheck dates (check-*in* vs check-*out* off-by-one is the classic) and the room type. → *Expect:* confirmation screen + email with a confirmation number.
7. **Save and integrate.** Confirmation number and address into your trip notes/calendar; note check-in/out times and the front desk's hours if arriving late (warn them for late arrivals — unclaimed rooms can be released). → *Expect:* the booking retrievable; late arrival flagged if relevant.

## Decision points

- Price far below the area's norm → reread the fine print: shared bath? distant "same-name" property? resort fee doubling it? mandatory transfer? Anomalies have causes.
- Longer stays (5+ nights) → apartment-hotels/aparthotels change the math (kitchen, laundry); also ask the hotel directly for a long-stay rate.
- Booking for someone else → put *their* name as guest at step 6; a room under your name alone can strand them at the desk.

## Failure modes & recovery

- **F1 No confirmation email:** check spam; retrieve via the booking site's account; if the card was charged with no retrievable booking, call the channel *now* with the charge reference.
- **F2 Plans changed on a refundable rate:** cancel *before* the deadline in step 5 — set an alarm for that date at booking time; deadlines pass silently.
- **F3 Arrival: "we don't have your booking":** show the confirmation number and the charge; desks resolve or walk you (comparable room elsewhere, on them) — calm persistence plus paper wins this.
- **F4 Room materially not-as-booked (bed count, smoking, broken AC):** raise it at the desk immediately, that night — swaps happen while rooms remain; documentation + the booking channel's support is the escalation path.

## Verification

The confirmation (number + email) shows correct dates, guest names, room type, and total; the cancellation deadline is in your calendar if refundable; and the hotel's location actually serves the trip's mapped anchors.

## Variations

- Peak events (conferences, holidays): book refundable *early* — prices climb and inventory vanishes; refine later.
- `jp` business hotels / capsule stays: tiny-but-precise rooms, strict check-in hours; `eu` city taxes often collected in cash at the desk — keep small currency.

## Safety & privacy

Medium risk: money against fine print. The three protective reads: total-with-fees (4), cancellation terms (5), and the dates double-check (6). Book only over the property's or major channels' real domains — hotel-phishing clones advertise aggressively on search engines.
