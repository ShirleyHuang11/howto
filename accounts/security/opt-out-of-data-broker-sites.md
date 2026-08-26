---
name: opt-out-of-data-broker-sites
domain: accounts
subdomain: security
locale: [generic, us]
interface: web
difficulty: intermediate
est_time: 2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

You reduce public exposure of your home address, phone numbers, relatives, and age by submitting opt-out requests to people-search and data-broker sites.

## Preconditions

- A dedicated email address or alias for privacy requests.
- Your common name variations, past addresses, and phone numbers.
- A place to track each broker, request date, confirmation link, and removal status.

## Steps

1. **Make an inventory of exposed listings.** Search your name with city, old cities, phone number, and address. → *Expect:* a list of broker pages or search-result URLs to target.
2. **Prioritize high-exposure sites.** Start with pages showing home address, family links, birth month, phone numbers, or court-record teasers. → *Expect:* the most sensitive listings are at the top of your tracker.
3. **Open the broker's official opt-out page.** Use the site's footer links for Opt Out, Privacy, Do Not Sell or Share, or Remove My Info. → *Expect:* you reach a form controlled by the broker, not an ad or paid removal service.
4. **Submit the minimum required information.** Provide the listing URL, name, email alias, and required verification fields. → *Expect:* the broker accepts the request or sends a verification email.
5. **Verify the request.** Click confirmation emails promptly; some expire within minutes or hours. → *Expect:* the broker shows a submitted, processing, or confirmed removal status.
6. **Record evidence.** Save the broker name, URL, request date, confirmation number, and expected processing time. → *Expect:* your tracker shows what is pending and what is complete.
7. **Check removal after the stated period.** Search the same listing URL and your name again. → *Expect:* the listing is gone, suppressed, or no longer exposes sensitive fields.
8. **Escalate under privacy law where available.** [BRANCH: covered jurisdiction, submit a formal deletion or opt-out request citing the applicable law | no specific law, use the broker's standard removal form] → *Expect:* a stronger request is logged when legal rights apply.

## Decision points

- Site asks for a government ID → provide only if legally necessary, redact ID number and photo if allowed, and consider skipping lower-risk brokers.
- Broker charges a fee for removal → look for the free privacy or opt-out form; do not pay a broker to remove its own listing.
- Listing reappears under a variation → submit a separate request for that URL and add the variation to your tracker.

## Failure modes & recovery

- **F1 Confirmation email missing:** check spam and alias forwarding → resubmit with a different email if needed.
- **F2 Broker refuses removal:** use the formal privacy request path or state attorney general/privacy regulator route where available.
- **F3 Listing disappears but search snippet remains:** wait for search-index refresh or request search-result removal from the search engine.
- **F4 New brokers appear later:** schedule quarterly searches and repeat the process.

## Verification

Your tracker shows each targeted broker as removed or escalated, and searching the exact old listing URLs no longer displays your sensitive personal details.

## Variations

- `us-california`: CCPA/CPRA rights may support requests to delete, opt out of sale or sharing, and limit sensitive personal information.
- `us-state-privacy-laws`: rights vary by state; use the broker's US privacy rights portal if your state is listed.
- `eu-uk`: GDPR or UK GDPR erasure and objection rights may apply.

## Safety & privacy

Medium risk because the task involves sensitive identity and address data. Use an email alias, avoid sending unredacted ID unless required, and track requests privately.
