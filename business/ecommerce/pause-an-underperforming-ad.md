---
name: pause-an-underperforming-ad
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

Pause an ad that is missing its performance target while preserving enough data to diagnose or relaunch it later.

## Preconditions

- Access to the ad platform and reporting dashboard.
- A defined performance threshold, such as ROAS, CPA, conversion rate, or spend without sales.
- Enough delivery data to make a decision.

## Steps

1. **Open the campaign report.** Filter to the relevant date range, attribution setting, campaign, ad set, and ad. → *Expect:* performance metrics for the exact ad being evaluated.
2. **Compare against the stop rule.** Check spend, conversions, revenue, CPA, ROAS, CTR, and frequency against the target. → *Expect:* the ad clearly passes or fails the rule.
3. **Check tracking before acting.** Confirm conversion tags and revenue reporting are working so the ad is not falsely blamed. → *Expect:* tracking status is healthy or the issue is identified.
4. **Record the current state.** Save or export metrics, creative, audience, budget, and learning status. → *Expect:* there is a snapshot for later analysis.
5. **Pause the ad.** ⚠️ *Irreversible:* pausing can disrupt learning and delivery, so confirm the selected entity is the underperforming ad, not the whole account. → *Expect:* the ad status changes to paused and spend stops for that ad.
6. **Check related budgets.** Confirm the budget does not simply shift to an equally poor ad unless that is intended. → *Expect:* remaining spend is assigned to acceptable campaigns or held.
7. **Document the next test.** Note whether to revise creative, audience, landing page, bid, or offer before relaunch. → *Expect:* the paused ad has a clear follow-up action.

## Decision points

- Tracking is broken → fix tracking before judging performance.
- Ad is new with too little spend → wait until the minimum data threshold is met.
- Campaign has a hard deadline → pause faster if spend threatens the cap.

## Failure modes & recovery

- **F1 Wrong ad paused:** detect a strong ad stopped by mistake → re-enable it and note the interruption.
- **F2 Spend continues:** detect charges after pause → check campaign, ad set, duplicated ads, and billing delay.
- **F3 Learning reset:** detect relaunch performance volatility → duplicate only when needed and expect a new learning period.
- **F4 Budget shifts badly:** detect remaining ads consuming spend with worse results → pause at the ad-set or campaign level.

## Verification

The specific underperforming ad status is paused, its spend is no longer increasing after platform reporting delay, and its metrics snapshot is saved with the reason for pausing.

## Variations

- `google-ads`: labels and experiments can preserve test context before pausing.
- `meta-ads`: pause at ad, ad set, or campaign level depending on where budget is controlled.

## Safety & privacy

Medium risk because pausing affects paid acquisition and spend allocation. Verify the selected ad ID and budget behavior before changing status.
