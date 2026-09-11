---
name: set-a-request-timeout
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 20min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You add explicit request timeouts so outbound API calls fail predictably instead of hanging threads, workers, or user requests forever.

## Preconditions

- The outbound API call site is known.
- You understand the caller's latency budget and whether the request runs in a web request, job worker, or CLI.
- A test can simulate a slow or non-responsive upstream.

## Steps

1. **Choose a timeout budget.** Set separate connect and read budgets when the client supports them, for example 2s connect and 10s total for an interactive request. → *Expect:* the timeout is shorter than the caller's own deadline.
2. **Configure the client explicitly.** [Node fetch | Python httpx] use `AbortSignal.timeout(10000)` or `httpx.Client(timeout=httpx.Timeout(10.0, connect=2.0))`. → *Expect:* the request code contains no implicit infinite timeout.
3. **Propagate cancellation where possible.** Pass the caller's cancellation signal or context into the API client. → *Expect:* aborted web requests or jobs stop waiting on the upstream call.
4. **Handle timeout errors distinctly.** Map timeout exceptions to a retryable or user-safe timeout error, separate from HTTP 500 responses. → *Expect:* logs and metrics can distinguish timeout from upstream status failures.
5. **Add a slow-upstream test.** Use a mock server that sleeps longer than the configured timeout. → *Expect:* the client raises the timeout error within the expected wall-clock range.
6. **Document the budget near configuration.** Explain why the value exists if it is not obvious from a global setting. → *Expect:* future maintainers know when to change the timeout.

## Decision points

- Streaming endpoint → use an idle/read timeout instead of a short total timeout.
- Batch job can wait longer than a web request → configure separate clients or per-call overrides.
- Timeout happens frequently in production → inspect upstream latency before simply increasing the limit.

## Failure modes & recovery

- **F1 Timeout too short:** detect legitimate calls failing near the limit → adjust budget based on p95/p99 latency and caller deadline.
- **F2 Timeout ignored:** detect tests taking longer than configured → verify the library option is correct and not overwritten by a shared client.
- **F3 Socket leak:** detect growing open connections after timeouts → ensure response bodies are closed and clients are reused correctly.
- **F4 Retried cancellation:** detect retries after the caller cancelled → propagate cancellation and stop retry loops when the parent context is done.

## Verification

Run the timeout test, for example `pytest tests/test_api_timeout.py -q` or `npm test -- request-timeout`; it exits 0 and proves a deliberately slow upstream fails within the configured timeout plus a small test tolerance.

## Variations

- `Node fetch`: use `AbortController` or `AbortSignal.timeout()` and catch `AbortError` or timeout-specific errors.
- `axios`: set `timeout` in milliseconds and verify adapter behavior in Node versus browsers.
- `Go`: use `context.WithTimeout` per request and an `http.Client` with transport-level timeouts.

## Safety & privacy

Low risk and usually local to the client. Do not print full URLs if query strings carry tokens, and coordinate timeout reductions for shared services because a too-aggressive value can increase visible failure rates.
