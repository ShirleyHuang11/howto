---
name: get-a-copy-of-your-vaccination-record
domain: healthcare
subdomain: navigation
locale: [generic, us]
interface: mixed
difficulty: intermediate
est_time: 30min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You obtain a reliable copy of your vaccination record for school, work, travel, medical care, or personal files.

## Preconditions

- Your legal name used at vaccination, date of birth, prior names if any, and contact information.
- Approximate vaccination locations: pediatrician, pharmacy, employer clinic, school, public health clinic, military, or state registry.
- Photo ID or portal access if required.

## Steps

1. **List likely record sources.** Start with your current clinician, childhood provider, pharmacies, schools, employers, and public health registry. → *Expect:* you have a ranked list of places to request from.
2. **Check patient and pharmacy portals.** Download immunization history from official portals where available. → *Expect:* at least some vaccine dates may appear immediately.
3. **Request the state or regional registry record.** In the US, search for your state's Immunization Information System request process. → *Expect:* the registry gives a request form, portal, or help-desk route.
4. **Submit identity information securely.** Provide required ID, prior names, and authorization forms only through official channels. → *Expect:* the requester accepts or begins processing the record request.
5. **Compare records for gaps.** Match vaccine names, dates, lot numbers if present, and doses across sources. → *Expect:* duplicate and missing entries are visible.
6. **Ask a clinician how to handle missing proof.** For some vaccines, a blood titer or repeat vaccination may be recommended if records cannot be found. → *Expect:* you have a medical plan for missing documentation.
7. **Save official copies.** Store PDFs or printouts with source name and date generated. → *Expect:* you can provide proof without restarting the search.

## Decision points

- Record needed for international travel → check destination requirements and ask a travel clinic about accepted proof formats.
- Childhood provider closed → contact the health system successor, state registry, school records office, or local health department.
- Name changed → include prior legal names and documentation if requested.

## Failure modes & recovery

- **F1 No registry match:** detect "no record found" → try prior names, prior addresses, and vaccine locations; then request from individual providers.
- **F2 Portal record incomplete:** detect missing childhood or pharmacy vaccines → combine sources and ask clinician to update your chart.
- **F3 School or employer requires a specific form:** detect rejection of a generic printout → ask what exact form or signature is required.
- **F4 Suspected error:** detect a wrong date, vaccine, or patient → contact the source that entered it and request correction.

## Verification

You have an official portal download, registry report, provider printout, or signed form showing vaccine names and dates, and it is accepted by the requesting organization or reviewed by your clinician for gaps.

## Variations

- `us`: each state runs its own Immunization Information System; adult records may be incomplete if providers did not report.
- COVID-19 records: many jurisdictions offer a SMART Health Card or digital certificate, but availability varies.

## Safety & privacy

Medium risk because vaccination records contain health and identity information. Use official portals, avoid posting vaccine cards publicly, and verify recipient requirements before sending full records.
