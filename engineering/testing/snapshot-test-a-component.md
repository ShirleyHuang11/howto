---
name: snapshot-test-a-component
domain: engineering
subdomain: testing
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

Add or update a component snapshot test that catches intentional structural output changes without replacing meaningful behavioral assertions.

## Preconditions

- The component output is deterministic for fixed props, locale, time, and IDs.
- The project already uses snapshot tooling such as Jest, Vitest, Storybook, or Playwright visual snapshots.
- Reviewers can inspect snapshot diffs.

## Steps

1. **Choose a stable component state.** Use fixed props and avoid live time, random IDs, network data, or environment-specific output. → *Expect:* repeated renders produce the same output.
2. **Render the component in a test.** [BRANCH: React | Vue | web component] Use the repository's render helper and providers. → *Expect:* the component renders without warnings.
3. **Add behavior assertions first.** Assert key accessible text, role, or state before snapshotting. → *Expect:* the test fails for important behavior even if the snapshot is broad.
4. **Create the snapshot.** Run the targeted command with snapshot update mode, such as `npm test -- Button.test.ts -u`. → *Expect:* a new or updated snapshot file is written.
5. **Inspect the snapshot diff.** Read the generated snapshot and confirm it contains only intended structure. → *Expect:* no secrets, huge blobs, random IDs, or unrelated output are captured.
6. **Run without update mode.** Execute the same test normally. → *Expect:* the snapshot test exits 0.
7. **Keep snapshots small.** If the snapshot is noisy, narrow the rendered component or use explicit assertions instead. → *Expect:* future diffs will be reviewable.

## Decision points

- Snapshot is longer than reviewers can understand → replace with targeted assertions or split into smaller snapshots.
- Output includes generated IDs or dates → inject deterministic values or serializers.
- Visual regression is the goal → use image snapshots with fixed viewport, fonts, and baseline policy.

## Failure modes & recovery

- **F1 Snapshot churn:** detect diffs on every run → remove randomness, mock time, or stabilize generated IDs.
- **F2 Snapshot hides behavior:** detect test only checks a huge tree → add explicit assertions for the user-visible contract.
- **F3 Accidental update:** detect unrelated snapshot changes after `-u` → revert unrelated snapshot files and update only intended ones.
- **F4 Environment-specific diff:** detect CI-only snapshot mismatch → align serializer, runtime, timezone, fonts, and OS assumptions.

## Verification

Run the snapshot test without update mode, for example `npm test -- Button.test.ts` or `npx vitest run Button.test.ts`; it exits 0, and the snapshot diff in review contains only the intended component output.

## Variations

- `Jest`: use `toMatchSnapshot` and update with `-u`.
- `Vitest`: use `toMatchSnapshot` and update with `-u` or `--update`.
- `Playwright visual`: use `toHaveScreenshot` with fixed viewport and reviewed baseline images.

## Safety & privacy

Low risk when snapshots are small and synthetic. Inspect snapshots before commit, never capture tokens or personal data, and do not mass-update snapshots to silence failures without reviewing diffs.
