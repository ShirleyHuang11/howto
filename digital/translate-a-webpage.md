---
name: translate-a-webpage
domain: digital
locale: [generic]
interface: web
difficulty: basic
est_time: 5min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Translate a webpage enough to understand and act on it while checking important details against the original language when needed.

## Preconditions

- You can open the webpage in a browser or translation service.
- You know the target language for translation.

## Steps

1. **Open the original page.** Use the direct URL instead of a screenshot when possible. → *Expect:* the original page loads.
2. **Translate with the browser or service.** [BRANCH: built-in browser translation | external translator] use built-in translation for convenience; paste text or URL into a trusted translator if needed. → *Expect:* the page text appears in your target language.
3. **Check layout-sensitive items.** Compare buttons, forms, prices, dates, units, addresses, and warnings against the original page. → *Expect:* critical interface details are not misplaced or mistranslated.
4. **Verify specialized terms.** Look up legal, medical, technical, cultural, or idiomatic phrases separately. → *Expect:* high-stakes terms are not accepted blindly.
5. **Avoid submitting secrets through translation.** Do not paste passwords, private messages, confidential contracts, or personal records into third-party translation boxes. → *Expect:* sensitive input stays out of unapproved services.
6. **Act only after confirmation.** Before buying, signing, traveling, or changing settings, confirm the key sentence or form field. → *Expect:* the action is based on checked meaning.

## Decision points

- The page controls money, legal rights, health, travel, or government services → get human or official-language help before final action.
- Automatic translation breaks the site → use side-by-side text translation or switch back to original for form submission.
- The site has an official language selector → prefer it over machine translation.

## Failure modes & recovery

- **F1 Button mistranslated:** detect action labels seem odd or risky → recover by switching to the original and translating the surrounding text separately.
- **F2 Hidden text unchanged:** detect menus, images, PDFs, or form errors remain untranslated → recover by copying text or using OCR cautiously.
- **F3 Private text exposure:** detect sensitive text pasted into a public translator → recover by deleting history if possible and using an approved tool.

## Verification

You can identify the page's purpose, key warnings, required fields, and intended action in the target language, and any high-stakes term has been independently checked.

## Variations

- `mobile-app`: use browser translation, camera translation, or share-sheet translation, then verify before submitting.
- `shopping`: confirm currency, shipping location, taxes, and return policy.
- `travel`: verify dates, station names, addresses, and entry requirements from official sources.

## Safety & privacy

Medium risk when translation affects money, rights, health, or travel. Machine translation can sound fluent while reversing meaning, especially with negation, legal terms, measurements, and idioms.
