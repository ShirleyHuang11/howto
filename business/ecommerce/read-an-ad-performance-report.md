---
name: read-an-ad-performance-report
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Read an ad performance report and decide whether the campaign is profitable, needs adjustment, or should be paused.

## Preconditions

- Access to ad platform reports, ecommerce revenue data, and attribution settings.
- A target CPA, ROAS, or profit contribution threshold.
- Known product margins and average fulfillment costs.

## Steps

1. **Set the reporting window.** Choose a date range long enough for attribution delay and matching the campaign objective. → *Expect:* report data covers the intended evaluation period.
2. **Confirm metric definitions.** Check attribution window, conversion event, revenue source, currency, and whether refunds are included. → *Expect:* metrics are comparable to the business target.
3. **Review spend and delivery.** Read impressions, reach, frequency, clicks, CPM, CPC, and total spend. → *Expect:* you know whether the campaign is getting enough traffic.
4. **Review conversion outcomes.** Read orders, revenue, CPA, ROAS, conversion rate, and average order value. → *Expect:* sales performance is visible for each campaign or ad.
5. **Calculate contribution profit.** Subtract ad spend, product cost, payment fees, fulfillment, and expected returns from attributed revenue. → *Expect:* each campaign is classified as profitable, break-even, or losing money.
6. **Segment by useful dimensions.** Compare creative, audience, product, placement, device, region, and new-versus-returning customers. → *Expect:* the strongest and weakest segments are identifiable.
7. **Decide the action.** [BRANCH: scale | hold | revise | pause] Tie the action to the target metric and confidence level. → *Expect:* every campaign has a documented next action.

## Decision points

- ROAS looks good but margin is low → use contribution profit, not revenue-only ROAS.
- Data volume is small → wait or combine similar ad sets before making a major decision.
- Platform revenue disagrees with store revenue → investigate attribution and deduplication before scaling.

## Failure modes & recovery

- **F1 Duplicate conversions:** detect reported orders above store orders → inspect pixel and conversion API deduplication.
- **F2 Attribution lag:** detect recent purchases arriving late → use a longer window or exclude the last few days.
- **F3 Refund blind spot:** detect high returns after profitable reports → include refund rate in contribution calculations.
- **F4 Blended spend confusion:** detect organic or email sales credited to ads → compare incrementality tests or holdout periods.

## Verification

The report identifies spend, revenue, CPA or ROAS, contribution profit, and a documented scale, hold, revise, or pause decision for each evaluated campaign.

## Variations

- `google-ads`: segment Shopping reports by product ID and search term where available.
- `meta-ads`: compare platform attribution with store analytics because view-through attribution can inflate results.

## Safety & privacy

Medium risk because decisions can increase spend. Do not scale based only on vanity metrics; include costs, refunds, and attribution limitations.
