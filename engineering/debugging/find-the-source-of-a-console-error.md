---
name: find-the-source-of-a-console-error
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: basic
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You trace a browser console error to the source code, dependency, or runtime data that causes it, then verify the fix with an automated browser or unit test.

## Preconditions

- You can reproduce the page or workflow in a browser.
- Source maps are available locally or in the deployed environment.
- You can run the frontend test or build command.

## Steps

1. **Capture the exact console error.** Copy the error type, message, stack trace, URL, browser, and steps to reproduce. → *Expect:* a precise error signature and reproduction path.
2. **Map stack frames to source.** Click the top application frame in DevTools or use source maps to locate the file and line. → *Expect:* a source file, component, function, or bundle module is identified.
3. **Separate app errors from extension noise.** Reproduce in an incognito or clean profile with extensions disabled. → *Expect:* the same error remains if it belongs to the app.
4. **Inspect runtime inputs.** Check props, API response shape, DOM element existence, feature flags, and environment variables used at the failing line. → *Expect:* the undefined value, bad type, missing element, or rejected promise is visible.
5. **Fix the cause.** Add the missing guard, correct the API contract, await the async value, repair import paths, or update the dependency usage. → *Expect:* the console error no longer appears in the reproduction path.
6. **Add a regression test.** [Playwright | Jest] create a test that exercises the page state and fails on console errors or the specific component behavior. → *Expect:* the test fails before the fix and passes after it.
7. **Run the build.** Execute `npm run build` or the project equivalent. → *Expect:* compilation succeeds without the original error reappearing.

## Decision points

- Stack points into minified vendor code → use source maps, inspect the first app frame, and check dependency version notes.
- Error appears only after API data loads → save the response fixture and test the component with that shape.
- Error is an unhandled promise rejection → trace the async call and add explicit error handling.
- Error is hydration-related → compare server-rendered markup, client-only state, and browser-only APIs.

## Failure modes & recovery

- **F1 Missing source maps:** detect stack only shows bundle offsets → reproduce locally with development build or upload correct source maps to the error tracker.
- **F2 Error caused by browser extension:** detect clean profile has no error → document as extension noise and avoid code changes.
- **F3 Test misses console failure:** detect UI test passes despite logged errors → configure the test runner to fail on page console errors.
- **F4 Race condition:** detect error only on slow network or reload → throttle network and add deterministic async waits in the test.

## Verification

`npm test` or `npm run test -- console-error` exits 0, `npm run build` exits 0, and a Playwright run has no unexpected `pageerror` or console error for the reproduced workflow.

## Variations

- `React`: inspect component props, hooks order, hydration warnings, and error boundaries.
- `Vue/Svelte`: inspect reactive values and lifecycle timing around the failing line.
- `Playwright`: attach `page.on('console')` and `page.on('pageerror')` assertions.
- `Sentry/browser error tracker`: use release and source-map artifacts to map production stack traces.

## Safety & privacy

Low risk when debugging locally. Do not paste production stack traces containing URLs, user IDs, or payload fragments into public issues. Avoid swallowing errors broadly just to quiet the console.

