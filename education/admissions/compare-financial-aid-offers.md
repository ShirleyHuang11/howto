---
name: compare-financial-aid-offers
domain: education
subdomain: admissions
locale: [generic, us]
interface: web
difficulty: intermediate
est_time: 1h-4h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-02
---

## Goal

You compare financial aid offers by true net cost, debt, work expectations, renewal rules, and affordability over the full program.

## Preconditions

- Financial aid offers from colleges.
- Each college's cost of attendance, including tuition, fees, housing, food, books, transportation, and personal expenses.
- Family budget, savings, and borrowing limits.

## Steps

1. **Collect complete aid letters and cost figures.** Download official offers and current cost of attendance for the same academic year. → *Expect:* every school is compared on the same year and cost basis.
2. **Separate gift aid from self-help.** Label grants and scholarships separately from loans, work-study, payment plans, and parent loans. → *Expect:* free money is not confused with debt or wages.
3. **Calculate net price.** Subtract grants and scholarships from total cost of attendance, not just tuition. → *Expect:* each school has a comparable out-of-pocket annual cost.
4. **Estimate four-year cost.** Account for renewable aid, GPA requirements, tuition increases, housing changes, and program length. → *Expect:* a rough total cost and debt picture emerges.
5. **Review loan amounts and borrowers.** Identify subsidized, unsubsidized, parent, private, or institutional loans and who is legally responsible. → *Expect:* you know which offers require student or parent debt.
6. **Check conditions and missing items.** Look for verification, satisfactory academic progress, enrollment level, residency, housing, major, honors, or outside-scholarship rules. → *Expect:* fragile aid is marked.
7. **Ask aid offices clarifying questions.** Request explanations for unclear terms, special circumstances, or competing offers. → *Expect:* unanswered cost questions are resolved in writing.
8. **Choose based on affordability and fit together.** Compare academic fit, likely completion, family risk, and total cost before committing. → *Expect:* the preferred option is financially realistic.

## Decision points

- Aid package includes large Parent PLUS or private loans → treat those as optional borrowing, not discount.
- Scholarship is not renewable → calculate later years without it unless renewal is confirmed.
- Family finances changed → ask about professional judgment or special circumstance review.

## Failure modes & recovery

- **F1 Comparing tuition only:** detect housing, fees, travel, or books omitted → recalculate using full cost of attendance.
- **F2 Loans counted as aid:** detect "award" totals including debt → separate gift aid from loans and work.
- **F3 Renewal surprise:** detect GPA or major requirement after enrollment → ask for renewal terms before committing.
- **F4 Outside scholarship displacement:** detect college reduces grants when outside aid arrives → ask how outside scholarships affect the package.

## Verification

You have a side-by-side comparison showing total cost of attendance, gift aid, net price, loans by borrower, work-study, renewal rules, and estimated multi-year cost for each college.

## Variations

- `us`: use the college's official aid offer, FAFSA Submission Summary, and net price information; terminology varies widely by school.
- `community-college-transfer`: compare two-year plus transfer costs, not just first-year price.
- `commuter`: adjust housing, food, transportation, parking, and family contribution assumptions.

## Safety & privacy

Medium risk because aid decisions affect debt and family finances. Do not accept loans or commit to a college until the borrower, amount, interest type, renewal terms, and total cost are clear.
