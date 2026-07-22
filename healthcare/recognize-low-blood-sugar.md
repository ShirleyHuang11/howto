---
name: recognize-low-blood-sugar
domain: healthcare
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: high
prerequisites: []
status: draft
last_verified: 2026-07-22
---

## Goal

Possible low blood sugar is recognized, treated promptly when safe, and escalated when it could be an emergency.

## Preconditions

- This applies especially to people with diabetes using insulin or medicines that can lower glucose.
- Symptoms can include shaking, sweating, hunger, headache, fast heartbeat, anxiety, dizziness, weakness, blurred vision, confusion, behavior change, seizure, or unconsciousness.
- If a glucose meter or continuous glucose monitor is available, use it, but do not delay treatment for severe symptoms.
- Call emergency services if the person is unconscious, having a seizure, unable to swallow, severely confused, or not improving.
- Do not give food or drink to someone who cannot swallow safely.

## Steps

1. **Check for severe symptoms.** Look for unconsciousness, seizure, inability to swallow, severe confusion, or collapse. → *Expect:* emergency signs are identified before giving anything by mouth.
2. **Call emergency services if severe.** [BRANCH: severe symptoms | awake and can swallow] call emergency services and use prescribed glucagon if available for severe symptoms; continue oral treatment only if safe. → *Expect:* severe hypoglycemia is treated as an emergency.
   - ⚠️ *Irreversible:* Do not put food, drink, or fingers in the mouth of a person who is unconscious or seizing.
3. **Check glucose if available.** Use a meter or CGM reading and note the time. → *Expect:* a low reading, often below 70 mg/dL or 3.9 mmol/L, supports treatment.
4. **Give fast sugar.** Give 15 grams of fast-acting carbohydrate, such as glucose tablets, glucose gel, regular soda, juice, or hard candy that can be chewed safely. → *Expect:* sugar is swallowed without choking.
5. **Wait 15 minutes.** Keep the person seated and recheck symptoms or glucose after 15 minutes. → *Expect:* symptoms start improving or the glucose can be remeasured.
6. **Repeat the 15-15 rule.** If glucose is still low or symptoms persist, give another 15 grams and wait 15 minutes. → *Expect:* glucose rises or symptoms improve after repeat treatment.
7. **Eat longer-acting food.** Once better, give a meal or snack with carbohydrate and protein if the next meal is not soon. → *Expect:* glucose is less likely to drop again.
8. **Identify the cause.** Check for missed meal, extra insulin, more exercise than usual, alcohol, vomiting, or medication error. → *Expect:* the likely trigger is known for prevention.
9. **Document and notify.** Record time, symptoms, glucose values, treatment, and tell the person's clinician if episodes recur. → *Expect:* follow-up information is available.

## Decision points

- Person cannot swallow, is unconscious, has a seizure, or remains severely confused → call emergency services and use glucagon if prescribed.
- Glucose stays low after repeated 15-gram treatments → seek urgent medical help.
- Symptoms occur in someone without known diabetes medication risk → get medical assessment.
- Low blood sugar happens during pregnancy, in a child, or after a medication mistake → call a clinician promptly.
- Recurrent lows → adjust prevention with the diabetes care team.

## Failure modes & recovery

- **F1 Choking risk:** detect drowsiness or poor swallowing, recover by stopping oral sugar and calling emergency services.
- **F2 Overtreatment:** detect repeated large sugary intake after recovery, recover by following measured 15-gram doses and rechecking.
- **F3 Delayed recurrence:** detect symptoms returning after initial improvement, recover with another check and longer-acting food.
- **F4 No supplies:** detect no glucose source available, recover by calling for help and using any safe fast carbohydrate.

## Verification

The person is alert, able to swallow, symptoms are improving, and glucose is above the low threshold or emergency help has been activated.

## Variations

- Glucagon kit: use the prescribed nasal spray or injection as labeled when the person cannot take sugar by mouth.
- CGM user: confirm with fingerstick if readings do not match symptoms and the person is stable.
- Child: use the diabetes care plan for the exact carbohydrate amount.

## Safety & privacy

High risk because severe low blood sugar can cause seizure, coma, or death. Share glucose readings and medication details with emergency responders or clinicians, and keep diabetes supplies accessible.
