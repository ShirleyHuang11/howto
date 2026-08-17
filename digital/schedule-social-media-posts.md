---
name: schedule-social-media-posts
domain: digital
locale: [generic]
interface: web
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-17
---

## Goal

Schedule social media posts for future publication with correct timing, assets, approvals, and account permissions.

## Preconditions

- You have posting access to the relevant social accounts.
- You have rights to use the text, images, video, music, hashtags, and links.

## Steps

1. **Select the scheduler.** [BRANCH: platform-native | third-party tool] use native scheduling for fewer permissions or a trusted tool for cross-platform calendars. → *Expect:* the scheduler can publish to the target account.
2. **Draft the post.** Write platform-specific copy, attach media, add alt text, and check links. → *Expect:* the preview matches the intended post.
3. **Confirm audience and account.** Verify profile, page, channel, visibility, and cross-posting settings before scheduling. → *Expect:* the post is assigned to the correct destination.
4. **Set date and timezone.** Choose the publish time and confirm the scheduler's timezone, especially for campaigns or travel. → *Expect:* the scheduled time matches the audience time.
5. **Review approvals and compliance.** Check brand, sponsorship disclosure, regulated claims, and crisis-sensitive timing. → *Expect:* required approvals are complete.
6. **Schedule the post.** Save or schedule the post. ⚠️ *Irreversible:* once the scheduled time arrives, the post may publish publicly before you notice an error. → *Expect:* the post appears in the scheduled queue.
7. **Verify after publishing.** Check the live post soon after release for formatting, media, tags, and link behavior. → *Expect:* the live post matches the approved version.

## Decision points

- The post mentions health, finance, politics, employment, or sponsored content → require stricter review and disclosures.
- The content depends on breaking news or crisis conditions → schedule closer to release or keep it as a draft.
- Third-party scheduler requests broad permissions → use the native platform instead if possible.

## Failure modes & recovery

- **F1 Wrong account:** detect the post is queued under the wrong profile → recover by deleting the scheduled item and recreating it under the right account.
- **F2 Timezone error:** detect queue time differs from plan → recover by editing the scheduled time before publication.
- **F3 Broken asset:** detect missing media, cropped video, or bad alt text → recover by replacing assets and previewing again.

## Verification

The scheduled queue shows the correct account, content, assets, visibility, date, timezone, and approval status, and the live post is checked after publication.

## Variations

- `mobile-app`: some platforms expose scheduling only for professional accounts or specific post types.
- `team`: use role-based approvals and avoid sharing account passwords.
- `campaign`: maintain a calendar with embargoes, launches, and blackout dates.

## Safety & privacy

Medium risk because scheduled posts can publish publicly, reveal private information, or violate advertising rules. Limit scheduler permissions and revoke tools you no longer use.
