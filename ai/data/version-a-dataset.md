---
name: version-a-dataset
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: medium
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You create a reproducible, immutable dataset version that can be traced to the exact files, schema, code, and split used for an AI experiment or release.

## Preconditions

- Source data files or tables and permission to store a versioned snapshot.
- A versioning tool such as DVC, LakeFS, Delta Lake, or object storage with manifests.
- A repository or experiment tracker where metadata can be recorded.

## Steps

1. **Define the dataset boundary.** List source locations, inclusion filters, date ranges, labels, and excluded records. → *Expect:* a written manifest scope that another engineer can reproduce.
2. **Compute file or table fingerprints.** Run `sha256sum data/raw/* > manifests/raw.sha256` or query table snapshot ids. → *Expect:* stable checksums or snapshot identifiers for every input.
3. **Create deterministic splits.** Use a fixed seed and stable key, such as `hash(user_id) % 100`, instead of row order. → *Expect:* split membership is unchanged when rows are reordered.
4. **Validate the schema before freezing.** Run a schema tool such as Great Expectations, Pandera, or `pyarrow` schema checks. → *Expect:* all required columns, types, and null constraints pass.
5. **Store the versioned artifact.** [BRANCH: DVC | LakeFS | object storage manifest] Run `dvc add data/processed` or write a manifest containing paths, checksums, row counts, and schema hash. → *Expect:* a dataset version id or manifest file is created.
6. **Tag the experiment metadata.** Record dataset version, code commit hash if available, preprocessing version, and label source in the training config. → *Expect:* a model run can point back to one exact dataset version.
7. **Protect released versions from mutation.** ⚠️ *Irreversible:* before deleting or rewriting any released dataset object, confirm backups and downstream dependencies; prefer creating a new version. → *Expect:* released versions are append-only or locked by policy.

## Decision points

- Dataset is small and file-based → DVC or content-addressed manifests are usually enough.
- Dataset is table-based and updated continuously → use snapshot-capable storage such as Delta Lake, Iceberg, BigQuery snapshots, or LakeFS.
- Labels can change over time → version labels separately from raw features.
- Regulatory retention applies → coordinate deletion and retention policy before freezing copies.

## Failure modes & recovery

- **F1 Non-reproducible split:** detect records moving between train and test after reload → split by stable entity hash and save split ids.
- **F2 Silent source mutation:** detect checksum mismatch for a supposedly fixed file → create a new dataset version and investigate storage permissions.
- **F3 Schema drift:** detect validation failures against old training code → add migration code or pin the model to the older schema.
- **F4 Missing lineage:** detect a model run with no dataset id → block promotion until lineage metadata is added.

## Verification

Rebuild the dataset from the recorded manifest in a clean directory. The check passes only if all checksums match, row counts per split match the manifest, schema validation passes, and the training config references the created dataset version id.

## Variations

- `DVC`: version data pointers in Git and store large blobs in remote object storage.
- `LakeFS`: version whole object-store branches and merge approved dataset changes.
- `Delta/Iceberg`: use table snapshot ids and time travel for warehouse-backed training data.

## Safety & privacy

Medium risk because versioned datasets can preserve PII or sensitive records longer than expected. Apply retention rules, access controls, and deletion workflows to every copy, including manifests and cached feature files.
