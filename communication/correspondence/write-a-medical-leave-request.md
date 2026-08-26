---
name: write-a-medical-leave-request
domain: communication
subdomain: correspondence
locale: [generic, us]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You request medical leave from work in writing with the needed dates, documentation path, and privacy boundaries.

## Preconditions

- Employer leave policy, HR contact, and any required forms.
- Expected start date, estimated duration, and whether leave is continuous or intermittent.
- Healthcare provider documentation if required, without unnecessary diagnosis details.

## Steps

1. **Review employer policy and legal options.** Check sick leave, short-term disability, FMLA or local protected leave, accommodation procedures, and notice deadlines. → *Expect:* you know which process applies.
2. **Decide what to disclose.** Share that you need medical leave, not detailed diagnosis information, unless required on medical certification forms. → *Expect:* the request protects your privacy.
3. **Write the initial request.** Include start date, expected return or review date, intermittent schedule if known, and how urgent duties will be handled. → *Expect:* HR or your manager can route the request.
4. **Send to the correct recipient.** [BRANCH: policy says HR first, send HR and copy manager only as needed | policy says manager first, notify manager and ask for HR forms] → *Expect:* the request enters the official leave process.
5. **Submit required forms securely.** Provide medical certification to HR, leave administrator, or insurer, not broadly to coworkers. → *Expect:* documentation is received by the proper office.
6. **Confirm pay, benefits, and job-protection status.** Ask how leave affects salary, PTO, insurance premiums, disability benefits, and return-to-work requirements. → *Expect:* you know financial and administrative consequences.
7. **Get approval or next steps in writing.** ⚠️ *Irreversible:* before relying on leave protection, confirm approval, dates, and obligations in writing. → *Expect:* you have a written leave status.
8. **Keep updates limited and timely.** Provide required status updates or extension requests before deadlines. → *Expect:* the leave remains compliant with policy.

## Decision points

- The need is sudden or emergency-related → notify as soon as practicable and complete forms afterward.
- You may need intermittent leave → request that format specifically and document expected frequency if known.
- Employer denies or delays protected leave → ask for the denial reason in writing and consider legal, union, or government agency guidance.
- You need workplace changes after return → request accommodation separately through the employer's process.

## Failure modes & recovery

- **F1 Too much medical detail:** detect diagnosis or treatment details in a manager email → move details to HR forms and keep manager updates functional.
- **F2 Missing certification:** detect HR warning that forms are incomplete → ask what is missing and have the provider correct it promptly.
- **F3 Unclear leave dates:** detect confusion about start, return, or intermittent schedule → send a written clarification.
- **F4 Benefits surprise:** detect unpaid premiums or pay gap → contact HR/benefits immediately and ask for payment options or disability claim status.

## Verification

You have written confirmation showing the leave type, approved dates or review date, documentation status, pay or benefit handling, and required next update or return-to-work step.

## Variations

- `us`: FMLA generally applies only if the employer and employee meet eligibility rules; state paid leave and sick leave laws vary.
- `union`: collective bargaining agreements may add notice, seniority, pay, or grievance rights.
- Template:
  "I am requesting medical leave beginning [date] through approximately [date/review date].
  Please let me know the required forms and where my healthcare provider should send certification.
  I will coordinate transition of urgent work with [person/team] while protecting medical privacy."

## Safety & privacy

Medium risk because employment, income, benefits, and medical privacy are involved. Send medical documentation only through authorized channels, keep written confirmations, and verify deadlines before relying on leave protection.
