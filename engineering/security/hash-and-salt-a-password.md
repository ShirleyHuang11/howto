---
name: hash-and-salt-a-password
domain: engineering
subdomain: security
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You store user passwords using a modern password hashing algorithm with per-password salts and verify login behavior without ever storing plaintext passwords.

## Preconditions

- Access to the authentication code, user table schema, and test database.
- A supported password hashing library for the application language.
- A migration plan if existing password hashes use an older algorithm.

## Steps

1. **Select a password hashing algorithm.** Prefer Argon2id; use bcrypt or scrypt when Argon2id is unavailable in the stack. → *Expect:* a maintained library is selected, such as `argon2`, `argon2-cffi`, `bcrypt`, or the framework's password hasher.
2. **Add library-backed hashing.** Replace custom SHA/MD5/HMAC password storage with the library call. Example Node: `await argon2.hash(password, { type: argon2.argon2id })`; Python: `PasswordHasher().hash(password)`. → *Expect:* stored values include algorithm, parameters, salt, and hash metadata.
3. **Verify passwords with constant-time library checks.** Use `argon2.verify(storedHash, candidate)` or the framework equivalent, not manual string comparison. → *Expect:* valid passwords authenticate and invalid passwords fail.
4. **Tune cost parameters in a benchmark.** Run a small benchmark in production-like hardware and target an acceptable login latency, often around 100-500 ms per hash. → *Expect:* parameters are documented and do not overload login workers.
5. **Migrate existing hashes safely.** On login, verify the legacy hash and rehash with the new algorithm after successful authentication; keep the legacy verifier only for existing accounts. → *Expect:* active users gradually move to the new hash format.
6. **Add authentication tests.** Test registration stores no plaintext, login accepts the correct password, rejects the wrong password, and rehashes legacy values. → *Expect:* automated tests cover the password lifecycle.
7. **Run the test suite and inspect stored samples.** Use `pytest -q`, `npm test`, or the project command, then query a test row. → *Expect:* tests exit 0 and the password column contains only encoded hash strings.

## Decision points

- Framework already has a password hasher → use it unless it is obsolete.
- Existing hashes are unsalted or fast-hash only → force password reset for high-risk accounts if migration cannot safely verify them.
- Login throughput is high → use rate limiting and worker capacity planning before increasing cost too far.
- Need password reset → issue time-limited reset tokens; never email passwords.

## Failure modes & recovery

- **F1 Plaintext accidentally stored:** detect raw password values in DB/tests → stop deployment, delete test data, and fix the registration path.
- **F2 Cost too high:** detect login latency spikes or CPU saturation → lower parameters within security guidance and scale auth workers.
- **F3 Legacy users locked out:** detect valid old passwords rejected → restore the legacy verifier path and add migration tests.
- **F4 Hash library mismatch:** detect `invalid hash` errors after deploy → ensure all app instances use compatible library versions and hash formats.

## Verification

The auth test suite exits 0, a direct test-database query shows password fields contain encoded Argon2id/bcrypt/scrypt hashes rather than plaintext, and login succeeds only for the correct password.

## Variations

- `Django/Rails/Laravel`: use the framework password hasher and migration helpers.
- `Node.js`: prefer `argon2` or `bcrypt` native packages; avoid plain `crypto.createHash` for passwords.
- `Legacy migration`: rehash-on-login is safer than bulk rehashing because plaintext passwords are unavailable.

## Safety & privacy

Medium risk because mistakes can lock users out or expose credentials. Never log passwords, scrub request bodies in auth logs, keep reset tokens short-lived, and review schema dumps for accidental plaintext.
