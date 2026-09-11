---
name: build-a-graphql-query
domain: engineering
subdomain: api
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You create a GraphQL query that requests only the needed fields, uses variables safely, and is validated against the schema before application code depends on it.

## Preconditions

- Access to the GraphQL endpoint, schema, or generated schema artifact.
- A GraphQL client, explorer, or CLI such as GraphiQL, Apollo, Relay, `graphql-codegen`, or `curl`.
- Authentication suitable for the target environment.

## Steps

1. **Inspect the schema.** Use the provider docs, GraphiQL explorer, or introspection such as `graphql-inspector introspect "$GRAPHQL_URL" --header "Authorization: Bearer $TOKEN"`. → *Expect:* the root query field and available return fields are known.
2. **Write the smallest query.** Select only fields the UI or service uses and include stable identifiers. → *Expect:* the query has no exploratory or unused fields.
3. **Use variables for dynamic values.** Define variables such as `query User($id: ID!) { user(id: $id) { id name } }`. → *Expect:* user input is not string-concatenated into the GraphQL document.
4. **Handle pagination explicitly.** For connections, request `edges`, `node`, and `pageInfo { hasNextPage endCursor }`. → *Expect:* large lists can be fetched deterministically.
5. **Run the query against a non-production endpoint.** Use `curl -sS -H "Content-Type: application/json" -d '{"query":"query ...","variables":{"id":"123"}}' "$GRAPHQL_URL" | jq .`. → *Expect:* the response contains `data` and no unexpected `errors`.
6. **Generate or validate types.** Run code generation such as `graphql-codegen --config codegen.yml` or the project's equivalent. → *Expect:* generated types compile and match the query.
7. **Add a client test.** Mock a success response and a GraphQL `errors` response. → *Expect:* the application reads expected data and handles GraphQL errors separately from HTTP failures.

## Decision points

- Schema disables introspection → use checked-in schema JSON, SDL, or provider documentation.
- Query becomes deeply nested → split into fragments or separate queries to avoid cost limits.
- Endpoint uses persisted queries → register the query hash through the provider's approved workflow.

## Failure modes & recovery

- **F1 Validation error:** detect messages like `Cannot query field` → refresh the schema and update field names or fragments.
- **F2 Variable type mismatch:** detect `Variable "$id" got invalid value` → align variable JSON and GraphQL types.
- **F3 Partial data with errors:** detect both `data` and `errors` in the response → handle nullable fields and surface the specific failed portion.
- **F4 Query cost exceeded:** detect cost or depth limit errors → remove fields, paginate, or request a backend-specific cost increase.

## Verification

Run schema validation and tests, for example `graphql-codegen --config codegen.yml && npm test -- graphql-query`; both commands exit 0 and the query succeeds against a test endpoint with `data` present and no unexpected `errors`.

## Variations

- `Apollo`: use typed `gql` documents and generated operation types.
- `Relay`: follow fragment colocation and compile with `relay-compiler`.
- `GitHub GraphQL`: use `gh api graphql -f query=@query.graphql -F owner=ORG`.

## Safety & privacy

Low risk if run against development data. Treat GraphQL responses as potentially sensitive, avoid logging variables containing personal data or tokens, and use least-privilege tokens for schema exploration.
