---
name: write-an-end-to-end-test
domain: engineering
subdomain: testing
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [engineering/run-the-test-suite]
status: draft
last_verified: 2026-09-11
---

## Goal

Add an end-to-end test that drives the application through a real user or API workflow and verifies the user-visible outcome.

## Preconditions

- The application can run in a local or CI test environment.
- Test data and accounts are disposable.
- Browser or API test tooling is installed, such as Playwright, Cypress, Selenium, or a CLI HTTP client.

## Steps

1. **Pick one critical journey.** Choose a workflow such as sign in, create order, checkout, or publish record. → *Expect:* the test has a user-visible success condition.
2. **Start the app in test mode.** Run the documented command, such as `npm run dev:test` or `docker compose up -d app`. → *Expect:* the app responds on the expected local URL.
3. **Prepare deterministic test data.** Seed users and records with a script or API fixture. → *Expect:* the test can run from a known starting state.
4. **Write the E2E script.** [BRANCH: Playwright | Cypress] Use accessible selectors such as `getByRole` and avoid brittle CSS-only selectors. → *Expect:* the script performs the workflow as a user would.
5. **Assert visible completion.** Check page text, URL, database-visible status, or API response that proves the workflow completed. → *Expect:* a broken workflow fails the test.
6. **Run headed once while developing.** Use `npx playwright test --headed path/to.spec.ts` or the tool equivalent. → *Expect:* the observed browser actions match the intended journey.
7. **Run headless for CI.** Execute `npx playwright test path/to.spec.ts` or the CI command. → *Expect:* the test exits 0 without manual interaction.
8. **Clean up or isolate data.** Delete created records or use unique test IDs per run. → *Expect:* rerunning the test does not fail because of old data.

## Decision points

- Workflow depends on email, payment, or third-party login → use a sandbox provider, emulator, or test bypass designed for CI.
- Test is slow or flaky → move lower-level assertions to unit or integration tests and keep E2E focused on one path.
- UI has no stable accessible labels → improve the UI's accessibility instead of adding fragile selectors.

## Failure modes & recovery

- **F1 Selector not found:** detect timeout waiting for an element → use accessible roles and wait for the correct page state.
- **F2 App not ready:** detect browser navigation errors or 5xx responses → add a readiness check before starting the E2E runner.
- **F3 Data collision:** detect duplicate user or record errors → generate unique IDs or reset the test database.
- **F4 CI browser missing:** detect Playwright browser install errors → run `npx playwright install --with-deps` in CI setup.

## Verification

Run the headless E2E command, for example `npx playwright test tests/e2e/checkout.spec.ts`; it exits 0, produces no unexpected retries, and the CI E2E job is green for the commit.

## Variations

- `Playwright`: use `getByRole`, traces, and browser projects for cross-browser coverage.
- `Cypress`: use `cy.intercept` only for controlled test boundaries, not to hide the behavior being tested.
- `API-only`: use a scripted HTTP workflow and assert status codes plus persisted state.

## Safety & privacy

Medium risk because E2E tests often create accounts, orders, or external calls. Use sandbox credentials, disable real payments and emails, keep screenshots free of personal data, and clean up generated records.
