---
name: run-a-transaction-safely
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

Group related database changes so they commit together, roll back together, and behave correctly under concurrent access.

## Preconditions

- The code path performs multiple related reads or writes.
- The database driver or ORM exposes explicit transaction APIs.
- You can run tests that simulate both success and failure.

## Steps

1. **Define the transaction boundary.** Include only the database work that must be atomic; keep network calls outside when possible. → *Expect:* the transaction scope is short and has a clear commit point.
2. **Open the transaction through the project API.** Use `BEGIN` directly or an ORM helper such as `await db.transaction(async (tx) => { ... })`. → *Expect:* all statements use the same transaction connection or `tx` object.
3. **Set isolation deliberately when needed.** For money, inventory, or uniqueness decisions, use row locks or stronger isolation, for example `SELECT ... FOR UPDATE`. → *Expect:* concurrent operations cannot both consume the same resource.
4. **Validate before writing.** Check invariants inside the transaction, close to the write. → *Expect:* stale pre-transaction reads cannot authorize invalid writes.
5. **Commit only after every required write succeeds.** Let exceptions roll back automatically or call `ROLLBACK` in a `catch` block. → *Expect:* failure leaves no partial state.
6. **Retry safe serialization failures.** Retry the whole transaction on SQLSTATE `40001` or deadlock errors with bounded backoff. → *Expect:* transient conflicts recover without duplicating side effects.
7. **Test rollback behavior.** Force an error after the first write. → *Expect:* no rows from the failed transaction remain committed.

## Decision points

- Transaction includes external API call → move the call before or after commit, or use an outbox pattern.
- High contention row → use explicit locks and short transactions.
- Idempotency required → include a unique idempotency key table in the transaction.
- Read-only consistency needed → use a read-only transaction or repeatable-read snapshot.

## Failure modes & recovery

- **F1 Partial write:** detect child row without parent or mismatched totals → wrap all related writes in one transaction and add constraints.
- **F2 Deadlock:** detect deadlock error from the database → retry the whole transaction with jitter and consistent lock ordering.
- **F3 Long lock wait:** detect timeout or blocked sessions → shorten transaction work and move non-database operations outside.
- **F4 Side effect duplicated:** detect duplicate emails or webhooks after retry → persist an outbox row and dispatch after commit.

## Verification

`pytest -q tests/test_transactions.py` exits 0, including a forced-error test proving rollback and a concurrent test proving only one conflicting operation commits.

## Variations

- `Postgres`: handle SQLSTATE `40001` for serialization and `40P01` for deadlocks.
- `MySQL/InnoDB`: understand default repeatable-read behavior and gap locks before range updates.
- `ORM`: ensure every query inside the transaction uses the transaction handle, not the global client.

## Safety & privacy

Medium risk because incorrect transactions corrupt shared state. Keep transactions short, avoid logging sensitive row contents, and require code review for financial, inventory, or permission-changing flows.
