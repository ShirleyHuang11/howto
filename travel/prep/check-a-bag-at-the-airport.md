---
name: check-a-bag-at-the-airport
domain: travel
subdomain: prep
locale: [generic]
interface: physical
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You check luggage with the airline correctly, keep essential items with you, and retain proof needed if the bag is delayed or damaged.

## Preconditions

- Airline ticket, identification, and any required travel documents.
- Packed bag within airline size, weight, and contents rules.
- Payment method for baggage fees if not prepaid.

## Steps

1. **Check baggage rules before leaving.** Confirm allowance, weight limit, size limit, fees, and prohibited items for your cabin, route, and airline. → *Expect:* the bag is eligible to check or you know the fee.
2. **Remove essentials and valuables.** Keep passport, ID, medication, electronics, keys, cash, fragile valuables, and one change of critical clothing in carry-on. → *Expect:* losing the checked bag would be inconvenient, not dangerous.
3. **Label the bag inside and outside.** Add name, phone, email, and destination address or itinerary copy inside the bag. → *Expect:* airline staff can identify the owner if the external tag comes off.
4. **Secure and weigh the bag.** Close zippers, remove old airline tags, weigh the bag, and use a TSA-accepted or airline-allowed lock if desired. → *Expect:* the bag is under the limit and free of old routing tags.
5. **Use the correct bag-drop process.** [BRANCH: staffed counter | self-tag kiosk | curbside check-in] Follow the airline instructions and present ID when required. → *Expect:* the airline accepts the bag and prints or scans a tag.
6. **Verify the routing tag.** Before the bag leaves, check final airport code, passenger name, and flight number if shown. → *Expect:* the tag routes to the correct destination.
7. **Keep the baggage receipt.** Save the paper claim stub or screenshot the bag tag number in the airline app. → *Expect:* you have a bag tag number for tracking or claims.
8. **Track the bag after check-in.** Use the airline app if available and confirm scan updates during the trip. → *Expect:* the bag shows accepted and later loaded or transferred when scans are available.

## Decision points

- Bag is overweight → move nonessential items to carry-on if allowed, pay the fee, or repack into another bag.
- Contains lithium batteries, power banks, or e-cigarettes → remove them to carry-on according to airline and security rules.
- International itinerary with customs at first entry → ask whether you must collect and recheck the bag.
- Tight connection → ask whether checking a bag is practical or whether carry-on is safer.

## Failure modes & recovery

- **F1 Bag tag shows wrong airport:** detect incorrect destination code → stop the process immediately and ask staff to retag the bag.
- **F2 Bag rejected for contents:** detect prohibited item at screening or counter → remove, discard, ship, or repack the item as allowed.
- **F3 Bag not on carousel:** detect no bag after unloading ends → file a delayed-bag report before leaving the airport.
- **F4 Bag damaged:** detect broken wheels, shell, zipper, or missing contents → report it to the airline baggage office immediately and keep photos.

## Verification

The bag has been accepted by the airline, the routing tag shows the correct destination, and you have a claim number or bag tag receipt saved.

## Variations

- `us`: TSA may inspect checked bags; use accepted locks if locking luggage.
- `international`: customs rules may require collecting checked bags at the first port of entry before a domestic connection.
- `sports-equipment`: oversized or special items often require a separate counter and earlier arrival.

## Safety & privacy

Medium risk because checked baggage can be lost, delayed, damaged, or searched. Keep identity documents, medication, valuables, lithium batteries, and essential electronics out of checked luggage.
