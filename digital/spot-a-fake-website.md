---
name: spot-a-fake-website
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 10min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-21
---

## Goal

Decide whether a website is likely legitimate before entering passwords, personal data, or payment details.

## Preconditions

- You have the website open but have not entered sensitive information.
- You know the real organization, product, or service you intended to visit.
- You can search the web or use a known bookmark for comparison.

## Steps

1. **Pause before interacting.** Do not type passwords, card numbers, or codes until the site passes basic checks. → *Expect:* no sensitive data has been submitted yet.
2. **Check the URL exactly.** Read the domain from right to left before the first single slash, watching for misspellings, extra words, and strange endings. → *Expect:* the domain matches the real organization exactly or raises a concern.
3. **Treat the padlock as limited.** Confirm HTTPS is present, but remember it only means the connection is encrypted. → *Expect:* you do not treat the padlock as proof the business is real.
4. **Reach the site independently.** Open a new tab and search for the organization or use a saved bookmark instead of the link that brought you there. → *Expect:* the independent route lands on the same domain or a different official one.
5. **Inspect contact and policy pages.** Look for a real address, support channel, return policy, privacy policy, and consistent company name. → *Expect:* business details are specific and consistent.
6. **Look for payment red flags.** Watch for wire transfer, crypto, gift cards, payment through friends-and-family, or pressure to bypass normal checkout. → *Expect:* payment options look standard for the transaction.
7. **Check outside reviews.** Search the domain plus "reviews", "scam", or "complaints" and read recent independent results. → *Expect:* there is a track record beyond the site's own testimonials.
8. **Test the offer against reality.** Compare prices, availability, and urgency claims with known retailers or official sites. → *Expect:* extreme discounts or impossible stock are treated as warnings.
9. **Decide before submitting.** [BRANCH: looks legitimate | uncertain or suspicious] proceed with a low-risk payment method, or close the site and use an official channel. → *Expect:* sensitive data is entered only on a site you can justify trusting.

## Decision points

- The URL uses a misspelled brand → close it and use the official site.
- The site asks for a one-time code after a link from email or text → assume phishing until verified independently.
- The price is far below every reputable seller → treat it as likely counterfeit, stolen, or fake.
- Reviews exist only on the site itself → look for independent evidence before buying.
- Payment avoids chargeback protection → do not proceed.

## Failure modes & recovery

- **F1 Lookalike domain:** detect swapped letters or extra words, recover by typing the known address manually.
- **F2 Padlock false confidence:** detect HTTPS on a strange domain, recover by checking ownership and reputation.
- **F3 Fake reviews:** detect generic testimonials with no outside footprint, recover by searching independent review sources.
- **F4 Payment trap:** detect gift card, wire, crypto, or friends-and-family demands, recover by abandoning checkout.
- **F5 Code theft:** detect a site asking for a login code unexpectedly, recover by closing it and changing the password if entered.

## Verification

Before entering sensitive data, the exact domain, independent access route, business details, reviews, and payment method all match a legitimate organization.

## Variations

- Banking and government sites: use bookmarks or typed addresses only.
- Shopping sites: prefer credit cards or protected checkout services for dispute rights.
- Event tickets: verify seller transfer rules on the official ticket platform.
- Charity donations: check the charity through an independent registry before donating.

## Safety & privacy

Fake sites can steal passwords, identity documents, payment details, and one-time codes. If you already submitted data, change the affected password, contact the payment provider, and monitor the account.
