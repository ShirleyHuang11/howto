---
name: give-an-agent-file-access-safely
domain: ai
subdomain: agents
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: high
prerequisites: [ai/agents/sandbox-agent-tool-actions]
status: draft
last_verified: 2026-09-22
---

## Goal

Your agent can read and write files only within explicit boundaries, with auditability and confirmation for destructive changes. Success means allowed file tasks work and forbidden reads, writes, path escapes, and deletions fail programmatically.

## Preconditions

- A filesystem tool layer you control, not arbitrary shell access.
- A configured workspace root, allowlist and denylist patterns, max file sizes, and encoding policy.
- Tests using temporary directories with allowed and forbidden paths.

## Steps

1. **Expose narrow file tools.** Provide operations like `read_file`, `list_files`, `write_file`, and `apply_patch` with schemas; avoid generic shell unless separately sandboxed. → *Expect:* the agent can only request declared file operations.
2. **Canonicalize and authorize paths.** Resolve symlinks and `..` before checking that the path stays inside allowed roots and outside denylisted paths. → *Expect:* path traversal fixtures are denied.
3. **Limit reads by type and size.** Reject binaries, huge files, secrets files, and unsupported encodings unless explicitly allowed. → *Expect:* large or denied files return a bounded error instead of content.
4. **Use patch-based writes with previews.** Require diffs for existing files and atomic writes for new files. ⚠️ *Irreversible:* deletions, overwrites, and bulk changes require explicit confirmation or versioned backup first. → *Expect:* write operations produce an auditable diff before mutation.
5. **Prevent secret exposure to the model.** Scan file content for secret patterns before returning it; redact or require elevated review. → *Expect:* fake API keys in test files are redacted in model-visible output.
6. **Audit every file operation.** Log trace ID, canonical path, operation, byte count, authorization decision, and diff hash. → *Expect:* the audit log reconstructs all file access by run.

## Decision points

- Agent only needs search/read → grant read-only access first.
- Agent needs edits → restrict to workspace roots and require patch previews.
- File may contain secrets or PII → redact, summarize, or require human approval before model exposure.
- Requested path is outside allowlist or through a symlink escape → deny and ask for a scoped path.

## Failure modes & recovery

- **F1 Path traversal:** detect `../` or symlink escape access → canonicalize before authorization and add regression tests.
- **F2 Secret leak:** detect secret regex matches in returned content → redact content and rotate real exposed credentials if needed.
- **F3 Destructive overwrite:** detect write without diff or backup → restore from backup/version control and require confirmation flow.
- **F4 Binary or huge file blowup:** detect memory or context pressure → enforce size limits and specialized parsers.

## Verification

Run filesystem safety tests in a temp workspace. Allowed reads and patch writes must succeed, outside-root paths and symlink escapes must fail, denied secret files must not expose raw secrets, destructive operations must pause for confirmation, and the audit log must contain one entry for every attempted operation.

## Variations

- `local coding agent`: use workspace-root allowlists and patch-only writes.
- `document agent`: parse supported document formats into text while preserving file provenance.
- `cloud storage`: map object keys to scoped prefixes and use signed, short-lived credentials.

## Safety & privacy

High risk because file access can leak secrets, corrupt source, or delete user data. Default to read-only, canonicalize paths, redact sensitive files, require confirmation for destructive writes, and keep a complete audit trail with recoverable diffs or backups.
