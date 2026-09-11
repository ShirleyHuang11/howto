---
name: cache-dependencies-in-ci
domain: engineering
subdomain: cicd
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: medium
prerequisites: [engineering/cicd/set-up-a-ci-pipeline]
status: draft
last_verified: 2026-09-11
---

## Goal

You add dependency caching to CI so repeated runs are faster while still installing from the lockfile and invalidating the cache when dependencies change.

## Preconditions

- The CI pipeline already installs dependencies and passes without caching.
- The package manager and lockfile path are known.
- You can inspect CI job timings before and after the change.

## Steps

1. **Measure the uncached baseline.** Record install duration from a recent green CI run. → *Expect:* a baseline time for dependency installation.
2. **Identify the correct cache target.** Choose package-manager cache directories rather than generated build output; examples include `~/.npm`, `~/.cache/pip`, `.pnpm-store`, `~/.cache/go-build`, or `vendor/bundle`. → *Expect:* the cache path is safe to restore across runs.
3. **Key the cache from lockfiles and runtime.** [GitHub Actions | GitLab CI] include OS, language version, and lockfile hash in the cache key. → *Expect:* dependency changes produce a new cache key.
4. **Restore cache before install.** Add the cache restore step before `npm ci`, `pip install`, `pnpm install --frozen-lockfile`, or equivalent. → *Expect:* the installer can reuse downloaded packages.
5. **Keep clean install semantics.** Do not replace lockfile installation with copying `node_modules` unless the package manager and CI support it safely. → *Expect:* dependency integrity checks still run.
6. **Save cache after successful install.** Let the CI cache action or runner save updated package cache content only after the job succeeds. → *Expect:* later runs show a cache hit.
7. **Compare timing.** Run CI twice: one expected miss, then one expected hit. → *Expect:* the second run has a cache hit and shorter install time.

## Decision points

- Lockfile is absent → add a lockfile before caching dependencies.
- Cache grows too large → cache package-manager download cache, not installed artifacts.
- Native dependencies are compiled → include OS, architecture, runtime version, and compiler-relevant files in the key.
- Cache hit still slow → verify the package manager is configured to use the cached directory.

## Failure modes & recovery

- **F1 Stale dependency cache:** detect missing or wrong package versions after dependency updates → include lockfile hash in the key and clear the bad cache.
- **F2 Cache masks install failure:** detect tests pass despite install command skipped → keep the install command mandatory after restore.
- **F3 Cache permission errors:** detect restore/save permission denied → use runner-owned cache paths or fix ownership before save.
- **F4 Cache quota exceeded:** detect CI warnings about storage limits → narrow cache paths and reduce restore keys.

## Verification

Two consecutive CI runs complete successfully: the first may report a cache miss, the second reports a cache hit for the dependency key, and the install step exits 0 with reduced duration compared with the baseline.

## Variations

- `GitHub Actions`: use `actions/cache` or built-in cache options on setup actions such as `setup-node`.
- `GitLab CI`: use `cache:key:files` with lockfiles and explicit `paths`.
- `Python`: prefer caching pip download wheels and still run `pip install -r requirements.txt`.
- `Node`: cache npm, pnpm, or yarn store; be cautious with direct `node_modules` caching.

## Safety & privacy

Medium risk because a bad cache can make CI unreliable. Do not cache files containing secrets, `.env` files, credentials, or private build artifacts. Keep cache keys specific enough to prevent cross-project contamination.

