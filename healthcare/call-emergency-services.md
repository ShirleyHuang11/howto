---
name: call-emergency-services
domain: healthcare
locale: [generic]
interface: phone-call
difficulty: basic
est_time: 5min
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Emergency services are contacted quickly, given accurate location and problem details, and kept connected until help is arranged.

## Preconditions

- There is an immediate threat to life, safety, or serious health: trouble breathing, chest pain, severe bleeding, stroke signs, unconsciousness, overdose, fire, violence, crash, or another emergency.
- The caller can use any working phone or ask a bystander to call.
- If calling might put the caller in danger, move to a safer place first if possible.
- This recipe supports emergency calling; follow the dispatcher over this text.

## Steps

1. **Get to relative safety.** Move away from traffic, fire, weapons, electrical hazards, or toxic fumes if you can do so without delaying urgent care. → *Expect:* you can speak and observe without becoming injured.
2. **Call the local emergency number.** Dial the emergency number for the location, or use the phone's emergency-call function. → *Expect:* the call rings or connects to a dispatcher.
3. **State the need first.** Say "medical emergency," "fire," "police," or "not sure" and describe the main problem in one sentence. → *Expect:* the dispatcher starts routing the right responders.
4. **Give the exact location.** Provide address, business name, floor, room, entrance, cross streets, landmarks, or GPS/map information. → *Expect:* responders have a place they can find.
5. **Give the callback number.** Say the number of the phone you are using, even if you think it appears automatically. → *Expect:* dispatch can reconnect if the call drops.
6. **Answer focused questions.** Report age if known, breathing status, consciousness, severe bleeding, hazards, number of people hurt, and what first aid is happening. → *Expect:* dispatch has enough detail to prioritize and guide care.
7. **Follow dispatcher instructions.** Put the phone on speaker if safe and do exactly what the dispatcher tells you. → *Expect:* care continues while help is being sent.
8. **Assign bystanders.** Ask specific people to meet responders, control pets, bring an AED or naloxone if relevant, and keep the area clear. → *Expect:* useful tasks happen without crowding the person.
9. **Stay on the line.** Do not hang up until the dispatcher says to, unless staying connected creates immediate danger. → *Expect:* dispatch can update instructions as the situation changes.
10. **Flag responders when they arrive.** Send someone visible to the entrance or wave responders in from a safe place. → *Expect:* emergency crews reach the person faster.

## Decision points

- Call will not connect → try another phone, landline, nearby business, vehicle emergency button, or ask a bystander to call.
- You cannot speak safely → keep the line open, make noise if possible, text emergency services only where available, or move before calling.
- Location is uncertain → give landmarks, road direction, mile marker, nearby signs, map coordinates, or a dropped pin.
- Multiple emergencies compete → report the greatest immediate threat first, then the number of people involved.
- Dispatcher instructions differ from this recipe → follow the dispatcher.

## Failure modes & recovery

- **F1 Wrong location:** detect confusion about address or entrance → recover by repeating landmarks, cross streets, floor, access code, and the caller's visible position.
- **F2 Caller hangs up too early:** detect no dispatcher confirmation → recover by calling back and saying the previous call disconnected.
- **F3 Bystanders all assume someone called:** detect no named caller → recover by assigning one specific person and confirming they connected.
- **F4 Phone battery low:** detect low charge warning → recover by switching to speaker only when needed, plugging in, or transferring caller role to another phone.

## Verification

Emergency dispatch has the exact location, callback number, emergency type, current condition, known hazards, and the caller remains available until dispatch releases the call or responders arrive.

## Variations

- No cellular service: move only as far as needed for signal if safe, use Wi-Fi calling, a landline, satellite SOS, roadside box, or send a specific person to call.
- Language barrier: state the language needed; many dispatch centers can add interpreters.
- Shared building: include unit, floor, gate code, elevator limits, and which entrance responders should use.

## Safety & privacy

High risk because delay or wrong location can be fatal. Share necessary personal and location information with dispatch, keep yourself safe, and do not transport a critically ill or injured person yourself if emergency responders can reach you.
