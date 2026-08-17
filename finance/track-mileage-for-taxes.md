---
name: track-mileage-for-taxes
domain: finance
locale: [generic]
interface: mobile-app
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Create a reliable mileage log that can support tax deductions or reimbursements for business, charitable, medical, or moving trips where allowed.

## Preconditions

- You know which trip purposes are deductible or reimbursable in your jurisdiction or employer policy.
- You have a notebook, spreadsheet, odometer photos, or mileage-tracking app.
- You can distinguish personal commuting from eligible mileage.
- You have the vehicle's starting odometer reading for the tax or reporting period.

## Steps

1. **Choose a log method.** Pick one system for date, destination, purpose, starting mileage, ending mileage, and miles driven. → *Expect:* one log format is ready before trips begin.
2. **Record the starting odometer.** Take a photo or write down the odometer at the beginning of the tax year, vehicle use, or reimbursement period. → *Expect:* the opening mileage is timestamped.
3. **Log each eligible trip.** Immediately after each trip, record date, start, destination, business or allowed purpose, and miles. → *Expect:* the trip appears in the log with enough detail to explain it later.
4. **Keep supporting evidence.** Save appointment notes, client visits, delivery records, invoices, or employer requests that match the trip. → *Expect:* each meaningful trip has a reason outside the mileage log.
5. **Separate personal miles.** Mark commuting, errands, and personal detours as non-deductible or personal. → *Expect:* only eligible miles are included in the tax or reimbursement total.
6. **Reconcile monthly.** Compare app totals, odometer changes, calendars, and receipts for gaps or duplicates. → *Expect:* monthly mileage totals are plausible and corrected.
7. **Close the period.** Record the ending odometer and summarize eligible miles by category. → *Expect:* annual or period totals can be copied into tax or reimbursement forms.

## Decision points

- Using a tax deduction → choose standard mileage or actual expense method only after checking current rules and required records.
- Employer reimbursement differs from tax rules → follow the employer policy for reimbursement and keep tax records separately.
- Shared vehicle → record driver and purpose so another person's trips are not mixed into your claim.
- App tracking is unreliable → switch to manual entries with odometer photos and calendar support.

## Failure modes & recovery

- **F1 Trip forgotten:** detect calendar event or receipt with no mileage entry → recover by reconstructing from maps and marking it as estimated.
- **F2 Commute included:** detect home-to-regular-work trips in the log → recover by removing them unless a current rule or policy allows them.
- **F3 Duplicate trip:** detect identical date, route, and miles repeated → recover by deleting one entry and documenting the correction.
- **F4 Missing odometer:** detect no opening or closing reading → recover by using service records, inspection records, or dated photos if available.

## Verification

The mileage log contains dated eligible trips, purposes, distances, opening and closing odometer readings, and a summarized total that matches the tax or reimbursement entry.

## Variations

- `us`: IRS standard mileage rates and allowed categories can change by year.
- `delivery-or-rideshare`: platform trip exports help support app-based mileage logs.
- `employer-reimbursement`: reimbursement categories may be narrower than tax categories.

## Safety & privacy

Medium risk because unsupported mileage claims can create tax problems and location logs reveal sensitive travel patterns. Limit app permissions where possible and store exports securely.
