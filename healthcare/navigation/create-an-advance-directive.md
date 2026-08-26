---
name: create-an-advance-directive
domain: healthcare
subdomain: navigation
locale: [generic, us]
interface: mixed
difficulty: advanced
est_time: 1h-2h
risk: high
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You create a legally valid advance directive that records your medical-treatment preferences and makes it available to the people and clinicians who may need it.

## Preconditions

- The official advance directive, living will, or healthcare directive form for your state or jurisdiction.
- A chosen healthcare agent if the form includes proxy appointment.
- Identification, witnesses or notary if required, and time to discuss preferences with trusted people.

## Steps

1. **Get the correct jurisdiction form.** Use your state health department, attorney general, bar association, hospital, or recognized legal-aid source. → *Expect:* the form matches where you live or receive care.
2. **Read the treatment-preference sections.** Review choices about life-sustaining treatment, artificial nutrition and hydration, comfort care, organ donation, and religious or personal wishes. → *Expect:* you understand what decisions the form asks you to make.
3. **Discuss your wishes with your chosen agent and clinician.** Explain what quality of life, comfort, and burdens of treatment mean to you. → *Expect:* the people involved can describe your preferences in their own words.
4. **Complete the form carefully.** Fill in your legal name, agent, alternate agents, instructions, and any limits on authority. → *Expect:* no required fields are blank or contradictory.
5. **Sign using the required formalities.** ⚠️ *Irreversible/legal significance:* signing can guide future medical decisions when you cannot speak; confirm the form, choices, witnesses, and notary requirements before signing. → *Expect:* signatures, witness statements, and notary seal if required are complete.
6. **Distribute copies.** Give copies to your agent, alternate agent, primary care clinician, hospital portal, and close family as appropriate. → *Expect:* key people can produce the document quickly.
7. **Store and review it.** Keep the original in an accessible place and review after major life, health, or relationship changes. → *Expect:* the directive remains current and reachable.

## Decision points

- You are unsure about medical implications → talk with a clinician before signing.
- Family conflict is likely → consider an attorney or ethics/social-work consultation to reduce ambiguity.
- You move states or countries → check whether the form should be updated for the new jurisdiction.

## Failure modes & recovery

- **F1 Invalid witnesses:** detect witnesses are prohibited relatives, agents, or beneficiaries under local rules → re-sign with qualified witnesses.
- **F2 Agent unaware:** detect the agent has never seen the document → discuss it and provide a copy.
- **F3 Document unavailable in crisis:** detect only one copy locked away → upload to the portal and give copies to agents.
- **F4 Preferences changed:** detect the document no longer reflects your wishes → revoke or replace it according to local rules and redistribute the new version.

## Verification

The advance directive is signed with required witnesses or notary, copies are held by your healthcare agent and clinician or portal, and the people named know how to access it.

## Variations

- `us`: requirements differ by state; some states combine healthcare proxy and living will, while others use separate forms.
- POLST/MOLST: these clinician-signed medical orders are different from advance directives and are usually for people with serious illness or frailty.

## Safety & privacy

High risk because the document can affect life-sustaining treatment when you cannot speak. Do not sign under pressure, confirm legal formalities, and tell agents where the current signed version is stored.
