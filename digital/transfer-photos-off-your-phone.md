---
name: transfer-photos-off-your-phone
domain: digital
locale: [generic]
interface: mixed
difficulty: basic
est_time: 1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-07-20
---

## Goal

Your phone's photos and videos exist as full-resolution files in a second location (computer or cloud), organized so you can find them, and verified complete before any copy is deleted from the phone.

## Preconditions

- The phone unlocked and, for a cable transfer, a data-capable cable (many charging cables carry power only).
- A destination with enough free space for the whole library; check the phone's storage usage for the number.
- Time proportional to the library. Thousands of photos over a cable can take an hour or more.

## Steps

1. **Check how much you are moving.** Read the phone's storage screen for total photo and video size, and confirm the destination has more free space than that. → *Expect:* a size figure and a destination with headroom.
2. **Pick the transfer path.** [BRANCH: cable to a computer (fastest, full quality, no account) | cloud sync (automatic, off-device, needs quota)] Cable for a one-time bulk offload; cloud for ongoing backup. → *Expect:* a clear choice and, for cable, the phone connected and unlocked.
3. **Cable path: set the phone to file transfer.** On the connection prompt choose "Transfer files" / "Photos", not "Charging only". → *Expect:* the phone's storage appears as a drive or device in the computer's file browser.
4. **Copy, do not move.** Drag the camera folder (DCIM and any others) to a dated folder on the destination. Copying leaves the originals in place until you have verified. → *Expect:* a progress bar; the copy finishes with a file count matching the phone.
5. **Verify the copy before trusting it.** Compare the file count, then open a dozen photos and one video from the destination at full size, including a recent and an old one. → *Expect:* files open, look sharp, and the count lines up. A folder of zero-byte files is a known cable failure.
6. **Give the copy structure.** Sort into folders by year, event, or however you will actually search later; a single dump of 10,000 files is technically a backup and practically unusable. → *Expect:* a browsable folder tree.
7. **Only now, delete from the phone if you need the space.** ⚠️ *Irreversible:* deletion removes your originals; delete only after step 5 passed. Most phones keep deleted items in a "Recently Deleted" album for ~30 days as a last safety net. → *Expect:* phone storage freed; the second copy untouched.

## Decision points

- Photos already in a phone cloud gallery → they may be low-resolution "optimized" copies on the device; download originals or export from the cloud, not from the thumbnails.
- iPhone to Windows (or Android to Mac) → use the file browser or the platform's transfer app; HEIC/HEVC files may need conversion to open everywhere.
- No computer → sync to cloud storage, confirm the upload finished from a second device, then clear the phone.

## Failure modes & recovery

- **F1 Zero-byte or missing files after copy:** the phone locked mid-transfer or the cable is power-only; unlock, keep it awake, use a data cable, recopy, and re-verify.
- **F2 Live Photos or videos split into odd pieces:** some transfers separate the still and the motion; use the platform's own export to keep pairs together.
- **F3 Deleted too soon and the copy was bad:** recover from "Recently Deleted" within its window; this is exactly why step 5 precedes step 7.
- **F4 Duplicates piling up on re-runs:** copy into a new dated folder each time, then deduplicate, rather than merging into one growing pile.

## Verification

Every photo and video sits in a second location at full resolution, the file count matches the phone, you have opened a sample and confirmed it is readable, the copy is organized into a browsable structure, and nothing was deleted from the phone until that verification passed.

## Variations

- `mobile-app`: phone-to-phone transfer tools handle a device upgrade in one pass, but still verify on the new phone before wiping the old one.
- Archival: for irreplaceable photos, follow `digital/back-up-your-files` so the offloaded library itself has a second copy.

## Safety & privacy

Medium risk: photos are personal and the deletion step is irreversible. The whole recipe is built around verify-before-delete. Never delete originals off a phone on the strength of an unverified copy, be cautious plugging into public or borrowed computers, and encrypt the destination if the library is sensitive.
