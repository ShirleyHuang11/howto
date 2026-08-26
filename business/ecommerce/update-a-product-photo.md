---
name: update-a-product-photo
domain: business
subdomain: ecommerce
locale: [generic]
interface: web
difficulty: basic
est_time: 30min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-08-25
---

## Goal

Replace or add product photos so the listing accurately shows the item and improves buyer confidence.

## Preconditions

- Admin access to product media.
- Accurate product sample or approved supplier images with usage rights.
- Image requirements for size, format, background, and marketplace policy.

## Steps

1. **Audit the current images.** Check whether photos are outdated, blurry, misleading, missing variants, or hiding flaws. → *Expect:* a clear list of images to replace or add.
2. **Prepare compliant images.** Crop, resize, name files, and remove unsupported overlays or watermarks. → *Expect:* images meet platform dimensions and policy.
3. **Confirm image rights and accuracy.** Use only owned, licensed, supplier-authorized, or platform-permitted photos. → *Expect:* every image can legally represent the product.
4. **Upload the new photos.** Add images to the product media library and assign them to the correct product or variant. → *Expect:* uploaded images appear in the admin preview.
5. **Set the image order and alt text.** Put the clearest main image first and add descriptive alt text for accessibility and search. → *Expect:* the product page preview has the intended primary image and labels.
6. **Preview before publishing.** Check desktop, mobile, zoom, thumbnails, and variant switching. ⚠️ *Irreversible:* publishing misleading images can create disputes, so confirm the photos match the shipped item. → *Expect:* the buyer-facing preview is accurate and usable.
7. **Save and verify live page.** Publish the update and refresh the live listing. → *Expect:* customers see the new product photo set.

## Decision points

- Variant photos differ materially → assign images by variant instead of using one generic gallery.
- Product has defects or open-box condition → include flaw photos to prevent disputes.
- Marketplace rejects the image → adjust background, text overlays, or resolution to meet policy.

## Failure modes & recovery

- **F1 Wrong variant image:** detect customer sees the wrong color or size → reassign media and check variant mapping.
- **F2 Slow page load:** detect large images hurting performance → compress and upload optimized files.
- **F3 Rights complaint:** detect takedown or supplier objection → remove disputed images and replace with authorized photos.
- **F4 Cache delay:** detect admin updated but live page unchanged → purge cache or wait for CDN refresh before escalating.

## Verification

The live product page displays the intended new photo set, with the correct primary image, variant mapping, and no rejected or misleading media.

## Variations

- `amazon`: main image usually requires a white background and no promotional text.
- Fashion: include model, flat lay, size reference, and detail shots.

## Safety & privacy

Medium risk because inaccurate images can cause returns and disputes. Do not use copyrighted or misleading images, and remove EXIF data if it exposes private location information.
