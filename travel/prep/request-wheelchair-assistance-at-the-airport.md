---
name: request-wheelchair-assistance-at-the-airport
domain: travel
subdomain: prep
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You arrange airport wheelchair or mobility assistance in advance so the traveler can move through check-in, security, boarding, connections, and arrival with appropriate support.

## Preconditions

- Airline booking reference, passenger name, flight numbers, and travel dates.
- The traveler's mobility needs, including whether they can walk short distances, climb stairs, or transfer seats.
- Contact information for the traveler or assisting companion.

## Steps

1. **Identify the operating airline for each flight.** Check the itinerary for codeshare flights and the airline actually operating each segment. → *Expect:* you know which airline must receive the assistance request.
2. **Open the accessibility or special-assistance request.** Use the airline booking portal, app, or phone line. → *Expect:* the reservation shows an option for wheelchair, mobility, or special assistance.
3. **Select the correct assistance level.** Choose airport wheelchair, ramp assistance, stair assistance, aisle chair, or help to the seat based on actual need. → *Expect:* the assistance code or description matches the traveler's mobility limits.
4. **Add connection and equipment details.** Note tight connections, personal mobility devices, batteries, service animals, or need for preboarding. → *Expect:* the request covers every flight segment and relevant equipment.
5. **Confirm the request on the booking.** Save the confirmation screen or ask the airline agent to read back the assistance details. → *Expect:* wheelchair or special-assistance notes are attached to the reservation.
6. **Plan extra airport time.** Arrive earlier than usual, especially for international flights, checked mobility devices, or large airports. → *Expect:* the itinerary includes time for assistance dispatch and security screening.
7. **Check in with airport staff on arrival.** Go to the airline counter, assistance desk, or curbside location and state the existing request. → *Expect:* staff can see the request and add the traveler to the assistance queue.
8. **Reconfirm at each transfer point.** Before landing or at the gate, remind crew or gate staff that assistance is needed for arrival or connection. → *Expect:* assistance is requested for deplaning and transfer.

## Decision points

- Traveler cannot climb aircraft stairs → request stair-free boarding or lift assistance and avoid airports where remote stands are likely.
- Personal wheelchair or scooter will travel → confirm battery type, dimensions, weight, and damage-report process.
- Tight connection → ask the airline whether the connection is realistic with assistance before travel.
- Assistance not visible in booking → call the airline and have the agent re-add it.

## Failure modes & recovery

- **F1 Assistance not waiting:** detect no wheelchair or escort at check-in, gate, or arrival → ask airline staff to dispatch assistance and stay near the desk or gate until assigned.
- **F2 Wrong assistance level:** detect staff only prepared for walking assistance when seat transfer is needed → ask for a supervisor and state the specific need, such as aisle chair or lift.
- **F3 Mobility device damaged:** detect damage on return → report to airline staff before leaving the airport and get a written property irregularity report.
- **F4 Connection missed due to delayed assistance:** detect assistance delay caused missed flight → ask the airline to rebook and document the timeline.

## Verification

The airline reservation shows wheelchair or mobility assistance for every flight segment, and the traveler knows where to check in for assistance at the departure airport.

## Variations

- `us`: airlines are covered by the Air Carrier Access Act; passengers can request disability assistance without paying extra.
- `eu-uk`: assistance is often coordinated by airports after the airline receives the request; request it at least 48 hours before travel when possible.
- `codeshare`: request assistance with both the ticketing airline and the operating airline if the booking does not clearly transfer the request.

## Safety & privacy

Medium risk because incorrect assistance can cause missed flights, falls, or damaged mobility devices. Provide only necessary medical details, confirm assistance before travel, and escalate immediately if the requested mobility support is missing or wrong.
