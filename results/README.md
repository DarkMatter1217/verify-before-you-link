# Results: where they are

The results stay where the code writes them, so every script works on them in place. This page is the index.
State: 2026-11-15 18:49 UTC. RQ2/RQ3 are still running; only finished runs are included (the log and saved answers are a snapshot of that moment).

| What | Location |
|---|---|
| RQ1 report (all tables, checks, model and hardware details) | [`LiSSA-RATLR-V2/lissa/results-local/rq1/rq1-report.md`](../LiSSA-RATLR-V2/lissa/results-local/rq1/rq1-report.md) |
| RQ1 numbers as CSV | [`.../rq1/rq1-results.csv`](../LiSSA-RATLR-V2/lissa/results-local/rq1/rq1-results.csv) |
| RQ1 links, LiSSA's result files, configs, logs | `LiSSA-RATLR-V2/lissa/results-local/rq1/` (`traceLinks-*.csv`, `results-*.md`, `configs/`, `logs/`) |
| RQ1 code version and differences from the original LiSSA | `.../rq1/code-version.txt`, `.../rq1/lissa-vs-upstream.diff` |
| RQ1 saved answers and embeddings (every model answer) | `LiSSA-RATLR-V2/lissa/cache-local-r2c/<project>-133742243/` |
| Harness reproduces RQ1 exactly | [`harness/data/check_rq1.md`](../harness/data/check_rq1.md) |
| RQ2/RQ3 candidates, split, code summaries, examples | `harness/data/` |
| RQ2/RQ3 prompt texts (frozen 14 Nov) | `harness/prompts/` |
| RQ2/RQ3 runs on dev (decisions, links, metrics, settings) | `harness/runs/<variant>__<model>__colab-l4__dev/` |
| RQ2/RQ3 pipeline log | [`harness/runs/pipeline-dev.log`](../harness/runs/pipeline-dev.log) |
| RQ2/RQ3 saved answers (every prompt's answer, with timing and token counts) | `harness/cache/<model>__colab-l4.jsonl` |
| GPT-4o results used for comparison (LiSSA's own) | `LiSSA-RATLR-V2/lissa/results-r2c/`, `Evaluation-Req2Code*.xlsx`, `statistical-evaluation/` |

Each run folder has `metrics.md` (readable tables), `metrics.json`, `decisions.csv` (one row per candidate pair, with the model's answer) and `run.json` (model digest, settings, file hashes, time).

## Main numbers so far

**RQ1**, average F1 over SMOS, eTour and iTrust (published rows recomputed over the same three projects):

| Qwen KISS | Qwen CoT | Llama KISS | Llama CoT | GPT-4o KISS | GPT-4o CoT |
|---|---|---|---|---|---|
| 0.348 | 0.247 | 0.264 | 0.265 | 0.356 | 0.365 |

**RQ2, dev slice, Qwen**, average F1 with LiSSA's strict rule (the reported result): fresh baseline 0.208, definition 0.203, summary 0.167. GPT-4o chain-of-thought on the same slice: 0.385.

The run folders also contain tolerant-rule scores (0.332, 0.325, 0.323). They are used only in RQ4, to measure the cost of answers that lack the `<trace>` tag (see [`reports/proposal-compliance.md`](../reports/proposal-compliance.md), section 2.5).

## Recomputing a table

```bash
python3 harness/analyze.py --parser strict table harness/runs/baseline__qwen2.5-coder-14b__colab-l4__dev
python3 harness/evaluate.py --slice dev --links SMOS=<traceLinks-SMOS…csv> eTour_en=<…> iTrust=<…>
```
