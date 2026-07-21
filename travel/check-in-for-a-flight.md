---
name: check-in-for-a-flight
domain: travel
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: [travel/book-a-flight]
status: draft
last_verified: 2026-07-20
---

## Goal

You are checked in for your flight with a boarding pass on your phone or in hand, bags handled, and you know your terminal, gate window, and boarding time.

## Preconditions

- A booked flight (PNR + name retrieves it) departing within the check-in window (typically opens 24–48 h before, closes 45–90 min before departure — airline-specific).
- Travel documents for the route: ID for domestic, passport (+ visa/ESTA-style authorization where required) for international.
- The airline's app installed, or access to their website.

## Steps

1. **Open check-in when the window opens.** Airline app/site → check-in → PNR + name. Doing it at window-open gets seat choice and kills the airport-queue dependency. → *Expect:* your itinerary loads and offers check-in.
2. **Complete the document/health/customs questions honestly.** International: passport details (often scanned by the app), destination address, any required declarations. → *Expect:* documents accepted; no "see agent at airport" flag (flag → F1).
3. **Confirm or change your seat.** Free options first; paid upgrades knowingly. → *Expect:* a seat assignment on the pass.
4. **Declare bags.** [BRANCH: carry-on only → done | checked bags → confirm/pay for them now (cheaper than at the counter)] → *Expect:* bag allowance attached; the pass or email states it.
5. **Obtain the boarding pass.** App wallet pass preferred (it updates gates live); screenshot it as backup; or print at home. → *Expect:* a scannable pass showing name, flight, seat, boarding *time*, and boarding group — gate may still say "TBD", that's normal.
6. **At the airport: drop bags if any.** Bag-drop desk or self-service kiosk within the *bag-drop deadline* (earlier than the check-in deadline — usually 45–60 min international). ⚠️ *Irreversible:* missing the bag deadline can mean flying without your bag or not flying — build the buffer. → *Expect:* bag tagged to your final destination (read the tag's airport code) and a receipt sticker in your possession.
7. **Clear security and verify the gate.** Pass + ID through security; then check the departure boards against your app — gates move. → *Expect:* through security with time to reach the gate by *boarding* time (not departure time), which is typically 30–45 min before departure.

## Decision points

- App check-in fails or route requires document verification → airport counter check-in: arrive at the airline's recommended time (2 h domestic / 3 h international is the safe default) and queue at your fare's desk.
- Connecting flights → confirm at bag-drop whether bags are tagged through and whether you must re-clear security/customs at the connection — the answer changes your layover math.
- Basic fares with no seat selection → check in at window-open anyway; auto-assigned seats get worse, not better, with time.

## Failure modes & recovery

- **F1 "Unable to check in online — see agent":** usually document verification (visas, passport scans) or a schedule change; go to the counter early, documents in hand — it's routine.
- **F2 Boarding pass won't load at the airport (dead phone/app):** the screenshot backup, or any airline kiosk reprints from PNR + name; keep the phone charged past security regardless — it's also your return pass.
- **F3 Name on pass doesn't match ID (noticed at security):** minor typos usually pass with agent judgment; real mismatches go back to the airline desk — this is why `travel/book-a-flight` step 4 exists.
- **F4 Running late against the deadlines:** call the airline while en route (some hold bag-drop briefly), go carry-on if the bag deadline is lost, and know the rebooking desk is the fallback — showing up late but *before departure* often converts to a same-day change fee rather than a lost ticket.

## Verification

A live boarding pass (plus backup) shows your correct name, flight, and seat; bags (if any) are tagged to the right final airport code with receipts in hand; and you're through security tracking the gate with the boarding time — not the departure time — as your deadline.

## Variations

- Budget carriers: online check-in may be *mandatory* with airport check-in fees — do step 1 without fail, and print if the airline demands paper.
- `us` domestic with PreCheck/`eu` fast-track: the security calculus shortens but the bag-drop deadline does not.

## Safety & privacy

Medium risk is missed-flight risk, governed entirely by deadlines: check-in close, bag-drop close, boarding time. The boarding pass barcode leaks your PNR — don't post it; with PNR + name, anyone can view or change your booking.
