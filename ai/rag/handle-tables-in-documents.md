---
name: handle-tables-in-documents
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

You preserve table structure during ingestion so retrieval and generation can answer questions that depend on rows, columns, units, and headers.

## Preconditions

- Documents containing tables in PDF, HTML, spreadsheets, markdown, or word-processing files.
- A parser that can extract table cells and surrounding text.
- A retrieval eval set with table-specific questions.
- A rendering or serialization strategy for tables.

## Steps

1. **Identify table sources.** Inventory document types and mark which pages or sections contain tables. → *Expect:* a table manifest with source document, page or section, and parser used.
2. **Extract structured cells.** [BRANCH: PDF table extractor | HTML parser | spreadsheet reader] Preserve row order, column headers, merged-cell notes, captions, and units. → *Expect:* each table becomes structured data, not only flattened text.
3. **Normalize headers and units.** Expand multi-row headers and attach units to column names or cell metadata. → *Expect:* values like `Revenue (USD millions)` remain unambiguous.
4. **Serialize for retrieval.** Create compact markdown or row-wise text chunks with table id, caption, headers, and relevant row groups. → *Expect:* every chunk can be traced to table id and row range.
5. **Index table chunks.** Embed serialized rows and add lexical fields for exact numbers, entities, and headers. ⚠️ *Data leaves your control:* hosted embedding APIs receive table contents; redact sensitive cells or use local embeddings. → *Expect:* vector and keyword retrieval can find table rows by entity, metric, or value.
6. **Generate with table-aware context.** Instruct the answer model to cite table id and row or column references, and to avoid recalculating unless asked. → *Expect:* answers cite the correct table and include units.
7. **Evaluate numeric and lookup questions.** Test row lookup, comparison, aggregation, and unit-sensitive questions. → *Expect:* exact-match or tolerance-based numeric checks pass.

## Decision points

- Tables are large → chunk by logical row groups and keep a table summary chunk.
- Questions require computation → route to a dataframe or SQL tool rather than pure text generation.
- PDF extraction is unreliable → use OCR/layout tooling or obtain source spreadsheets.
- Exact numbers matter → add lexical search and structured filters.

## Failure modes & recovery

- **F1 Header loss:** detect answers with numbers but wrong metric → preserve expanded headers in every row chunk.
- **F2 Merged-cell ambiguity:** detect rows missing category labels → fill down merged labels during extraction and mark them as inferred.
- **F3 Numeric hallucination:** detect values not present in cells → require cited cell references and exact-value validation.
- **F4 Bad PDF parsing:** detect shifted columns or empty cells → compare extracted tables to rendered page samples and switch parser.

## Verification

The ingestion test must validate table schema, preserve headers and units, map every serialized row to source coordinates, and answer a table-specific eval set with exact numeric match or approved tolerance for at least the configured pass rate.

## Variations

- `spreadsheet`: keep sheets as structured data and query them with SQL or dataframe tools.
- `financial-pdf`: use layout-aware extraction and human spot checks for critical tables.
- `html-docs`: parse native table elements and preserve links in cells.

## Safety & privacy

Tables often contain financials, health data, or customer records. Redact sensitive cells before external APIs, preserve document permissions, validate numeric claims programmatically, and avoid letting the model invent calculations when a deterministic tool is available.
