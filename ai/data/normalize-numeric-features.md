---
name: normalize-numeric-features
domain: ai
subdomain: data
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 45min
risk: low
prerequisites: []
status: draft
last_verified: 2026-09-22
---

## Goal

You scale numeric features with train-only statistics so models train stably and serving uses exactly the same transformation.

## Preconditions

- Numeric feature columns identified and separated from labels and IDs.
- Train/validation/test splits or a time-based split plan.
- A preprocessing pipeline such as scikit-learn `Pipeline`, Spark ML, TensorFlow preprocessing, or a feature store transform.
- Range and outlier expectations for important numeric fields.

## Steps

1. **Select numeric columns intentionally.** Exclude labels, IDs, timestamps used only for splitting, and already-normalized embeddings unless needed. → *Expect:* a numeric feature list with units and expected ranges.
2. **Inspect distributions and outliers.** Compute min, max, quantiles, missingness, skew, and impossible values. → *Expect:* a profile showing which columns need standard scaling, robust scaling, log transform, clipping, or no scaling.
3. **Split before fitting scalers.** Create train/validation/test splits first, respecting time or group constraints. → *Expect:* validation and test values do not affect scaling statistics.
4. **Fit the scaler on training data only.** [BRANCH: standard | min-max | robust | log-plus-standard] Fit means, variances, medians, quantiles, or bounds only on train. → *Expect:* scaler parameters are saved with the model artifacts.
5. **Transform all splits with the saved scaler.** Apply the fitted transform to train, validation, test, and later serving data. → *Expect:* transformed arrays have consistent columns and no unsupported nulls or infinities.
6. **Validate transformed ranges.** Check mean and variance for standard-scaled train columns, expected bounds for min-max, and finite values after logs. → *Expect:* normalization metrics match the chosen method.
7. **Add the scaler to the serving pipeline.** Package preprocessing with the model or load the exact scaler artifact by version. → *Expect:* online inference uses the same column order and parameters as training.
8. **Run a baseline comparison.** Train with and without normalization where relevant and compare convergence, metrics, and calibration. → *Expect:* normalization improves stability or is documented as unnecessary for the chosen model.

## Decision points

- Model is tree-based and insensitive to scaling → normalization may be unnecessary, but still handle invalid ranges.
- Features have heavy outliers → prefer robust scaling or clipping before standard scaling.
- Feature is strictly positive and highly skewed → apply log transform before scaling.
- Serving receives values outside training range → monitor drift and choose clipping or alerting.

## Failure modes & recovery

- **F1 Data leakage:** detect scaler fit on full dataset → refit on train only and rerun evaluation.
- **F2 Infinite values:** detect `NaN` or `inf` after log or division → add missing handling, epsilon, or input validation.
- **F3 Column-order mismatch:** detect serving predictions change when columns reorder → enforce saved feature schema.
- **F4 Outlier domination:** detect near-zero variance for most normalized values → switch to robust scaling or clipping.
- **F5 Train-serve skew:** detect online normalized values using different scaler stats → load versioned scaler artifacts in serving.

## Verification

Run preprocessing tests that assert scaler parameters are fit only on training rows, transformed train numeric columns meet the expected normalization properties, validation/test transforms produce finite values with the saved parameters, column order matches the schema, and serving sample transformations equal offline transformations for the same inputs.

## Variations

- `standard-scaler`: good default for linear models, neural nets, and distance-based methods.
- `robust-scaler`: uses medians and quantiles for outlier-heavy features.
- `min-max`: useful when bounded inputs are required, but sensitive to future out-of-range values.

## Safety & privacy

Low risk, but leakage through normalization can inflate validation metrics. Fit only on training data, version scaler parameters, avoid logging sensitive numeric fields, and monitor production ranges for drift.
