---
name: navigate-with-a-maps-app
domain: transit
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 15min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

A maps app takes you from here to a named destination on foot or by transit/car — including the two skills the app can't do for you: picking the *right* destination entry, and getting your first hundred meters pointed correctly.

## Preconditions

- A maps app with location permission granted, and either mobile data or offline maps downloaded for the area.
- The destination's name or address — precise enough to disambiguate ("Starbucks" is a set; "Starbucks on 5th & Main" is a place).

## Steps

1. **Search and pick the destination *carefully*.** Same-name traps: chains (which branch?), cities sharing street names, "Springfield" in the wrong state/country. Check the result's address and map position against what you know before routing. → *Expect:* the pin sits where the destination plausibly is — right city, right district.
2. **Choose the mode and read the route candidates.** Walk/transit/drive/bike change everything. Glance at the 2–3 offered routes: time, arrival estimate, and their character (transfers for transit, tolls/highway for driving, stairs for walking). → *Expect:* a chosen route whose shape you could sketch: "blue line 4 stops, then a 5-minute walk."
3. **Solve the first-100-meters problem before moving.** The classic failure is walking confidently the wrong way. Anchor the map: watch your dot move a few steps, or use the compass/AR-walking mode, or match one visible landmark ("the river should be on my left"). → *Expect:* your first movement makes the dot travel *along* the route, not away from it.
4. **Follow the route with the app as advisor, not autopilot.** Glance-and-walk (don't screen-stare into traffic and lampposts); at each decision point the app announces/vibrates. Transit mode: it names the stop to exit — cross-check with the vehicle's own announcements (`transit/take-a-city-bus` step 5). → *Expect:* progress ticking off; estimated arrival stable or improving.
5. **Handle re-routing calmly.** Missed a turn → the app re-plans in seconds; keep moving safely rather than U-turning on impulse. Transit disruption → re-run the route; apps ingest live service data unevenly, so posted station notices outrank the app (`transit/ride-a-subway` decision points). → *Expect:* a new route absorbed without drama.
6. **Land the last meters.** GPS is ±10–30 m in cities: at the pin, look up and find the actual entrance (often around the corner from the pin), building numbers, or the venue's sign. "You have arrived" is a suggestion; the door is the fact. → *Expect:* you at the door, not standing in the road where the pin says.

## Decision points

- Battery below ~30% at the start → screenshot the route overview + key turns now; navigation is a battery hog and a dead phone deletes the map *and* your ticket/ride apps.
- No data / roaming abroad → offline maps downloaded on Wi-Fi beforehand make search-and-walk work; transit real-time needs data though — paper timetable photos are the honest backup.
- Multi-stop errands → the route-with-stops feature orders them better than your instinct; or run stops nearest-first manually.

## Failure modes & recovery

- **F1 Blue dot wrong/frozen:** toggle location off/on, step outdoors or away from tall buildings (urban canyon), give it 30 s; meanwhile navigate one block by street names — the skill the dot was replacing.
- **F2 Routed somewhere absurd (the same-name trap fired):** step 1's check failed — re-search with the added qualifier (city, cross-street) and audit the *distance* readout before moving again ("34 km" to a coffee shop is the tell).
- **F3 Transit route confidently wrong (canceled line, wrong platform):** the station's own signage and staff are the ground truth; apps lag reality — re-plan from what the station says.
- **F4 Walking directions into hostile terrain (missing sidewalk, closed gate):** apps map paths, not conditions — back out to the last good point and take the parallel obvious street; report the error in-app if you're feeling civic.

## Verification

You're at the destination's actual entrance, roughly on the estimated time, with battery surviving; and the route's shape matched what you sketched at step 2 — or diverged for reasons you understood at the time.

## Variations

- Regional apps outperform the global ones locally: `cn` (Amap/Baidu — Google Maps is nonfunctional), `jp` (transit apps with platform-number precision), `kr` (Naver/Kakao) — the recipe transfers, the app choice is local knowledge.
- Driving mode adds its own layer (lane guidance, speed alerts, phone mounting is a legal requirement in many places) — mount before moving, program before driving.

## Safety & privacy

Low risk with two behavioral lines: eyes up at street crossings (screen-staring pedestrians are a real casualty class), and location history — the app remembers everywhere you go unless you tell it not to (pause/auto-delete settings exist; visit them once).
