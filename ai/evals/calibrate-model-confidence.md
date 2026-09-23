---
name: calibrate-model-confidence
domain: ai
subdomain: evals
locale: [generic]
interface: mixed
difficulty: intermediate
est_time: 1h
risk: medium
prerequisites: [ai/evals/measure-task-accuracy]
status: draft
last_verified: 2026-09-22
---

## Goal

You align model confidence scores with empirical correctness so downstream systems can decide when to answer, ask for help, or abstain. The result includes calibration curves and threshold choices.

## Preconditions

- Eval examples with correctness labels.
- A confidence signal: model self-reported probability, classifier probability, logprob-derived score, or judge confidence.
- A script or notebook with `numpy`, `pandas`, and `scikit-learn`.

## Steps

1. **Collect confidence and correctness.** For each example, save `confidence` in `[0,1]` and `correct` as boolean. ⚠️ *Data leaves your control:* external calls for confidence must use approved eval data. → *Expect:* every scored example has both fields.
2. **Bucket predictions.** Divide examples into confidence bins such as 0.0-0.1 through 0.9-1.0. → *Expect:* each bin has count, mean confidence, and empirical accuracy.
3. **Compute calibration metrics.** Calculate expected calibration error, Brier score, and reliability diagram data. → *Expect:* overconfidence and underconfidence are quantified.
4. **Fit calibration if needed.** Use temperature scaling, isotonic regression, or Platt scaling on a validation split. → *Expect:* calibrated confidence improves ECE on held-out data.
5. **Choose operating thresholds.** Select thresholds for answer, abstain, or human review based on precision/coverage tradeoff. → *Expect:* threshold report shows expected accuracy at each coverage level.

## Decision points

- Model is overconfident → require abstention threshold or calibrated probability before automation.
- Calibration improves validation but not test → avoid overfitting; gather more data.
- Confidence unavailable → train a separate verifier or use ensemble disagreement.

## Failure modes & recovery

- **F1 Self-confidence is uncalibrated:** detect high confidence with low accuracy → calibrate or replace signal.
- **F2 Data leakage:** detect calibration trained and tested on same examples → split data and rerun.
- **F3 Sparse bins:** detect bins with very few examples → use adaptive binning or more data.
- **F4 Distribution shift:** detect production confidence/accuracy differs → monitor calibration online.

## Verification

The calibration script outputs reliability bins, ECE, Brier score, and threshold table. The calibrated signal passes only if held-out ECE is below the configured threshold, such as `ECE <= 0.05`, and chosen thresholds meet required precision or abstention targets.

## Variations

- `classification`: use class probabilities and per-class calibration.
- `open-ended QA`: use verifier confidence or judge confidence rather than raw model self-report.
- `agent`: calibrate confidence on final task success and tool-state validation.

## Safety & privacy

Do not present uncalibrated confidence as certainty, especially in high-impact domains. Store confidence telemetry carefully because it may be used for automated decisions affecting users.
