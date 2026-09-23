---
name: handle-imbalanced-classes
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

You train and evaluate a classifier when one or more classes are rare, using metrics and sampling methods that reflect real operating costs.

## Preconditions

- A labeled classification dataset with a fixed train, validation, and test split.
- Python with `pandas`, `scikit-learn`, and optionally `imbalanced-learn`.
- A business or product definition of false-positive and false-negative cost.

## Steps

1. **Measure the class distribution.** Run `y_train.value_counts(normalize=True)` and repeat for validation and test. → *Expect:* a class-ratio table showing whether rare classes are present in every split.
2. **Use stratified splitting if needed.** Recreate splits with `train_test_split(..., stratify=y)` or `StratifiedKFold`. → *Expect:* each split contains all classes at roughly comparable rates.
3. **Choose metrics that expose rare-class performance.** Track `average_precision`, per-class recall, macro F1, and a confusion matrix instead of accuracy alone. → *Expect:* a baseline report where the majority-class-only model scores poorly on rare-class metrics.
4. **Apply imbalance handling inside training only.** [BRANCH: class weights | oversampling | undersampling] Use `class_weight="balanced"` or put `SMOTE()` inside an `imblearn.pipeline.Pipeline`. → *Expect:* validation data remains untouched and sampling is applied only during fit.
5. **Tune the decision threshold.** Sweep thresholds on validation probabilities with `precision_recall_curve`. → *Expect:* a selected threshold that meets the required precision or recall constraint.
6. **Calibrate if probabilities are used operationally.** Fit `CalibratedClassifierCV` or evaluate reliability curves. → *Expect:* calibrated probabilities have lower Brier score or visibly better calibration on validation.
7. **Lock a final test evaluation.** Run the chosen pipeline and threshold once on the held-out test set. → *Expect:* a final confusion matrix and rare-class metric report that were not used for tuning.

## Decision points

- Rare-class recall is below requirement → increase class weight, use oversampling, collect more examples, or lower the decision threshold.
- Precision collapses after oversampling → tune the threshold, calibrate probabilities, or reduce synthetic sampling.
- The rare class has fewer than a few dozen examples → prioritize data collection and manual review over aggressive resampling.
- Production base rate differs from training → recalibrate thresholds using a representative validation set.

## Failure modes & recovery

- **F1 Inflated validation score:** detect oversampling before the train/validation split → rebuild the pipeline so resampling happens inside each training fold.
- **F2 Accuracy trap:** detect high accuracy but near-zero minority recall → replace accuracy with macro and precision-recall metrics.
- **F3 Unstable threshold:** detect large metric swings across folds → use more data, cross-validated threshold selection, or a human-review band.
- **F4 Miscalibrated probabilities:** detect poor Brier score or calibration curve → calibrate on validation data and recheck threshold metrics.

## Verification

The final report must include class distribution, per-class precision and recall, macro F1, average precision for the rare class, and a confusion matrix. The recipe passes only if the selected validation threshold meets the declared operating constraint and the held-out test rare-class recall is above the project threshold.

## Variations

- `scikit-learn`: use `class_weight`, `StratifiedKFold`, and threshold tuning on `predict_proba`.
- `imbalanced-learn`: use `Pipeline` with `SMOTE`, `RandomUnderSampler`, or combined samplers.
- `deep learning`: use weighted loss, focal loss, balanced batch sampling, and probability calibration.

## Safety & privacy

Medium risk because rare classes often represent fraud, abuse, medical findings, or safety incidents. Do not hide poor rare-class performance behind aggregate metrics, and review threshold changes before automating consequential decisions.
