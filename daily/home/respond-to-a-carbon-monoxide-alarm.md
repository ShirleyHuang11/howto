---
name: respond-to-a-carbon-monoxide-alarm
domain: daily
subdomain: home
locale: [generic]
interface: mixed
difficulty: basic
est_time: 10min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

A carbon monoxide alarm triggers immediate evacuation, emergency notification, and no re-entry until professionals declare the space safe.

## Preconditions

- A carbon monoxide alarm is sounding, or people have headache, dizziness, nausea, weakness, confusion, chest pain, or sleepiness near fuel-burning appliances.
- Call emergency services or the local gas/emergency utility from outside.
- Do not ignore or silence the alarm and stay inside to investigate.
- Do not re-enter until firefighters, utility workers, or qualified professionals clear the building.
- Carbon monoxide is odorless and can be fatal.

## Steps

1. **Leave immediately.** Get everyone outside into fresh air without searching for the source. → *Expect:* exposure begins to stop.
2. **Help vulnerable people.** Assist children, older adults, disabled people, and pets only if it does not trap you inside. → *Expect:* household members are moving out.
3. **Avoid switches and flames if gas is suspected.** Do not light flames or operate unnecessary electrical switches if you also smell gas. → *Expect:* ignition risk is reduced.
4. **Call emergency services from outside.** Report the carbon monoxide alarm, symptoms, address, and fuel-burning appliances. → *Expect:* responders are dispatched or utility help is arranged.
5. **Check symptoms.** Ask everyone about headache, dizziness, nausea, confusion, chest pain, and breathing trouble. → *Expect:* possible poisoning is identified.
6. **Get medical help for symptoms.** [BRANCH: symptoms present | no symptoms] request medical evaluation for anyone symptomatic; keep asymptomatic people outside too. → *Expect:* poisoning is not missed.
7. **Account for everyone.** Use the meeting place and report missing people to responders. → *Expect:* rescuers know if someone may still be inside.
8. **Do not re-enter.** ⚠️ *Irreversible:* going back inside can cause collapse and death; confirm clearance from responders before entry. → *Expect:* no one returns to contaminated air.
9. **Ventilate only if instructed.** Let responders or the utility decide when doors and windows should be opened. → *Expect:* investigation and safety are not compromised.
10. **Arrange repair before reuse.** Have fuel-burning appliances, vents, chimneys, and detectors inspected. → *Expect:* the source is corrected before normal occupancy.

## Decision points

- Anyone has symptoms → call emergency services and request medical evaluation.
- Alarm stops after fresh air or reset → still stay out and have the source checked.
- Smell of gas accompanies the alarm → evacuate, avoid ignition sources, and call the gas emergency line or emergency services.
- Alarm is old or malfunctioning suspected → replace it only after the building has been cleared safe.
- Multi-unit building → notify neighbors or management from outside if safe.

## Failure modes & recovery

- **F1 Alarm silenced:** detect reset without evacuation → recover by leaving immediately and calling from outside.
- **F2 Re-entry to open windows:** detect someone going back in → recover by stopping them and waiting for responders.
- **F3 Symptoms dismissed as flu:** detect multiple people or pets sick indoors → recover by treating as carbon monoxide until proven otherwise.
- **F4 Appliance reused too soon:** detect furnace, stove, generator, or fireplace restarted before inspection → recover by shutting it off from a safe place if instructed and arranging service.

## Verification

Everyone is outside in fresh air, emergency services or the gas emergency utility has been contacted, symptomatic people are getting medical evaluation, and no one re-enters until professionals clear the building.

## Variations

- Generator use: keep generators outdoors far from doors, windows, and vents; never use one in a garage.
- Apartment building: evacuate and notify building management after calling emergency services.
- Travel lodging: leave the room, alert staff from outside the affected area, and call emergency services for symptoms.

## Safety & privacy

High risk because carbon monoxide can cause unconsciousness and death without warning. Share location and symptom information with emergency responders and do not prioritize belongings or investigation over evacuation.
