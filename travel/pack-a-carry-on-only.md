---
name: pack-a-carry-on-only
domain: travel
locale: [generic]
interface: physical
difficulty: basic
est_time: 1h
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Pack everything needed for a trip into a carry-on bag and personal item without violating common airline size, weight, or liquids rules.

## Preconditions

- Airline carry-on and personal-item limits for the specific ticket.
- Trip length, weather, laundry access, and required events known.
- A compliant liquids bag if flying through security with liquids.

## Steps

1. **Check the airline limits.** Look up size, weight, and personal-item rules for your fare, especially on budget airlines. → *Expect:* you know the maximum bag dimensions and any weight cap.
2. **Build a capsule wardrobe.** Pick tops, bottoms, layers, and shoes that mix together in one color plan. → *Expect:* most tops work with most bottoms.
3. **Wear the bulkiest items.** Put heavy shoes, coat, or sweater on your travel outfit. → *Expect:* suitcase volume is reserved for smaller items.
4. **Pack by outfit count.** Use enough underwear and socks, then fewer outer layers that can repeat. → *Expect:* clothing covers the trip without packing one full outfit per day unnecessarily.
5. **Roll and cube soft items.** Roll clothes into packing cubes or tight rows, with wrinkle-prone pieces folded on top. → *Expect:* the bag closes without sitting on it.
6. **Follow the liquids rule.** Put travel-size liquids, gels, and aerosols in the required clear bag where the airport can inspect it. → *Expect:* security screening will not require digging through the suitcase.
7. **Use the personal item strategically.** Put documents, medication, electronics, chargers, snacks, and one emergency clothing layer under the seat. → *Expect:* essentials stay reachable even if the carry-on is gate-checked.
8. **Separate must-not-lose items.** Keep passport, wallet, keys, medicine, and critical devices on your body or in the personal item. → *Expect:* a gate-checked roller would not strand you.
9. **Weigh and test carry.** Weigh the bag if the airline has a cap, then walk with both bags for five minutes. → *Expect:* you can lift the carry-on overhead and move without repacking.
10. **Leave a little return space.** Remove one low-value item or pack a foldable tote for laundry. → *Expect:* the bag can close on the way home.

## Decision points

- Airline has a strict weight cap → prioritize lighter fabrics and move dense essentials to the personal item if allowed.
- Trip includes formal wear → pack one flexible outfit rather than separate shoes and accessories for every event.
- No laundry access → add underwear and socks before adding extra bulky clothes.
- Medical liquids exceed normal limits → check security rules and carry documentation if needed.

## Failure modes & recovery

- **F1 Bag too large:** detect it failing the sizer or measurement, recover by moving items to a smaller bag or checking it before security.
- **F2 Liquids rejected:** detect oversized containers at screening, recover by discarding, transferring, or checking the item when possible.
- **F3 Overpacked personal item:** detect it does not fit under a chair, recover by removing nonessentials before boarding.
- **F4 Gate-check surprise:** detect boarding staff tagging rollers, recover by pulling medicine, documents, batteries, and valuables out first.

## Verification

Both bags meet the airline limits, close fully, and contain documents, medicine, electronics, clothing, toiletries, and trip-specific essentials.

## Variations

- Business trip: pack one neutral jacket and shirts that all match it.
- Warm-weather trip: use quick-dry clothing and sandals that can handle walking.
- Winter trip: wear the coat and pack thin thermal layers instead of bulky sweaters.

## Safety & privacy

Low risk. Keep identification, medication, lithium batteries, and valuables out of checked or gate-checked luggage, and do not pack prohibited items.
