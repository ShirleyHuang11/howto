---
name: prevent-sql-injection
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You change database access so untrusted input cannot alter SQL structure, and you verify the protection with tests that include malicious input.

## Preconditions

- The code path building or executing SQL is identified.
- A test database or isolated environment is available.
- The database driver or ORM supports parameterized queries.
- Security-sensitive behavior can be covered by automated tests.

## Steps

1. **Find SQL string construction.** Search for raw query building such as `rg "SELECT|INSERT|UPDATE|DELETE|execute\\("`. → *Expect:* candidate call sites using user input are identified.
2. **Classify inputs.** Identify values, identifiers, sort directions, and SQL fragments separately. → *Expect:* every untrusted input has a safe handling plan.
3. **Replace value interpolation with parameters.** Use placeholders such as `WHERE email = $1`, `WHERE email = ?`, or ORM bind parameters. → *Expect:* user values are passed separately from SQL text.
4. **Whitelist identifiers and directions.** For table/column/order choices, map user options to hardcoded allowed identifiers instead of binding them as values. → *Expect:* unsupported options are rejected before query execution.
5. **Add regression tests with attack strings.** Include inputs such as `' OR '1'='1` and `x'; DROP TABLE users; --`. → *Expect:* the query returns no unauthorized rows and schema remains intact.
6. **Run tests and static checks.** Execute the focused test suite and any security linter. → *Expect:* tests pass and no risky string interpolation remains in the touched path.
7. **Review database privileges.** Ensure the application user has only needed permissions. → *Expect:* even a query bug cannot drop unrelated tables or read other schemas.

## Decision points

- Input is a value → use query parameters.
- Input chooses a column or sort direction → use a whitelist mapping to literal SQL identifiers.
- Raw SQL is unavoidable → isolate it, parameterize values, and add focused tests.
- Legacy path is too broad for one change → protect the exposed endpoint first and create follow-up tasks.

## Failure modes & recovery

- **F1 Parameters used for identifiers:** detect SQL errors or quoted column names as strings → replace with a whitelist of hardcoded identifiers.
- **F2 Injection test still returns data:** detect malicious input bypasses filters → inspect remaining interpolation and add failing-case coverage.
- **F3 ORM escape hatch unsafe:** detect raw SQL helper bypassing parameterization → switch to ORM parameter API or safe query builder.
- **F4 Overprivileged DB user:** detect app can `DROP` or read unrelated schemas → reduce grants and rotate credentials if exposure occurred.

## Verification

Automated tests using malicious input pass, the generated query uses bind parameters for values, and a schema check after the test confirms protected tables still exist.

## Variations

- `Node pg`: use `client.query('SELECT * FROM users WHERE email = $1', [email])`.
- `Python psycopg`: use `cursor.execute('SELECT * FROM users WHERE email = %s', (email,))`.
- `Django/Rails/Prisma`: prefer ORM filters; when using raw SQL, use the framework's parameter binding API.

## Safety & privacy

Medium risk because SQL injection can expose or destroy data. Do not test against production with destructive payloads, avoid logging raw malicious strings alongside secrets, and apply least-privilege database grants.
