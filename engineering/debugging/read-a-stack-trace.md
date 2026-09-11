---
name: read-a-stack-trace
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

You identify where an error originated, separate application frames from framework noise, and decide the next code location to inspect or test.

## Preconditions

- You have the full stack trace, not only the final error line.
- Source code for the application version that produced the trace is available.
- Logs or test output include timestamps, request IDs, or CI job links when relevant.

## Steps

1. **Capture the complete trace.** Copy the exception type, message, and all frames from logs, test output, or the browser console. → *Expect:* the top error and call stack are available in one place.
2. **Read the error message first.** Identify the exception class and the specific complaint, such as `KeyError: 'user_id'` or `TypeError: cannot read properties of undefined`. → *Expect:* you know what operation failed.
3. **Find the first application frame.** Scan from the top toward the bottom until a frame points to repository code instead of dependency code. → *Expect:* one file and line number are the primary inspection point.
4. **Open surrounding code.** Inspect 20 to 40 lines around that frame and the immediate caller. → *Expect:* you can name the variable, call, or assumption that failed.
5. **Trace data backward.** Follow the failing value to where it was created, parsed, or passed in. → *Expect:* there is a plausible source for the bad value or missing state.
6. **Reproduce with a focused command.** Run the failing test, request, or script such as `pytest -q tests/test_api.py::test_missing_user_id`. → *Expect:* the same stack trace appears on demand.
7. **Write the next action.** Choose a fix, an added assertion, or a narrower diagnostic log. → *Expect:* the debugging path continues from evidence rather than guessing.

## Decision points

- Top frame is library code → keep scanning for the nearest application frame that passed invalid input.
- Trace is minified or transpiled → load source maps or reproduce in development mode.
- Trace is from production only → match it to the deployed commit before editing.
- Multiple exceptions are chained → start with the root cause shown after `Caused by`, `The above exception`, or nested `cause`.

## Failure modes & recovery

- **F1 Truncated trace:** detect missing middle frames or log clipping → fetch raw CI logs or increase log limit.
- **F2 Wrong code version:** detect line numbers that do not match current source → check the deployed commit or build artifact.
- **F3 Framework wrapper noise:** detect many middleware frames → find the first route, controller, handler, or job frame in app code.
- **F4 Misleading secondary exception:** detect cleanup or error-handler failure after the original exception → inspect chained causes and earlier log lines.

## Verification

Running the focused reproduction command produces the same exception type and first application frame, and after the fix the same command exits 0 or returns the expected non-error status.

## Variations

- `Python`: read from the bottom for call origin but inspect the final exception and traceback chain carefully.
- `JavaScript`: use source maps for bundled code and inspect async stack frames when available.
- `Java/JVM`: inspect `Caused by` blocks and suppressed exceptions.
- `Go`: standard errors may need `%w` chains or panic stack traces; use logs and wrapped error checks together.

## Safety & privacy

Low risk when reading local traces, but production traces can include tokens, emails, payloads, or database values. Redact sensitive fields before sharing and avoid pasting customer data into third-party tools.
