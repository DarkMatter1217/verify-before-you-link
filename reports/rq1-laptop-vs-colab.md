# RQ1: laptop run vs Colab run

- **Laptop (main result):** MacBook Pro, Apple M5 Pro, 24 GB; Ollama 0.40.14; finished 17 Nov 2026.
- **Colab (second run):** NVIDIA L4; Ollama 0.40.2; finished 15 Nov 2026. RQ2/RQ3 use this run's candidate pairs (`harness/data/candidates-rq1.json`).
- Same models (same digests, Q4_K_M), same LiSSA code and settings (temperature 0, seed 133742243, context 16,384 tokens, answers up to 4,096 tokens). The hardware and the Ollama version differ together, so their effects cannot be separated.

## Retrieval: candidate pairs (bge-m3, top 20)

| Project | Pairs per run | Shared | Shared share |
|---|---|---|---|
| SMOS | 1,340 | 1,328 | 99.1% |
| eTour_en | 1,160 | 1,139 | 98.2% |
| iTrust | 2,620 | 2,600 | 99.2% |

## Decisions and links

Same decisions: yes/no answers that agree, over the candidate pairs both runs share. Link overlap: links accepted by both runs / links accepted by either (Jaccard). For comparison, GPT-4o's own runs with three seeds overlap 0.79–0.88.

| Model | Prompt | Project | Links laptop / Colab | Same decisions | Link overlap |
|---|---|---|---|---|---|
| qwen2.5-coder-14b | KISS | SMOS | 277 / 280 | 99.3% | 0.961 |
| qwen2.5-coder-14b | KISS | eTour_en | 436 / 438 | 98.9% | 0.947 |
| qwen2.5-coder-14b | KISS | iTrust | 390 / 388 | 99.3% | 0.950 |
| qwen2.5-coder-14b | chain-of-thought | SMOS | 193 / 198 | 96.8% | 0.802 |
| qwen2.5-coder-14b | chain-of-thought | eTour_en | 221 / 223 | 96.0% | 0.805 |
| qwen2.5-coder-14b | chain-of-thought | iTrust | 439 / 469 | 97.5% | 0.864 |
| llama3.1-8b | KISS | SMOS | 1,151 / 1,155 | 98.1% | 0.964 |
| llama3.1-8b | KISS | eTour_en | 1,130 / 1,130 | 99.4% | 0.958 |
| llama3.1-8b | KISS | iTrust | 1,967 / 1,989 | 97.1% | 0.948 |
| llama3.1-8b | chain-of-thought | SMOS | 1,179 / 1,172 | 88.7% | 0.864 |
| llama3.1-8b | chain-of-thought | eTour_en | 948 / 929 | 83.1% | 0.783 |
| llama3.1-8b | chain-of-thought | iTrust | 1,812 / 1,762 | 83.9% | 0.778 |

## Average F1 over the three projects (LiSSA's strict rule)

| Model | Prompt | All requirements: laptop | Colab | Test slice: laptop | Colab |
|---|---|---|---|---|---|
| qwen2.5-coder-14b | KISS | 0.346 | 0.348 | 0.346 | 0.347 |
| qwen2.5-coder-14b | chain-of-thought | 0.243 | 0.247 | 0.250 | 0.250 |
| llama3.1-8b | KISS | 0.265 | 0.264 | 0.264 | 0.263 |
| llama3.1-8b | chain-of-thought | 0.257 | 0.265 | 0.254 | 0.261 |

The test slice has 205 of the 256 requirements (see `harness/data/split.json`). The RQ2/RQ3 baseline is LiSSA's chain-of-thought prompt asked again by our harness on Colab; on the test slice it scores 0.249 with Qwen (`harness/runs/baseline__qwen2.5-coder-14b__colab-l4__test`).
