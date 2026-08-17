---
name: howto-money-starter
description: Take control of your money — budget, bank, build credit, don't get burned. Verified howto recipes for: Money Starter.
---

# Money Starter — howto skill

Take control of your money — budget, bank, build credit, don't get burned.

When the user needs any task below, follow its verified steps in order. Each step's **Expect** is the observation that confirms it worked; steps marked ⚠ are irreversible — confirm before doing them. For the full recipe (decision points, failure recovery, variations) use the howto MCP `get_howto(<id>)` or read the linked source.

## create a simple budget  
`finance/create-a-simple-budget`

**Goal:** You have a written monthly budget where income minus fixed costs leaves a known amount, that amount is split into a few spending caps, and a short weekly check keeps you inside them.

1. **Write down net monthly income.** Use what actually lands in the account, after tax and deductions. Irregular income: use the lowest of the last three months, not the average.  → *Expect:* one income number you would bet on.
2. **List fixed costs and total them.** Rent/mortgage, utilities, insurance, loan and phone payments, subscriptions. Pull them straight off statements so none are forgotten.  → *Expect:* a fixed-cost total; every line traceable to a real transaction.
3. **Compute the leftover.** Income minus fixed costs. This is what is genuinely yours to allocate.  → *Expect:* a positive number. Zero or negative → F1.
4. **Carve out savings first, before spending caps.** Move a fixed slice (even 5-10%) to the top, treated like a bill, not what happens to survive the month.  → *Expect:* a savings figure subtracted from the leftover.
5. **Split the rest into a few category caps.** Keep it to 4-6 buckets (groceries, transport, eating out, everyday/fun). Fewer buckets get followed; twenty do not.  → *Expect:* caps summing to the post-savings leftover, no bucket left uncovered.
6. **Set up the weekly check ritual.** Pick a fixed 10-minute slot (Sunday works). Open the app/statement, tally the week's spend per bucket, compare to a quarter of each cap.  → *Expect:* a recurring calendar reminder and a first tally done.
7. **Adjust caps after one real month, not mid-week.** If groceries always overrun and eating-out is always under, move the money between them. The budget serves you.  → *Expect:* month-two caps that match how you actually live.

**Done when:** A written budget exists where income minus fixed costs minus savings equals the sum of your category caps, and at least one weekly check has been completed with actual spend compared against the caps.

## open a bank account  
`finance/open-a-bank-account`

**Goal:** A current/checking account is open in your name at a bank you chose deliberately, with the card, online access, and any direct deposits or payments pointed at it.

1. **Choose the bank on fees and fit, not proximity nostalgia.** Compare three candidates on: monthly fee and how to waive it, ATM network, foreign transaction fees if you travel, app quality, and branch access if you value it. Online-only banks win on fees; branch banks win when you need a human.  → *Expect:* one chosen bank and a named account type, with its fee schedule actually read.
2. **Gather the exact document list from the bank's site.** Newcomers: check which proofs of address are accepted before showing up; this is the step that fails immigrants and students most often, and some banks explicitly accept alternatives (employer letters, university letters).  → *Expect:* every listed document in hand, originals where required.
3. **Apply online or book a branch appointment.** Online flows verify identity by document photo and a selfie or video call; branch flows do it at the desk. Answer the regulatory questions (occupation, source of funds, tax residency) accurately. They are legally required, not curiosity.  → *Expect:* an application submitted and an account number issued, sometimes instantly, sometimes after a review of days.
4. **Complete the security setup the moment access arrives.** Set the online banking credentials from the bank's official app or site, enable the strongest offered 2FA, and store everything in your password manager (`accounts/enable-two-factor-authentication` applies in full).  → *Expect:* you can log in, see the empty account, and the recovery paths point at you.
5. **Activate the card when it arrives and set the PIN.** Follow the mailed or in-app activation; test with one small purchase or an ATM balance check (`daily/errands/use-an-atm`).  → *Expect:* a working card with a PIN only you know.
6. ⚠ **Point your money at the account.** Salary: give the account details to payroll. Recurring payments: move them over deliberately, one list, one session (`finance/pay-a-bill-online` for each). Fund it with an initial transfer. ⚠️ *Irreversible:* typos in account numbers on inbound transfers are painful to unwind, so copy-paste details from the app rather than retyping.  → *Expect:* a test deposit lands, and the payment list shows what moved and what remains.
7. **If this replaces an old account, run both in parallel for one full billing cycle.** Watch what still hits the old account, migrate the stragglers, then close the old one properly rather than leaving it to rot (`accounts/delete-an-account` logic applied to banking: get written confirmation of closure).  → *Expect:* a clean cutover with no bounced payment in the gap.

**Done when:** You can log in with 2FA, the card works, a test deposit arrived, the fee waiver condition is understood and met, and either no old account exists or it survived a full parallel cycle and was closed with confirmation.

## build an emergency fund  
`finance/build-an-emergency-fund`

**Goal:** You have a separate account holding a target number of months of essential expenses, fed by an automatic transfer, kept apart from daily spending, and used only for genuine emergencies.

1. **Compute one month of essentials.** Sum only what you must pay to keep living: housing, food, utilities, insurance, minimum debt, transport. Exclude discretionary spending.  → *Expect:* a monthly essentials number smaller than your total spending.
2. **Set the target in months.** Stable single income, few dependents: 3 months. Variable income, dependents, or sole earner: 6 months or more. Multiply essentials by the chosen count.  → *Expect:* a target fund size with an explicit rationale.
3. **Set a starter milestone first.** A full fund is daunting; aim for one small round figure (one month, or a fixed starter amount) as the first goal so momentum is visible.  → *Expect:* a near-term milestone you can reach in weeks, not years.
4. **Open a separate account for it.** A distinct high-yield savings account, not a sub-label inside your checking account. Friction is the feature: it should take a day, not a tap, to reach.  → *Expect:* a new account with a zero or starter balance, kept off your everyday card.
5. **Automate the transfer on payday.** Schedule a standing transfer for the day after income lands, so the money leaves before you can spend it. Start with an amount you will not miss and raise it later.  → *Expect:* a recurring transfer confirmed; the first one executes next payday.
6. **Let it grow untouched and review quarterly.** Do not check it daily or move it into anything illiquid. Every quarter, recompute essentials (rent rises) and nudge the transfer up.  → *Expect:* balance climbing each month; target adjusted for cost-of-living changes.
7. **Define what counts as an emergency, in writing.** Job loss, urgent medical bills, essential home or car repair. A sale is not an emergency. Writing the rule now prevents rationalizing later.  → *Expect:* a short written list of qualifying uses.
8. ⚠ **Refill after any use.** ⚠️ *Irreversible:* spending the fund is the point, but treat replenishment as the next priority: restart or raise the transfer until it is back to target.  → *Expect:* after a withdrawal, the automatic transfer resumes toward the target.

**Done when:** A separate account holds at least your starter milestone (and is climbing toward the month-based target), an automatic payday transfer is active, and you have a written definition of what the fund may be used for.

## check your credit report  
`finance/check-your-credit-report`

**Goal:** Review your credit report for accuracy, understand which items help or hurt credit, and start disputes for errors or signs of identity theft.

1. **Use the official free source.** Go to the government-approved or bureau-approved free annual credit report site, not an ad or paid monitoring page.  → *Expect:* you can request reports without buying a score or subscription.
2. **Request the right bureau reports.** Choose one or all available credit bureaus depending on your review plan.  → *Expect:* you know which bureau's file you are reading.
3. **Verify identity carefully.** Answer identity questions and avoid guessing if a question appears unfamiliar.  → *Expect:* the report opens or gives a clear next step for manual verification.
4. **Save the report securely.** Download or print the report to a private location before leaving the session.  → *Expect:* you can review it later without logging in again.
5. **Read personal information.** Check name variations, addresses, employers, birth date, and identity numbers where shown.  → *Expect:* old but accurate history is separated from wrong or suspicious identity data.
6. **Review account sections.** Check each loan, card, balance, limit, payment status, open date, closed date, and ownership type.  → *Expect:* every account is yours and reported accurately.
7. **Review inquiries and public records.** Look for recent hard inquiries, collections, bankruptcies, judgments where applicable, or other negative items.  → *Expect:* unfamiliar or outdated items are marked for action.
8. **Classify what helps and hurts.** Identify on-time payments, low balances, long account history, and healthy account mix as helpful; late payments, high utilization, collections, defaults, and unnecessary hard inquiries as harmful.  → *Expect:* you know which items affect creditworthiness.
9. **Dispute errors.** [BRANCH: bureau error | creditor error] submit a bureau dispute for wrong report data; contact the creditor or collector when the source is reporting bad information.  → *Expect:* you receive a confirmation number or written dispute record.
10. **Set a review frequency.** Schedule periodic checks, commonly at least annually and more often after identity theft, denied credit, major loans, or disputes.  → *Expect:* the next review date is on your calendar.

**Done when:** Each available report has been saved, personal data and account sections have been reviewed, errors are either absent or disputed, and the next review date is scheduled.

## pay a bill online  
`finance/pay-a-bill-online`

**Goal:** A due bill (utility, phone, credit card, rent) is paid online before its due date, with a confirmation number saved.

1. **Read the bill.** Note amount due, due date, account/customer number, and whether the amount looks normal for the season.  → *Expect:* you can state amount, date, and account number; anomalies (double last month's?) get investigated before paying.
2. **Choose the payment channel.** [BRANCH: biller's own portal | your bank's bill-pay | wallet/payment app] First time on a biller portal: reach it by typing the URL from the paper bill, never from an email link.  → *Expect:* you are logged in at the correct channel (`accounts/log-in`).
3. **Locate the bill in the portal.** Billing/Payments section → current statement.  → *Expect:* portal's amount due and due date match the bill in hand; mismatch → F1.
4. **Enter payment details.** Select or add the funding source; enter/confirm the amount — pay the statement balance unless intentionally paying partial.  → *Expect:* a review screen: payee, amount, funding source, payment date.
5. **Check the scheduled date lands on or before the due date.** Bank bill-pay may take 1–3 business days to deliver — schedule accordingly.  → *Expect:* delivery/processing date ≤ due date.
6. ⚠ **Confirm the payment.** ⚠️ *Irreversible:* online payments to billers are hard to recall once processed — verify payee and amount on the review screen now.  → *Expect:* a confirmation screen with a confirmation/reference number.
7. **Save the confirmation.** Screenshot or note the number with the date.  → *Expect:* confirmation stored; an email receipt typically follows.
8. **Verify settlement within a few days.** Bank statement shows the debit; biller portal shows balance cleared.  → *Expect:* exactly one debit of the right amount; biller balance updated.

**Done when:** The confirmation number is saved, the funding account shows exactly one debit for the intended amount, and the biller's portal shows the balance paid with no late flag by the due date.

## set up autopay  
`digital/set-up-autopay`

**Goal:** Autopay is enabled for a bill with the right payment source, amount rule, due-date buffer, and monitoring so payments happen without overdrafts or missed bills.

1. **Open the biller's billing page directly.** Use a bookmark, typed address, or the biller's app.  → *Expect:* the account shows your current balance and due date.
2. **Choose the payment source deliberately.** Prefer a source with predictable funds and no processing fee; avoid debit if overdraft risk is high.  → *Expect:* you know the source, fees, and whether the biller stores it.
3. **Pick the amount rule.** [BRANCH: full balance | statement balance | minimum due | fixed amount] Choose the smallest rule that still meets your goal without creating debt or late fees.  → *Expect:* the autopay setup page shows the chosen rule in plain language.
4. **Set a safe payment date.** Schedule payment several days before the due date while leaving enough paycheck or account buffer to avoid overdraft.  → *Expect:* the payment date, due date, and funding date make sense together.
5. **Enter and verify payment details.** Type routing/account or card numbers carefully, then compare the last four digits and billing address.  → *Expect:* the saved payment method shows the expected institution and last four digits.
6. ⚠ **Confirm autopay enrollment.** ⚠️ *Irreversible:* an authorized autopay can pull money automatically, so confirm amount rule, account, and date before enabling.  → *Expect:* status changes to autopay on, enrolled, or automatic payments enabled.
7. **Save the confirmation.** Screenshot or download the autopay page showing amount rule, payment source, and first scheduled date.  → *Expect:* proof exists outside the biller site.
8. **Verify the first run.** Check both the biller and payment account after the first scheduled payment.  → *Expect:* the biller marks paid and the payment account shows one matching debit or charge.
9. **Monitor monthly.** Keep statement alerts on even after autopay works.  → *Expect:* you receive bill amount and payment posted notifications.

**Done when:** Autopay status is active, first scheduled payment posts once to the biller and payment source, and alerts remain enabled for future bills.

## track your spending  
`finance/track-your-spending`

**Goal:** Record and review spending clearly enough to see where money goes and choose specific changes.

1. **Pick one method.** [BRANCH: app | spreadsheet | envelope] choose an app for automation, a spreadsheet for control, or envelopes for cash limits.  → *Expect:* one system is selected before you start categorizing.
2. **List all spending sources.** Include checking, credit cards, cash, payment apps, subscriptions, and shared bills.  → *Expect:* no regular payment path is missing.
3. **Create practical categories.** Use categories such as housing, groceries, transport, eating out, subscriptions, health, debt, gifts, and fun.  → *Expect:* every transaction has an obvious place.
4. **Enter the last 30 days.** Import or type transactions, then split mixed purchases only when the split changes decisions.  → *Expect:* one month of spending is visible in the chosen system.
5. **Mark fixed and flexible costs.** Separate rent, insurance, and debt from groceries, dining, rides, shopping, and subscriptions.  → *Expect:* you can see which costs can change soon.
6. **Find the leaks.** Sort categories from largest to smallest and look for repeated small charges, unused subscriptions, fees, and impulse purchases.  → *Expect:* at least one specific spending leak is named.
7. **Set a weekly review.** Put a recurring 15 minute calendar block to update transactions and compare against your target.  → *Expect:* the next review has a date and time.
8. **Choose one adjustment.** Pick a measurable change, such as canceling one subscription or setting a dining-out cap.  → *Expect:* the tracking leads to an action, not just a report.

**Done when:** At least 30 days of spending is categorized, a weekly review is scheduled, and one named spending leak has a concrete action assigned.

## dispute a card charge  
`finance/dispute-a-card-charge`

**Goal:** An incorrect, fraudulent, or undelivered-goods charge on your card is formally disputed, and the dispute is tracked to a credit or a justified rejection.

1. **Classify the charge.** [BRANCH: fraud (you never transacted) → skip to step 3 | merchant error (wrong amount, duplicate, goods not delivered/not as described) → step 2] Decode the merchant string first — many "unknown" charges are legitimate with unfamiliar billing names; search the string before crying fraud.  → *Expect:* a confident classification.
2. **Attempt merchant resolution and document it.** Contact merchant support, state the problem, request a refund; save the ticket/emails and give them the stated response window.  → *Expect:* either a refund (done once it posts on a statement; no dispute is filed) or a documented refusal/non-response, which the dispute will require.
3. **For fraud: freeze the card immediately.** In the banking app: lock/freeze the card, then request a replacement.  → *Expect:* card locked; further charges impossible.
4. **Open the dispute with the issuer.** Banking app/site → the transaction → "Dispute charge", or call the number on the card. Provide the classification, the story, and upload the evidence from steps 1–2.  → *Expect:* a dispute case number and a stated timeline.
5. **Answer follow-up requests promptly.** Issuers may mail/message questionnaires; missing their deadlines forfeits the dispute.  → *Expect:* every issuer request answered within its window; case shows "under review".
6. **Track the provisional credit.** Many issuers credit the amount provisionally during investigation.  → *Expect:* a provisional credit line on the statement (not guaranteed in all jurisdictions).
7. **Receive the outcome.** *Note:* a first credit is not final. A resolved-in-your-favor dispute can still be reversed if the merchant provides counter-evidence, so keep your evidence until the written final-resolution notice.  → *Expect:* written resolution: permanent credit, or rejection with reasons.
8. **If rejected and you disagree: escalate.** Request the merchant's counter-evidence, rebut in writing, and if the issuer won't move, complain to the financial regulator/ombudsman for your jurisdiction.  → *Expect:* an escalation case with its own timeline.

**Done when:** Either the merchant's refund posted on a statement with no dispute needed, or the dispute case shows final resolution: a permanent credit for the full disputed amount (or a reasoned rejection you accepted). For fraud cases, the compromised card is dead and its recurring billers migrated.

## understand your credit score  
`finance/understand-your-credit-score`

**Goal:** You know what your credit score is, which behaviors move it, where to check it for free without harming it, and the real steps that repair it over time (not the myths).

1. **Get your score and report for free.** Use a bureau's statutory free report or a reputable free score service. Checking your own is a "soft" inquiry and never lowers your score.  → *Expect:* a current score plus the full report behind it.
2. **Read the report for errors first.** Wrong balances, accounts you never opened, a debt already paid still shown as owing, or an address that is not yours. Errors are common and drag the score.  → *Expect:* every account and inquiry recognized, or an error list to dispute (F1).
3. **Learn the levers that actually move it.** In rough order of weight: payment history (pay on time, always), amounts owed (keep balances low relative to limits), length of history, credit mix, and new applications.  → *Expect:* you can name your weakest lever from your own report.
4. **Fix utilization, the fastest legitimate lever.** Keep balances well under your limits (a common guideline is under 30%, lower is better). Paying a card down before its statement date lowers the reported balance.  → *Expect:* reported balances that are a small fraction of limits.
5. **Automate on-time payments.** One missed payment can dent a score for years; set autopay for at least the minimum on every account so a busy month never becomes a late mark.  → *Expect:* autopay active on every credit account.
6. **Space out new applications.** Each formal application is a "hard" inquiry that dips the score slightly; several in a short window reads as distress. Apply only when needed.  → *Expect:* no unnecessary hard inquiries planned.
7. **Discard the myths.** Checking your own score does not hurt it; carrying a balance to "build credit" is false and just costs interest; closing an old card can hurt by shortening history and cutting available credit.  → *Expect:* you can refute each myth. ⚠️ *Irreversible:* do not close your oldest account to tidy up; the lost history and limit can drop the score for years.
8. **Re-check periodically and after big steps.** Look again in a few months, and before any major application (mortgage, loan).  → *Expect:* a trend line over time, not a single snapshot.

**Done when:** You have retrieved your score and full report for free, every account and inquiry on it is recognized (or under dispute), you can name the levers moving your score and refute the common myths, and on-time autopay plus low utilization are in place.

## set up direct deposit  
`finance/set-up-direct-deposit`

**Goal:** Your employer or payer has verified bank instructions and will send future payments directly to your account.

1. **Get bank details from a trusted source.** Use your bank app, online banking, a void check, or bank letter.  → *Expect:* routing and account numbers match the deposit account.
2. **Confirm account type.** Decide checking or savings and whether deposits are allowed.  → *Expect:* the account type is clear.
3. **Open the payer's form.** [BRANCH: payroll portal | paper form | HR email process]  → *Expect:* you have the official direct-deposit setup method.
4. **Enter bank information carefully.** Type routing number, account number, bank name, and account type exactly.  → *Expect:* no digit is missing or transposed.
5. **Choose deposit allocation.** Select full net pay, fixed dollar amount, percentage, or remainder if splitting accounts.  → *Expect:* the form shows where each portion will go.
6. **Attach proof if required.** Upload a void check, bank letter, or direct-deposit form from the bank.  → *Expect:* the payer has documentation to verify the account.
7. ⚠ **Submit and save confirmation.** Send the form and keep a screenshot, confirmation number, or copy. ⚠️ *Irreversible:* wrong account digits can send wages to the wrong place; verify every digit before submitting.  → *Expect:* payroll marks the request received.
8. **Watch the first deposit.** Expect a prenote or one payroll-cycle delay, then verify the first actual deposit amount.  → *Expect:* money lands in the intended account on payday.

**Done when:** The first real payment appears in the intended bank account for the expected amount, and the payroll portal or paystub lists the same direct-deposit account ending digits.

## 🗺️ get out of debt (journey)  
`journeys/get-out-of-debt`

A long-horizon plan spanning this whole area — read `journeys/get-out-of-debt.md` or ask the howto MCP. Mind the gates and re-plan triggers.

