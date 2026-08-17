---
name: search-your-email
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 2min
risk: low
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Find a specific email or set of emails using your mail app's search tools.

## Preconditions

- You can open the mailbox where the email may be stored.
- You know at least one clue: sender, recipient, subject word, date, attachment, or phrase.

## Steps

1. **Open search.** Click or tap the mail app's search box or magnifying glass. → *Expect:* the cursor is in the email search field.
2. **Enter a narrow clue.** Type a sender name, email address, subject word, or exact phrase. → *Expect:* matching messages appear or the app offers search suggestions.
3. **Apply filters.** Add date, folder, attachment, unread, sender, or recipient filters if too many results appear. → *Expect:* the result list gets shorter and more relevant.
4. **Open likely matches.** Select a result and check sender, date, subject, and body. → *Expect:* you can tell whether it is the email you need.
5. **Save or act on the result.** Star, flag, move, download, or reply once you find the right email. → *Expect:* the needed follow-up action is complete.

## Decision points

- You remember an exact phrase → search with quotation marks if your app supports it.
- You remember a date range → filter by that range before trying many keywords.
- The email may be archived or spam → include All Mail, Archive, Junk, or Trash in the search scope.

## Failure modes & recovery

- **F1 No results:** detect an empty result list → broaden the term, remove filters, or search all folders.
- **F2 Too many results:** detect hundreds of matches → add sender, date, attachment, or subject filters.
- **F3 Search index stale:** detect recent email missing → refresh, restart the app, or search from webmail.

## Verification

The target email is open or selected, and its sender, date, subject, or contents match the clue you were searching for.

## Variations

- `gmail`: use search chips or operators such as `from:`, `to:`, `subject:`, and `has:attachment`.
- `outlook`: use the search box filters for From, Subject, Has Attachments, and Date.
- `mobile-app`: filters may appear after running the first search.

## Safety & privacy

Email search results can expose sensitive subject lines and previews. Be careful when searching on shared screens or in public places.
