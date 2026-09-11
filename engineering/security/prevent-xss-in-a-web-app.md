---
name: prevent-xss-in-a-web-app
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [engineering/add-input-validation]
status: draft
last_verified: 2026-09-11
---

## Goal

You prevent cross-site scripting by treating user-controlled data as untrusted, rendering with safe escaping, and verifying malicious payloads do not execute.

## Preconditions

- The affected page, component, template, or API field is identified.
- Browser tests or a local web server can exercise the UI.
- A CSP plan exists or can be added separately with `engineering/set-up-a-content-security-policy`.

## Steps

1. **Find untrusted render paths.** Search for dangerous sinks: `rg 'innerHTML|dangerouslySetInnerHTML|v-html|raw\\(|unsafeHTML|document\\.write|bypassSecurityTrust' .`. → *Expect:* every manual HTML injection point is reviewed.
2. **Use framework escaping by default.** Render user text as text nodes or escaped template variables, not raw HTML. → *Expect:* payloads such as `<script>alert(1)</script>` display as text or are removed.
3. **Sanitize only when rich HTML is required.** Use a maintained sanitizer such as DOMPurify or the server framework equivalent with a strict allowlist. → *Expect:* allowed tags remain and scripts/event handlers are stripped.
4. **Avoid unsafe URL and attribute sinks.** Validate `href`, `src`, and style values; block `javascript:` URLs and untrusted inline event attributes. → *Expect:* malicious URLs are rejected or rendered inert.
5. **Add regression tests with XSS payloads.** Include script tags, image `onerror`, SVG payloads, encoded values, and `javascript:` links. → *Expect:* tests assert no alert execution and safe DOM output.
6. **Run browser-level verification.** Use Playwright/Cypress to intercept dialogs and inspect the DOM. Example: `npx playwright test tests/xss.spec.ts`. → *Expect:* tests exit 0 and no dialog is triggered.
7. **Deploy with monitoring for blocked scripts.** Watch CSP reports or frontend errors after rollout. → *Expect:* no legitimate flows are broken and attempted script execution is blocked.

## Decision points

- Product needs user-authored rich text → sanitize with an allowlist and store either source plus sanitized render cache or sanitize on output consistently.
- Dangerous sink is from a third-party widget → isolate it in a sandboxed iframe if it cannot be removed.
- Legacy templates mix HTML and data → prioritize high-traffic and authenticated pages first.
- Inline scripts are required → plan nonce-based CSP rather than broad `unsafe-inline`.

## Failure modes & recovery

- **F1 Payload still executes:** detect browser dialog, DOM event handler, or test failure → remove the unsafe sink and add a regression fixture.
- **F2 Sanitizer too permissive:** detect allowed event handlers or unsafe URLs → tighten allowlist and upgrade sanitizer.
- **F3 Legitimate formatting stripped:** detect user content losing approved markup → add only necessary tags/attributes to the allowlist.
- **F4 Double escaping:** detect visible HTML entities like `&amp;lt;` → ensure data is escaped exactly once at output.

## Verification

`npx playwright test tests/xss.spec.ts` or the project browser test command exits 0, malicious payload fixtures do not execute JavaScript, and static search no longer shows unreviewed dangerous sinks.

## Variations

- `React`: avoid `dangerouslySetInnerHTML`; if unavoidable, sanitize immediately before rendering.
- `Vue/Angular`: avoid `v-html` and bypass trust APIs unless sanitized and reviewed.
- `Server templates`: rely on auto-escaping and use explicit safe/raw markers only for trusted constants.

## Safety & privacy

Medium risk because XSS can steal sessions or act as users. Do not paste real customer content into tests, keep payloads synthetic, and review any rich-text sanitization changes carefully.
