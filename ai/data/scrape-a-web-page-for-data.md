---
name: scrape-a-web-page-for-data
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You extract structured data from a web page in a respectful, reproducible way that obeys access rules and produces validated records.

## Preconditions

- The target URL, allowed use case, and confirmation that scraping is permitted by terms, robots.txt, or an API alternative.
- Python with `requests`, `beautifulsoup4`, and optionally `playwright` for JavaScript-rendered pages.
- A schema for the records you intend to extract.

## Steps

1. **Check permission and API alternatives.** Review robots.txt, terms, rate limits, and whether an official API or export exists. → *Expect:* a documented allowed path for data access.
2. **Fetch one page politely.** Use `requests.get(url, headers={"User-Agent": "research-bot contact@example.com"}, timeout=20)`. → *Expect:* HTTP 200 and HTML content, or a clear refusal status.
3. **Parse stable selectors.** Use BeautifulSoup CSS selectors or semantic attributes rather than brittle visual positions. → *Expect:* extracted fields match the visible page for a sample record.
4. **Handle dynamic pages if needed.** [BRANCH: static HTML | Playwright] Use Playwright only when required to render JavaScript content. → *Expect:* the rendered DOM contains the target fields.
5. **Validate extracted records.** Parse into Pydantic models or JSON Schema and reject incomplete records. → *Expect:* valid records serialize to JSON or CSV with expected fields.
6. **Throttle and cache requests.** Add delays, retries with backoff, and local caching. → *Expect:* repeated development runs do not hammer the site.
7. **Log provenance.** Store source URL, fetch timestamp, HTTP status, parser version, and content hash. → *Expect:* each row can be traced to a page and extraction run.

## Decision points

- Official API exists → use it instead of scraping HTML.
- robots.txt or terms disallow the path → stop or request permission.
- HTML layout changes often → add parser tests on saved fixtures and monitor extraction counts.
- Page contains personal data → assess consent, minimization, and retention before collection.

## Failure modes & recovery

- **F1 HTTP 403 or 429:** detect blocked or rate-limited requests → slow down, authenticate if permitted, use the official API, or stop.
- **F2 Selector drift:** detect zero records or missing required fields → update selectors using saved HTML fixtures and add regression tests.
- **F3 Duplicate records:** detect repeated ids or URLs → deduplicate by canonical URL or stable record key.
- **F4 Dynamic content missing:** detect empty fields in static HTML → use Playwright or locate the underlying authorized API call.

## Verification

Run the scraper on a fixed test URL or saved HTML fixture. The check passes only if HTTP status is acceptable, at least the expected number of records is extracted, every record validates against the schema, and duplicate keys are zero.

## Variations

- `requests + BeautifulSoup`: best for static pages and small jobs.
- `Playwright`: use for JavaScript-rendered pages, with screenshots or DOM snapshots for tests.
- `Scrapy`: use for larger crawls with built-in throttling and item pipelines.

## Safety & privacy

Medium risk from legal, privacy, and site-load concerns. Respect robots.txt and terms, identify your client, limit rate, avoid scraping private or sensitive data without authorization, and do not bypass access controls.
