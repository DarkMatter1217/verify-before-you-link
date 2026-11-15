# Progress report

**Project:** Verify Before You Link: Local LLMs for Requirements Traceability (CSI5187, Fall 2026)
**Team:** Prabhjot Singh and Rahul
**Date:** 15 November 2026, about 18:30 UTC

## Summary

- **RQ1 is done** on a Colab L4 GPU: LiSSA unchanged with Qwen2.5-Coder-14B and Llama-3.1-8B, all 20,480 model calls. A second RQ1 run is in progress on Rahul's laptop.
- **Best local result:** Qwen with LiSSA's short (KISS) prompt reaches an average F1 of **0.348**, close to GPT-4o's 0.356 with the same prompt and 0.365 with chain-of-thought, on the same three projects.
- **RQ2/RQ3 on the dev slice are running.** The Qwen baseline and the `definition` variant are done; `summary` is about three-quarters done. The dev passes should finish around 16 November, 13:00–15:00 UTC.
- **Main problem so far:** Qwen often leaves out the `<trace>` tag that LiSSA's strict rule requires (65–75% of its chain-of-thought answers), which costs it recall.
- **Nothing has been run on the test slice.** It will be run once, after the dev choices are frozen.

## 1. Setup and checks

| Item | Result |
|---|---|
| Data | SMOS, eTour, iTrust from LiSSA's package: 256 requirements, 442 code files, 1,638 gold links, 5,120 candidate pairs. All match the proposal. |
| Our scoring reproduces LiSSA's | P/R/F1 recomputed from LiSSA's GPT-4o trace-link files match LiSSA's own result files (`harness/selftest.py`). |
| LiSSA on Ollama | Works after two fixes in its Ollama connection (context size, embedding endpoint); see [`code-changes.md`](code-changes.md). |
| Harness reproduces LiSSA exactly | `check_rq1`: the same 5,120 candidates; all 10,240 chain-of-thought prompts found in RQ1's saved answers; links and P/R/F1 identical for both models ([`harness/data/check_rq1.md`](../harness/data/check_rq1.md)). |
| Dev/test split | 20/80 per project, seed 5187: dev 51 requirements (SMOS 13, eTour 12, iTrust 26), test 205. |
| Software | Ollama 0.40.2; Qwen `9ec8897f747e`, Llama `46e0c10c039e`, both Q4_K_M; bge-m3; temperature 0; seed 133742243; context 16,384 tokens. |

## 2. RQ1 results (Colab L4, one seed)

Averages over SMOS, eTour and iTrust. The published rows are recomputed over the same three projects (the paper's averages also include Dronology, which we cannot run). Full tables: [`rq1-report.md`](../LiSSA-RATLR-V2/lissa/results-local/rq1/rq1-report.md).

| Approach | Avg. P | Avg. R | Avg. F1 | Avg. F2 |
|---|---|---|---|---|
| Retrieval only, bge-m3 (recall ceiling) | 0.190 | 0.506 | 0.251 | 0.335 |
| **Qwen2.5-Coder-14B, KISS** | 0.451 | 0.360 | **0.348** | 0.350 |
| Qwen2.5-Coder-14B, chain-of-thought | 0.405 | 0.219 | 0.247 | 0.225 |
| Llama-3.1-8B, KISS | 0.209 | 0.498 | 0.264 | 0.345 |
| Llama-3.1-8B, chain-of-thought | 0.210 | 0.453 | 0.265 | 0.336 |
| GPT-4o, KISS (published) | 0.405 | 0.463 | 0.356 | 0.401 |
| GPT-4o, chain-of-thought (published) | 0.399 | 0.460 | 0.365 | 0.406 |
| GPT-4o-mini, chain-of-thought (published) | 0.361 | 0.479 | 0.342 | 0.396 |
| FTLR, optimised (published) | 0.351 | 0.475 | 0.398 | 0.439 |

| F1 per project | SMOS | eTour | iTrust |
|---|---|---|---|
| Qwen, KISS | 0.304 | 0.480 | 0.261 |
| Qwen, chain-of-thought | 0.200 | 0.392 | 0.151 |
| Llama, KISS | 0.408 | 0.284 | 0.101 |
| Llama, chain-of-thought | 0.394 | 0.310 | 0.089 |
| GPT-4o, chain-of-thought | 0.294 | 0.526 | 0.276 |

**Observations**
1. A free 14B model on one GPU comes within about 0.01–0.02 average F1 of GPT-4o with LiSSA's KISS prompt.
2. Chain-of-thought hurts Qwen: 3,277 of its 5,040 chain-of-thought answers have no `<trace>` tag and count as "no" under LiSSA's rule.
3. Llama says "yes" often: high recall, low precision, and it fails on iTrust (F1 about 0.09–0.10).
4. Retrieval limits recall: bge-m3's top 20 contain fewer gold links than the OpenAI embeddings in LiSSA's runs (recall 0.506 vs. 0.588 on average; eTour 0.666 vs. 0.815, iTrust 0.402 vs. 0.531). No classifier can find links that retrieval missed.

## 3. RQ2/RQ3 on the dev slice (in progress)

The pipeline runs both passes on dev: for each model, a fresh baseline plus the four variants, then the round-2 combination, a repeatability check, and claim verification (RQ3). GPT-4o chain-of-thought on the same dev slice reaches an average F1 of 0.385 (0.385–0.394 over LiSSA's three seeds).

| Qwen2.5-Coder-14B, dev slice | Strict F1 (P / R) | Tolerant F1 | Answers without `<trace>` |
|---|---|---|---|
| Baseline, fresh run in this session | 0.208 (0.435 / 0.157) | 0.332 | 718 of 1,020 |
| Baseline, RQ1's answers (earlier session) | 0.235 (0.429 / 0.187) | 0.337 | 685 of 1,020 |
| + definition | 0.203 (0.532 / 0.138) | 0.325 | 764 of 1,020 |
| + summary, + project, + examples | running | | |

- **Definition:** precision went up and recall went down; F1 is unchanged within noise.
- **Time on the L4:** median 4.0 s per call, about 92 s per requirement (20 candidate pairs).
- Llama's dev runs, the combination and the verification come after Qwen's variants.

## 4. Repeatability

| Check | Result |
|---|---|
| 20 RQ1 questions asked again in a later session | text identical 8/20; yes/no identical 17/20 |
| Qwen dev baseline, two runs in different sessions | strict F1 0.235 vs. 0.208; tolerant 0.337 vs. 0.332 |
| GPT-4o, LiSSA's three seeds (for comparison) | links overlap 79–88%; dev average F1 0.385–0.394 |
| Within one session (50 pairs per model) | runs after classification (pending) |

Because answers differ slightly between sessions, all dev comparisons now run in one session, with a fresh baseline. See [`proposal-compliance.md`](proposal-compliance.md), section 2.2.

## 5. Compute

| Run | Where | Time |
|---|---|---|
| RQ1 | Colab L4 | 14 Nov 20:30 – 15 Nov 13:32 UTC (about 17 h) |
| RQ2/RQ3 dev, both passes | Colab L4, one session | started 15 Nov 14:42 UTC; about 22–24 h expected |
| RQ1, second run | Rahul's MacBook Pro (M5 Pro, 24 GB) | in progress |

Colab use is about 1.94 compute units per hour; about 1,320 units were left on 15 November.

## 6. Problems and how they were solved

| Problem | Solution |
|---|---|
| Ollama's old embedding endpoint failed on long code files (HTTP 500) | LiSSA now uses Ollama's current endpoint; inputs are cut at bge-m3's 8,192-token limit |
| Ollama silently cuts prompts beyond its default context | Context set to 16,384 tokens in LiSSA and on the Ollama server |
| One RQ1 run takes about 27 h on a laptop | RQ1–RQ3 moved to a Colab L4 (the free Colab T4 was tested and was no faster than the laptop; Kaggle's free quota of 30 GPU hours a week was too small) |
| Answers differ slightly between Colab sessions | Fresh same-session baseline; dev comparisons in one session; differences measured and reported |
| Stopping a notebook cell also stopped the Ollama server | The pipeline now runs as a separate background process; the notebook only shows its progress |
| An idle second Colab session doubled the cost | Closed; only one session runs at a time, checked every hour |

## 7. Changes from the original plan

All are explained in [`proposal-compliance.md`](proposal-compliance.md):
- Colab GPU instead of laptops for RQ1–RQ3 (RQ4 timings stay on a laptop).
- RQ1 with one seed instead of five.
- A round-2 combination prompt as one more candidate for "best prompt".
- A fresh dev baseline in the same session as the variants.

## 8. Next steps

Details and commands: [`project-flow/README.md`](../project-flow/README.md).

1. Finish the dev passes (automatic, about 16 November midday UTC).
2. Freeze the best prompt per model and τ, and record them with the date and file hashes.
3. Run the test slice once (about 80–90 GPU hours, 17–21 November).
4. Run the Wilcoxon tests and build the result tables (by 28 November).
5. RQ4: code up to 100 errors (both authors, Cohen's κ) and measure laptop runtimes.
6. Write the report (by mid-December; hard deadline 21 December).

## 9. Open decisions

- **Which RQ1 run is the main result:** Rahul's laptop run (matches the proposal's wording) or the Colab run? Recommended: the laptop run as the main result and the Colab run as a second run that shows the run-to-run difference.
- **Approval of the frozen dev choices** before the test runs start.
