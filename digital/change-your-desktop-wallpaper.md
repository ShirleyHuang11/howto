---
name: change-your-desktop-wallpaper
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

Set a new desktop wallpaper image.

## Preconditions

- You have an image available or are willing to choose a built-in wallpaper.
- You can change personalization settings on the device.

## Steps

1. **Open wallpaper settings.** [BRANCH: Windows | Mac] Windows: right-click the desktop and choose `Personalize`; Mac: choose `Apple menu > System Settings > Wallpaper`. → *Expect:* wallpaper or background settings are visible.
2. **Choose an image source.** Select a built-in image, solid color, photo folder, or `Browse photos`/`Add Photo`. → *Expect:* image choices or a file picker appears.
3. **Select the wallpaper.** Click the image you want to use. → *Expect:* the desktop preview updates.
4. **Set fit or display options.** Choose Fill, Fit, Stretch, Tile, Center, or the closest available option. → *Expect:* the image is framed acceptably on the screen.
5. **Close settings.** Exit the settings window after the wallpaper appears correctly. → *Expect:* the desktop shows the new wallpaper.

## Decision points

- Image looks cropped → choose Fit or Center instead of Fill.
- Multiple monitors are connected → set the same image for all screens or choose per-display images.

## Failure modes & recovery

- **F1 Setting disabled:** detect by grayed-out controls or policy message → ask the device administrator.
- **F2 Image missing:** detect by file picker not finding it → download, copy, or move the image to an accessible folder.
- **F3 Wallpaper looks blurry:** detect by pixelated display → choose a higher-resolution image.

## Verification

The desktop background displays the selected image after settings are closed.

## Variations

- `windows`: `Settings > Personalization > Background` offers picture, solid color, slideshow, and fit controls.
- `macos`: `System Settings > Wallpaper` manages desktop images and dynamic wallpapers.

## Safety & privacy

Low risk. Avoid wallpaper images that reveal private photos, addresses, client names, or sensitive work during screen sharing.
