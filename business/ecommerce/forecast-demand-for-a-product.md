---
name: forecast-demand-for-a-product
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You forecast expected product demand for a defined future period so purchasing, staffing, and marketing decisions have a measurable baseline.

## Preconditions

- Historical sales, inventory availability, price, promotion, and traffic data for the product or comparable products.
- Known future events such as promotions, seasonality, launches, or supply limits.
- A forecast horizon such as next week, month, or quarter.

## Steps

1. **Define the forecast scope.** Select SKU, channel, geography, and date range. → *Expect:* one forecast target with a clear horizon and unit of measure.
2. **Clean the historical data.** Remove canceled orders, test orders, stockout-constrained periods, and one-time anomalies unless they will repeat. → *Expect:* a usable historical demand series.
3. **Establish a baseline.** Calculate average demand over comparable recent periods, adjusting for day-of-week or seasonality. → *Expect:* a baseline units-per-period estimate.
4. **Account for known drivers.** Add expected effects from promotions, price changes, email campaigns, holidays, ad spend, or product-page changes. → *Expect:* documented upward or downward adjustments.
5. **Check supply constraints.** Note current inventory, inbound stock, supplier lead time, and maximum fulfillable units. → *Expect:* the forecast distinguishes unconstrained demand from sellable supply.
6. **Create low, expected, and high scenarios.** Use conservative, most-likely, and aggressive assumptions. → *Expect:* a demand range rather than a single fragile number.
7. **Compare to purchasing needs.** Translate forecast into reorder quantity, safety stock, or production requirement. → *Expect:* a replenishment recommendation tied to the forecast.
8. **Share and timestamp the forecast.** Save assumptions, data source, owner, and creation date. → *Expect:* stakeholders can audit why the forecast was made.
9. **Reconcile actuals after the period.** Compare forecast to real demand and record error. → *Expect:* future forecasts improve from measured variance.

## Decision points

- Product had stockouts → estimate lost demand or use traffic/waitlist signals to avoid underforecasting.
- Product is new → use comparable SKUs, waitlist size, ad tests, or preorder data.
- Promotion is planned → forecast promo and non-promo demand separately.

## Failure modes & recovery

- **F1 Forecast uses sales instead of demand:** detect inventory outages during the history window → adjust for lost sales.
- **F2 One-time spike treated as normal:** detect influencer, press, or clearance event → separate anomaly from baseline.
- **F3 Ignoring price changes:** detect future price differs from historical price → apply elasticity or use comparable periods.
- **F4 No postmortem:** detect repeated forecast misses without review → add forecast-error tracking after every horizon.

## Verification

The product has a timestamped demand forecast for a defined period with low, expected, and high unit estimates, documented assumptions, and a resulting purchasing or inventory recommendation.

## Variations

- Seasonal apparel: forecast by size and color, not only style total.
- Consumables: include subscription renewals and reorder cadence.
- Marketplace channels: separate organic marketplace demand from owned-site demand.

## Safety & privacy

Medium risk because forecasts drive purchasing commitments and may use customer/order data. Use aggregated data where possible, protect sales reports, and require approval before buying inventory based on the forecast.
