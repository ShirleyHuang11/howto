---
name: set-up-a-connection-pool
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

You configure database connection pooling so the application reuses connections efficiently without exhausting the database's connection limit.

## Preconditions

- The database maximum connections and reserved admin connections are known.
- The number of app instances, workers, and threads is known.
- The app's database client or external pooler supports configurable limits.
- Metrics exist for open connections, wait time, and query latency.

## Steps

1. **Inventory current connection usage.** [BRANCH: Postgres | MySQL] Run `SELECT count(*) FROM pg_stat_activity;` or `SHOW STATUS LIKE 'Threads_connected';`. → *Expect:* current active/idle connection count is known.
2. **Calculate a safe pool size.** Divide available database connections across app instances and worker processes, leaving headroom for migrations and admin access. → *Expect:* a per-process pool limit such as `DB_POOL_SIZE=10`.
3. **Configure the application pool.** Set pool size, idle timeout, acquisition timeout, and max lifetime using the framework or driver settings. → *Expect:* configuration is explicit and environment-specific.
4. **Use an external pooler if needed.** [BRANCH: PgBouncer | RDS Proxy | ProxySQL] Configure transaction pooling or proxy pooling when many short-lived app processes exceed DB limits. → *Expect:* apps connect to the pooler endpoint and the pooler connects to the database.
5. **Test under representative concurrency.** Run a load test or worker concurrency test. → *Expect:* requests complete without connection exhaustion or excessive wait time.
6. **Monitor database and pool metrics.** Watch active connections, pool wait time, idle connections, and query latency. → *Expect:* connections stay below the database limit with low wait time.
7. **Roll out gradually.** Apply to one environment or small production slice first. → *Expect:* metrics improve or remain stable before full rollout.

## Decision points

- App has many serverless instances → use a managed proxy or pooler to prevent connection storms.
- Transactions rely on session state → avoid transaction pooling or remove session-level assumptions.
- Pool wait time is high but DB is idle → increase pool size carefully or investigate leaked connections.
- DB CPU is saturated → reducing connections may help; increasing pool size will likely worsen it.

## Failure modes & recovery

- **F1 Too many connections:** detect `remaining connection slots are reserved` or MySQL `Too many connections` → lower per-process pool size or add an external pooler.
- **F2 Connection leaks:** detect active connections never returning to idle → ensure code closes/releases clients in `finally` blocks.
- **F3 PgBouncer session incompatibility:** detect prepared statement or temp table errors → use session pooling or adjust driver settings.
- **F4 Pool starvation:** detect request timeouts waiting for a connection → tune pool size, reduce long transactions, or add capacity.

## Verification

Under representative load, database connection count remains below the configured safe limit, pool acquisition errors are zero, and the app health endpoint returns `200`.

## Variations

- `Postgres PgBouncer`: transaction pooling works best for stateless transactions; verify prepared statement behavior.
- `RDS Proxy`: configure IAM/secrets integration and verify apps use the proxy endpoint.
- `Node/pg`, `SQLAlchemy`, `HikariCP`: set max pool size and acquisition timeout in the client configuration.

## Safety & privacy

Medium risk because bad pool settings can create outages or overload the database. Keep admin connection headroom, store database credentials in secrets management, and avoid logging connection strings with passwords.
