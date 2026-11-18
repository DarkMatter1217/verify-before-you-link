# Progress report

**Project:** Verify Before You Link: Local LLMs for Requirements Traceability (CSI5187, Fall 2026)
**Team:** Prabhjot Singh and Rahul
**Date:** 16 November 2026. Checkpoint: RQ1 done, RQ2/RQ3 dev passes done, choices frozen, test slice about to start.
**Updated:** 18 November 2026: Rahul's laptop RQ1 run finished and is now the main RQ1 result (sections 2, 4 and 5). The test slice is tracked in [`test-timeline.md`](test-timeline.md).

## Summary

- **RQ1 is done, twice:** LiSSA unchanged with Qwen2.5-Coder-14B and Llama-3.1-8B, all 20,480 model calls, on Rahul's laptop (the main result, as the proposal planned) and on a Colab L4 GPU. The two runs differ by at most 0.008 average F1.
- **RQ1, best local result:** Qwen with LiSSA's short (KISS) prompt reaches an average F1 of **0.346**, close to GPT-4o's 0.356 with the same prompt and 0.365 with chain-of-thought, on the same three projects.
- **RQ2 on dev:** what helps depends on how each model fails.
  - Labelled examples fix Qwen's answer format: average F1 rises from 0.208 to **0.308**.
  - A precise definition, plus a code summary, curbs Llama's over-linking: average F1 rises from 0.281 to **0.316**.
  - The other kinds of information don't help.
- **RQ3 on dev:** claim verification lowers F1 at every threshold, for both models.
- **Against GPT-4o (dev average F1 0.385):** both models are below it on average, but each beats GPT-4o on one project: Llama on SMOS, Qwen on iTrust.
- **Scoring:** as the proposal says ("exactly as LiSSA does"), every result uses LiSSA's own answer rule (strict parsing). A second, tolerant rule is used only in RQ4, to measure what the missing-tag error costs.
- **Freeze:** the best prompt per model and τ were frozen and committed before any test-slice call ([`harness/FROZEN.md`](../harness/FROZEN.md)). The test slice runs next.

## 1. Setup and checks

| Item | Result |
|---|---|
| Data | SMOS, eTour, iTrust from LiSSA's package: 256 requirements, 442 code files, 1,638 gold links, 5,120 candidate pairs. All match the proposal. |
| Our scoring reproduces LiSSA's | P/R/F1 recomputed from LiSSA's GPT-4o trace-link files match LiSSA's own result files (`harness/selftest.py`). |
| LiSSA on Ollama | Works after two fixes in its Ollama connection (context size, embedding endpoint); see [`code-changes.md`](code-changes.md). |
| Harness reproduces LiSSA exactly | `check_rq1`: the same 5,120 candidates; all 10,240 chain-of-thought prompts found in RQ1's saved answers; links and P/R/F1 identical for both models ([`harness/data/check_rq1.md`](../harness/data/check_rq1.md)). |
| Dev/test split | 20/80 per project, seed 5187: dev 51 requirements (SMOS 13, eTour 12, iTrust 26), test 205. |
| Software | Ollama 0.40.14 on the laptop, 0.40.2 on Colab; Qwen `9ec8897f747e`, Llama `46e0c10c039e`, both Q4_K_M; bge-m3; temperature 0; seed 133742243; context 16,384 tokens. |

## 2. RQ1 results (Rahul's laptop, one seed, all 256 requirements)

Averages over SMOS, eTour and iTrust. The published rows are recomputed over the same three projects (the paper's averages also include Dronology, which we cannot run). Full tables: [`rq1-laptop/rq1-report.md`](../LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/rq1-report.md). The last column is the second run on Colab ([`rq1/rq1-report.md`](../LiSSA-RATLR-V2/lissa/results-local/rq1/rq1-report.md); comparison in [`rq1-laptop-vs-colab.md`](rq1-laptop-vs-colab.md)).

| Approach | Avg. P | Avg. R | Avg. F1 | Avg. F2 | Avg. F1, Colab run |
|---|---|---|---|---|---|
| Retrieval only, bge-m3 (recall ceiling) | 0.190 | 0.506 | 0.250 | 0.335 | 0.251 |
| **Qwen2.5-Coder-14B, KISS** | 0.448 | 0.358 | **0.346** | 0.347 | 0.348 |
| Qwen2.5-Coder-14B, chain-of-thought | 0.404 | 0.211 | 0.243 | 0.219 | 0.247 |
| Llama-3.1-8B, KISS | 0.210 | 0.498 | 0.265 | 0.346 | 0.264 |
| Llama-3.1-8B, chain-of-thought | 0.205 | 0.443 | 0.257 | 0.327 | 0.265 |
| GPT-4o, KISS (published) | 0.405 | 0.463 | 0.356 | 0.401 | |
| GPT-4o, chain-of-thought (published) | 0.399 | 0.460 | 0.365 | 0.406 | |
| GPT-4o-mini, chain-of-thought (published) | 0.361 | 0.479 | 0.342 | 0.396 | |
| FTLR, optimised (published) | 0.351 | 0.475 | 0.398 | 0.439 | |

**Observations**
1. A free 14B model on a laptop comes within about 0.01–0.02 average F1 of GPT-4o with LiSSA's KISS prompt.
2. Chain-of-thought hurts Qwen: 3,352 of its 5,040 chain-of-thought answers have no `<trace>` tag and count as "no" under LiSSA's rule (3,277 in the Colab run).
3. Llama says "yes" often: high recall, low precision, and it fails on iTrust (F1 about 0.08–0.10).
4. Retrieval limits recall: bge-m3's top 20 contain fewer gold links than the OpenAI embeddings in LiSSA's runs (recall 0.506 vs. 0.588 on average). No classifier can find links that retrieval missed.

## 3. RQ2 and RQ3 on the dev slice (finished 16 Nov, 11:26 UTC)

Average F1 with LiSSA's strict rule. GPT-4o chain-of-thought on the same slice: **0.385** (0.385–0.394 over LiSSA's three seeds; SMOS 0.267, eTour 0.601, iTrust 0.286).

| Prompt | Qwen2.5-Coder-14B | Llama-3.1-8B |
|---|---|---|
| Baseline (LiSSA's prompt, fresh run) | 0.208 | 0.281 |
| + definition | 0.203 | **0.312** |
| + summary | 0.167 | 0.285 |
| + project | 0.156 | 0.268 |
| + examples | **0.308** | 0.157 |
| Round-2 combination (rule fixed in advance) | definition+examples 0.307 | **definition+summary 0.316** |
| **Best on dev** | **examples, 0.308** | **definition+summary, 0.316** |

**RQ2 observations**
- **Qwen's problem is format, not judgement.** Most added information makes Qwen leave out the `<trace>` tag more often (718 → 764–808 of 1,020 answers). Labelled examples show the format and halve the missing tags (486), which lifts F1 by 0.10.
- **Llama's problem is over-linking.** The baseline predicts 792 links at precision 0.225. The definition makes it stricter (precision 0.308; iTrust F1 0.084 → 0.158).
- **The same information helps one model and hurts the other:** labelled examples make Llama far too cautious (recall 0.458 → 0.113).
- **Per project, the local models beat GPT-4o in places:** Llama on SMOS (0.30–0.38 vs. 0.27) and Qwen's definition+examples on iTrust (0.298 vs. 0.286).

**RQ3: claim verification**, average F1 by threshold τ ("unclear" counts as not supported):

| Run | none | τ 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |
|---|---|---|---|---|---|---|
| Qwen baseline | 0.208 | 0.159 | 0.145 | 0.109 | 0.055 | 0.015 |
| Qwen examples | 0.308 | 0.267 | 0.256 | 0.183 | 0.113 | 0.042 |
| Llama baseline | 0.281 | 0.250 | 0.218 | 0.192 | 0.163 | 0.106 |
| Llama definition | 0.312 | 0.269 | 0.218 | 0.189 | 0.154 | 0.092 |
| Llama definition+summary | 0.316 | 0.265 | 0.221 | 0.178 | 0.131 | 0.062 |

- **τ chosen by the fixed rule:** 0.2.
- **Qwen:** verification raises precision (examples: 0.505 → 0.625 at τ 0.2), but recall falls more.
- **Llama:** precision barely moves; correct and wrong links are removed at about the same rate.
- **Invented identifiers:** many claims cite classes or methods that don't exist in the file: 22–30% of Qwen's claims and 38–44% of Llama's.
- **Sensitivity check:** counting "unclear" as supported changes little.

## 4. Repeatability

| Check | Qwen | Llama |
|---|---|---|
| 50 questions asked again in the same session: identical text | 36 of 50 | 9 of 50 |
| … same yes/no decision | 49 of 50 (98%) | 46 of 50 (92%) |
| RQ1's answers vs. a fresh run (another session), 1,020 dev pairs: same decision | 96.7% | to be computed offline |
| RQ1, laptop run vs. Colab run (different hardware and Ollama version): same decision, chain-of-thought / KISS | 96.0–97.5% / 98.9–99.3% | 83.1–88.7% / 97.1–99.4% |
| … average F1, chain-of-thought / KISS | 0.243 vs. 0.247 / 0.346 vs. 0.348 | 0.257 vs. 0.265 / 0.265 vs. 0.264 |
| Dev baseline F1, RQ1's answers vs. fresh run | 0.235 vs. 0.208 | — |
| For comparison: GPT-4o, LiSSA's three seeds | links overlap 79–88%; dev average F1 0.385–0.394 | |

- **On the Colab GPU, answers vary slightly even within one session.** For Qwen, this is about as much as between sessions.
- **This is random noise, not bias.** Differences smaller than this run-to-run variation are not treated as effects. See [`proposal-compliance.md`](proposal-compliance.md), section 2.2.

## 5. Compute

| Run | Where | Time | Compute units |
|---|---|---|---|
| RQ1, second run | Colab L4, Ollama 0.40.2 | 14 Nov 20:30 – 15 Nov 13:32 UTC (about 17 h) | about 33 |
| RQ2/RQ3 dev, both passes | Colab L4, one session | 15 Nov 14:42 – 16 Nov 11:26 UTC (about 21 h) | about 41 |
| RQ1, main run | Rahul's MacBook Pro (M5 Pro, 24 GB), Ollama 0.40.14 | 12–17 Nov, about 18 h of model time in 27 batches | — (own laptop) |

Colab use is about 1.94 compute units per hour; about 1,284 units were left on 16 November.

## 6. Problems and how they were solved

| Problem | Solution |
|---|---|
| Ollama's old embedding endpoint failed on long code files (HTTP 500) | LiSSA now uses Ollama's current endpoint; inputs are cut at bge-m3's 8,192-token limit |
| Ollama silently cuts prompts beyond its default context | Context set to 16,384 tokens in LiSSA and on the Ollama server |
| One RQ1 run takes about 27 h on a laptop | RQ1–RQ3 moved to a Colab L4 (the free Colab T4 was tested and was no faster than the laptop; Kaggle's free quota of 30 GPU hours a week was too small) |
| Answers differ slightly between runs, even within a session | Measured and reported; dev comparisons ran in one session; the test runs in chunks of requirements |
| Stopping a notebook cell also stopped the Ollama server | The pipeline runs as a separate background process; the notebook only shows its progress |
| An idle second Colab session doubled the cost | Closed; only one session runs at a time, checked every 50 minutes |

## 7. Changes from the original plan

All are explained in [`proposal-compliance.md`](proposal-compliance.md):
- Colab GPU instead of laptops for RQ2–RQ3 (RQ1's main run and RQ4's timings are on a laptop).
- RQ1 with one seed instead of five.
- A round-2 combination prompt as one more candidate for "best prompt".
- A fresh dev baseline in the same session as the variants.
- Strict parsing (LiSSA's rule) for every result; tolerant parsing only inside RQ4's error analysis. Reason: the proposal fixes the scoring to LiSSA's, and the published GPT-4o numbers use only the strict rule, while RQ4 asks which error types remain, and the missing tag is one of them.

## 8. Next steps

Details and commands: [`project-flow/README.md`](../project-flow/README.md).

1. **Test slice** (starting 16 Nov): every variant, the best prompt and the 2×2 with verification, both models; about 95–100 GPU hours over about 5 Colab sessions.
2. Wilcoxon tests and result tables (Rahul leads; by 24–28 November).
3. RQ1: the two runs are compared ([`rq1-laptop-vs-colab.md`](rq1-laptop-vs-colab.md)) and LiSSA's own prompts are timed on the laptop ([`timing.md`](../LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/timing.md)). Still to do: the RQ4 runtime sample of the RQ2/RQ3 configurations on Rahul's laptop.
4. RQ4 error coding (both, Cohen's κ), by 5 December.
5. Report, by mid-December (hard deadline 21 December).

## 9. Open decisions

- **Which RQ1 run is the main result:** decided on 18 November: Rahul's laptop run, as the proposal planned. The Colab run is reported as a second run that shows the run-to-run difference.
