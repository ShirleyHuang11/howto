---
name: split-features-and-labels
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

You separate model inputs from target labels without leakage and produce train-ready `X` and `y` objects with reproducible column definitions.

## Preconditions

- A cleaned dataset with a documented label column or columns.
- A feature schema that identifies allowed inputs and forbidden leakage fields.
- A split strategy if train/validation/test sets are being created.
- A modeling framework such as scikit-learn, PyTorch, TensorFlow, Spark ML, or XGBoost.

## Steps

1. **Identify the prediction target.** Choose the exact label column, prediction horizon, and label encoding. → *Expect:* `target_column` is unambiguous and matches the task definition.
2. **List allowed feature columns.** Exclude labels, post-outcome fields, IDs used only for joining, timestamps after prediction time, and human annotations not available at inference. → *Expect:* a feature list that contains no known leakage columns.
3. **Create `X` and `y` explicitly.** In pandas, use `y = df[target_column]` and `X = df[feature_columns].copy()`. → *Expect:* `target_column` is absent from `X` and `y` length equals `X` row count.
4. **Encode labels consistently.** Map classes to stable IDs or use typed regression targets, saving the mapping with the dataset. → *Expect:* label values are valid and reproducible across runs.
5. **Keep split keys separate.** Preserve entity IDs, group IDs, and timestamps for splitting or auditing, but do not include them as model features unless justified. → *Expect:* split metadata is available without leaking into `X`.
6. **Build preprocessing inside a pipeline.** Fit encoders, imputers, scalers, and feature selectors only on training data. → *Expect:* validation/test transformations use train-fitted parameters.
7. **Assert shape and schema.** Check columns, dtypes, row counts, label distribution, and absence of forbidden fields. → *Expect:* a schema report for `X` and `y` passes.
8. **Save feature definitions.** Store feature column order, label mapping, and preprocessing version with the model run. → *Expect:* serving code can reproduce the same input order and meaning.

## Decision points

- A column is only available after the outcome → exclude it as leakage.
- IDs improve validation suspiciously → test grouped splits and remove memorization-prone identifiers.
- Multi-label task → use a multi-hot `y` matrix with a saved label order.
- Time-series task → split by time before fitting preprocessing.

## Failure modes & recovery

- **F1 Label leakage in features:** detect target column or post-outcome fields in `X` → remove and rerun metrics.
- **F2 Misaligned rows:** detect `X.index` differs from `y.index` → join by stable IDs and assert alignment.
- **F3 Unstable label mapping:** detect class IDs changing between runs → persist mapping and sort labels deterministically.
- **F4 Preprocessing leakage:** detect transformers fit on full data → wrap preprocessing in train-only pipelines.
- **F5 Serving column mismatch:** detect missing or reordered columns at inference → validate against saved feature schema.

## Verification

Run assertions that `target_column not in X.columns`, forbidden feature intersection is empty, `len(X) == len(y)`, indices are aligned, label values match the saved mapping, preprocessing is fit only on train data, and feature column order equals the saved schema.

## Variations

- `classification`: save class-to-ID mapping and monitor class balance.
- `regression`: validate numeric target ranges and outliers.
- `multimodal`: keep feature references such as image paths or embeddings separate from labels but aligned by ID.

## Safety & privacy

Low risk, but leakage can invalidate an entire model. Keep target and post-outcome fields out of features, avoid using direct identifiers unless the model truly needs them, and preserve metadata for audits without feeding it blindly to the model.
