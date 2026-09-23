---
name: use-role-and-persona-prompting
domain: ai
subdomain: prompting
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You use role and persona instructions to improve domain fit, tone, and decision criteria without letting persona override accuracy, safety, or task requirements.

## Preconditions

- A task with a known audience or domain, such as support, tutoring, code review, or clinical admin.
- Examples of desired and undesired tone.
- A small eval set that checks correctness and style.

## Steps

1. **Define the useful role.** Specify expertise and responsibilities, not a fictional biography. → *Expect:* the prompt says what the assistant does and which standards it applies.
2. **Separate role from tone.** Put persona style in a short section after task and safety requirements. → *Expect:* removing the style section does not remove core task constraints.
3. **Add domain decision criteria.** Include the checks a competent practitioner would use, such as evidence quality or risk triage. → *Expect:* outputs mention relevant criteria when making recommendations.
4. **Test against neutral prompting.** Run the same cases with and without the role instruction. → *Expect:* a comparison of accuracy, helpfulness, and style adherence.
5. **Check for overclaiming.** Include cases where the role must defer, ask for missing data, or refuse. → *Expect:* the model does not pretend to have licenses, access, or certainty it lacks.
6. **Lock the useful phrasing.** Keep the shortest role description that improves eval results. → *Expect:* a versioned prompt with measured style and correctness scores.

## Decision points

- Role improves tone but hurts accuracy → shorten persona and strengthen task criteria.
- Domain is regulated or high impact → include boundaries and escalation instructions.
- User asks the model to act as a real person → state assistant identity and capabilities honestly.

## Failure modes & recovery

- **F1 Persona overreach:** detect claims of credentials or access → add explicit capability limits.
- **F2 Style dominates content:** detect pleasant but incomplete answers → score required facts separately from tone.
- **F3 Stereotyped voice:** detect exaggerated or offensive persona behavior → replace persona with professional communication criteria.
- **F4 Inconsistent tone:** detect large variance across runs → lower temperature and add a few tone examples.

## Verification

Run `python eval_persona.py --baseline neutral.md --candidate persona.md --cases persona_eval.jsonl`; the candidate must maintain correctness within 1 percentage point of baseline, improve style score by at least 10%, and produce zero credential-overclaim violations.

## Variations

- `support`: define empathy, brevity, and escalation rules.
- `code review`: define severity-first findings and evidence requirements.
- `tutoring`: define Socratic help and when to give direct answers.

## Safety & privacy

Role prompts can make outputs feel more authoritative than they are. Be explicit about limitations, avoid impersonating real professionals, and do not let style instructions weaken safety or privacy constraints.
