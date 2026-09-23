---
name: build-an-mcp-server
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You build a Model Context Protocol server that exposes well-scoped tools or resources to an agent. Success means an MCP client can discover the server, call a tool with validated arguments, and receive a schema-valid result.

## Preconditions

- A recent MCP SDK for your language, such as TypeScript or Python.
- A clear list of resources/tools to expose and the permissions each one needs.
- Local credentials or mock data for the backing service.

## Steps

1. **Create the MCP server project.** [BRANCH: TypeScript | Python] Initialize a package, install the MCP SDK, and add a server entrypoint. → *Expect:* the server starts locally without syntax or import errors.
2. **Define tool schemas with strict inputs.** Use JSON Schema or SDK-native schemas for each tool argument, including descriptions and required fields. → *Expect:* invalid arguments are rejected before business logic runs.
3. **Implement least-privilege handlers.** Read only the configured resources and return compact structured data; avoid broad filesystem or network access. → *Expect:* a valid tool call returns `content` or structured JSON matching the declared output shape.
4. **Handle errors as data.** Convert backing-service failures into typed MCP errors or structured error content without leaking stack traces. → *Expect:* failing fixtures produce sanitized error responses.
5. **Configure transport.** Use stdio for local desktop/CLI clients or HTTP/SSE for remote clients with authentication. ⚠️ *Data leaves your control:* remote MCP servers may receive user prompts, tool arguments, and resource contents; review logging and auth first. → *Expect:* the selected client can list tools and call one tool.
6. **Add integration tests with an MCP client.** Start the server, list tools, call valid and invalid inputs, and assert responses. → *Expect:* the test suite passes and records no unauthorized resource access.

## Decision points

- Tool accesses private data → require authentication, authorization, and redaction before returning results.
- Tool mutates external state → require confirmation metadata and idempotency support.
- Client is local only → stdio is simpler and avoids exposing a network service.
- Multiple agents will connect remotely → use authenticated HTTP transport and rate limits.

## Failure modes & recovery

- **F1 Schema mismatch:** detect client sends valid-looking args but handler fails → align SDK schema and handler types, then add a failing fixture.
- **F2 Overbroad resource exposure:** detect client can read unintended files or records → narrow resource paths and authorization checks.
- **F3 Leaky errors:** detect stack traces or secrets in MCP responses → sanitize errors and disable debug output in production.
- **F4 Transport auth gap:** detect remote calls without identity → add auth middleware and reject anonymous requests.

## Verification

Run an MCP integration test that starts the server, verifies `tools/list` includes the expected tool name and input schema, calls the tool with valid arguments and receives schema-valid output, calls it with invalid arguments and receives a validation error, and confirms denied resources cannot be read.

## Variations

- `stdio MCP`: best for local IDE or desktop clients where the process is launched by the client.
- `HTTP MCP`: useful for shared services; add authentication, TLS, logging, and rate limits.
- `resource-only server`: expose documents or database rows as resources when no action is needed.

## Safety & privacy

Medium risk because MCP can expose local files, databases, and internal APIs to agents. Start with read-only tools, scope credentials, sanitize logs and errors, authenticate remote transports, and require explicit confirmation for state-changing tools.
