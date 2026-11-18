# Results: where they are

The results stay where the code writes them, so every script works on them in place. This page is the index.
State: 18 November 2026. RQ1 is final (two runs). The dev passes of RQ2/RQ3 are complete. On the test slice, Qwen is complete and Llama is running.

**RQ1 has two runs.** The main result is the run on Rahul's laptop (MacBook Pro, M5 Pro, 24 GB; Ollama 0.40.14), as the proposal planned. The second run, on a Colab L4 GPU (Ollama 0.40.2), shows how much a repeat run differs; RQ2 and RQ3 use its candidate pairs. The two runs agree to within 0.008 average F1: [`reports/rq1-laptop-vs-colab.md`](../reports/rq1-laptop-vs-colab.md).

| What | Location |
|---|---|
| RQ1 report, main run (all tables, checks, model and hardware details) | [`LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/rq1-report.md`](../LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/rq1-report.md) |
| RQ1 numbers as CSV, main run | [`.../rq1-laptop/rq1-results.csv`](../LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/rq1-results.csv) |
| RQ1 links, LiSSA's result files, configs, logs, Ollama logs | `LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/` (`traceLinks-*.csv`, `results-*.md`, `configs/`, `logs/`, `ollama-logs/`) |
| RQ1 time per question and per requirement on the laptop (for RQ4) | [`.../rq1-laptop/timing.md`](../LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/timing.md) |
| RQ1 saved answers and embeddings, main run | `LiSSA-RATLR-V2/lissa/cache-local-r2c-laptop/<project>-133742243/` |
| RQ1 second run (Colab): report, links, logs, saved answers | [`.../rq1/rq1-report.md`](../LiSSA-RATLR-V2/lissa/results-local/rq1/rq1-report.md), `.../rq1/`, `LiSSA-RATLR-V2/lissa/cache-local-r2c/` |
| RQ1 code version and differences from the original LiSSA (the same Java changes in both runs) | `.../rq1-laptop/code-version.txt`, `.../rq1-laptop/lissa-vs-upstream.diff` (and the same files in `.../rq1/`) |
| Harness reproduces RQ1 exactly (against the Colab run) | [`harness/data/check_rq1.md`](../harness/data/check_rq1.md) |
| RQ2/RQ3 candidates, split, code summaries, examples | `harness/data/` |
| RQ2/RQ3 prompt texts (frozen 14 Nov) | `harness/prompts/` |
| RQ2/RQ3 runs on dev (decisions, links, metrics, settings) | `harness/runs/<variant>__<model>__colab-l4__dev/` |
| RQ2/RQ3 pipeline log | [`harness/runs/pipeline-dev.log`](../harness/runs/pipeline-dev.log) |
| RQ2/RQ3 runs on test | `harness/runs/<variant>__<model>__colab-l4__test/`, comparisons in `harness/runs/test-comparisons-<model>.json`, log in `harness/runs/pipeline-test.log`, stages in [`reports/test-timeline.md`](../reports/test-timeline.md) |
| RQ2/RQ3 saved answers (every prompt's answer, with timing and token counts) | `harness/cache/<model>__colab-l4.jsonl` |
| GPT-4o results used for comparison (LiSSA's own) | `LiSSA-RATLR-V2/lissa/results-r2c/`, `Evaluation-Req2Code.xlsx` |

Each run folder has `metrics.md` (readable tables), `metrics.json`, `decisions.csv` (one row per candidate pair, with the model's answer) and `run.json` (model digest, settings, file hashes, time).

## Main numbers so far

**RQ1**, average F1 over SMOS, eTour and iTrust (published rows recomputed over the same three projects):

| Run | Qwen KISS | Qwen CoT | Llama KISS | Llama CoT | GPT-4o KISS | GPT-4o CoT |
|---|---|---|---|---|---|---|
| **Laptop (main)** | **0.346** | **0.243** | **0.265** | **0.257** | 0.356 | 0.365 |
| Colab (second run) | 0.348 | 0.247 | 0.264 | 0.265 | | |

**RQ2/RQ3, dev slice**, average F1 with LiSSA's strict rule (the reported result; GPT-4o chain-of-thought on the same slice: 0.385):

| Prompt | Qwen2.5-Coder-14B | Llama-3.1-8B |
|---|---|---|
| Baseline | 0.208 | 0.281 |
| + definition | 0.203 | 0.312 |
| + summary | 0.167 | 0.285 |
| + project | 0.156 | 0.268 |
| + examples | **0.308** | 0.157 |
| Round-2 combination | definition+examples 0.307 | **definition+summary 0.316** |
| Best prompt + verification, τ = 0.2 | 0.267 | 0.265 |

Claim verification lowered F1 at every τ for both models. Full tables: `harness/runs/*__dev/metrics.md` and `.../verify-strict/metrics.md`; the summary is at the end of `harness/runs/pipeline-dev.log`. The choices frozen for the test slice are in [`harness/FROZEN.md`](../harness/FROZEN.md).

**RQ2/RQ3, test slice** (205 requirements), average F1 with LiSSA's strict rule; GPT-4o on the same requirements: 0.352–0.354. Llama is still running.

| Prompt | Qwen2.5-Coder-14B | Wilcoxon vs. baseline (Holm) |
|---|---|---|
| Baseline | 0.249 | |
| + definition | 0.199 | worse, p 0.016 |
| + summary | 0.220 | no difference |
| + project | 0.213 | no difference |
| + examples (frozen best) | **0.322** | better, p 0.0002 |
| Baseline + verification, τ = 0.2 | 0.220 | worse, p 0.016 |
| Examples + verification, τ = 0.2 | 0.279 | no difference |

The run folders also contain tolerant-rule scores. They are used only in RQ4, to measure the cost of answers that lack the `<trace>` tag (see [`reports/proposal-compliance.md`](../reports/proposal-compliance.md), section 2.5).

## Recomputing a table

```bash
python3 harness/analyze.py --parser strict table harness/runs/baseline__qwen2.5-coder-14b__colab-l4__dev
python3 harness/evaluate.py --slice dev --links SMOS=<traceLinks-SMOS…csv> eTour_en=<…> iTrust=<…>
```
