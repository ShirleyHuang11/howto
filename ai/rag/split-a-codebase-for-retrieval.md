---
name: split-a-codebase-for-retrieval
domain: ai
subdomain: rag
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

You chunk a codebase so retrieval returns complete, meaningful code units with enough surrounding context for an LLM to answer engineering questions.

## Preconditions

- A local checkout or approved source archive.
- Language-aware parsers where available, such as tree-sitter, plus a fallback text splitter.
- Ignore rules for vendored code, generated files, secrets, binaries, and build artifacts.
- A code-search eval set with queries and relevant files or symbols.

## Steps

1. **Define inclusion rules.** Use `.gitignore`, language filters, file-size limits, and secret scans to select indexable files. → *Expect:* an inventory excludes binaries, lockfiles if undesired, generated folders, and known secrets.
2. **Parse code into semantic units.** [BRANCH: tree-sitter | language server | fallback splitter] Split by functions, classes, modules, markdown sections, and configuration blocks. → *Expect:* chunks align to real code boundaries when parsers support the language.
3. **Attach repository metadata.** Store path, language, symbol name, imports, exported identifiers, start line, end line, and commit hash. → *Expect:* each chunk can be linked back to an exact file span.
4. **Add parent context.** Prepend compact module or class headers when needed so standalone functions make sense. → *Expect:* chunks remain under token limits while preserving relevant scope.
5. **Handle large files.** Split long functions or generated-like files into overlapping windows only after semantic splitting fails. → *Expect:* no chunk exceeds the embedding model max input size.
6. **Embed and index.** [BRANCH: code-aware embedding | general embedding + lexical search] ⚠️ *Data leaves your control:* hosted embedding APIs receive source code; confirm approval or use local embeddings for proprietary code. → *Expect:* index rows include vectors and searchable path/symbol metadata.
7. **Evaluate code retrieval.** Test queries for symbols, behavior, errors, and architecture questions. → *Expect:* gold file or symbol appears in top 5 for the target percentage of eval queries.

## Decision points

- Symbol queries fail → add lexical search over paths and identifiers.
- Behavioral questions fail → include nearby comments, tests, and call-site context.
- Proprietary code cannot leave infra → use local embeddings and self-hosted vector storage.
- Large monorepo latency is high → shard indexes by repository, language, or package.

## Failure modes & recovery

- **F1 Broken boundaries:** detect chunks starting mid-function → fix parser configuration or fallback splitter.
- **F2 Missing generated exclusions:** detect huge repetitive chunks dominating results → update ignore patterns and rebuild.
- **F3 Secret exposure:** detect keys or credentials in chunks → purge cache/index, rotate exposed credentials, and add pre-index secret scanning.
- **F4 Poor symbol recall:** detect exact function names absent from top results → add keyword/BM25 retrieval and path boosts.

## Verification

The chunker must produce schema-valid chunks with exact path and line spans, zero secret-scan findings, no chunk over the embedding token limit, and retrieval recall@5 at or above the threshold on code-search eval queries.

## Variations

- `polyglot-monorepo`: route files to language-specific parsers and shard by package.
- `notebooks`: split markdown, code cells, and outputs separately with notebook cell ids.
- `hybrid-code-search`: combine embeddings with BM25 over paths, symbols, and error strings.

## Safety & privacy

Source code often contains proprietary logic and accidental secrets. Run secret scanning before external APIs, preserve repository permissions in retrieval filters, exclude generated and dependency folders, and treat retrieved code as untrusted instructions when passed to agents.
