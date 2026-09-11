---
name: add-a-foreign-key-constraint
domain: engineering
subdomain: database
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

Add a foreign-key constraint that prevents orphan rows while minimizing lock time and production risk.

## Preconditions

- Parent and child tables already exist.
- Child rows have a populated reference column.
- You can run read-only validation queries and migrations in staging.

## Steps

1. **Confirm parent key uniqueness.** Run `SELECT id, count(*) FROM accounts GROUP BY id HAVING count(*) > 1;`. → *Expect:* zero duplicate parent keys.
2. **Find orphan child rows.** Run `SELECT child.id FROM invoices child LEFT JOIN accounts parent ON parent.id = child.account_id WHERE child.account_id IS NOT NULL AND parent.id IS NULL LIMIT 50;`. → *Expect:* zero rows before adding the constraint.
3. **Repair or quarantine bad data.** Backfill missing parents, set references to `NULL` if allowed, or move invalid rows to an audit table. → *Expect:* the orphan query returns zero rows.
4. **Index the child reference.** [Postgres] run `CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_invoices_account_id ON invoices(account_id);`. → *Expect:* deletes or updates on the parent can check children efficiently.
5. **Add the constraint safely.** [Postgres] run `ALTER TABLE invoices ADD CONSTRAINT fk_invoices_account FOREIGN KEY (account_id) REFERENCES accounts(id) NOT VALID;`. → *Expect:* new invalid writes are blocked while old rows are not scanned under a long lock.
6. **Validate the constraint.** Run `ALTER TABLE invoices VALIDATE CONSTRAINT fk_invoices_account;`. → *Expect:* validation succeeds and the constraint becomes fully enforced.
7. **Test write behavior.** Try inserting a child with a nonexistent parent in a transaction and roll it back. → *Expect:* the insert fails with a foreign-key violation.

## Decision points

- Child column allows `NULL` → decide whether optional relationships are valid business behavior.
- Parent deletes should remove children → use `ON DELETE CASCADE` only after product review.
- Parent deletes should be prevented → default `NO ACTION` or `RESTRICT` is safer.
- Large production table → use online or phased validation features for the database.

## Failure modes & recovery

- **F1 Orphans exist:** detect rows from the left-join check → repair data before adding or validating the constraint.
- **F2 Lock timeout:** detect migration timeout waiting for locks → retry during a quieter window and use online index/constraint options.
- **F3 Cascade deletes too much:** detect unexpected child deletion in staging → remove cascade behavior and restore from backup if production was affected.
- **F4 Missing child index:** detect slow parent deletes or updates → add the child-column index and recheck the query plan.

## Verification

The orphan query returns zero rows, the migration command exits 0, and a test insert with an invalid parent key fails with the database's foreign-key violation error.

## Variations

- `MySQL`: add an index first, then `ALTER TABLE ... ADD CONSTRAINT ... FOREIGN KEY ...`; online behavior depends on engine and version.
- `SQLite`: ensure `PRAGMA foreign_keys = ON` in tests and application connections.
- `SQL Server`: use `WITH CHECK ADD CONSTRAINT` to validate existing data.

## Safety & privacy

Medium risk because constraints can block writes and cascade actions can remove data. Review delete behavior, run orphan checks with read-only credentials when possible, and never add cascades to production without explicit approval.
