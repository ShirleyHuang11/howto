---
name: decide-er-vs-urgent-care
domain: healthcare
locale: [generic]
interface: mixed
difficulty: basic
est_time: 5min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Choose emergency care, urgent care, a nurse line, or routine care based on clear danger signs.

## Preconditions

- This is triage guidance, not a diagnosis.
- If the person may die, lose function, or get worse quickly, choose emergency services.
- Have the person's age, main symptom, medical conditions, medications, allergies, and location ready.
- When unsure between ER and urgent care, call emergency services or a nurse line for real-time advice.
- Do not drive yourself if symptoms could impair driving.

## Steps

1. **Check immediate danger.** Look for chest pain, stroke signs, severe bleeding, trouble breathing, seizure, fainting, major trauma, poisoning, or severe allergic reaction. → *Expect:* any life-threatening sign is identified within seconds.
2. **Call emergency services for red flags.** [BRANCH: red flag present | no red flag] call emergency services now if a red flag is present; continue triage only if none are present. → *Expect:* emergency help is activated when symptoms are dangerous.
   - ⚠️ *Irreversible:* Do not delay emergency care to compare prices, wait for a ride, or finish home treatment.
3. **Screen for stroke.** Check face drooping, arm weakness, speech trouble, sudden confusion, sudden severe headache, sudden vision loss, or sudden balance trouble. → *Expect:* possible stroke goes to emergency services even if symptoms improve.
4. **Screen breathing and circulation.** Treat severe shortness of breath, blue lips, choking, severe weakness, clammy skin, or new confusion as emergency signs. → *Expect:* unstable breathing or circulation is not sent to urgent care.
5. **Screen bleeding and injury.** Treat spurting blood, bleeding that soaks dressings after 10 minutes of firm pressure, deep wounds, head injury with confusion, or possible broken neck, hip, or spine as emergency signs. → *Expect:* major trauma is routed to the ER.
6. **Use urgent care for stable problems.** Consider urgent care for minor fractures or sprains, small cuts that may need stitches, mild asthma or flu symptoms, urinary symptoms, ear pain, rashes, or minor burns without danger signs. → *Expect:* the problem is uncomfortable but stable.
7. **Call a nurse line when uncertain.** Use the number on an insurance card, clinic portal, local health system, or public health service. → *Expect:* a clinician or triage service gives next-step advice.
8. **Choose routine care for non-urgent issues.** Use primary care for medication refills, chronic symptom follow-up, mild symptoms improving at home, or preventive questions. → *Expect:* care is scheduled without emergency delay.
9. **Recheck during waiting.** If symptoms worsen, new red flags appear, or the person becomes hard to wake, change the plan to emergency services. → *Expect:* escalation happens immediately when risk changes.

## Decision points

- Chest pain, stroke signs, severe bleeding, severe breathing trouble, poisoning, or severe allergic reaction → call emergency services.
- Stable illness or minor injury that needs same-day assessment but not resuscitation → urgent care may be appropriate.
- Unclear severity, complex medical history, pregnancy, infant, older adult, or immunocompromised person → call a nurse line or clinician.
- Cost concern but possible emergency → seek emergency care first and address billing later.
- Symptoms are mild and improving → routine care or self-care may be reasonable with monitoring.

## Failure modes & recovery

- **F1 Under-triage:** detect any red flag after choosing urgent care → call emergency services immediately.
- **F2 Self-driving risk:** detect dizziness, chest pain, fainting, vision change, or severe pain → get an ambulance or another driver.
- **F3 Wrong facility:** detect urgent care refusal or transfer recommendation → follow transfer instructions and bring paperwork.
- **F4 Delayed advice:** detect no nurse line response while symptoms worsen → stop waiting and call emergency services.

## Verification

The person is routed to emergency services, urgent care, a nurse line, or routine care with all red-flag symptoms checked explicitly.

## Variations

- Insurance-based systems: use the nurse line and in-network directory only after emergency symptoms are ruled out.
- Rural area: call emergency services for guidance when distance makes facility choice uncertain.
- Pediatric symptoms: lower the threshold for urgent or emergency advice, especially for infants under 3 months with fever.

## Safety & privacy

High risk because delayed emergency care can cause death or permanent harm. Share only needed medical details with triage staff, but do not withhold symptoms, medications, pregnancy status, or substance exposure.
