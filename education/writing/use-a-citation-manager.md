---
name: use-a-citation-manager
domain: education
subdomain: writing
locale: [generic]
interface: web
difficulty: intermediate
est_time: 1h-2h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-02
---

## Goal

You use a citation manager to collect sources, organize notes, insert citations, and produce a bibliography with fewer formatting errors.

## Preconditions

- A citation manager account or app, such as Zotero, EndNote, Mendeley, Paperpile, or RefWorks.
- Browser connector or database export access.
- A word processor compatible with the citation tool.

## Steps

1. **Choose the tool required or supported by your institution.** Check library guidance and collaboration needs before installing. → *Expect:* the manager works with your school, databases, and writing software.
2. **Install the browser connector and word processor plugin.** Follow the tool's official setup instructions. → *Expect:* you can save sources from the browser and insert citations in documents.
3. **Create a project collection.** Make a folder for the assignment, paper, thesis, or topic. → *Expect:* new sources have a clear destination.
4. **Import sources from reliable pages.** Save records from databases, journal pages, library catalogs, or DOI pages rather than random snippets. → *Expect:* each item has usable metadata and, where allowed, a PDF.
5. **Check imported metadata.** Open each record and correct author names, titles, dates, DOI, pages, and publication type. → *Expect:* obvious citation-generator errors are fixed early.
6. **Attach notes and tags.** Add summary notes, keywords, methods, or relevance labels. → *Expect:* you can find sources by theme later.
7. **Insert citations while drafting.** Use the word processor plugin instead of typing citations manually. → *Expect:* in-text citations or footnotes are linked to library records.
8. **Generate and inspect the bibliography.** Choose the required style, refresh the document, and proofread entries manually. → *Expect:* the bibliography updates from cited items and remaining errors are caught.
9. **Back up or sync the library.** Enable sync if permitted and export a backup for major projects. → *Expect:* source data is not trapped on one device.

## Decision points

- You work with a research group → choose a manager with shared libraries and agree on naming rules.
- You handle sensitive or unpublished sources → avoid cloud sync unless approved.
- The citation style is unusual → install the exact style file or verify manually against the style guide.

## Failure modes & recovery

- **F1 Bad imported metadata:** detect titles in all caps, missing authors, or wrong item type → edit the record before citing it.
- **F2 Broken document links:** detect citations that no longer refresh → use the manager's plugin repair tools or restore from backup.
- **F3 Duplicate sources:** detect the same article multiple times → merge duplicates before final bibliography generation.
- **F4 Wrong citation style:** detect APA output for an MLA assignment → switch style and refresh all citations.

## Verification

The document contains plugin-managed citations, the bibliography refreshes successfully, and a manual spot-check confirms key entries match the required style.

## Variations

- `zotero`: use the browser connector, collections, tags, notes, and word processor plugin; it is widely supported by university libraries.
- `endnote`: common in labs and medical settings; check group library rules before syncing.
- `apa-example`: Garcia, P. L. (2021). Digital note-taking in first-year writing. College Composition Studies, 9(3), 201-219.

## Safety & privacy

Medium risk if libraries contain unpublished research, participant data, or private PDFs. Follow copyright rules, use institutional storage where required, and do not sync confidential material to unauthorized cloud accounts.
