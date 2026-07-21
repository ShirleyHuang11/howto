---
name: read-a-payslip
domain: finance
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

You can walk your payslip from gross to net, name every deduction, confirm the figures are correct (including your tax code), and know how to escalate an error to payroll.

## Preconditions

- A payslip in hand: paper or the PDF/portal your employer provides.
- Your employment terms: agreed salary or hourly rate, contracted hours, and any benefits you signed up for (pension, insurance).
- The prior payslip, if you have one, so you can compare period to period.

## Steps

1. **Confirm the identity and period header.** Your name, employee/tax ID, and the pay period dates. Wrong period or ID means you may be reading someone else's or a duplicate. → *Expect:* header matches you and the current period.
2. **Read the gross pay.** This is total earnings before any deduction: base plus overtime, bonus, commission, allowances. Check it against your rate times hours, or salary divided by pay periods. → *Expect:* gross equals what your contract implies for this period.
3. **Walk each deduction line by line.** Typically: income tax, social/national insurance or payroll tax, pension contribution, and any voluntary items (health cover, union, salary-sacrifice). Know which are mandatory and which you opted into. → *Expect:* every deduction line identified as tax, statutory, or elective.
4. **Check the tax code or withholding setting.** A wrong tax code is the most common quiet error and silently over- or under-taxes you all year. Compare it to last period and to any code your tax authority issued. → *Expect:* the tax code matches your authority's notice; unchanged from last period unless you know why. Mismatch → F1.
5. **Verify pre-tax versus post-tax ordering.** Pension and salary-sacrifice items usually come off before tax is calculated, lowering taxable pay; confirm they reduced the taxed amount rather than being taken after. → *Expect:* pre-tax deductions visibly reduce the figure that tax is charged on.
6. **Arrive at net pay and match it to your bank.** Gross minus all deductions equals net (take-home). This number must equal the deposit that hits your account. → *Expect:* net on the slip equals the credit in your bank statement to the cent.
7. **Read the year-to-date totals.** The YTD columns accumulate gross, tax, and deductions across the tax year; a lurching YTD figure signals a one-off error earlier. → *Expect:* YTD roughly equals this period times periods elapsed.

## Decision points

- Net does not match the bank deposit → do not assume the bank is wrong; the slip and the payment come from the same run, so a mismatch means a correction or a split payment. Query payroll (F3).
- Gross is lower than expected → check for unpaid leave, a missed overtime claim, or a benefit newly deducted; identify the exact line before raising it.
- Tax code changed without notice → confirm with the tax authority first, because employers apply codes the authority issues; the fix may belong there, not with payroll.

## Failure modes & recovery

- **F1 Wrong tax code:** you are being taxed on the wrong basis; contact your tax authority to confirm the correct code, then give payroll the corrected code in writing. Overpaid tax is usually refunded; underpaid tax will be reclaimed, so fix it early.
- **F2 Missing or wrong hours/overtime:** compare to your own record; submit the discrepancy to payroll with dates and the timesheet, and expect a correction on the next run or an off-cycle adjustment.
- **F3 Net does not match the deposit:** email payroll with the slip's net, the deposited amount, and the date; keep it in writing so any correction is documented.
- **F4 A deduction you never authorized:** flag it immediately; unauthorized deductions from pay are unlawful in many jurisdictions and payroll must justify or reverse them.

## Verification

You can state your gross, name every deduction and whether it is mandatory or elective, the tax code matches your authority's record, and the net figure equals the amount deposited in your bank account.

## Variations

- `uk`: PAYE payslips show a tax code (e.g. 1257L) and National Insurance; a code ending oddly or starting BR/0T often signals emergency taxing worth querying.
- `us`: pay stubs show federal and state withholding driven by your W-4; adjust the W-4 rather than the stub if withholding is off.

## Safety & privacy

Medium risk: a payslip carries your name, tax ID, salary, and sometimes bank details, making it prime material for identity theft. Store it encrypted or locked, shred paper copies, and never send it unredacted over email or messaging when proving income; redact the ID and account numbers.
