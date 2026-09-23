---
name: sample-a-large-dataset
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 30min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You create a smaller dataset that preserves the important distributional properties needed for development, evaluation, or labeling.

## Preconditions

- A large source dataset with stable record ids.
- A clear purpose for the sample: debugging, training, evaluation, annotation, or cost estimation.
- Python, SQL, Spark, DuckDB, or another tool that can sample without loading everything into memory.

## Steps

1. **Define the sampling target.** Choose sample size, required strata, rare-class minimums, and whether the sample must be deterministic. → *Expect:* a written sampling spec with acceptance thresholds.
2. **Profile key distributions.** Compute counts for label, language, source, date bucket, and other critical segments. → *Expect:* a baseline distribution table from the full dataset or a trusted aggregate.
3. **Choose the sampling method.** [BRANCH: random | stratified | reservoir | time-window] Use stratified sampling when rare groups matter and reservoir sampling for streams. → *Expect:* a method that matches the sample purpose.
4. **Sample with a fixed seed or stable hash.** For example, use `WHERE MOD(ABS(HASH(id)), 1000) < 10` or `df.sample(frac=0.01, random_state=42)`. → *Expect:* rerunning the command selects the same rows when the source is unchanged.
5. **Validate sample representativeness.** Compare full and sample distributions with max absolute proportion difference or KL divergence for selected fields. → *Expect:* differences stay within the declared tolerance, except intentionally oversampled strata.
6. **Save sample metadata.** Record source version, query, seed, sample size, strata, and timestamp. → *Expect:* a manifest explains exactly how the sample was produced.
7. **Separate development and evaluation samples.** Keep eval samples fixed and untouched by prompt or model tuning. → *Expect:* the eval sample is marked read-only and not used for iterative development.

## Decision points

- Rare labels are missing from a random sample → switch to stratified or minimum-per-class sampling.
- You need an unbiased metric estimate → use probability sampling and avoid manual cherry-picking.
- You need debugging variety → stratify across known edge cases and sources.
- Source data changes daily → sample by stable ids and record the source snapshot.

## Failure modes & recovery

- **F1 Missing rare segment:** detect zero rows for a required class → oversample that segment and store sampling weights if estimating metrics.
- **F2 Non-repeatable sample:** detect different ids on rerun → use a fixed seed plus stable ordering or hash-based sampling.
- **F3 Memory failure:** detect local process killed while sampling → sample in SQL, DuckDB, Spark, or streaming reservoir mode.
- **F4 Biased eval set:** detect hand-picked easy examples → rebuild from a documented probability or stratified process.

## Verification

Run a script that checks exact sample row count, deterministic ids across two runs, required minimum count per stratum, and max absolute distribution difference against the source summary. The sample passes only if all declared thresholds are met and the manifest contains source version and seed.

## Variations

- `SQL warehouse`: use hash predicates or `TABLESAMPLE` plus stratified window functions.
- `Spark`: use `sampleBy()` for stratified sampling at scale.
- `streaming`: use reservoir sampling when the full dataset cannot be stored first.

## Safety & privacy

Low risk if access stays within the same controls as the source. Samples can be easier to leak than full datasets; apply the same PII redaction, encryption, and retention policies.
