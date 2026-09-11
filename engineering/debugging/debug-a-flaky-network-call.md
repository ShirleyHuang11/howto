---
name: debug-a-flaky-network-call
domain: engineering
subdomain: debugging
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You reproduce an intermittent network failure, identify whether it is caused by DNS, connection setup, TLS, server responses, timeouts, retries, or client logic, and land a fix that is proven by an automated test or repeatable probe.

## Preconditions

- You can run the affected client locally or in a staging environment.
- You know the target URL, method, headers required for authentication, and the expected success status.
- You have safe test credentials or a mock server; never use production secrets in logs.
- Network tools are installed: `curl`, `dig` or `nslookup`, and optionally `tcpdump` or `mitmproxy`.

## Steps

1. **Capture the failing request exactly.** Record method, URL, headers excluding secrets, body shape, timeout values, proxy settings, and the observed error. → *Expect:* a redacted reproduction note with the same endpoint and client settings as the failing path.
2. **Run a repeated baseline probe.** Use `for i in $(seq 1 50); do curl -sS -o /tmp/net.out -w "$i %{http_code} %{time_namelookup} %{time_connect} %{time_appconnect} %{time_starttransfer} %{time_total}\n" --max-time 10 "https://example.com/api/health" || echo "$i curl_failed"; done`. → *Expect:* a list showing whether failures are DNS, connect, TLS, HTTP, or timeout related.
3. **Check DNS stability.** Run `for i in $(seq 1 20); do dig +short example.com; done | sort | uniq -c`. → *Expect:* stable expected addresses, or evidence of inconsistent resolution.
4. **Inspect client timeout and retry behavior.** Find the call site and verify connect timeout, read timeout, total deadline, retry count, idempotency handling, and backoff. → *Expect:* a concrete explanation of how many attempts happen and when the client gives up.
5. **Reproduce under controlled fault injection.** [BRANCH: unit test | integration proxy] use a mock server that delays, resets, or returns `503`; for example, add a test with `nock`, `responses`, `WireMock`, or `toxiproxy`. → *Expect:* the flaky condition fails deterministically before the fix.
6. **Apply the smallest resilient fix.** Add bounded retries only for idempotent requests, increase too-short deadlines, repair proxy or DNS configuration, or fix connection-pool exhaustion. → *Expect:* the controlled failure now succeeds or fails with a clear typed error and no unbounded retry loop.
7. **Run the repeated probe again.** Use the same loop and target from step 2. → *Expect:* materially lower failure rate, stable timing, and no new slow tail beyond the accepted budget.

## Decision points

- Failures are only `000` with high `time_namelookup` → debug DNS or resolver configuration before changing application code.
- Failures are TLS handshake errors → inspect certificates, SNI, system clock, and corporate proxy trust roots.
- Only non-idempotent `POST` calls fail → do not blindly retry; add idempotency keys or surface a safe error.
- Repeated probes pass but app fails → inspect client pool limits, cancellation context, and per-request headers.

## Failure modes & recovery

- **F1 Hidden production secret in logs:** detect bearer tokens or cookies in captured output → delete the log artifact, rotate exposed credentials if necessary, and rerun with redaction.
- **F2 Retry storm:** detect many fast retries or upstream rate-limit responses → cap retries, add exponential backoff with jitter, and respect `Retry-After`.
- **F3 False local success:** detect local probes pass while CI or staging fails → compare DNS, proxy, IPv4/IPv6, CA bundle, and environment variables.
- **F4 Flaky test remains nondeterministic:** detect pass/fail variation in the new test → replace real network dependency with a deterministic mock or fault-injection proxy.

## Verification

The controlled failure test exits 0 after the fix, for example `pytest -q tests/test_network_client.py` or `npm test -- network-client`, and the repeated `curl` probe returns the expected `2xx` or documented error rate for at least 50 attempts without secret leakage.

## Variations

- `Python requests/httpx`: set explicit connect/read timeouts and use `pytest` plus `responses`, `respx`, or `toxiproxy`.
- `Node fetch/axios`: use `AbortController`, `nock` or `msw`, and retry only idempotent operations.
- `Go net/http`: configure `http.Client.Timeout`, transport dial/TLS timeouts, and table-test retry behavior.
- `Kubernetes`: compare app pod DNS with `kubectl exec deploy/app -- nslookup example.com`.

## Safety & privacy

Low risk when using test endpoints and redacted logs. Do not print authorization headers, cookies, request bodies containing personal data, or private URLs. Avoid increasing retry counts against production until the upstream owner confirms acceptable load.

