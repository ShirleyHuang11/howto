---
name: encode-categorical-features
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

You convert categorical columns into model-ready numeric features without leaking target information or changing feature meaning between train and inference.

## Preconditions

- A tabular dataset with declared train, validation, and optional test splits.
- Python with `pandas` and `scikit-learn` installed.
- A list of categorical columns and the prediction target, if any.

## Steps

1. **Profile category cardinality.** Run `df[cat_cols].nunique(dropna=False).sort_values()` and inspect missing-value rates. → *Expect:* a table of category counts and null counts per categorical column.
2. **Choose an encoding by model family and cardinality.** Use one-hot encoding for low-cardinality linear/tree models, ordinal encoding only for real ordered categories, and target/frequency encoding only inside cross-validation. → *Expect:* each categorical column has an assigned encoding strategy.
3. **Fit encoders on training data only.** Build a `ColumnTransformer`, for example `OneHotEncoder(handle_unknown="ignore", min_frequency=10, sparse_output=True)` on `X_train`. → *Expect:* `fit()` completes without seeing validation or test rows.
4. **Transform all splits with the same fitted object.** Run `X_train_enc = preprocessor.fit_transform(X_train)` and `X_val_enc = preprocessor.transform(X_val)`. → *Expect:* train and validation matrices have the same number and order of columns.
5. **Persist the preprocessing artifact.** Save the fitted transformer with `joblib.dump(preprocessor, "artifacts/categorical_preprocessor.joblib")`. → *Expect:* a loadable artifact exists and contains the learned category mapping.
6. **Test unknown and missing categories.** Transform a tiny row containing a never-seen category and a null. → *Expect:* transformation succeeds without a new column or runtime error.
7. **Record feature names.** Call `preprocessor.get_feature_names_out()` when supported and save the list beside the model. → *Expect:* a deterministic feature-name file matches the encoded matrix width.

## Decision points

- Cardinality is small and stable → use one-hot encoding with unknown-category handling.
- Cardinality is very high → use hashing, frequency encoding, embeddings, or group rare categories before one-hot encoding.
- Category has a real order → use an explicit ordinal map reviewed by a domain owner.
- Validation score jumps suspiciously after target encoding → check for target leakage and refit inside folds only.

## Failure modes & recovery

- **F1 Unknown category error:** detect `Found unknown categories` at inference → set `handle_unknown="ignore"` or add an explicit unknown bucket and retrain the encoder.
- **F2 Train-serving skew:** detect different feature counts between training and production → deploy the saved transformer with the model and reject ad hoc refits.
- **F3 Memory blow-up:** detect a huge dense matrix after one-hot encoding → keep sparse output, group rare values, or switch to hashing.
- **F4 Fake ordinal signal:** detect poor validation performance from arbitrary integer labels → replace label encoding with one-hot or learned embeddings.

## Verification

Load the saved transformer, transform `X_train`, `X_val`, and a synthetic row with an unseen category. The check passes only if all transformed matrices have the same column count, no transform call raises, and `len(get_feature_names_out()) == X_val_enc.shape[1]` when feature names are available.

## Variations

- `scikit-learn`: use `ColumnTransformer` and persist the whole preprocessing pipeline with the estimator.
- `pandas`: use `get_dummies()` only for exploration; production requires saved column alignment.
- `deep learning`: map categories to integer ids with reserved `<UNK>` and `<PAD>` ids, then learn embeddings.

## Safety & privacy

Low risk if data stays local. Categorical values can still contain PII such as names, emails, account ids, or ZIP codes; redact or bucket sensitive identifiers before exporting features or sending data to any external service.
