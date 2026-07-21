---
name: make-a-dinner-reservation
domain: daily
subdomain: social
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: low
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

A restaurant holds a table for the correct party, date, time, and contact name, with special requests recorded when possible.

## Preconditions

- You know the restaurant, meal date, preferred time, party size, and contact information.
- You can use the restaurant website, reservation app, or phone.
- You know any accessibility, seating, allergy, or celebration requests.
- You are ready to accept a nearby time if the exact slot is unavailable.

## Steps

1. **Gather the basics.** Write down date, time range, party size, name, phone number, and any special request. → *Expect:* you can answer the booking questions without pausing.
2. **Choose the booking channel.** [BRANCH: app or website | phone call] use the online system for standard tables, or call for large groups, accessibility needs, or unclear availability. → *Expect:* you are using the channel most likely to handle the request.
3. **Search or ask for the table.** Enter or say the party size, date, and preferred dinner time. → *Expect:* available slots, a host response, or a waitlist option appears.
4. **Pick the best slot.** Choose the closest acceptable time and note indoor, outdoor, bar, or counter seating if offered. → *Expect:* the booking summary matches your actual plan.
5. **Add special requests briefly.** Mention allergies, wheelchair access, high chair, quiet table, birthday note, or seating preference without demanding guarantees. → *Expect:* the request is attached or acknowledged.
6. **Confirm contact details.** Give the correct name, phone, email, and any deposit or card hold only after reviewing terms. ⚠️ *Irreversible:* cancellation fees or deposits may apply, so confirm the date, time, party size, and policy before submitting payment details. → *Expect:* the restaurant can reach you and the policy is understood.
7. **Save the confirmation.** Screenshot, email, calendar entry, or write down confirmation number, time, address, and cancellation deadline. → *Expect:* you can find the reservation details later.
8. **Update or cancel courteously.** If plans change, cancel as early as possible or adjust the party size before the deadline. → *Expect:* the restaurant can release or resize the table.

## Decision points

- Exact time unavailable → take a nearby time, join the waitlist, or choose another restaurant.
- Party is larger than the app limit → call and ask for group availability or a manager callback.
- Allergy or mobility need is critical → call even if the app accepts notes.
- Deposit, cancellation fee, or prepaid menu appears → confirm everyone agrees before booking.

## Failure modes & recovery

- **F1 Wrong party size:** detect the summary shows too few or too many guests → edit before confirming or call the restaurant.
- **F2 No confirmation received:** detect missing email, text, or app record → check spam and call with name, date, and time.
- **F3 Special request not guaranteed:** detect vague wording or no note field → call during slower hours and ask the host to add it.
- **F4 Late cancellation:** detect you are inside the fee window → call anyway, be brief, and accept any stated fee.

## Verification

A confirmation record shows the restaurant name, correct date, dinner time, party size, contact name, and cancellation policy.

## Variations

- `phone-call`: call before dinner rush, usually midafternoon, and repeat the details back.
- `mobile-app`: check push notifications and email because some apps require final confirmation.
- `walk-in-only`: ask about peak wait times and arrive early with the full party nearby.

## Safety & privacy

Low risk. Share only the contact and payment details needed for the booking. Treat card holds and prepaid menus as money commitments, and cancel promptly when you cannot attend.
