---
name: set-up-direct-deposit
domain: finance
locale: [generic]
interface: mixed
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Your employer or payer has verified bank instructions and will send future payments directly to your account.

## Preconditions

- You have a checking or savings account that accepts direct deposit.
- You can find the routing number, account number, account type, and bank name.
- You have access to the employer payroll portal or paper direct-deposit form.
- You understand whether you want the whole paycheck or a split amount deposited.

## Steps

1. **Get bank details from a trusted source.** Use your bank app, online banking, a void check, or bank letter. → *Expect:* routing and account numbers match the deposit account.
2. **Confirm account type.** Decide checking or savings and whether deposits are allowed. → *Expect:* the account type is clear.
3. **Open the payer's form.** [BRANCH: payroll portal | paper form | HR email process] → *Expect:* you have the official direct-deposit setup method.
4. **Enter bank information carefully.** Type routing number, account number, bank name, and account type exactly. → *Expect:* no digit is missing or transposed.
5. **Choose deposit allocation.** Select full net pay, fixed dollar amount, percentage, or remainder if splitting accounts. → *Expect:* the form shows where each portion will go.
6. **Attach proof if required.** Upload a void check, bank letter, or direct-deposit form from the bank. → *Expect:* the payer has documentation to verify the account.
7. **Submit and save confirmation.** Send the form and keep a screenshot, confirmation number, or copy. ⚠️ *Irreversible:* wrong account digits can send wages to the wrong place; verify every digit before submitting. → *Expect:* payroll marks the request received.
8. **Watch the first deposit.** Expect a prenote or one payroll-cycle delay, then verify the first actual deposit amount. → *Expect:* money lands in the intended account on payday.

## Decision points

- If the bank lists wire and ACH routing numbers, use the ACH or direct-deposit routing number.
- If splitting deposits, make one account the remainder account so rounding does not fail.
- If payday is soon, ask payroll whether the change will start this cycle or the next.
- If you are paid by a contractor platform, the setup may be in payout settings rather than HR payroll.

## Failure modes & recovery

- **F1 Wrong routing number:** detect payroll rejection or bank mismatch, recover by checking the bank's ACH routing number.
- **F2 Account number typo:** detect no deposit or returned deposit, recover by contacting payroll immediately with corrected details.
- **F3 Prenote delay mistaken for failure:** detect a zero-dollar test or skipped first cycle, recover by waiting the stated payroll timeline.
- **F4 Split allocation invalid:** detect percentages over 100 or no remainder, recover by simplifying to one full-deposit account.
- **F5 Old account still active:** detect payment to a previous account, recover by confirming effective date and closing old instructions after transition.

## Verification

The first real payment appears in the intended bank account for the expected amount, and the payroll portal or paystub lists the same direct-deposit account ending digits.

## Variations

- Paper forms: write clearly and attach a void check only if the payer requires it.
- Multiple jobs: set up direct deposit separately with each payer.
- Government benefits: use the agency's official portal or phone line, not a third-party ad.

## Safety & privacy

Medium risk because bank account numbers are sensitive. Use official payroll channels, avoid sending details over unsecured email when a portal exists, and verify first deposit before closing any old account.
