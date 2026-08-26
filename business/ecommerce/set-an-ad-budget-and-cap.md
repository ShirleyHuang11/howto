---
name: set-an-ad-budget-and-cap
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: basic
est_time: 20min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Set an ad budget and cap so a campaign can run without exceeding the business's approved spend limit.

## Preconditions

- Access to the ad platform and campaign settings.
- Approved maximum spend for the day, week, month, or promotion.
- Knowledge of whether the platform uses daily budgets, lifetime budgets, account caps, or insertion orders.

## Steps

1. **Identify the control level.** Locate account spend limits, campaign budgets, ad-set budgets, and billing thresholds. → *Expect:* you know which setting actually limits spend.
2. **Translate the approved budget.** Convert the total cap into daily or lifetime values using the campaign schedule. → *Expect:* a numeric budget that matches the approved cap.
3. **Set campaign or ad-set budget.** Enter the daily or lifetime budget in the appropriate field and confirm currency. → *Expect:* the campaign shows the intended budget value.
4. **Set an account-level cap if available.** Add a secondary spend limit for the billing account or campaign group. → *Expect:* a hard stop or alert exists above the campaign budget.
5. **Check pacing and overspend rules.** Read how the platform may spend above the daily average and compensate later. → *Expect:* you understand the maximum possible short-term spend.
6. **Save the settings.** ⚠️ *Irreversible:* active ads may spend immediately under the new cap, so confirm currency, schedule, and budget before saving. → *Expect:* the new budget is active or scheduled.
7. **Set monitoring alerts.** Create platform, analytics, or finance alerts at 50%, 80%, and 100% of the cap. → *Expect:* someone will be notified before the budget is exhausted.

## Decision points

- Platform can exceed daily budget temporarily → use lifetime budget or account cap for strict promotions.
- Multiple ad sets share one campaign budget → confirm priority before using campaign budget optimization.
- Currency differs from finance approval → convert and document the exchange rate used.

## Failure modes & recovery

- **F1 Decimal or currency error:** detect spend far above expectation → pause campaigns and correct the budget immediately.
- **F2 Cap set at wrong level:** detect another campaign still spending → apply account-level limit or pause unrelated campaigns.
- **F3 Budget resets after duplication:** detect copied campaign with default budget → audit duplicated entities before launch.
- **F4 Alert not received:** detect no notification at threshold → add email recipients and a manual daily spend check.

## Verification

The active campaign and any account-level control show budget values that keep maximum spend at or below the approved cap, and alerting is configured for spend thresholds.

## Variations

- `google-ads`: daily budgets may overdeliver on individual days while respecting monthly charging limits.
- `meta-ads`: campaign and ad-set budget optimization change where the cap is enforced.

## Safety & privacy

Medium risk because a wrong number can spend real money. Confirm currency, decimal placement, campaign scope, and schedule before saving budget changes.
