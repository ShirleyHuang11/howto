---
name: keep-a-personal-health-record
domain: healthcare
subdomain: navigation
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You maintain a private, current health record that helps with appointments, emergencies, insurance, and caregiving.

## Preconditions

- A secure folder, encrypted notes app, password manager attachment, or physical binder.
- Current medication bottles or pharmacy list.
- Access to patient portals or paper records from major clinicians.

## Steps

1. **Choose a secure storage method.** Use one digital folder with backup, a physical binder, or both. → *Expect:* there is a single trusted place for health documents.
2. **Create a one-page summary.** Include name, date of birth, emergency contacts, clinicians, conditions, surgeries, allergies, medications, devices, and insurance. → *Expect:* emergency basics fit on one page.
3. **Record medications accurately.** List name, strength, dose, timing, reason, prescriber, pharmacy, and start/stop dates. → *Expect:* the medication list matches current bottles or pharmacy records.
4. **Save key records.** Add immunizations, lab trends, imaging reports, operative notes, discharge summaries, advance directives, and major diagnoses. → *Expect:* important records are organized by date or category.
5. **Track appointments and follow-up.** Keep visit summaries, pending tests, referrals, and next appointment dates. → *Expect:* open tasks are visible.
6. **Include insurance and billing basics.** Store plan name, member ID, pharmacy benefit info, prior authorization letters, and major claim appeals. → *Expect:* coverage information is available when needed.
7. **Set an update routine.** Update after every medication change, hospitalization, new diagnosis, vaccine, or insurance change. → *Expect:* the record stays current rather than becoming an archive.
8. **Share selectively.** Give relevant parts to clinicians or caregivers, not the whole file unless needed. → *Expect:* others receive only information needed for care.

## Decision points

- You have complex care → use categories by condition and add a current care-team contact list.
- You travel often → keep a compact medication/allergy summary accessible offline.
- You are a caregiver → confirm legal access, portal proxy status, and emergency contact permissions.

## Failure modes & recovery

- **F1 Record goes stale:** detect medication or insurance changes missing → schedule a monthly or post-visit update reminder.
- **F2 Too hard to find documents:** detect mixed file names and duplicates → rename files with date, provider, and document type.
- **F3 Privacy exposure:** detect records stored in shared email or unprotected cloud folders → move to secure storage and remove unnecessary copies.
- **F4 Clinician needs original records:** detect summary is not enough → request official records from the provider or portal.

## Verification

Your personal health record contains a current one-page summary, medication list, allergies, clinician contacts, insurance details, and recent key records, stored securely and retrievable within minutes.

## Variations

- `us`: patient portals often allow downloads of visit summaries, labs, immunizations, and Continuity of Care Documents.
- Paper-first: use a binder with tabs for summary, medications, labs, imaging, hospitalizations, and insurance.
- Family record: keep each person's files separate to avoid dangerous medication or identity mix-ups.

## Safety & privacy

Medium risk because health records include sensitive medical and identity data. Protect files with strong passwords or locked storage, share the minimum necessary, and keep medication and allergy information accurate.
