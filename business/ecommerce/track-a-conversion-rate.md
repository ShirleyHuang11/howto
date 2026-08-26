---
name: track-a-conversion-rate
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

You measure the percentage of visitors who complete a defined ecommerce action, using a consistent event, time window, and denominator.

## Preconditions

- Access to store analytics, web analytics, or tag manager.
- A defined conversion action such as purchase, checkout started, lead submitted, or waitlist joined.
- Permission to process analytics data under the site's privacy policy.

## Steps

1. **Choose one conversion event.** Define the exact success action and avoid mixing purchases with softer events. → *Expect:* a named event such as `purchase_completed` or `email_signup`.
2. **Define the audience denominator.** Choose sessions, users, product-page visitors, or campaign clicks depending on the question. → *Expect:* a clear formula: conversions divided by the selected visitor count.
3. **Set the measurement window.** Pick dates, time zone, and attribution lookback, excluding abnormal outages if documented. → *Expect:* all reports use the same date range and time zone.
4. **Verify event firing.** Complete a test action or inspect recent events to confirm the conversion event fires once per success. → *Expect:* the analytics event appears with correct timestamp and revenue or item metadata if relevant.
5. **Filter internal and invalid traffic.** Exclude staff IPs, test orders, bot traffic, and duplicate transactions where the platform supports it. → *Expect:* the dataset reflects real customer behavior.
6. **Calculate the rate.** Divide conversions by the selected denominator and record the raw counts beside the percentage. → *Expect:* a conversion rate with both numerator and denominator visible.
7. **Segment the result.** Compare by channel, device, landing page, product, or new/returning customer. → *Expect:* at least one segment reveals where performance differs materially.
8. **Create a recurring report.** Save a dashboard, scheduled email, or spreadsheet tab with the formula and source. → *Expect:* the same metric can be refreshed without redefining it.
9. **Annotate changes.** Record promotions, site releases, pricing changes, and tracking updates that affect comparability. → *Expect:* future rate changes have operational context.

## Decision points

- Purchase volume is low → use a longer window or track checkout-start rate as a leading indicator.
- Analytics and platform orders disagree → use the store backend for financial truth and analytics for behavior trends.
- Consent mode blocks some tracking → report modeled or consented-only data explicitly.

## Failure modes & recovery

- **F1 Double-counted conversions:** detect more purchase events than real orders → deduplicate by order ID or fix the event trigger.
- **F2 Broken tracking after a theme change:** detect conversion rate dropping to zero while orders continue → inspect tag placement and checkout permissions, then replay a test order.
- **F3 Wrong denominator:** detect a rate that combines campaign clicks with all-site conversions → rebuild the report around matched source and conversion scope.
- **F4 Test orders polluting data:** detect staff transactions in reports → filter them out and document the exclusion rule.

## Verification

The report shows a conversion rate for a named event, date range, time zone, numerator, denominator, and data source, and the conversion count reconciles with the underlying order or event log within an accepted tolerance.

## Variations

- Google Analytics 4: use key events and compare with ecommerce purchases by transaction ID.
- Shopify analytics: use online store conversion rate for store sessions, not all marketing clicks.
- Server-side tracking: verify event delivery and deduplication keys across browser and server events.

## Safety & privacy

Medium risk because analytics may involve customer identifiers and revenue data. Respect consent settings, avoid exporting unnecessary personal data, and do not make financial decisions from a metric whose event firing has not been verified.
