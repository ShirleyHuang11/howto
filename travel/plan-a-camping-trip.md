---
name: plan-a-camping-trip
domain: travel
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Plan a camping trip with an appropriate campsite, weather-ready gear, food, water, route details, and emergency backup.

## Preconditions

- You know the destination region, group size, dates, and comfort level.
- You can check campsite rules, permits, weather, fire restrictions, and road conditions.
- You have or can borrow shelter, sleep, cooking, water, lighting, and first-aid gear.

## Steps

1. **Choose the camping style.** [BRANCH: campground | dispersed | backcountry] pick the option that matches skills, permits, bathroom needs, and vehicle access. → *Expect:* the trip type fits the group, including kids or first-timers.
2. **Reserve or confirm the site.** Book the campsite or confirm legal dispersed camping rules, arrival time, fees, and quiet hours. → *Expect:* you know where sleeping is allowed.
3. **Check seasonal conditions.** Review forecast, overnight lows, fire bans, insects, wildlife notices, and road closures. → *Expect:* the gear list reflects actual conditions.
4. **Build the gear list by system.** Pack shelter, sleep insulation, cooking, water, clothing, lighting, hygiene, navigation, trash, and first aid. → *Expect:* no basic camp system is missing.
5. **Plan food and water.** Choose meals that fit stove or fire rules, pack enough drinking water or treatment, and store food against animals. → *Expect:* every meal and water source is accounted for.
6. **Share the itinerary.** Send location, route, vehicle, group names, and return time to someone not on the trip. → *Expect:* a trusted person knows when to raise concern.
7. **Prepare arrival and backup plans.** Note check-in rules, sunset time, nearby town, emergency exit, and bad-weather alternative. → *Expect:* late arrival or closure will not leave the group improvising.

## Decision points

- Fire ban is active → bring a stove allowed under the current rule or plan no-cook meals.
- Overnight low is near gear limits → upgrade sleeping bags, pads, and layers or change dates.
- New campers or children are coming → choose a developed campground close to home.

## Failure modes & recovery

- **F1 Site unavailable:** detect no reservation or full campground → switch to a legal backup site before departure.
- **F2 Weather turns unsafe:** detect lightning, flood, extreme heat, or high wind forecast → delay, relocate, or use lodging.
- **F3 Water plan fails:** detect dry source or too little carried water → reroute to a known water point or end the trip.
- **F4 Food attracts animals:** detect unsecured food or trash → use lockers, canisters, vehicle storage where allowed, or hang according to local rules.

## Verification

The trip has a legal campsite, weather-appropriate gear, food and water plan, route and emergency contacts, and a documented backup plan before departure.

## Variations

- `family-camping`: add extra warm layers, comfort items, simple meals, and an early bedtime plan.
- `bear-country`: follow local food-storage rules exactly and carry required bear safety gear.
- `desert`: plan shade, extra water, and temperature swings.

## Safety & privacy

Medium risk from weather, fire, wildlife, navigation errors, water shortage, and remote travel. Share itinerary privately with a trusted contact and avoid posting empty-home travel dates publicly.
