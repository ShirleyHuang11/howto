---
name: file-a-simple-tax-return
domain: finance
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Prepare and file a simple tax return with the required income forms, basic deductions or credits, and records saved for future proof.

## Preconditions

- Tax year and filing jurisdiction are known.
- Government tax ID or taxpayer number.
- Wage, interest, unemployment, retirement, or other income forms.
- Records for basic deductions, credits, withholding, and estimated payments.
- Bank account details if using direct deposit or direct debit.

## Steps

1. **Confirm the filing deadline.** Check the official tax agency calendar for the tax year and your jurisdiction. → *Expect:* you know the due date and extension rules.
2. **Gather tax documents.** Collect wage statements, interest forms, retirement forms, unemployment forms, tuition or childcare forms, and prior-year return if useful. → *Expect:* all expected documents are in one folder.
3. **Choose filing method.** [BRANCH: reputable tax software | official free filing | paper forms | tax preparer] Pick the simplest method allowed for your situation. → *Expect:* you have a trusted filing path ready.
4. **Enter personal information.** Add legal name, tax ID, address, filing status, dependents, and bank details carefully. → *Expect:* the software or form accepts identity fields without errors.
5. **Enter income forms.** Copy employer, payer, income, withholding, and account numbers exactly from each form. → *Expect:* totals match the source forms.
6. **Review deduction basics.** Compare standard deduction or default allowance against any simple itemized deductions the software supports. → *Expect:* the selected deduction method is shown and explained.
7. **Check credits and payments.** Add withholding, estimated payments, education, child, retirement saver, or other simple credits only if you have support. → *Expect:* refund or balance due updates after each entry.
8. **File and pay or request refund.** Review the return, then e-file or mail it. ⚠️ *Irreversible:* once accepted, corrections usually require an amended return, so review names, IDs, income, and bank numbers first. → *Expect:* you receive an e-file acceptance, mailing proof, refund status, or payment confirmation.
9. **Keep records.** Save the filed return, all forms, receipts, software confirmation, and payment proof. → *Expect:* a complete tax-year folder is stored securely.

## Decision points

- Self-employment, rental income, crypto, foreign accounts, major stock sales, or business expenses → get qualified help.
- Missing a tax form → download it from the payer or wait before filing.
- Cannot pay full balance → file on time anyway and request a payment plan.
- Need more time to prepare → file an extension if available, but remember payment may still be due.
- Refund looks too large or too small → compare against withholding and prior-year return before submitting.

## Failure modes & recovery

- **F1 Missing income form:** detect payer income not entered; recover by obtaining the form or transcript before filing.
- **F2 Rejected e-file:** detect agency rejection code; recover by correcting the named field and resubmitting.
- **F3 Wrong bank number:** detect account details error before acceptance; recover by correcting before filing or contacting the agency after rejection.
- **F4 Underpayment:** detect balance due you cannot pay; recover by filing anyway and arranging payment.
- **F5 Complex issue discovered:** detect schedules or questions you do not understand; recover by pausing and using official help or a credentialed preparer.

## Verification

The tax agency or filing software shows the return was accepted or mailed with proof, and your saved folder contains the filed return plus source documents.

## Variations

- `us`: IRS Free File, state returns, and local returns may be separate.
- `employee-only`: wage statements and standard deduction often keep the return simple.
- `student`: tuition forms and education credits may apply.
- `retired`: pension and social benefit tax rules can vary.
- `paper-filing`: use certified mail or tracked delivery when available.

## Safety & privacy

Tax returns contain identity, income, dependent, and bank data. Use official sites or reputable software, avoid public Wi-Fi, and store records in a private encrypted or locked location.
