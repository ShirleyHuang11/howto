---
name: send-standardized-test-scores
domain: education
subdomain: admissions
locale: [generic, us]
interface: web
difficulty: intermediate
est_time: 30min-7d
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-02
---

## Goal

You send official standardized test scores to the correct schools or application services before the deadline, without accidentally sending the wrong test date or recipient.

## Preconditions

- You know which tests the program accepts and whether scores are required, optional, or self-reported first.
- You can log in to the test provider account.
- You have the recipient's official school code, department code, or application service instruction.

## Steps

1. **Read each program's testing policy.** Confirm required tests, optional rules, superscoring, self-reporting, and official-score deadlines. → *Expect:* a list of recipients and exactly which scores each needs.
2. **Choose the score set deliberately.** [BRANCH: score choice allowed | all scores required] Select the dates or all-score option that matches the policy. → *Expect:* the order includes only permitted score reports.
3. **Find the official recipient code.** Use the program's admissions page or application portal, especially for graduate departments. → *Expect:* the code and department name match the program, not just the university.
4. **Log in to the test provider.** Use the official provider account for SAT, ACT, GRE, TOEFL, IELTS, GMAT, LSAT, MCAT, or the relevant exam. → *Expect:* your score history and score-send options appear.
5. **Add recipients and review deadlines.** Enter each code, check processing times, and choose standard or rush only when useful. → *Expect:* each recipient line shows the correct institution and delivery method.
6. **Pay and submit the report order.** ⚠️ *Irreversible:* score reports usually cannot be recalled after processing, so confirm recipients and score dates first. → *Expect:* a receipt, order number, and estimated send date.
7. **Record the confirmation.** Save the order number, recipients, score dates, and delivery estimate. → *Expect:* you can prove when and where the scores were sent.
8. **Check application portals.** Look for received or matched status after the provider's processing window. → *Expect:* the application checklist shows official scores received or the admissions office confirms matching.

## Decision points

- Program is test-optional -> send scores only if they strengthen the application under that program's guidance.
- Recipient requires scores through a central application service -> send to the service code, not separately to the school.
- Scores will arrive after the deadline -> ask admissions whether self-reported scores or proof of order can hold the file temporarily.

## Failure modes & recovery

- **F1 Wrong school code:** detect a score report sent to the wrong campus or department -> place a corrected order and notify admissions with the new confirmation.
- **F2 Portal not updated:** detect no checklist change after delivery -> send the confirmation number and identifying details to admissions.
- **F3 Score-choice mistake:** detect an unintended test date in the order -> contact the provider immediately; if it processed, ask the school how they review extra scores.
- **F4 Name or birthdate mismatch:** detect unmatched scores -> ask the provider and school to reconcile using applicant ID, former name, and test registration details.

## Verification

Each application portal or admissions office confirms the official score report is received and matched to your applicant record before the relevant deadline.

## Variations

- `us`: SAT, ACT, GRE, and many professional tests use school or department codes; code lookup is more reliable on the program page than on a general search.
- Self-report-first programs: enter scores in the application, then send official scores only if admitted or requested.

## Safety & privacy

Medium risk because reports cost money and disclose education records. Confirm recipient codes and test dates before payment, use official provider sites, and do not share account passwords with counselors or agents.
