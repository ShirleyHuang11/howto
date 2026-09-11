---
name: deploy-a-static-site
domain: engineering
subdomain: deploy
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min-1h
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-11
---

## Goal

You build and publish a static site from a known commit, then verify the deployed URL serves the expected content. The deployment is repeatable through CI or a provider CLI.

## Preconditions

- The site has a build command or a directory of static files.
- Hosting provider project or bucket exists.
- Required environment variables for build-time public config are known.
- CI or local tooling can run the build.

## Steps

1. **Identify the source commit and output directory.** Record the commit SHA and build output path such as `dist`, `build`, `out`, or `public`. → *Expect:* one immutable source revision and one publish directory are known.
2. **Install dependencies reproducibly.** [BRANCH: npm, `npm ci` | pnpm, `pnpm install --frozen-lockfile` | static HTML, skip dependency install] → *Expect:* install exits 0 without changing lockfiles.
3. **Run the production build.** Execute the project build, such as `npm run build`, `hugo --minify`, or `jekyll build`. → *Expect:* build exits 0 and creates the output directory.
4. **Inspect generated assets.** Confirm `index.html` exists and asset paths are correct for the intended base URL. → *Expect:* output directory contains HTML and referenced assets.
5. **Deploy the output directory.** [BRANCH: Netlify, `netlify deploy --prod --dir=<dir>` | Vercel, `vercel deploy --prod` | S3, `aws s3 sync <dir>/ s3://<bucket>/ --delete`] ⚠️ *Irreversible:* production visitors may see the new content immediately; confirm deploy target and rollback version before publishing. → *Expect:* provider returns a production deployment URL or sync summary.
6. **Invalidate CDN cache if required.** [BRANCH: CloudFront, `aws cloudfront create-invalidation --distribution-id <id> --paths '/*'` | provider-managed CDN, wait for deploy activation] → *Expect:* cache invalidation is created or provider marks deploy active.
7. **Verify the live site.** Run `curl -fsS https://<host>/` and check a known asset with `curl -I https://<host>/<asset>`. → *Expect:* homepage returns 200 and assets return 200 with appropriate content type.
8. **Record deployment metadata.** Note commit SHA, provider deploy ID, URL, and verification result. → *Expect:* deployment history can map the live site to source.

## Decision points

- Site uses client-side routing → configure fallback to `index.html` for deep links.
- Assets are fingerprinted → long cache TTL is safe; HTML should have shorter cache.
- Public env vars changed → rebuild before deploy because static sites bake them in.
- Build output includes secrets → stop, remove them, rotate exposed values, and rebuild.

## Failure modes & recovery

- **F1 Build output missing:** detect no `index.html` or empty directory → fix build command or output path.
- **F2 Deep links return 404:** detect `curl -I https://<host>/some/route` returns 404 → add SPA rewrite rules.
- **F3 Stale CDN content:** detect old commit visible after deploy → invalidate cache or purge provider CDN.
- **F4 Secret baked into files:** detect API keys in generated assets → rotate the key and remove it from build-time public config.

## Verification

The production deploy command exits 0, `curl -fsS https://<host>/` returns HTML from the new commit, and `curl -I https://<host>/<known-asset>` returns HTTP 200 with the expected content type.

## Variations

- `Netlify`: deploy `--prod --dir` and verify the published deploy URL.
- `Vercel`: framework detection selects the output directory unless overridden.
- `S3 + CloudFront`: sync files, set cache headers, then invalidate changed paths.
- `GitHub Pages`: publish from Actions artifact or configured branch.

## Safety & privacy

Medium risk because static deploys can expose built files publicly. Do not include secrets in client bundles, confirm the production target before syncing with `--delete`, and keep the previous deploy ID for rollback.
