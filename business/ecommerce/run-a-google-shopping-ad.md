---
name: run-a-google-shopping-ad
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Launch a Google Shopping campaign for eligible products with a controlled budget, valid feed, and measurable conversion tracking.

## Preconditions

- Google Merchant Center and Google Ads access.
- Approved product feed with prices, availability, images, shipping, and tax settings.
- Conversion tracking installed and a daily budget cap.

## Steps

1. **Confirm product-feed health.** Open Merchant Center diagnostics and resolve disapprovals for the products you want to advertise. → *Expect:* selected products are approved and eligible for Shopping ads.
2. **Verify landing pages and policies.** Check price, availability, returns, contact information, and checkout security. → *Expect:* feed data matches the live site and policy issues are absent.
3. **Confirm conversion tracking.** Test purchase or checkout events in Google Ads and analytics. → *Expect:* a recent test conversion or tag assistant event appears correctly.
4. **Create the campaign.** Choose Shopping or Performance Max with Merchant Center products, target locations, language, and bidding strategy. → *Expect:* the campaign draft contains the intended product source and market.
5. **Set budget and exclusions.** Enter the daily budget cap, excluded products, negative keywords where available, and brand-safety settings. → *Expect:* spend cannot exceed the planned daily cap by configuration.
6. **Review and publish.** ⚠️ *Irreversible:* ads can spend money once enabled, so confirm budget, products, geography, and conversion action first. → *Expect:* the campaign status changes to enabled or under review.
7. **Check after launch.** Review impressions, clicks, spend, product status, and conversion tracking after the first traffic arrives. → *Expect:* spend and traffic appear only for the intended products and regions.

## Decision points

- Products are disapproved → fix feed or policy issues before launching.
- Conversion tracking is unverified → launch only with a very small test budget or wait.
- Target return on ad spend is required → use historical conversion data before automated value bidding.

## Failure modes & recovery

- **F1 Feed mismatch:** detect price or availability warning → pause affected products and resync the feed.
- **F2 Spend with no conversions:** detect clicks but no tracked sales → verify checkout tag, attribution window, and landing-page relevance.
- **F3 Wrong region spend:** detect clicks from excluded markets → tighten location settings and shipping availability.
- **F4 Account policy suspension:** detect Merchant Center or Ads suspension → stop campaign changes and follow the policy appeal checklist with evidence.

## Verification

The Shopping campaign is enabled or under review, uses approved products from Merchant Center, has conversion tracking selected, and has a daily budget at or below the approved cap.

## Variations

- `us`: configure state sales-tax presentation and shipping rates consistently with the website.
- Small catalog: standard Shopping may offer clearer product-level control than Performance Max.

## Safety & privacy

Medium risk because ads spend money and use tracking. Confirm budget caps, conversion tags, regions, and product eligibility before enabling the campaign.
